"""
Services utils
"""

import logging
import os
from openai import OpenAI

logger = logging.getLogger(__name__)


def generate_image(description):
    """
    openAI service to request an image generation using the provided description.
    """
    open_ai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    prompt = f"Generate an image using this description: {description}"
    logger.info("→ image request | model=%s size=%s prompt=%r", "gpt-image-2", "1024x1024", prompt)

    image_generation = open_ai.images.generate(
        model="gpt-image-2",
        n=1,
        size="1024x1024",
        prompt=prompt,
    )

    try:
        image = image_generation.data[0]
        # gpt-image models return base64 image data rather than a hosted URL,
        # so wrap it in a data URI the browser can render directly.
        image_data = {
            "image_url": f"data:image/png;base64,{image.b64_json}",
            "revised_prompt": image.revised_prompt or "",
        }
        # Log the response summary but not the base64 blob, which is huge.
        logger.info(
            "← image response | revised_prompt=%r image_bytes=%d",
            image_data["revised_prompt"],
            len(image.b64_json or ""),
        )
    except Exception:
        logger.exception("← image request failed")
        image_data = {}

    return image_data
