from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import plotly
import plotly.express as px
import json

app = Flask(__name__)

# Sample career dataset
careers = pd.DataFrame({
    "career": ["Data Scientist", "Software Engineer", "UI/UX Designer", "Network Engineer"],
    "skill_level_math": [5, 4, 2, 3],
    "skill_level_coding": [5, 5, 2, 3],
    "skill_level_creativity": [2, 3, 5, 2],
    "skill_level_communication": [3, 4, 4, 3]
})

label_encoder = LabelEncoder()
careers["career_encoded"] = label_encoder.fit_transform(careers["career"])

X = careers[["skill_level_math", "skill_level_coding", "skill_level_creativity", "skill_level_communication"]]
y = careers["career_encoded"]

model = RandomForestClassifier()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    user_skills = {}
    if request.method == "POST":
        math = int(request.form.get("math"))
        coding = int(request.form.get("coding"))
        creativity = int(request.form.get("creativity"))
        communication = int(request.form.get("communication"))

        user_input = np.array([[math, coding, creativity, communication]])
        prediction = model.predict(user_input)[0]
        result = label_encoder.inverse_transform([prediction])[0]

        user_skills = {
            "Math": math,
            "Coding": coding,
            "Creativity": creativity,
            "Communication": communication
        }

    return render_template("index.html", result=result, user_skills=user_skills)

@app.route("/dashboard")
def dashboard():
    fig = px.bar(careers, x="career",
                 y=["skill_level_math","skill_level_coding","skill_level_creativity","skill_level_communication"],
                 barmode='group',
                 title="Career Skill Comparison")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("dashboard.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
