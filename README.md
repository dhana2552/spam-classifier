# spam-classifier

A basic spam classifier which predicts if the email or sms texts are spam or not spam.

Datasets
The datasets were downloaded from kaggle https://www.kaggle.com/uciml/sms-spam-collection-dataset

Implementation
There are 2 files: spam_detection.ipynb, app.py

movie_recommender_system.ipynb
In this file, a complete analysis, data cleaning and model building were handled. The final model and vectorizers were then pickled to be used by app.py


app.py
This file contains code to get the end user mmessage and deploy predictions in streamlit.

# Reference: 
The project was practiced by following the youtube video https://www.youtube.com/watch?v=YncZ0WwxyzU&t=189s. My sincere thanks to Mr. Nitish Singh for simple and easy to understand solution
