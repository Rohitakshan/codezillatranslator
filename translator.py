import openai
import os
from dotenv import load_dotenv
from prompt_templates import build_prompt

load_dotenv()
client = openai.OpenAI(api_key="OPENAI_API_KEY")

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
