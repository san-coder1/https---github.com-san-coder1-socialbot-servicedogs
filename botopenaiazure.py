import os
from openai import AzureOpenAI
from prompthelper import *

def get_response_from_openai(user_input):
    """
    Creates an Azure OpenAI client and generates response using Azure Open AI endpoint & key
    """
    client = AzureOpenAI(
        azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-01"
    )
    
    messages = get_messages(user_input)  

    completion = client.chat.completions.create (
        messages = messages,
        model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return completion.choices[0].message.content

def main():
    print("bot: Hello! how can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("bot: goodbye!")
            break

        response = get_response_from_openai(user_input)

        print("bot:", response)

if __name__ == "__main__":
    main()