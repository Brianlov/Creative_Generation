import streamlit as st
from transformers import pipeline

import streamlit as st
from transformers import pipeline

# Path to the model
model_path = "/content/text_lora_model"

# Load the pipeline on CPU
generator = pipeline("text-generation", model=model_path, device=-1)  # CPU mode

# Input for the prompt
prompt = st.text_input("Enter a prompt:")

# Generate text when the button is clicked
if st.button("Generate Text"):
    if prompt:
        result = generator(prompt, max_length=20, num_return_sequences=1)
        st.write("Generated Text:")
        st.write(result[0]['generated_text'])
    else:
        st.write("Please enter a prompt.")
