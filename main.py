import os
import uuid

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from lotify.client import Client

app = FastAPI()

templates = Jinja2Templates(directory="templates")

CLIENT_ID = os.getenv("LINE_CLIENT_ID")
SECRET = os.getenv("LINE_CLIENT_SECRET")
URI = os.getenv("LINE_REDIRECT_URI")
lotify = Client(client_id=CLIENT_ID, client_secret=SECRET, redirect_uri=URI)


@app.get("/")
async def home(request: Request):
    link = lotify.get_auth_link(state=uuid.uuid4())
    return templates.TemplateResponse(
        request=request, name="notify_index.html", context={"auth_url": link}
    )


@app.get("/callback")
async def confirm(code: str, request: Request):
    token = lotify.get_access_token(code)
    return templates.TemplateResponse(
        request=request, name="notify_confirm.html", context={"token": token}
    )


@app.post("/notify/send")
async def send(request: Request):
    payload = await request.json()
    response = lotify.send_message(
        access_token=payload.get("token"), message=payload.get("message")
    )
    return response


@app.post("/notify/send/sticker")
async def send_sticker(request: Request):
    payload = await request.json()
    response = lotify.send_message_with_sticker(
        access_token=payload.get("token"),
        message=payload.get("message"),
        sticker_id=630,
        sticker_package_id=4,
    )
    return response


@app.post("/notify/send/url")
async def send_url(request: Request):
    payload = await request.json()
    response = lotify.send_message_with_image_url(
        access_token=payload.get("token"),
        message=payload.get("message"),
        image_fullsize=payload.get("url"),
        image_thumbnail=payload.get("url"),
    )
    return response


@app.post("/notify/send/path")
async def send_file(request: Request):
    payload = await request.json()
    response = lotify.send_message_with_image_file(
        access_token=payload.get("token"),
        message=payload.get("message"),
        file=open("./test_data/dog.png", "rb"),
    )
    return response


@app.post("/notify/revoke")
async def revoke(request: Request):
    payload = await request.json()
    response = lotify.revoke(access_token=payload.get("token"))
    return response


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    uvicorn.run("main.app", host="0.0.0.0", port=port)
