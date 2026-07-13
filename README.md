# 🎓 Student Stress Predictor

A Machine Learning web application built with **Streamlit** that predicts a student's stress level based on various academic, personal, and lifestyle factors.

The application uses a **Random Forest Classifier** trained on student data and demonstrates an end-to-end Machine Learning workflow including data preprocessing, feature engineering, model training, serialization, and deployment.

---

## 🚀 Demo

You can run the application locally using Streamlit.

```bash
streamlit run app.py
```

---

# 📌 Features

- Predicts student stress level
- Interactive web interface using Streamlit
- Handles missing values automatically
- Encodes categorical variables
- Scales numerical features (if applicable)
- Uses a complete Scikit-learn Pipeline
- Uses ColumnTransformer for preprocessing
- Random Forest Classification
- Model serialization using Joblib
- Clean and modular project structure

---

# 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Joblib


# 📊 Machine Learning Workflow

### 1. Data Collection

- Student stress dataset

---

### 2. Data Preprocessing

The preprocessing pipeline includes:

- Handling missing values
- Encoding categorical features
- Scaling numerical features (if used)

The preprocessing is implemented using:

- Pipeline
- ColumnTransformer

---

### 3. Model Training

Algorithm Used:

- Random Forest Classifier

The model was trained after applying the preprocessing pipeline.

---

### 4. Model Saving

The trained model and preprocessing pipeline were saved using Joblib.

```python
import joblib

joblib.dump(model, "model.pkl")
joblib.dump(preprocessor, "pipeline.pkl")
```

They are later loaded inside the Streamlit application for prediction.

---

# 🖥️ User Interface

The Streamlit application allows users to:

- Enter student details
- Submit the input
- Instantly receive the predicted stress level

# 📈 Input Features

Example input features may include:

Student_Type,Sleep_Hours,Study_Hours,Social_Media_Hours,Attendance,Exam_Pressure,Family_Support,Month,Stress_Level




# 🎯 Prediction

The model predicts the student's stress level based on the provided input features.

---



# 🧠 Concepts Demonstrated

This project demonstrates practical implementation of:

- Machine Learning Classification
- Data Preprocessing
- Feature Engineering
- Pipeline
- ColumnTransformer
- Random Forest Classifier
- Model Serialization using Joblib
- Streamlit Deployment


# 📚 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- Feature importance visualization
- Probability prediction


# 🤝 Contributing

Contributions are welcome.

If you have suggestions or improvements, feel free to fork the repository and submit a pull request.



⭐ If you found this project useful, consider giving the repository a star!
