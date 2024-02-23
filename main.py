import os
import random
from typing import Union
import uvicorn

from fastapi.openapi.docs import get_swagger_ui_html

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, UploadFile, File, Body, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

import api.sdwebui
from api import common
from api.schemas import Txt2ImgRequest
from config import Config

app = FastAPI(
    title="HXQ SD Webui API", summary="HXQ SD Webui API", docs_url=None, redoc_url=None
)

origins = [
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


sd_webuiapi = api.sdwebui.sd_webuiapi
common_api = common.common_api

TEMP_PATH = Config.get_temp_path()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/js/swagger-ui-bundle.js",
        swagger_css_url="/static/js/swagger-ui.css",
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    image_list = common_api.get_images()

    return templates.TemplateResponse("index.html", {"request": request, "image_list": image_list})


@app.get("/get_file/{file_name}")
def get_file(file_name: str):
    file_path = os.path.isfile(os.path.join(TEMP_PATH, file_name))
    if file_path:
        return FileResponse(os.path.join(TEMP_PATH, file_name))
    else:
        return {"code": 404, "message": "file does not exist."}


@app.get("/get_images")
async def get_images(keyword: str = ""):
    images = common_api.get_images(keyword)
    return {"images": images, "info": f"images for {keyword}"}


@app.post("/api/txt2img")
async def txt2img(txt2img_request: Txt2ImgRequest):
    resp = sd_webuiapi.text2img_api(txt2img_request.txt2img_input)
    return f"txt2img success"


if __name__ == "__main__":
    uvicorn.run(app="__main__:app", host="0.0.0.0", port=32102, reload=True)
