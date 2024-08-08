 
                                            Flight Customer Satisfaction Prediction


Overview
          This folder contains files related to the flight customer satisfaction prediction project. The goal of this project is to build a machine learning model to 
          predict customer satisfaction based on flight and customer experience data.

Contents
         data/: Contains datasets used for training and testing the model.
         notebooks/: Jupyter notebooks for exploratory data analysis (EDA) and model development.
         models/: Contins the trained machine learning model files.
         static/: Static assets like CSS and JavaScript files for the web application.
         templates/: HTML templates used in the Flask web application.
         app.py: The main Flask application script that serves the web interface.
         requirements.txt: List of Python packages required to run the application.


Prerequisites
          Python: Ensure Python 3.6 or higher is installed on your machine.
          Flask: A lightweight web framework for Python.

Inputs
          Each feature seems to represent different aspects of a flight, such as:
          - duration: Flight duration
          - days_left: Days left until the flight
          - price: Price of the flight
          - airline_*: Different airlines
          - source_city_*: Different source cities
          - departure_time_*: Different times of departure
          - stops_*: Number of stops
          - arrival_time_*: Different times of arrival
          - destination_city_*: Different destination cities
          - class_Business: Indicates whether the flight is business class
