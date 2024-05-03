from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

class ServiceDogClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = SVC(kernel='linear', probability=True)

    def train(self, X_train, y_train):
        X_train_vectorized = self.vectorizer.fit_transform(X_train)
        self.classifier.fit(X_train_vectorized, y_train)

    def predict(self, X):
        X_vectorized = self.vectorizer.transform(X)
        return self.classifier.predict(X_vectorized)