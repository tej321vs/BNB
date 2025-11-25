
# AI-Powered Student Career Pathway Navigator

This project helps students identify the most suitable career pathway using AI-driven recommendations. By entering core skills (**Math, Coding, Creativity, Communication**), students get instant suggestions for potential careers best aligned with their strengths.

---

## Features

* Input skill ratings (1–5) for Math, Coding, Creativity, and Communication
* AI-generated career predictions using a **Random Forest Classifier**
* Interactive **dashboard** comparing user skills with multiple career paths
* Simple and responsive web interface for quick access
* Deployable on **Google Cloud Run** for easy cloud access

---

## How It Works

1. **Frontend:** A web form collects skill scores from the user.
2. **Backend:** Flask server receives the data and runs the **Random Forest model** to predict the most suitable career.
3. **Dashboard:** Using **Plotly**, it visualizes the user’s skills compared with recommended career paths.
4. **Output:** Users receive a career suggestion along with visual insights for better decision-making.

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Machine Learning:** scikit-learn (Random Forest Classifier)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly for interactive dashboards
* **Deployment:** Google Cloud Run (serverless, scalable deployment)

---

## Getting Started

1. Clone the repository:

```bash
git clone <your-repo-link>
cd bnb
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the backend server:

```bash
python app.py
```

4. Open the app:

* **Local:** `http://localhost:5000`
* **Cloud Run:** Use the public URL provided after deployment

5. Enter your skill scores and click **Predict Career** to see recommendations and the interactive dashboard.

---

## Example

| Math | Coding | Creativity | Communication | Prediction        |
| ---- | ------ | ---------- | ------------- | ----------------- |
| 5    | 5      | 3          | 2             | Software Engineer |
| 2    | 3      | 5          | 5             | UI/UX Designer    |
| 4    | 4      | 2          | 3             | Data Scientist    |
| 3    | 3      | 5          | 2             | Graphic Designer  |

---

## Skills Demonstrated

* **Programming:** Python, Flask
* **Machine Learning:** Random Forest, scikit-learn
* **Data Analysis:** Pandas, NumPy
* **Web Development:** HTML, CSS, JavaScript
* **Data Visualization:** Plotly interactive dashboards
* **Cloud Deployment:** Google Cloud Run, serverless architecture
* **Project Skills:** AI-driven decision making, problem-solving, and UX design

---

## Future Improvements

* Expand the dataset for more career options
* Add **user login and skill tracking** over time
* Generate **downloadable reports (PDF/CSV)** for students
* Integrate **more advanced AI models** for personalized recommendations

---

## Author

* Name: **Venkat Teja**
* Event: **Build and Blog Marathon 2025**


