from ServiceDogClassifier import *

def train_service_dog_classifier():
    # Example training data
    X_train = [
        "What are the benefits of having a service dog?",
        "How can I train a service dog?",
        "Are service dogs allowed in restaurants?",
        "Can service dogs detect seizures?",
        "What breeds are commonly used as service dogs?",
        "What is the life expectancy of a Labrador Retriever?",
        "How do I groom my pet dog?",
        "What food is toxic for pet dogs?",
        "How can I teach my dog to sit?",
        "What are the symptoms of a sick dog?",

    ]
    y_train = [
        "service_dog",
        "service_dog",
        "service_dog",
        "service_dog",
        "service_dog",
        "non_service_dog",
        "non_service_dog",
        "non_service_dog",
        "service_dog",
        "non_service_dog"
    ]

    classifier = ServiceDogClassifier()
    classifier.train(X_train, y_train)
    return classifier

def is_about_service_dogs(user_input, classifier):
    prediction = classifier.predict([user_input])
    return prediction[0] == "service_dog"