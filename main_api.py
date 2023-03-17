from ai_manager import AIManager

from fastapi import FastAPI, Request
import uvicorn

import urllib3
import shutil
import base64


app = FastAPI()
http = urllib3.PoolManager()
ai = AIManager()
path_to_img = "img_api.jpg"


@app.post("/detect")
async def detect(info: Request):
    req_info = await info.json()

    img_url = req_info.get("img_url")
    if not(img_url is None):
        with open(path_to_img, "wb") as out:
            r = http.request('GET', img_url, preload_content=False)
            shutil.copyfileobj(r, out)
    else:
        img_base64 = req_info.get("img_base64")
        if img_base64 is None:
            return {"message": "No image for detect!"}
        decoded_img = base64.decode((img_base64))
        img_file = open(path_to_img, 'wb')
        img_file.write(decoded_img)
        img_file.close()

    detected_items = ai.detect_api(path_to_img)
    return_info = {"message": "Success!"}
    return_info['detected_items'] = detected_items

    return return_info


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5228, log_level="info")