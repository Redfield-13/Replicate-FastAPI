from typing import Union
from fastapi import FastAPI
import replicate
import os
import requests
import time

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
        "prompt": prompt,
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
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}

@app.get("/multilang")
def read_image(audiourl: Union[str, None] = None, source_lang: Union[str, None] = None, target_lang: Union[int, None] = None, duration_factor: Union[int, None] = None):

    payload = {
            "version": "fe1ce551597dee59a90f1fb418747c81214177f28c4e8728df96b06d2a2a6093",
            "input": {
            "audio_input": audiourl,
            "source_lang": source_lang,
            "target_lang": target_lang,
            "duration_factor": duration
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
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}

@app.get("/subtitler")
def read_image(videourl: Union[str, None] = None, batch_size: Union[str, None] = None):

    payload = {
            "version": "410415fa53d2d3cfb180c2bbbf4a4a8bdb13f794e1bac515244741ef8685e4b3",
            "input": {
            "file": videourl,
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
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


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
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/yollo")
def read_image(imageUrl: Union[str, None] = None, class_name: Union[str, None] = None, num_of_box: Union[str, None] = None, score_thr: Union[str, None] = None, nms_thr: Union[str, None] = None):

    payload = {
            "version": "dc084a6692fe16e76d780e4ee218680fee1b09ecba9dca9dbd2b0579f951bf38",
            "input": {
            "nms_thr": nms_thr,
            "score_thr": score_thr,
            "class_names": class_name,
            "input_media": imageUrl,
            "return_json": false,
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
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}


@app.get("/yollo")
def read_image(imageUrl: Union[str, None] = None, class_name: Union[str, None] = None, num_of_box: Union[str, None] = None, score_thr: Union[str, None] = None, nms_thr: Union[str, None] = None):

    payload = {
            "version": "dc084a6692fe16e76d780e4ee218680fee1b09ecba9dca9dbd2b0579f951bf38",
            "input": {
            "nms_thr": nms_thr,
            "score_thr": score_thr,
            "class_names": class_name,
            "input_media": imageUrl,
            "return_json": false,
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
      print(response)
      response_status = requests.get(get_url, headers=headers).json()['status']
      print(response_status)
    

    p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
    print(p_time)
    bill_body = { "billingId":"replicate_music_gen", "quantity":p_time }
    bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
    print(bill_res.json())

    return {"link":requests.get(get_url, headers=headers).json()['output']}