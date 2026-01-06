# Emotion Detection Web Application

This repository contains a final project for a course on AI and web development. The project is a web application that detects emotions in text using IBM Watson's Emotion Prediction API.

## Overview

The application analyzes input text and returns scores for five emotions: anger, disgust, fear, joy, and sadness. It also identifies the dominant emotion based on the highest score.

## Features

- Emotion analysis using Watson NLP API
- Flask-based web server
- Error handling for invalid inputs
- Test suite for emotion detection functionality

## Technologies Used

- Python
- Flask
- IBM Watson NLP API
- HTML/CSS for front-end (in templates and static directories)

## How to Run

1. Ensure you have Python installed.
2. Install dependencies (if any, e.g., requests, flask).
3. Run the server: `python final_project/server.py`
4. Access the application at `http://localhost:5000`

## API Usage

Send a POST request to `/emotionDetector` with form data `textToAnalyze` containing the text to analyze.

Example response: "For the given statement, the system response is 'anger': 0.1, 'disgust': 0.0, 'fear': 0.2, 'joy': 0.5, 'sadness': 0.2. The dominant emotion is joy."

Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): 2026-01-06 10:41:34
Current User's Login: ngwanatiyani