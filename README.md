# AI-Powered Student Career Pathway Navigator

## 📖 Project Overview
The **AI-Powered Student Career Pathway Navigator** is a comprehensive web application developed for the **Build and Blog Marathon 2025**. This platform addresses the critical disconnect between academic education and industry requirements. By leveraging Artificial Intelligence and Machine Learning, the application analyzes a student's unique profile—including technical skills, soft skills, and interests—to recommend personalized career trajectories.

Unlike generic career quizzes, this system utilizes data-driven insights to visualize skill gaps, projected salary growth, and learning roadmaps, empowering students to make informed decisions about their professional future.

## 🌟 Key Features
* **AI-Driven Recommendations:** Utilizes Natural Language Processing (NLP) and similarity matching algorithms to map user inputs against a robust dataset of career profiles.
* **Interactive Dashboards:** Integrated **Plotly** visualizations provide dynamic charts showing market demand, salary trends, and skill overlap analysis.
* **Skill Gap Analysis:** Automatically identifies missing competencies for a target role and suggests specific areas for improvement.
* **Responsive Design:** A fully responsive frontend built with HTML5 and CSS3 ensures accessibility across desktop and mobile devices.
* **Scalable Architecture:** Designed with a microservices mindset, containerized via Docker, and deployed on Google Cloud Run for high availability.

## 🛠️ Technical Architecture & Stack

### Backend Infrastructure
* **Core Framework:** **Python 3.9+** with **Flask** (acting as the REST API and web server).
* **Server:** **Gunicorn** (Production-grade WSGI server optimized for containerized environments).
* **Routing:** Custom route handlers in `app.py` manage form submissions, API endpoints, and page rendering.

### Data Science & Machine Learning
* **Data Processing:** **Pandas** and **NumPy** are used for cleaning and structuring the career dataset (`data.csv`).
* **Algorithm:**
    * **TF-IDF Vectorization:** Converts text-based skill descriptions into numerical vectors.
    * **Cosine Similarity:** Calculates the mathematical distance between the student's skill vector and career profile vectors to determine the best fit.

### Frontend Interface
* **Templating:** **Jinja2** (server-side rendering) for dynamic content injection.
* **Visualization:** **Plotly.js** (JSON serialization via Flask) to render interactive graphs directly in the browser.
* **Styling:** Custom CSS with Flexbox/Grid for layout management.

### DevOps & Cloud Deployment
* **Containerization:** **Docker** is used to package the application and its dependencies, ensuring consistency across development and production environments.
* **Cloud Provider:** **Google Cloud Run** (Serverless).
* **Version Control:** Git & GitHub for source code management.

## 📂 Repository Structure
This repository contains the full source code for the application:

```text
BNB/
├── app.py                # Main application logic, route definitions, and ML inference
├── requirements.txt      # List of Python dependencies (Flask, Pandas, Scikit-learn, etc.)
├── Dockerfile            # Instructions for building the container image for Cloud Run
├── data/
│   └── career_data.csv   # Dataset containing career paths, required skills, and salary info
├── static/
│   ├── css/
│   │   └── style.css     # Custom stylesheets for the user interface
│   └── images/           # Assets and logos
├── templates/
│   ├── index.html        # Landing page with student input form
│   ├── dashboard.html    # Results page displaying charts and recommendations
│   └── layout.html       # Base Jinja2 template for consistent header/footer
└── README.md             # Project documentation
