# AI Blog Generator: Your AI Writing Companion

## Description

AI Blog Generator is an AI-powered blogging assistant built with Streamlit. It helps you generate comprehensive and engaging blog posts using advanced language models and create accompanying images with Stable Diffusion.

## Features

- Generate blog posts based on title and keywords
- Customize word count (250-1000 words)
- Create up to 5 relevant images per blog
- Uses Groq's Llama 3.1-8B model for text generation
- Stable Diffusion v1-4 for image generation
- User-friendly Streamlit interface

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd AI_Blog_Generator

   ```

2. Install dependencies:
   ```
   pip install streamlit groq diffusers torch
   ```

## Setup

1. Obtain a Groq API key from [Groq Console](https://console.groq.com/).

2. Edit `api_key.py` and replace `"Your_groq_api_key"` with your actual API key:

   ```python
   groq_api_key = "your_actual_api_key_here"
   ```

3. The Stable Diffusion model will be downloaded automatically on first run (cached in `model/` directory).

## Usage

1. Run the application:

   ```
   streamlit run app.py
   ```

2. Open the provided URL in your browser.

3. In the sidebar:

   - Enter your blog title
   - Input keywords (comma-separated)
   - Select desired word count
   - Choose number of images (1-5)

4. Click "Generate My Blog" to create your content.

## Dependencies

- streamlit
- groq
- diffusers
- torch

## Notes

- First run may take longer due to model download.
- Ensure you have sufficient disk space for the model (~4GB).
- Images are generated on GPU for better performance.
