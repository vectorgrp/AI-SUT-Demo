import os
import copy

import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')
from PIL import Image
import numpy as np

import demo_utils
import SilAdapter
import label_maps

class sut():
    def __init__(self):
        SilAdapter.connect()
        self.load_model()
        self.label_map = label_maps.get_image_label_map()
        self.input = []

    def __del__(self):
        SilAdapter.disconnect()

    def load_model(self):
        self.model = tf.keras.applications.xception.Xception()


    def prep_in_data(self):
        print("New input data received")
        img = demo_utils.retrieve_canoe_img(SilAdapter.SutExchange.InputImage)
        self.origin_shape = img.size
        pil_to_tensor =  tf.convert_to_tensor(tf.keras.applications.xception.preprocess_input(np.expand_dims(img, axis=0)))
        size = (299, 299)
        pil_to_tensor = tf.image.resize(pil_to_tensor, size)
        
        self.input = pil_to_tensor
        return pil_to_tensor

    def prep_out_data(self, **kwargs):
        print("prep out data")
        anno_list = demo_utils.prep_annotation_classifier(self.topk.indices[0].numpy(),
                                    [self.label_map[v] for v in self.topk.indices[0].numpy()],
                                    self.topk.values[0].numpy(),
                                    topk = 3)

        SilAdapter.SutExchange.ImageAnnotation.annotations=anno_list


    def inference(self, **kwargs):
        print("Trying to inference")
        self.output = self.model(self.input)
        self.topk = tf.math.top_k(self.output, k =3)
        print(self.label_map[self.topk.indices[0][0].numpy()])

    def xai_inference(self, **kwargs):
        if not(hasattr(self, "xai_model")):
            print("wrapping the model")
            os.environ["PYDEVD_WARN_EVALUATION_TIMEOUT"] = "10"  # if the model is deployed on CPU, it can be quite slow
            self.xai_model = demo_utils.tf_guided_backprop_wrap(self.model)

        grad_input = copy.deepcopy(self.input)      
        self.xai_map  = demo_utils.tf_backprop(self.xai_model, grad_input)
        print("xAI gradient calculation done")

    def prep_out_xai(self, **kwargs):
        tx_img = demo_utils.prep_xai_send("xai_map",
                                        self.xai_map,
                                        self.origin_shape[0],
                                        self.origin_shape[1] )
        SilAdapter.SutExchange.ImageAnnotation.outputImage = tx_img
        print("xAI sent")

    def run(self):
        self.prep_in_data()
        op_num = SilAdapter.SutExchange.InputImage.operationMode.copy()

        if op_num.numerator == 0:
            print("Perform inference")
            self.inference()
            self.prep_out_data()

        elif op_num.numerator == 1:
            print("Gather explaination")
            self.xai_inference()
            self.prep_out_xai()
            self.inference()
            self.prep_out_data()

    def onImageChange(self, **kwargs):
        SilAdapter.SutExchange.InputImage.inputImage.register_on_update_handler(self.run)
        print("Callback active")
        return self.input


if __name__ == "__main__":
    sut_instance = sut()
    # uncomment to explicitely run an inference
    # sut_instance.run()
    sut_instance.onImageChange()
    print("Press any key to exit")
    input()
