# AI-Powered Student Career Navigator

This project helps students identify the most suitable career pathway using AI-driven recommendations. By entering core skills (Math, Coding, Creativity, Communication), students get instant suggestions for potential careers best aligned with their strengths.

## Features

- Enter your skill ratings (1-5) in Math, Coding, Creativity, and Communication
- Click 'Predict Career' to get an AI-generated career suggestion based on the entered data
- Simple, responsive web interface for quick access

## How It Works

The frontend collects skill scores from users. On submit, it sends the data to a Python backend (Flask/FastAPI) which uses a machine learning model or simple rules-based AI to predict suitable careers. The prediction logic can be further improved using larger datasets.

## Tech Stack

- Frontend: HTML, CSS, JavaScript (or React)
- Backend: Python (Flask, FastAPI, or similar)
- AI Logic: ML model or rules-based approach

## Getting Started

1. Clone this repo.
2. Run pip install -r requirements.txt to install dependencies.
3. Start the backend server: python app.py
4. Open index.html in your browser.
5. Enter skill scores and click 'Predict Career'.

## Example

| Math | Coding | Creativity | Communication | Prediction       |
|------|--------|------------|---------------|------------------|
| 5    | 5      | 3          | 2             | Software Engineer|
| 2    | 3      | 5          | 5             | Marketing       |

