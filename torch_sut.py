import os
import copy

import torchvision
from torchvision import transforms
from PIL import Image

import demo_utils
import SilAdapter
import label_maps

class sut():
    def __init__(self):
        SilAdapter.connect()
        self.load_model()
        self.label_map = label_maps.get_coco_label_map()
        self.input = []

    def __del__(self):
        SilAdapter.disconnect()

    def load_model(self):
        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            pretrained=True)
        self.model.eval()
        print("Model loaded")

    def prep_in_data(self):
        img = demo_utils.retrieve_canoe_img()
        print("New input data received")

        if img is not None:
            pil_to_tensor = transforms.ToTensor()(img).unsqueeze_(0)
            self.input = pil_to_tensor
            return pil_to_tensor

    def prep_out_data(self, **kwargs):
        print("prep out data")
        anno_list = demo_utils.prep_annotation(self.output[0]["labels"].detach().numpy(),
                                    [self.label_map[v] for v in self.output[0]["labels"].detach().numpy()],
                                    self.output[0]["scores"].detach().numpy(),
                                    self.output[0]["boxes"].detach().numpy(),
                                    topk = 15)

        SilAdapter.SutExchange.ImageAnnotation.annotations=anno_list

    def inference(self, **kwargs):
        print("Trying to inference")
        self.output = self.model(self.input)
        print(self.output[0]["scores"][0])

    def xai_inference(self, **kwargs):
        if not(hasattr(self, "xai_model")):
            print("wrapping the model")
            os.environ["PYDEVD_WARN_EVALUATION_TIMEOUT"] = "10"  # if the model is deployed on CPU, it can be quite slow
            self.xai_model = demo_utils.torch_guided_backprop_wrap(self.model)

        grad_input = copy.deepcopy(self.input)      
        self.xai_map  = demo_utils.torch_backprop(self.xai_model, grad_input)
        print("xAI gradient calculation done")

    def prep_out_xai(self, **kwargs):
        tx_img = demo_utils.prep_xai_send("xai_map",
                                        self.xai_map,
                                        self.input.shape[3],
                                        self.input.shape[2])
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
            print("Gather AI explanation")
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
