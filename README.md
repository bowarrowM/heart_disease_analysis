# Heart Disease Analysis & Prediction Project

### Note: This PROJECT and README is a work-in-progress. Feedback and suggestions are welcome!

This is a Python-based data analysis and machine learning project using the UCI Heart Disease Dataset (from Kaggle).
The project covers data preprocessing, exploratory data analysis (EDA), visualization, SQL database integration (PostgreSQL), and predictive modeling.
Comments and reasoning are included throughout the code for clarity.

## Project Overview

The purpose of this project is to analyze heart disease data, explore correlations and distributions, and build a machine learning model to predict the presence of heart disease.
Key aspects of the project include:

Exploratory Data Analysis (EDA): summary statistics, missing values, duplicates

Data Visualization: categorical and numerical feature distributions

Data Cleaning & Preprocessing: handling nulls, encoding categorical variables

Database Integration: optional PostgreSQL connection for storing/querying the dataset. Currently commented out in my version but modify as wanted.

Model Training & Evaluation: predictive modeling with performance metrics and confusion matrix

## Project Structure
├── .env                  # Environment variables / database credentials (gitignored)
├── all_imports.py        # Library imports and dataset loading
├── data_analysis.py      # EDA: info, shape, nulls, summary stats
├── plots_visualization.py# Visualizations for EDA
├── sqlDB_connection.py   # PostgreSQL database connection (optional)
├── model.py              # Preprocessing, training, evaluation, confusion matrix
├── README.md             # Project overview and instructions
└── requirements.txt      # Required Python packages

## Setup Instructions

### Clone the repository

git clone <repo-url>
cd heart-disease-project


### Install dependencies

pip install -r requirements.txt


Open the project in your preferred IDE (VS Code, PyCharm, etc.)

Create your .env file (not included in the repo for security) and add your credentials (listed below):

### PostgreSQL database URL
DB_URL="postgresql://username:password@localhost:5432/db_name"

### Local dataset path (Kaggle CSV)
DATA_PATH="path/to/heart_disease_data.csv"


Alternatively, you can add the paths/credentials directly into your Python scripts if preferred.

## Notes

All scripts contain comments explaining code logic and reasoning.

SQL integration is optional; you can run the project fully with CSV data.

Visualizations and model evaluation results are generated automatically via the scripts.
