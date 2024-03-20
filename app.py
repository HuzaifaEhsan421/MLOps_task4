from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import matplotlib
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_regression
# import random forest
from sklearn.ensemble import RandomForestRegressor
import pickle
matplotlib.use('Agg')

app = Flask(__name__)

# Replace with your data and models
model_RF = pickle.load(open('model_RF.pkl', 'rb'))

def plot_predictions(start_date, end_date, model):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    user_data = (pd.date_range(start_date, end_date) - start_date) / np.timedelta64(1, 'D')
    user_data = user_data.values.reshape(-1, 1)

    predictions = model.predict(user_data)

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=pd.date_range(start_date, end_date), y=predictions.flatten(), label='Predicted')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Predicted Stock Prices')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/graph.png')  # Save the graph as an image file
    plt.close()  # Close the plot to release memory

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        plot_predictions(start_date, end_date, model_RF)
        return render_template('index.html', graph=True)
    return render_template('index.html', graph=False)

if __name__ == '__main__':
    app.run(debug=True)
