
# Cricket Player Run Predictor


This project is a machine learning application that predicts how many runs a cricket batsman is likely to score in a match. It uses key player performance statistics like rating, balls faced, and strike rate to generate these predictions.

What it does:
The core of this project is a predictive model, specifically a Random Forest Regressor, which has been trained on historical cricket data. It cleans and processes this data, then uses the trained model to estimate a player's probable score. Beyond just the prediction, it also includes a user-friendly Flask web application where anyone can input player metrics and get an instant run prediction.

Who it's for:
This tool is perfect for:

Cricket enthusiasts and analysts who want data-driven insights into player performance and match scenarios.
Aspiring data scientists and machine learning engineers looking for a practical, end-to-end project that demonstrates skills in data cleaning, model building, evaluation, and web deployment (using Flask).
Anyone interested in seeing how machine learning can be applied to sports analytics to derive actionable insights.


## Tech Stack & Libraries

**Python Version:** 3.8+

**Key Libraries:**
* `pandas`: For data manipulation and analysis.
* `numpy`: For numerical operations.
* `scikit-learn`: For machine learning model building (Linear, Lasso, Random Forest).
* `matplotlib`, `seaborn`: For data visualization and EDA.
* `flask`: For building the web application API.
* `pickle`: For serializing and loading the trained ML model.

**Tools:**
* **Jupyter Notebook:** Used extensively for data exploration, preprocessing, model training, and evaluation.
* **VS Code:** For general code development and Flask application setup.
## Model Building & Performance

Algorithms Used:
I experimented with and evaluated three different regression algorithms to determine the most effective predictor:

Multiple Linear Regression: Served as the foundational baseline model.
Lasso Regression: Applied as an L1-regularized model, particularly useful for its feature selection capabilities in potentially sparse data.
Random Forest Regressor: Chosen for its robustness and ability to handle complex relationships, this ensemble model ultimately outperformed the others.
Model Performance (Mean Absolute Error - MAE):
The Mean Absolute Error (MAE) was used as the primary evaluation metric due to its easy interpretability (average absolute difference between predicted and actual values).

Random Forest Regressor: MAE = 8.21 (Achieved the lowest error, indicating superior predictive accuracy).
Linear Regression: MAE = 10.55
Lasso Regression: MAE = 9.89


## EDA Highlights

Exploratory Data Analysis (EDA) was crucial for understanding the dataset and identifying key relationships:

Discovered a strong positive correlation between player Rating, Strike Rate, and the Runs scored. This confirmed these metrics as significant predictors.
Utilized scatter plots and heatmaps to visualize these trends and correlations effectively.
Concluded that Rating and Strike Rate were the most impactful features for predicting runs.
## Deployment (Flask Web App)

The core machine learning model is integrated into a user-friendly Flask web application, enabling real-time run predictions through a simple browser interface.

How It Works:
Users navigate to the web application.
They input values for:
Player Rating
Balls Faced
Strike Rate
The Flask backend passes these inputs to the pre-trained Random Forest Regressor model.
The model returns a predicted run value, which is displayed to the user.
Example Interaction:
# Example Input to the web app:
Rating: 4.2
Balls Faced: 28
Strike Rate: 135

# Example Output from the model:
Predicted Runs: 33.8

#📊 Prediction Error Distribution  
![Prediction Error](images/prediction_error.png)

# 🥧 Dismissal Type Distribution  
![Dismissals](images/dismissal_types.png)

# 📍 Top Locations by Average Runs  
![Top Locations](images/top_locations.png)
## How to run local

How to Run Locally
Follow these steps to set up and run the Cricket Player Run Predictor on your local machine:

Bash

# Step 1: Clone the repository
git clone [https://github.com/AyushNagras-07/ds_cricket_project.git](https://github.com/AyushNagras-07/ds_cricket_project.git)
cd ds_cricket_project

# Step 2: Create and activate a virtual environment (highly recommended)
python -m venv venv
source venv/bin/activate       # On Windows, use: `venv\Scripts\activate`

# Step 3: Install all required project dependencies
pip install -r requirements.txt

# Step 4: Navigate into the FlaskAPI directory
cd FlaskAPI

# Step 5: Run the Flask web application
python app.py

# Step 6: Access the web app in your browser
👉 Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
## Acknowledgements

This project is a culmination of learning and practical application, inspired by the exciting intersection of data science and cricket analytics.

References:
scikit-learn Official Documentation
Flask Official Documentation
Inspiration for data engineering and project design from various cricket statistics analysis resources.
https://youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&si=uFiz64xstDk8wsYw
