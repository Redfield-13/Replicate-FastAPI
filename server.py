from typing import Union
from fastapi import FastAPI
import replicate
import os


os.environ["REPLICATE_API_TOKEN"] = "r8_JGNyG3Yu1sZqWvGoCBSA95Rp8g95MnF18b7Lj"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/llava")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None):
    output = replicate.run(
        "yorickvp/llava-13b:a0fdc44e4f2e1f20f2bb4e27846899953ac8e66c5886c5878fa1d6b73ce009e5",
        input={
            "image":url,
            "top_p": 1,
            "prompt":prompt ,
            "max_tokens": 1024,
            "temperature": 0.2
        }
    )
    message = ""
    for item in output:       
        print(item, end="")
        message = message + item
    return {"message":message}


@app.get("/photomaker")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None):
    output = replicate.run(
        "tencentarc/photomaker:ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4",
        input={
            "prompt":"img" + prompt,
            "num_steps": 50,
            "style_name": "Photographic (Default)",
            "input_image": url,
            "num_outputs": 1,
            "guidance_scale": 5,
            "negative_prompt": "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
            "style_strength_ratio": 20
            }
    )
    return {"message":output}