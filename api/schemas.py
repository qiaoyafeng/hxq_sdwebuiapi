import datetime
from typing import List, Union, Optional

from pydantic import BaseModel


class Txt2ImgRequest(BaseModel):
    txt2img_input: dict = {
        "prompt": "",
        "negative_prompt": "",
        "seed": 1,
        "steps": 20,
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "n_iter": 1,
        "batch_size": 1,
    }
