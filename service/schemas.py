import datetime
from typing import List, Union, Optional

from pydantic import BaseModel


class ResourceCreate(BaseModel):
    url: str
    keyword: str
    info: str

