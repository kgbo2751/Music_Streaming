from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .jellyfin_client import get_my_music

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home(request: Request):
    # 5곡 가져오기
    music_list = get_my_music(limit=5)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "music_list": music_list}
    )