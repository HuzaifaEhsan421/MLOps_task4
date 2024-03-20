# Flask Stock Price Prediction App

This is a Flask web application for predicting stock prices using machine learning models.

## Overview

This project utilizes Flask, a micro web framework in Python, to create a web API for predicting stock prices based on historical data. The machine learning model is trained using historical stock price data, and the predictions are served through a RESTful API endpoint.

## Features

- Predict stock prices using a trained machine learning model
- RESTful API endpoint for making predictions
- Docker containerization for easy deployment

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/HuzaifaEhsan421/MLOps_task4.git
    cd MLOps_task4
    ```

2. Build the Docker image:

    ```bash
    docker build -t stock-app .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 stock-app
    ```

4. Access the Flask app in your web browser at `http://localhost:5000`.

