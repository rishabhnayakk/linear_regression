# Linear Regression — House Price Predictor

A small Python example that trains a linear regression model on a sample house-area dataset and predicts an estimated house price from an area entered at runtime.

## How It Works

1. Builds a sample dataset with house area (square feet) as the input feature and price (in lakh) as the target.
2. Uses pandas to organize the data.
3. Trains a LinearRegression model from scikit-learn.
4. Prompts for a house area and prints the predicted price in lakh.

## Requirements

- Python 3
- pandas
- scikit-learn

Install the dependencies:

~~~bash
python -m pip install pandas scikit-learn
~~~

## Run

From the repository root:

~~~bash
python linear_regression.py
~~~

Enter the house area in square feet when prompted. The program prints the predicted price in lakh.

## Project Structure

~~~text
linear_regression/
├── linear_regression.py
└── README.md
~~~

## Dataset and Limitations

The training data is hard-coded in linear_regression.py and contains only five sample observations. It is intended for learning the basic regression workflow, not for real-estate valuation. Predictions may be unreliable, especially for areas outside the sample data range. Use a larger, representative dataset and evaluate model performance before applying this approach to real decisions.
