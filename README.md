# Bitcoin Price Prediction 📈

A Machine Learning project that analyzes historical Bitcoin market data and predicts whether the Bitcoin price will increase or decrease on the next day.

## About the Project

This project uses historical Bitcoin price data to explore market trends and build classification models that predict the next day's price direction.

The dataset includes daily market information such as Open, High, Low, Close, and Volume.

## Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Yahoo Finance (`yfinance`)

## Feature Engineering

Several features are created to help the models identify patterns in Bitcoin price movements:

- Daily price returns
- Previous closing price
- Rolling averages (3-day and 30-day)
- Weekly returns
- Price comparison with the 30-day moving average
- Quarter-end indicator

## Machine Learning Models

The following classification algorithms are used:

- Logistic Regression
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)

## Model Evaluation

The models are evaluated using the ROC-AUC score on training and validation datasets.

The data is split chronologically to preserve the time order and avoid random shuffling.

## Project Structure

```text
Bitcoin-Price-Prediction/
│
├── Bitcoin-Price-Prediction.ipynb
├── bitcoin.csv
├── bitcoin_updated.csv
├── update.py
└── README.md
```

## Dataset

Historical Bitcoin market data is used in this project.

The `update.py` script retrieves newer daily Bitcoin data using Yahoo Finance and saves the updated dataset.

## Disclaimer

This project is for educational purposes only and should not be considered financial or investment advice.