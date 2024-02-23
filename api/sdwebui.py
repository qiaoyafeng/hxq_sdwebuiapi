from api.client import api as api_client
from service.image import image_service


class SDWebuiAPI:
    def __init__(self):
        self.api_client = api_client
        self.image_service = image_service

    def text2img_api(self, txt2img_req):
        print(f"txt2img_req type: {type(txt2img_req)}, txt2img_req: {txt2img_req}")
        resp = self.api_client.txt2img(**txt2img_req)
        images = resp.images
        parameters = resp.parameters
        info = resp.info
        images_urls = self.image_service.save_images(images, parameters, info)
        return images_urls

    def get_loras(self):
        resp = self.api_client.get_loras()
        return resp

    def get_sd_models(self):
        resp = self.api_client.get_loras()
        return resp


sd_webuiapi = SDWebuiAPI()
