from typing import Union

from fastapi import FastAPI

import replicate

import os
os.environ["REPLICATE_API_TOKEN"] = "r8_JGNyG3Yu1sZqWvGoCBSA95Rp8g95MnF18b7Lj"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/imagedesc")
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
        # https://replicate.com/yorickvp/llava-13b/api#output-schema
        
        print(item, end="")
        message = message + item

    return {"message":message}