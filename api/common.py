from service.image import image_service


class CommonAPI:
    def __init__(self):
        self.image_service = image_service

    def get_images(self, keyword: str = ""):
        images = self.image_service.get_images(keyword)
        return images


common_api = CommonAPI()
