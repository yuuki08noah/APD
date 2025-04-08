import joblib

model = joblib.load('todo_classifier.joblib')
vectorizer = joblib.load('vectorizer.joblib')

if __name__ == '__main__':
    x = vectorizer.transform(['Classify Something'])
    category = model.predict(x)
    print(category)