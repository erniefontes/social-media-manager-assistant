import os
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Load environment variables
load_dotenv()


class AnthropicHandler:
    def __init__(self):
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)

    def __post_init__(self):
        self.validate_api_key()

    def validate_api_key(self):
        # Implementation to validate the API key
        try:
            # Attempt a simple API call to validate the key
            self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1,
                messages=[{"role": "user", "content": "Hello."}],
            )
            return True
        except Exception as e:
            print(f"API key validation failed: {str(e)}")
            return False

    def send_prompt(self, prompt, max_tokens=1000):
        # Implementation to send a prompt to the Anthropic API
        try:
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            return response
        except Exception as e:
            self.handle_error(e)
            return None

    def handle_error(self, error):
        # Implementation for error handling
        print(f"An error occurred: {str(error)}")


# Example usage
if __name__ == "__main__":
    handler = AnthropicHandler()

    if handler.validate_api_key():
        print("API key is valid.")
        response = handler.send_prompt("Tell me a brief joke about programming.")
        if response:
            print("LLM Response:")
            print(response.content)
    else:
        print("Invalid API key. Please check your environment variables.")
