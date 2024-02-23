import json
import uuid
from config import Config
from service.crud import create_resource, get_resource
from service.schemas import ResourceCreate

TEMP_PATH = Config.get_temp_path()


class ImageService:
    def __init__(self):
        pass

    def save_images(self, images: list = [], parameters={}, info={}):
        print(f"save_images: images:{images}, parameters type: {type(parameters)}----parameters: {parameters}, info type:{type(info)}--info:{info}")
        images_urls = []
        for image in images:
            image_name = f"{uuid.uuid4().hex}.png"
            image_path = f"{TEMP_PATH}/{image_name}"
            image.save(image_path)
            create_resource(
                ResourceCreate(
                    url=image_name,
                    keyword=parameters.get("prompt", ""),
                    info=json.dumps(info),
                )
            )

            images_urls.append(image_path)
        return images_urls

    def get_images(self, keyword: str = ""):
        images = get_resource(keyword)
        return images


image_service = ImageService()



