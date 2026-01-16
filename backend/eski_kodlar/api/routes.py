# from fastapi import APIRouter
# from pydantic import BaseModel
# from ebced.hesaplayici import isim_ebced_hesapla

# router = APIRouter(prefix="/ebced", tags=["Ebced"])


# class IsimRequest(BaseModel):
#     isim: str


# class IsimResponse(BaseModel):
#     isim: str
#     ebced: int


# @router.post("/isim", response_model=IsimResponse)
# def isim_ebced_endpoint(data: IsimRequest):
#     toplam = isim_ebced_hesapla(data.isim)
#     return {
#         "isim": data.isim,
#         "ebced": toplam
#     }





# from fastapi import APIRouter
# from schemas.yil import YilYorumuRequest
# from ebced.element import yil_element_hesapla
# from yorumlar.yil_yorumlari import yil_yorumlari
# from yorumlar.eksik_element_yorumlari import eksik_element_yorumlari

# router = APIRouter()

# @router.post("/yil-yorumu")
# def yil_yorumu(data: YilYorumuRequest):

#     yil_element = yil_element_hesapla(data.yil)
#     kisi_element = data.kisi_element

#     baskin_element = max(kisi_element, key=kisi_element.get)



#     return {
#         "yil": data.yil,
#         "yil_element": yil_element,
#         "baskin_element": baskin_element,
       
#     }

# @router.get("/")
# def root():
#     return {"status": "API ayakta"}


# from fastapi import APIRouter
# from schemas import YilYorumRequest 
# from ebced.analiz_motoru import tam_analiz
# from ebced.element import yil_etkisi
# from ebced.yorum_motoru import element_yorumlari
# from ebced.isim_analizi import isim_soyisim_ebced
# from ebced.element import yil_detayli_etkisi



# router = APIRouter()



# @router.get("/")
# def health_check():
#     return {"status": "API çalışıyor"}

# @router.get("/ebced")
# def ebced_endpoint(isim: str, soyisim: str):
#     return isim_soyisim_ebced(isim, soyisim)

# @router.post("/yil-yorumu")
# def yil_yorumu(data: dict):
#     kisi_element = data["kisi_element"]
#     yil_element = data["yil_element"]
#     return {
#         "yorumlar": yil_etkisi(kisi_element, yil_element)
#     }

# @router.post("/element-yorumu")
# def element_yorumu(data: dict):
#     kisi_element = data["kisi_element"]
#     return {
#         "yorumlar": element_yorumlari(kisi_element)
#     }

# @router.post("/tam-analiz")
# def analiz(data: dict):
#     kisi_element = data["kisi_element"]
#     yil_element = data["yil_element"]
#     return tam_analiz(kisi_element, yil_element)

# @router.post("/yil-detay")
# def yil_detay(data: YilYorumRequest):
#     return {
#         "yorumlar": yil_detayli_etkisi(
#             data.kisi_element.dict(),
#             data.yil_element
#         )
#     }

from fastapi import APIRouter
from schemas.yil import YilYorumRequest, YilYorumResponse
from yorumlar.yil_yorumlari import yil_yorumlari
from yorumlar.eksik_element_yorumlari import eksik_element_yorumlari
from ebced.tam_analiz import tam_analiz
from yorumlar.baskin_element_yorumlari import baskin_element_yorumlari
from yorumlar.eksik_element_yorumlari import eksik_element_yorumlari

router = APIRouter()


@router.post("/yil-yorumu", response_model=YilYorumResponse)
def yil_yorumu(data: YilYorumRequest):
    kisi_element = data.kisi_element
    yil_element = data.yil_element

    baskin_element = max(kisi_element, key=kisi_element.get)

    yorumlar = []
    yorumlar += yil_yorumlari(baskin_element, yil_element)
    yorumlar += eksik_element_yorumlari(kisi_element)

    return {
        "baskin_element": baskin_element,
        "yorumlar": yorumlar
    }


@router.post("/tam-analiz")
def tam_analiz_endpoint(data: dict):
    return tam_analiz(
        data.get("isim"),
        data.get("soyisim"),
        data.get("yil")
    )