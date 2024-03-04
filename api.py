import replicate

import os
os.environ["REPLICATE_API_TOKEN"] = "r8_JGNyG3Yu1sZqWvGoCBSA95Rp8g95MnF18b7Lj"


output = replicate.run(
    "yorickvp/llava-13b:a0fdc44e4f2e1f20f2bb4e27846899953ac8e66c5886c5878fa1d6b73ce009e5",
    input={
        "image": "https://th.bing.com/th/id/OIP.5v96A-PPJ70qVOkFzcu1CAAAAA?w=400&h=421&rs=1&pid=ImgDetMain",
        "top_p": 1,
        "prompt": "Are you allowed to swim here?",
        "max_tokens": 1024,
        "temperature": 0.2
    }
)

for item in output:
    # https://replicate.com/yorickvp/llava-13b/api#output-schema
    print(item, end="")