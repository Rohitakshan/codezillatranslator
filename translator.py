import openai
import os
from dotenv import load_dotenv
from prompt_templates import build_prompt

load_dotenv()
client = openai.OpenAI(api_key='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')

def translate_text(input_text, target_language, style, tone):
    prompt = build_prompt(input_text, target_language, style, tone)

    try:
        print("🧪 Prompt:\n", prompt)
        chat_response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a stylistic translator AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return chat_response.choices[0].message.content.strip()

    except Exception as e:
        print("💥 OpenAI API error:", e)


'''import openai
import os
from dotenv import load_dotenv
import gradio as gr
from prompt_templates import build_prompt

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key="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")



def translate_text(input_text, target_language, style, tone):
    prompt = build_prompt(input_text, target_language, style, tone)
    try:
        chat_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a stylistic translator AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return chat_response.choices[0].message.content.strip()
    except Exception as e:
        return f"💥 OpenAI API error: {e}"

# Dropdown options
LANGUAGES = [
    "English", "Spanish", "French", "German", "Chinese", "Japanese",
    "Russian", "Arabic", "Hindi", "Portuguese", "Italian"
]

STYLES = [
    "Formal", "Informal", "Poetic", "Technical", "Conversational"
]

TONES = [
    "Neutral", "Friendly", "Serious", "Enthusiastic", "Polite"
]

def translate_wrapper(input_text, target_language, style, tone):
    if not input_text.strip():
        return "⚠️ Please enter text to translate."
    return translate_text(input_text, target_language, style, tone)

with gr.Blocks() as demo:
    gr.Markdown("# 🌍 Stylish Translator")
    gr.Markdown("Translate text with your choice of language, style, and tone.")

    with gr.Row():
        target_lang = gr.Dropdown(LANGUAGES, label="Target Language", value="English")
        style_dd = gr.Dropdown(STYLES, label="Style", value="Formal")
        tone_dd = gr.Dropdown(TONES, label="Tone", value="Neutral")

    input_box = gr.Textbox(lines=6, placeholder="Type or paste your text here...", label="Input Text")
    output_box = gr.Textbox(lines=6, label="Translated Text", interactive=False)

    translate_btn = gr.Button("Translate ✨")
    translate_btn.click(
        fn=translate_wrapper,
        inputs=[input_box, target_lang, style_dd, tone_dd],
        outputs=[output_box]
    )

if __name__ == "__main__":
    demo.launch()'''




