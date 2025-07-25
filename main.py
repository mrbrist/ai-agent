import os
import sys
from dotenv import load_dotenv
from google import genai
from config import SYSTEM_PROMPT

from functions.get_files_info import schema_get_files_info, available_functions
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    user_prompt = sys.argv[1]

    messages = []
    messages.append(genai.types.Content(
        role='user', parts=[genai.types.Part(text=user_prompt)]))

    for i in range(0, 20):
        agent_response = client.models.generate_content(model="gemini-2.0-flash-001",
                                                        contents=messages,
                                                        config=genai.types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT))

        if agent_response.candidates:
            for c in agent_response.candidates:
                if len(c.content.parts) == 1:
                    print(agent_response.text)
                    return
                messages.append(c.content)

        if agent_response.function_calls:
            response = call_function(agent_response.function_calls[0])
            messages.append(genai.types.Content(
                role='tool', parts=[response.parts[0]]))

            if response.parts[0].function_response.response:
                if len(sys.argv) >= 3:
                    if sys.argv[2] == "--verbose":
                        print(
                            f"-> {response.parts[0].function_response.response}")
            else:
                raise Exception("Function call failed")

        else:
            print(agent_response.text)

        if len(sys.argv) >= 3:
            if sys.argv[2] == "--verbose":
                print(f"User prompt: {sys.argv[1]}")
                print(
                    f"Prompt tokens: {agent_response.usage_metadata.prompt_token_count}")
                print(
                    f"Response tokens: {agent_response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
