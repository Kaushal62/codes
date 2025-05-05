from sklearn.tree import DecisionTreeClassifier

# Step 1: Mapping categorical data to numbers
def encode_input(data):
    encoding = {
        "attendance": {"poor": 0, "average": 1, "good": 2, "excellent": 3},
        "punctuality": {"poor": 0, "average": 1, "good": 2, "excellent": 3},
        "project_completion": {"late": 0, "on_time": 1},
        "peer_feedback": {"negative": 0, "neutral": 1, "positive": 2}
    }
    return [
        encoding["attendance"][data["attendance"]],
        encoding["punctuality"][data["punctuality"]],
        encoding["project_completion"][data["project_completion"]],
        encoding["peer_feedback"][data["peer_feedback"]],
    ]

# Step 2: Training data
X = [
    encode_input({"attendance": "excellent", "punctuality": "excellent", "project_completion": "on_time", "peer_feedback": "positive"}),
    encode_input({"attendance": "good", "punctuality": "good", "project_completion": "on_time", "peer_feedback": "positive"}),
    encode_input({"attendance": "average", "punctuality": "average", "project_completion": "late", "peer_feedback": "neutral"}),
    encode_input({"attendance": "poor", "punctuality": "poor", "project_completion": "late", "peer_feedback": "negative"})
]

y = ["Excellent", "Good", "Average", "Needs Improvement"]

# Step 3: Train the AI model
model = DecisionTreeClassifier()
model.fit(X, y)
model.score(X, y)  # Check the accuracy of the model

# Step 4: Get user input
def get_user_input():
    print("\nPlease enter the following details (options are case-sensitive):")
    attendance = input("Attendance (poor/average/good/excellent): ")
    punctuality = input("Punctuality (poor/average/good/excellent): ")
    project_completion = input("Project Completion (late/on_time): ")
    peer_feedback = input("Peer Feedback (negative/neutral/positive): ")

    return {
        "attendance": attendance,
        "punctuality": punctuality,
        "project_completion": project_completion,
        "peer_feedback": peer_feedback
    }

# Step 5: Predict performance using AI
def ai_evaluate_performance(inputs):
    try:
        encoded = encode_input(inputs)
        prediction = model.predict([encoded])
        return prediction[0]
    except KeyError:
        return "Invalid input provided. Please use valid options."

# Step 6: Main program

user_data = get_user_input()
result = ai_evaluate_performance(user_data)
print("\nPerformance Evaluation (AI):", result)
