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
