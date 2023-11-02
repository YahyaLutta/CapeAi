import openai
import os

openai.api_key = "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"
response = openai.Image.create(
    prompt="cad blueprint planes",
    n=1,
    size="1024x1024"
    )
    
image_url = response['data'][0]['url']
print(image_url)
    
    