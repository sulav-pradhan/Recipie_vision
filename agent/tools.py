import base64
import numpy as np
import tempfile
import os
import cv2

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()
# vision_llm = ChatOpenAI(model="gpt-4o")
# vision_llm = ChatGoogleGenerativeAI(model = "gemini-3-pro-preview")
vision_llm = ChatOllama(model = "qwen2.5vl:3b")

@tool
def extract_text(img_path: str) -> str:
    """
    Extracts text from an image specified by its file path. This function reads the
    image file, encodes the image data as base64, sends the image content to a
    vision-capable language model to extract text, and returns the resulting text
    content.

    :param img_path: The file path of the image from which text is to be extracted.
    :type img_path: str
    :return: Extracted text from the image, or an empty string if an error occurs
        during the process.
    :rtype: str
    :raises Exception: If any error occurs during image reading, encoding,
        or processing the response from the model.
    """
    all_text = ""
    try:
        # Read image and encode as base64
        with open(img_path, "rb") as image_file:
            image_bytes = image_file.read()

        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Prepare the prompt including the base64 image data
        message = [
            HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": (
                            "Extract all the text from this image. "
                            "Return only the extracted text, no explanations."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            )
        ]

        # Call the vision-capable model
        response = vision_llm.invoke(message)

        # Handle response.content which could be a list or string
        if isinstance(response.content, list):
            # Extract text from list of content blocks
            for block in response.content:
                if isinstance(block, dict) and block.get("type") == "text":
                    all_text += block.get("text", "") + "\n\n"
                elif isinstance(block, str):
                    all_text += block + "\n\n"
        else:
            # If it's a string, just append it
            all_text += response.content + "\n\n"

        return all_text.strip()

    except Exception as e:
        error_msg = f"Error extracting text: {str(e)}"
        print(error_msg)
        return ""