

# Student Performance Prediction Using Machine Learning

## Project Overview

Student Performance Prediction is a Machine Learning project developed to predict students' academic performance based on various factors such as study hours, previous scores, extracurricular activities, sleep hours, and sample question papers practiced.

This project uses the **Linear Regression algorithm** to predict the Performance Index. The trained model is integrated with a Flask web application that allows users to enter student details and obtain predicted performance.

## Objectives

- Predict students' academic performance using Machine Learning.
- Analyze the relationship between study habits and student performance.
- Perform data preprocessing and feature selection.
- Train and evaluate a Linear Regression model.
- Develop a web application using Flask.
- Deploy the trained model for real-time predictions.

## Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib
- **Model Serialization:** Pickle
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Deployment:** Render

## Dataset Information

**Dataset Name:** Student_Performance.csv

The dataset contains 10,000 records and 6 columns.

### Dataset Attributes

| Column Name | Description |
|---|---|
| Hours Studied | Number of hours spent studying |
| Previous Scores | Student's previous academic scores |
| Extracurricular Activities | Participation in extracurricular activities (Yes/No) |
| Sleep Hours | Number of hours of sleep |
| Sample Question Papers Practiced | Number of sample papers practiced |
| Performance Index | Student's performance index |

### Independent Variables

The following five features are used as input variables:

1. Hours Studied
2. Previous Scores
3. Extracurricular Activities
4. Sleep Hours
5. Sample Question Papers Practiced

### Dependent Variable

- Performance Index

The Performance Index is the target variable predicted by the Machine Learning model.

## Project Structure

```text
Student-Performance-Prediction/
│
├── Student_Performance.csv
├── main.py
├── app.py
├── Model.pkl
├── requirements.txt
├── Procfile
│
└── templates/
    └── index.html
```

### File Description

- `Student_Performance.csv` - Dataset used for training the model.
- `main.py` - Performs data preprocessing, model training, testing, evaluation, and model saving.
- `app.py` - Flask application that loads the trained model and generates predictions.
- `Model.pkl` - Saved Linear Regression model.
- `requirements.txt` - Contains the required Python libraries.
- `Procfile` - Contains the application startup command for deployment.
- `templates/index.html` - Frontend interface for entering student details and displaying predictions.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Student-Performance-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Required Libraries

Create a `requirements.txt` file:

```text
Flask
numpy
pandas
matplotlib
scikit-learn
gunicorn
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Model Training Process

The model training process is implemented in `main.py`.

### 1. Data Loading

- Load the Student_Performance.csv dataset using Pandas.
- Display the first five records.
- Check dataset shape, missing values, and data types.

### 2. Data Preprocessing

The categorical column `Extracurricular Activities` is converted into numerical values.

- Yes → 1
- No → 0

This encoding allows the Linear Regression algorithm to process categorical data.

### 3. Feature Selection

Separate the dataset into independent variables (X) and the dependent variable (y).

- X contains five input features.
- y contains the Performance Index.

### 4. Train-Test Split

The dataset is divided into training and testing sets using `train_test_split()`.

- Training Data: 80%
- Testing Data: 20%
- Random State: 42

### 5. Model Selection

The project uses the **Linear Regression** algorithm from Scikit-learn.

```python
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)
```

The model learns the relationship between the input features and the Performance Index.

### 6. Model Testing

The trained model predicts student performance using the testing dataset.

### 7. Model Evaluation

The model is evaluated using the following performance metrics:

- **R² Score:** Measures how well the model explains variations in the target variable.
- **Mean Squared Error (MSE):** Measures the average squared difference between actual and predicted values.
- **Root Mean Squared Error (RMSE):** Measures the average prediction error in the target variable's units.

Both training and testing performance are evaluated.

### 8. Model Saving

The trained model is saved using Pickle.

```python
with open("Model.pkl", "wb") as f:
    pickle.dump(self.reg, f)
```

The saved model is loaded into the Flask application to generate predictions.

## Running the Project Locally

### Step 1: Train the Model

```bash
python main.py
```

This performs preprocessing, training, testing, model evaluation, and saves the trained model as `Model.pkl`.

### Step 2: Run the Flask Application

```bash
python app.py
```

### Step 3: Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

### Step 4: Enter Student Details

Enter the following details in the web application:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

Click the **Predict** button to obtain the predicted Performance Index.

## Deployment

The Flask application can be deployed using **Render**.

### Step 1: Upload the Project to GitHub

Push all required project files to your GitHub repository.

### Step 2: Create a Procfile

Create a file named `Procfile` in the root directory.

```text
web: gunicorn app:app
```

### Step 3: Create a Web Service on Render

1. Log in to Render.
2. Select New Web Service.
3. Connect your GitHub repository.
4. Select the Python environment.

### Step 4: Configure Build and Start Commands

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

### Step 5: Deploy the Application

Click Deploy and wait for the deployment process to complete.

After successful deployment, Render provides a public URL to access the Student Performance Prediction application.
## Results

The Linear Regression model was trained using 80% of the dataset and evaluated using the remaining 20%.

### Model Evaluation Results

The model performance was evaluated using R² Score, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

| Evaluation Metrics | Training Data | Testing Data |
|---|---:|---:|
| R² Score | 0.9887 (98.87%) | 0.9890 (98.90%) |
| Mean Squared Error (MSE) | 4.1697 | 4.0826 |
| Root Mean Squared Error (RMSE) | 2.0420 | 2.0206 |

### Performance Analysis

- **Training R² Score:** 98.87%
- **Testing R² Score:** 98.90%
- **Training MSE:** 4.1697
- **Testing MSE:** 4.0826
- **Training RMSE:** 2.0420
- **Testing RMSE:** 2.0206

The model achieved a testing R² score of approximately **98.90%**, indicating that it explains a high proportion of the variation in the Performance Index.

The training and testing results are very close, indicating consistent model performance on both datasets.

### Sample Prediction

The trained model accepts five input features and predicts the student's Performance Index.

**Sample Input:**

| Feature | Value |
|---|---:|
| Hours Studied | 7 |
| Previous Scores | 99 |
| Extracurricular Activities | 1 (Yes) |
| Sleep Hours | 9 |
| Sample Question Papers Practiced | 1 |

**Predicted Output:** The model generates the predicted Performance Index based on the given student details.

### Result Summary

- Successfully loaded and processed 10,000 student records.
- Converted categorical data into numerical values.
- Trained the Linear Regression model.
- Achieved 98.87% training R² score and 98.90% testing R² score.
- Evaluated model performance using MSE and RMSE.
- Saved the trained model using Pickle.
- Integrated the trained model with Flask.
- Developed a web application to predict student performance.



## Future Enhancements

- Compare different Machine Learning algorithms.
- Improve prediction accuracy.
- Add interactive data visualizations.
- Enhance the user interface.
- Implement input validation and error handling.
- Provide detailed student performance analysis.

## Conclusion

The Student Performance Prediction project demonstrates the application of Machine Learning in predicting students' academic performance based on different study-related and lifestyle-related factors.

By using Linear Regression, the project analyzes student information and predicts the Performance Index. Flask provides a user-friendly interface for entering student details and obtaining predictions.

This project demonstrates an end-to-end Machine Learning workflow, including data preprocessing, feature selection, model training, evaluation, model serialization, Flask integration, and deployment.

---
