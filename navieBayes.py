from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Training data: questions and their corresponding answers
data = {
    "notice period": 0,
    "expected": 6,
    "current": 1.2,
    "Please enter your current annual compensation in INR. Example: 200000": 120000,
    "Please enter your expected annual compensation in INR. Example: 350000": 500000,
    "Please enter your notice period in days. Example: 45": 5,
    "How many years of work experience do you have with TypeScript?": 5,
    "How many years of work experience do you have with Node.js?": 5,
    "How many years of work experience do you have with Amazon Web Services (AWS)?": 1,
    "How many years of Information Technology experience do you currently have?": 3
}

# Convert the dictionary into training data: X as the questions, y as the answers
X_train = list(data.keys())  # Questions
y_train = list(data.values())  # Corresponding answers

# Create a pipeline that vectorizes the text data and applies the Linear Regression model
model = make_pipeline(TfidfVectorizer(), LinearRegression())

# Train the model
model.fit(X_train, y_train)

# Define a function to predict the answer for a new question
def predict_answer_linear_regression(question):
    return model.predict([question])[0]

# Example new questions to predict answers for
new_questions = [
    "How many years of work experience do you have with Node.js?",
    "Please enter your expected annual compensation in INR. Example: 350000",
    "What is your notice period in days?"
]

# Predict answers for the new questions
for question in new_questions:
    predicted_answer = predict_answer_linear_regression(question)
    print(f"Question: {question}")
    print(f"Predicted Answer: {predicted_answer}\n")
