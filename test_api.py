from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_api():
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
    if not api_key:
        print("Error: OPEN_ROUTER_API_KEY is not set in the .env file.")
        return

    print("Testing connection to OpenRouter API...")
    try:
        # Initialize the model
        llm = ChatOpenAI(
            model="apodex/apodex-1.1-mini:free", 
            temperature=0.2,
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1"
        )
        
        # Send a simple query
        response = llm.invoke("Hello, are you working? Please reply with a short sentence.")
        
        # Parse the response (handling list returns just in case)
        content_raw = response.content
        if isinstance(content_raw, list):
            content_str = content_raw[0].get("text", "") if isinstance(content_raw[0], dict) else str(content_raw[0])
        else:
            content_str = str(content_raw)
            
        print("\nSuccess! API Key is valid and working. Received response:")
        print("-" * 40)
        print(content_str)
        print("-" * 40)
        
    except Exception as e:
        print("\nFailed to get a response. Please check if your API key is correct. Error details:")
        print(e)

if __name__ == "__main__":
    test_api()
