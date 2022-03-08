
from msilib.schema import Error
from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt
from io import BytesIO
import base64
import io

import SilAdapter


## xAI functions for tensorflow and pytorch
def torch_guided_backprop_wrap(model):
    import torch
    def relu_hook_function(module, grad_in, grad_out):
        if isinstance(module, torch.nn.ReLU):
            return (torch.clamp(grad_in[0], min=0.),)

    for i, module in enumerate(model.modules()):
        if isinstance(module, torch.nn.ReLU):
            print(model.named_modules())
            module.register_backward_hook(relu_hook_function)
    return model

def tf_guided_backprop_wrap(model):
    import tensorflow as tf
    @tf.custom_gradient
    def guidedRelu(x):
        def grad(dy):
            return tf.cast(dy>0,"float32") * tf.cast(x>0, "float32") * dy
        return tf.nn.relu(x), grad

    layer_dict = [layer for layer in model.layers[1:] if hasattr(layer,'activation')]
    for layer in layer_dict:
        if layer.activation == tf.keras.activations.relu:
            layer.activation = guidedRelu

    return model

def torch_backprop(model, input):
# Expects a pretrained torchvision object detector. 
    input.requires_grad = True
    out = model(input)
    best_score = out[0]["scores"][0]
    best_score.backward()
    salimap = input.grad
    salimap = salimap[0].detach().numpy().transpose(1, 2, 0)
    salimap_norm = normalize(salimap)
    return salimap_norm

def tf_backprop(model, input):
    import tensorflow as tf

    with tf.GradientTape() as tape:
        tape.watch(input)
        scores = model(input)
        best_score = tf.math.reduce_max(scores)
       
    salimap = tape.gradient(best_score, input)
    salimap = salimap[0].numpy()
    salimap_norm = normalize(salimap)
    return salimap_norm

def normalize(salimap):
    salimap = salimap[:, :, 0] + salimap[:, :, 1] + salimap[:, :, 2]
    salimap_norm = (salimap - np.min(salimap)) / (np.max(salimap) - np.min(salimap))
    return salimap_norm



## helper functions for operating with CANoe via SilAdapter

def prep_xai_send(name, np_array, width, height):
    # applying a threshold and a transparent channel
    imgByteArr = BytesIO()
    np_array[np_array < 0.2] = 0
    PIL_image = Image.fromarray(
        np.uint8((1-np_array) * 255)).convert('RGBA')
    PIL_image = PIL_image.resize((width, height))
    pixdata = PIL_image.getdata()
    newData = []
    threshold = 140
    for pix in pixdata:
        if pix[0] < threshold and pix[1] < threshold and pix[2] < threshold:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(pix)
    PIL_image.putdata(newData)
    PIL_image.save(imgByteArr, format="PNG")
    imgByteArr = imgByteArr.getvalue()

    tx_img = SilAdapter.SutExchange.TransmittedImage()
    tx_img.dataArray = bytearray(imgByteArr)
    tx_img.imageName = str(name)
    tx_img.width = width
    tx_img.height = height
    return tx_img

def prep_annotation(labelids, labels, confs, bboxs, topk=3):
    anno_list = []
    for i in range(topk):
        anno = SilAdapter.SutExchange.Annotation()                                   
        bbox = SilAdapter.SutExchange.Rectangle()
        anno.labelID = int(labelids[i])
        anno.label = str(labels[i])
        anno.confidence = float(confs[i])
        raw_bbox = bboxs[i]
        bbox.xMin = int(raw_bbox[0])
        bbox.xMax = int(raw_bbox[2])
        bbox.yMin = int(raw_bbox[1])
        bbox.yMax = int(raw_bbox[3])

        anno.boundingBox = bbox
        anno_list.append(anno)
    return anno_list

def prep_annotation_classifier(labelids, labels, confs,  topk=3):
    anno_list = []
    for i in range(topk):
        anno = SilAdapter.SutExchange.Annotation()
        anno.labelID = int(labelids[i])
        anno.label = str(labels[i])
        anno.confidence = float(confs[i])
        anno_list.append(anno)
    return anno_list

def decode_bytes_img_do(message_bytes) -> Image:
    with BytesIO(message_bytes) as stream:
        image = Image.open(stream).convert("RGB")

    return image

def decode_base64_str_img(base64_string):
    base64_bytes = base64_string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    with BytesIO(message_bytes) as stream:
        image = Image.open(stream).convert("RGB")

    return image


def retrieve_canoe_img():
    try:
        print("Trying to retrieve data from CANoe")  
        img_do = SilAdapter.SutExchange.InputImage.inputImage.copy()
    except:
        print("Trying to retrieve data from CANoe")
        return False

    try:
        img = Image.open(io.BytesIO(img_do.dataArray))

    except TypeError:
        img = decode_base64_str_img(img_do.dataArray)

    except UnicodeEncodeError:
        img = decode_bytes_img_do(img_do.dataArray)

    except:
        print("Can't read image")
        return

    return img