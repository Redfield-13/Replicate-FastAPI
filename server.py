from typing import Union
from fastapi import FastAPI
import replicate
import os
import requests
import time
import json
import ast

# Replace with your actual Replicate API token
api_token = "r8_TUB6o0Jc8ZNjce850ARcYaikasKKSPa27qrAB"

req_url = "https://api.replicate.com/v1/predictions"


headers = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json"
}


x_api_key = "3519453c563ceedb574c541cf00636f0f9d3b66c"
billig_url = "http://57.128.22.167:7775/bill-user"
billng_headers = {
    'x-api-key': "3519453c563ceedb574c541cf00636f0f9d3b66c",
    "Content-Type": "application/json"
}


os.environ["REPLICATE_API_TOKEN"] = "r8_TUB6o0Jc8ZNjce850ARcYaikasKKSPa27qrAB"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/llava")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None, top_p: Union[float, None] = None, temperature: Union[float, None] = None, max_tokens: Union[int, None] = None):
    
    payload = {
        "version": "a0fdc44e4f2e1f20f2bb4e27846899953ac8e66c5886c5878fa1d6b73ce009e5",
        "input": {
        "image": url,
        "top_p": top_p,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
        }
    }
    response = requests.post(req_url, headers=headers, json=payload)

    print(response)
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"llava_images_inquiries", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    output = requests.get(get_url, headers=headers).json()['output']
    message = ""
    print(response)
    for item in output:       
        print(item, end="")
        message = message + item


    return {"Description": message}


@app.get("/photomaker")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None, negprompt: Union[str, None] = None, style_name: Union[str, None] = None, num_steps: Union[int, None] = None, style_ratio: Union[int, None] = None, num_output: Union[int, None] = None, guide: Union[int, None] = None, seed: Union[int, None] = None):
    payload = {
        "version": "ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4",
        "input": {
        "prompt":"img" + prompt,
        "num_steps": num_steps,
        "style_name": style_name,
        "input_image": url,
        "num_outputs": num_output,
        "guidance_scale": guide,
        "negative_prompt": negprompt,
        "style_strength_ratio": style_ratio
        }
    }
    response = requests.post(req_url, headers=headers, json=payload)

    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(5)

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_photo_maker", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/musicgen")
def read_image(model: Union[str, None] = None, prompt: Union[str, None] = None, duration: Union[int, None] = None):

    payload = {
            "version": "b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
            "input": {
                "top_k": 250,
                "top_p": 0,
                "prompt": 'have piano',
                "duration": 3,
                "temperature": 1,
                "continuation": False,
                "model_version": 'stereo-melody-large',
                "output_format": "wav",
                "continuation_start": 0,
                "multi_band_diffusion": False,
                "normalization_strategy": "peak",
                "classifier_free_guidance": 3
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(5)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}

@app.get("/multilang")
def read_image(audiourl: Union[str, None] = None, source_lang: Union[str, None] = None, target_lang: Union[str, None] = None, duration_factor: Union[int, None] = None):

    payload = {
            "version": "fe1ce551597dee59a90f1fb418747c81214177f28c4e8728df96b06d2a2a6093",
            "input": {
            "audio_input": audiourl,
            "source_lang": source_lang,
            "target_lang": target_lang,
            "duration_factor": duration_factor
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(8)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_multi_lang", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}

@app.get("/subtitler")
def read_image(videoUrl: Union[str, None] = None, batch_size: Union[int, None] = None):

    payload = {
            "version": "410415fa53d2d3cfb180c2bbbf4a4a8bdb13f794e1bac515244741ef8685e4b3",
            "input": {
            "file": videoUrl,
            "batch_size": batch_size
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(8)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_subtitler", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())
    output_array = requests.get(get_url, headers=headers).json()['output']
    array = ast.literal_eval(output_array)
    final_output = ''
    print(output_array)
    for item in array:
      final_output += item["text"]
    return {"link": final_output}


@app.get("/objectidentify")
def read_image(videourl: Union[str, None] = None, mode: Union[str, None] = None):

    payload = {
            "version": "0603fcf7e739006289629061606d265e2c5e8876cfbcd470925ad96b17a77231",
            "input": {
            "mode": mode,
            "video": videourl
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(5)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_object_identify", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/yollo")
def read_image(imageUrl: Union[str, None] = None, class_name: Union[str, None] = None, num_of_box: Union[int, None] = None, score_thr: Union[float, None] = None, nms_thr: Union[float, None] = None, return_json: Union[bool, None] = None):

    payload = {
            "version": "dc084a6692fe16e76d780e4ee218680fee1b09ecba9dca9dbd2b0579f951bf38",
            "input": {
            "nms_thr": nms_thr,
            "score_thr": score_thr,
            "class_names": class_name,
            "input_media": imageUrl,
            "return_json": return_json,
            "max_num_boxes": num_of_box
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
      if response_status == "failed":
        print(requests.get(get_url, headers=headers).json())
        break
      time.sleep(5)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_yollo", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/waveform")
def read_image(audioUrl: Union[str, None] = None, bg_color: Union[str, None] = None, fg_alpha: Union[int, None] = None, bars_color: Union[str, None] = None, bar_count: Union[int, None] = None, bar_width: Union[int, None] = None, caption_text: Union[str, None] = None):

    payload = {
            "version": "116cf9b97d0a117cfe64310637bf99ae8542cc35d813744c6ab178a3e134ff5a",
            "input": {
            "audio": audioUrl,
            "bg_color": bg_color,
            "fg_alpha": fg_alpha,
            "bar_count": bar_count,
            "bar_width": bar_width,
            "bars_color": bars_color,
            "caption_text": caption_text
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_waveform", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/llavabb")
def read_image(imageUrl: Union[str, None] = None, prompt: Union[str, None] = None, top_p: Union[int, None] = None, temperature: Union[int, None] = None, max_tokens: Union[int, None] = None, history: Union[str, None] = None):

    payload = {
            "version": "41ecfbfb261e6c1adf3ad896c9066ca98346996d7c4045c5bc944a79d430f174",
            "input": {
            "image": imageUrl,
            "top_p": top_p,
            "prompt": "What\'"+prompt,
            "history": history,
            "max_tokens": max_tokens,
            "temperature": temperature
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_llavabb", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/pasd")
def read_image(imageUrl: Union[str, None] = None, prompt: Union[str, None] = None, Negprompt: Union[str, None] = None, seed: Union[int, None] = None, guide_scale: Union[int, None] = None, conditioning_scale: Union[int, None] = None, denoise_steps: Union[int, None] = None, upsample_scale: Union[int, None] = None):

    payload = {
            "version": "d59e83ee13c42b137aee558c483e3acc0a8ecdacb1444a7be48152f008dcc195",
            "input": {
            "image": imageUrl,
            "prompt": prompt,
            "n_prompt": Negprompt,
            "denoise_steps": denoise_steps,
            "guidance_scale": guide_scale,
            "upsample_scale": upsample_scale,
            "conditioning_scale": conditioning_scale
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_pasd", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/animate")
def read_image(model: Union[str, None] = None, ModuleType: Union[str, None] = None, prompt: Union[str, None] = None, n_prompt: Union[str, None] = None, steps: Union[int, None] = None, guidance_scale: Union[int, None] = None, seed: Union[int, None] = None):

    payload = {
            "version": "beecf59c4aee8d81bf04f0381033dfa10dc16e845b4ae00d281e2fa377e48a9f",
            "input": {
            "path": ModuleType,
            "seed": seed,
            "steps": steps,
            "prompt": prompt,
            "n_prompt": n_prompt,
            "motion_module": model,
            "guidance_scale": guidance_scale
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_animate", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/infinitezoom")
def read_image(output_format: Union[str, None] = None, prompt: Union[str, None] = None,  inpaint_iter: Union[int, None] = None):

    payload = {
            "version": "a2527c5074fc0cf9fa6015a40d75d080d1ddf7082fabe142f1ccd882c18fce61",
            "input": {
            "prompt": prompt,
            "inpaint_iter": inpaint_iter,
            "output_format": output_format
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_infinite_zoom", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/diffusionanime")
def read_image(prompt_start: Union[str, None] = None, prompt_end: Union[str, None] = None,  width: Union[int, None] = None,  hieght: Union[int, None] = None,  num_inference_steps: Union[int, None] = None,  prompt_strength: Union[int, None] = None,
num_animation_frames: Union[int, None] = None, num_interpolation_steps: Union[int, None] = None, guidance_scale: Union[int, None] = None, gif_frames_per_second: Union[int, None] = None,  
gif_ping_pong: Union[int, None] = None,  film_interpolation: Union[bool, None] = None,  intermediate_output: Union[bool, None] = None, seed: Union[int, None] = None, output_format: Union[str, None] = None,):

    payload = {
            "version": "ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5",
            "input": {
            "width": 512,
            "height": 512,
            "prompt_end": "tall rectangular black monolith, a white room in the future with a bed, victorian details and a tall black monolith, a detailed matte painting by Wes Anderson, behance, light and space, reimagined by industrial light and magic, matte painting, criterion collection",
            "prompt_start": "tall rectangular black monolith, monkeys in the desert looking at a large tall monolith, a detailed matte painting by Wes Anderson, behance, light and space, reimagined by industrial light and magic, matte painting, criterion collection",
            "gif_ping_pong": true,
            "output_format": "mp4",
            "guidance_scale": 7.5,
            "prompt_strength": 0.9,
            "film_interpolation": true,
            "intermediate_output": false,
            "num_inference_steps": 50,
            "num_animation_frames": 25,
            "gif_frames_per_second": 20,
            "num_interpolation_steps": 5
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    print(response.json())
    get_url = response.json()['urls']['get']
    response_status = requests.get(get_url, headers=headers).json()['status']
    print(response_status)
    while response_status != 'succeeded':
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_diffusion_anime", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}