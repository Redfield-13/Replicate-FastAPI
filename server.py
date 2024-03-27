from typing import Union
from fastapi import FastAPI
import replicate
import os
import requests
import time
import json
import ast

# Replace with your actual Replicate API token
api_token = "r8_bkSrCAbkZHKuYnVKrUoX87ERiykqDqG1Uz8AI"

req_url = "https://api.replicate.com/v1/predictions"


headers = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json"
}

def process_res(response):
  print(response.json())
  get_url = response.json()['urls']['get']
  response_status = requests.get(get_url, headers=headers).json()['status']
  print(response_status)
  while response_status != 'succeeded':
    response_status = requests.get(get_url, headers=headers).json()['status']
    print("status: " + response_status)
    if response_status == "failed":
      print(requests.get(get_url, headers=headers).json())
      break
    if response_status != "succeeded":
      time.sleep(7.5)
      

  p_time = requests.get(get_url, headers=headers).json()['metrics']['predict_time']
  print(p_time)
  bill_body = { "billingId":"replicate_diffusion_anime", "quantity":p_time }
  bill_res = requests.post(billig_url, headers=billng_headers, json=bill_body)
  print(bill_res.json())


  return {"link":requests.get(get_url, headers=headers).json()['output']}



x_api_key = "3519453c563ceedb574c541cf00636f0f9d3b66c"
billig_url = "http://57.128.22.167:7775/bill-user"
billng_headers = {
    'x-api-key': "3519453c563ceedb574c541cf00636f0f9d3b66c",
    "Content-Type": "application/json"
}


os.environ["REPLICATE_API_TOKEN"] = "r8_bkSrCAbkZHKuYnVKrUoX87ERiykqDqG1Uz8AI"

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

    return(process_res(response))


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

    return(process_res(response))


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
   
    return(process_res(response))

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
   
    return(process_res(response))

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
   
    return(process_res(response))


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
   
    return(process_res(response))


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
   
    return(process_res(response))


@app.get("/waveform")
def read_image(audioUrl: Union[str, None] = None, bg_color: Union[str, None] = "#000000", fg_alpha: Union[float, None] = 0.75, bar_count: Union[int, None] = 100, bar_width: Union[int, None] = 0.4, caption_text: Union[str, None] = "80s trancecore, driving rhythm section, ambient textures, boomwhackers, persian scale mode, tribute recording", bars_color: Union[str, None] = "#ffffff"):

    payload = {
            "version": "116cf9b97d0a117cfe64310637bf99ae8542cc35d813744c6ab178a3e134ff5a",
            "input": {
            "audio": audioUrl,
            "bg_color": "#000000",
            "fg_alpha": fg_alpha,
            "bar_count": bar_count,
            "bar_width": bar_width,
            "bars_color": bars_color,
            "caption_text": caption_text
          }
    }
    print(req_url)
    print(payload)

    response = requests.post(req_url, headers=headers, json=payload)
   
    return(process_res(response))


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
   
    return(process_res(response))


@app.get("/pasd")
def read_image(url: Union[str, None] = None, prompt: Union[str, None] = None, negprompt: Union[str, None] = None, seed: Union[float, None] = None, guide_scale: Union[float, None] = None, conditioning_scale: Union[float, None] = None, denoise_steps: Union[float, None] = None, upsample_scale: Union[float, None] = None):

    payload = {
            "version": "d59e83ee13c42b137aee558c483e3acc0a8ecdacb1444a7be48152f008dcc195",
            "input": {
            "image": url,
            "prompt": prompt,
            "n_prompt": negprompt,
            "denoise_steps": denoise_steps,
            "guidance_scale": guide_scale,
            "upsample_scale": upsample_scale,
            "conditioning_scale": conditioning_scale
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    return(process_res(response))


@app.get("/animate")
def read_image(model: Union[str, None] = None, ModuleType: Union[str, None] = None, prompt: Union[str, None] = None, n_prompt: Union[str, None] = None, steps: Union[float, None] = None, guidance_scale: Union[float, None] = None, seed: Union[float, None] = None):

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
   
    return(process_res(response))


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
   
    return(process_res(response))


@app.get("/diffusionanime")
def read_image(prompt_start: Union[str, None] = None, prompt_end: Union[str, None] = None, width: Union[int, None] = None, hieght: Union[int, None] = None, num_inference_steps: Union[float, None] = None, prompt_strength: Union[float, None] = None, num_animation_frames: Union[float, None] = None, num_interpolation_steps: Union[float, None] = None, guidance_scale: Union[float, None] = None, gif_frames_per_second: Union[float, None] = None,gif_ping_pong: Union[bool, None] = None,film_interpolation: Union[bool, None] = None,intermediate_output: Union[bool, None] = None,seed: Union[float, None] = None, output_format: Union[str, None] = None):

    payload = {
            "version": "ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5",
            "input": {
              "width": width,
              "height": hieght,
              "prompt_end": prompt_end,
              "prompt_start": prompt_start,
              "gif_ping_pong": gif_ping_pong,
              "output_format": output_format,
              "guidance_scale": guidance_scale,
              "prompt_strength": prompt_strength,
              "film_interpolation": film_interpolation,
              "intermediate_output": intermediate_output,
              "num_inference_steps": num_inference_steps,
              "num_animation_frames": num_animation_frames,
              "gif_frames_per_second": gif_frames_per_second,
              "num_interpolation_steps": num_interpolation_steps
            }
    }
    print(req_url)

    response = requests.post(req_url, headers=headers, json=payload)
   
    return(process_res(response))


@app.get("/coqui")
def read_image(text: Union[str, None] = None, speaker: Union[str, None] = None,  language: Union[str, None] = "en", cleanup_voice: Union[bool, None] = None):

    payload = {
            "version": "684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e",
            "input": {
              "text": text,
              "speaker": speaker,
              "language": language,
              "cleanup_voice": cleanup_voice
            }
    }
    print(payload)

    response = requests.post(req_url, headers=headers, json=payload)
   
    return(process_res(response))


@app.get("/stablediffusion")
def read_image(prompt: Union[str, None] = None, width: Union[int, None] = None, height: Union[int, None] = None, num_outputs: Union[int, None] = None, guidance_scale: Union[float, None] = None, scheduler: Union[str, None] = None,num_inference_steps: Union[float, None] = None):

      payload = {
              "version": "ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
              "input": {
                "width": width,
                "height": height,
                "prompt": prompt,
                "scheduler": scheduler,
                "num_outputs": num_outputs,
                "guidance_scale": guidance_scale,
                "num_inference_steps": num_inference_steps
              }
      }
      print(req_url)

      response = requests.post(req_url, headers=headers, json=payload)
    
      return(process_res(response))
