import streamlit as st
import groq
from openai import OpenAI
from diffusers import StableDiffusionPipeline
import torch
from api_key import groq_api_key


client_groq = groq.Groq(
    api_key=groq_api_key,
)

model = "llama-3.1-8b-instant"


pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", cache_dir="model")
pipe = pipe.to("cpu")


# set app to wide mode
st.set_page_config(layout='wide')
# title of app
st.title('BlogCraft: Your AI Writing Companion')

# create a sub-header
st.subheader('Now you can craft perfect blogs with the help of AI.\n BlogCraft is your new AI Blog Campanion')


# sidebar for user input
with st.sidebar:
    st.title('Input Your Blog Details')
    st.subheader('Enter Details of the Blog You want to generate')

    # Blog title
    blog_title = st.text_input('Blog Title')

    # keywords input
    Keywords = st.text_area('Keywords (comma-separated)')

    # Number of words 
    num_words = st.slider('Number of Words', min_value=250, max_value=1000, step=250)

    # Number of images 
    num_images = st.number_input('Number of Images', min_value=1, max_value=5, step=1)

    blog = f"""Generate a comprehensive and engaging blog post based on the title "{blog_title}", incorporating the following keywords:{Keywords}.

    The blog post should be approximately {num_words} words in length and written for an online audience. Ensure that all specified keywords are naturally and meaningfully integrated into the content. The article must be original, informative, and maintain a clear, consistent tone throughout. The final output should provide valuable insights while remaining accessible and engaging for readers."""

    # Submit button
    submit_button = st.button('Generate My Blog')

if submit_button:
    chat_completion = client_groq.chat.completions.create(
        messages=[{"role": "user", "content": blog}],
        model=model,
    )
    response = chat_completion.choices[0].message.content

    st.write(response)

    # Generate image prompts based on the blog
    prompt_generation = f"Generate {num_images} detailed and creative image prompts based on the blog title '{blog_title}' and keywords '{Keywords}'. Each prompt should be suitable for Stable Diffusion image generation and illustrate aspects of the blog post. Number them as 1., 2., etc."

    chat_completion_prompts = client_groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt_generation}],
        model=model,
    )
    prompts_response = chat_completion_prompts.choices[0].message.content

    # Parse the prompts (assuming numbered list)
    prompts = []
    for line in prompts_response.split('\n'):
        if line.strip() and line[0].isdigit():
            prompts.append(line.split('. ', 1)[1].strip())

    # Generate and display images with loading indicators
    st.subheader("Generated Images")
    for i, prompt in enumerate(prompts[:num_images]):
        with st.spinner(f"Generating image {i+1}..."):
            image = pipe(prompt).images[0]
        st.image(image, caption=f"Image {i+1}: {prompt}")
