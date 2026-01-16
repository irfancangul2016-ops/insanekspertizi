from pydantic import BaseModel
from typing import Dict, List


class KisiElementleri(BaseModel):
    Ateş: int
    Su: int
    Hava: int
    Toprak: int


class YilYorumRequest(BaseModel):
    yil_element: str
    kisi_element: KisiElementleri


class YorumResponse(BaseModel):
    yorumlar: List[str]


class TamAnalizResponse(BaseModel):
    baskin_element: str
    yorumlar: List[str]