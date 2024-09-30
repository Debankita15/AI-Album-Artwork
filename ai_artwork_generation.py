# ai_artwork_generation.py
import torch
from diffusers import StableDiffusionPipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def generate_artwork(prompt, output_path):
    """
    Generates artwork based on a text prompt using Stable Diffusion.
    
    Parameters:
        prompt (str): The text prompt to generate artwork.
        output_path (str): The file path to save the generated artwork.
    
    Returns:
        None
    """
    try:
        # Retrieve the Hugging Face token from environment variables
        huggingface_token = os.getenv('HUGGINGFACE_TOKEN')
        if not huggingface_token:
            raise ValueError("HUGGINGFACE_TOKEN is not set in environment variables.")
        
        # Check if CUDA is available for GPU acceleration
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        # Load the Stable Diffusion model from Hugging Face with authentication
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            use_auth_token=huggingface_token
        )
        pipe = pipe.to(device)

        # Optional: Enable memory-efficient attention if using a GPU
        if device == "cuda":
            pipe.enable_attention_slicing()

        # Generate the image
        print("Generating artwork...")
        image = pipe(prompt).images[0]

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the image
        image.save(output_path)
        print(f"Artwork generated successfully at {output_path}")

    except Exception as e:
        print(f"Error during artwork generation: {e}")
