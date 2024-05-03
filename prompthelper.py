def get_messages(input_text):
    """
    Creates a list of messages to be used in the OpenAI completion API.

    Parameters:
        input_text (str): The user input text.

    Returns:
        list: A list of messages formatted for the OpenAI completion API.
    """
    messages = [
        {"role": "system", "content": "You are an AI assistant that helps people find information about service dogs only."},
        {"role": "system", "content": "You do not answer any other questions other than service dogs."},
        {"role": "user", "content": "Tell me about service dogs."},  # Direct the conversation to service dogs
        {"role": "user", "content": input_text}
    ]  
    return messages 
