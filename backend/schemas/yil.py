from pydantic import BaseModel
from typing import Dict, List


class YilYorumRequest(BaseModel):
    yil_element: str
    kisi_element: Dict[str, int]


class YilYorumResponse(BaseModel):
    baskin_element: str
    yorumlar: List[str]