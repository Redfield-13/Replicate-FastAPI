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
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None,
                top_p: Union[float, None] = None, temperature: Union[float, None] = None,
                  max_tokens: Union[int, None] = None):
    output = replicate.run(
        "yorickvp/llava-13b:a0fdc44e4f2e1f20f2bb4e27846899953ac8e66c5886c5878fa1d6b73ce009e5",
        input={
            "image":url,
            "top_p": top_p,
            "prompt":prompt ,
            "max_tokens": max_tokens,
            "temperature": temperature/100
        }
    )
    message = ""
    for item in output:       
        print(item, end="")
        message = message + item
    return {"message":message}


@app.get("/photomaker")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None,
                negprompt: Union[str, None] = None, style_name: Union[str, None] = None,
                  num_steps: Union[int, None] = None, style_ratio: Union[int, None] = None,
                    num_output: Union[int, None] = None, guide: Union[int, None] = None,
                      seed: Union[int, None] = None):
    output = replicate.run(
        "tencentarc/photomaker:ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4",
        input={
            "prompt":"img" + prompt,
            "num_steps": num_steps,
            "style_name": style_name,
            "input_image": url,
            "num_outputs": num_output,
            "guidance_scale": guide,
            "negative_prompt": negprompt,
            "style_strength_ratio": style_ratio
            }
    )
    return {"message":output}


@app.get("/musicgen")
def read_image(model: Union[str, None] = None, prompt: Union[str, None] = None,
                duration: Union[int, None] = None):
    output = replicate.run(
        "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
        input={
            "top_k": 250,
            "top_p": 0,
            "prompt": prompt,
            "duration": duration,
            "temperature": 1,
            "continuation": False,
            "model_version": model,
            "output_format": "wav",
            "continuation_start": 0,
            "multi_band_diffusion": False,
            "normalization_strategy": "peak",
            "classifier_free_guidance": 3
            }
    )
    print(output)
    return {"link":output}

@app.get("/audio-to-waverform")
def read_image(audio: Union[str, None] = None, caption_text: Union[str, None] = None):
    """Create a waveform video from audio"""
    output = replicate.run(
        "fofr/audio-to-waveform:116cf9b97d0a117cfe64310637bf99ae8542cc35d813744c6ab178a3e134ff5a",
        input={
            "audio": audio,
            #background color of the waveform
            "bg_color": "#000000",
            #opacity of foreground waveform
            "fg_alpha": 0.75,
            #number of bars in the waveform
            "bar_count": 100,
            #width of bars in wave form
            "bar_width": 0.4,
            #color of the waveform
            "bars_color": "#ffffff",
            #catption text for the video
            "caption_text": caption_text
        }
    )
    print(output)
    return {"message": output}

@app.get("/llave-v1-6")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None,
                top_p: Union[float, None] = None, temperature: Union[float, None] = None,
                 max_tokens: Union[int, None] = None):
    """LLaVA v1.6: Large Language and Vision Assistant (Nous-Hermes-2-34B)"""
    output = replicate.run(
        "yorickvp/llava-13b:a0fdc44e4f2e1f20f2bb4e27846899953ac8e66c5886c5878fa1d6b73ce009e5",
        input={
            "image":url,
            "top_p": top_p,
            "prompt":prompt ,
            "max_tokens": max_tokens,
            "temperature": temperature/100
        }
    )
    message = ""
    for item in output:       
        print(item, end="")
        message = message + item
    return {"message":message}

@app.get("/stable_diffusion_infinite_zoom")
def read_image(prompt: Union[str, None] = None,
                output_format: Union[str, None] = None, inpaint_iter: Union[int, None] = 2):
    """Use Runway's Stable-diffusion inpainting model to create an infinite loop video"""
    output = replicate.run(
    "arielreplicate/stable_diffusion_infinite_zoom:a2527c5074fc0cf9fa6015a40d75d080d1ddf7082fabe142f1ccd882c18fce61",
    input={
        "prompt": prompt,
        "inpaint_iter": inpaint_iter,
        "output_format": output_format
    })
    print(output)
    return {"message": output}
