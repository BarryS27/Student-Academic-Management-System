import os
from . import config

try:
    from openai import OpenAI
    from dotenv import load_dotenv
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

class AIAssistant:
    def __init__(self):
        self.client = None
        self.is_ready = False
        self._initialize_client()

    def _initialize_client(self):
        if AI_AVAILABLE:
            env_path = config.BASE_DIR / '.env'
            load_dotenv(dotenv_path=env_path)
            
            api_key = os.getenv("API_KEY")
            if api_key:
                self.client = OpenAI(api_key=api_key)
                self.is_ready = True

    def get_response(self, user_query, custom_system_prompt=None):
        if not AI_AVAILABLE:
            return "❌ Error: Missing libraries. Please run: pip install openai python-dotenv"
        
        if not self.is_ready or not self.client:
            return "❌ Error: API_KEY not found in .env file."

        sys_prompt = custom_system_prompt if custom_system_prompt and custom_system_prompt.strip() else config.DEFAULT_SYSTEM_PROMPT

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_query}
                ]
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ AI Connection Error: {str(e)}"