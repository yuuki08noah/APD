import joblib
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
CATEGORY = ['공부', '운동', '업무', '게임', '쇼핑']

def predict_category(task: str) -> dict:
    model = joblib.load('todo_classifier.joblib')
    vectorizer = joblib.load('vectorizer.joblib')

    x = vectorizer.transform([task])
    category = model.predict(x)[0]
    return {'task': task, 'category': category}

def predict_category_v2(task: str) -> dict:
    result = classifier(task, CATEGORY)
    top_label = result['labels'][0]
    return {"task": task, "category": top_label}