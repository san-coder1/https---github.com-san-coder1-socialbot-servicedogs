import os
from openai import OpenAI
from prompthelper import *
from classifier import *

def get_response_from_openai(user_input, classifier):
    if not is_about_service_dogs(user_input, classifier):
        return "I'm sorry, I can only answer questions about service dogs."
    client = OpenAI()
    completion = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages = get_messages(user_input)
    )   
    return completion.choices[0].message.content

def main():
    classifier = train_service_dog_classifier()  # Train the classifier
    print("bot: Hello! how can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("bot: goodbye!")
            break

        response = get_response_from_openai(user_input, classifier)

        print("bot:", response)

if __name__ == "__main__":
    main()