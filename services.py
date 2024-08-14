'''
Services utils
'''
import os
from openai import OpenAI


def generate_image(description):
    '''
    openAI service to request an image generation using the provided description.
    '''
    open_ai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    image_generation = open_ai.images.generate(
        model = 'dall-e-3',n = 1,size = '1024x1024',
        prompt = f'Generate an image using this description: {description}'
    )

    try:
        image_data = {
            'image_url': image_generation.data[0].url,
            'revised_prompt': image_generation.data[0].revised_prompt
        }
    except Exception:
        image_data = {}

    return image_data
