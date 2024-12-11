{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2bb7df02-88d1-4ce1-b07a-cd2528ae216d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "import streamlit as st\n",
    "\n",
    "# Step 1: Data Preprocessing\n",
    "def preprocess_data(file_path):\n",
    "    # Load the dataset\n",
    "    data = pd.read_csv(file_path)\n",
    "    \n",
    "    # Handle missing values in the RiskLevel column\n",
    "    data['RiskLevel'] = data['RiskLevel'].fillna(data['RiskLevel'].mode()[0])\n",
    "    \n",
    "    # Standardize RiskLevel values (strip spaces, capitalize)\n",
    "    data['RiskLevel'] = data['RiskLevel'].str.strip().str.capitalize()\n",
    "    \n",
    "    # Map RiskLevel to integers\n",
    "    risk_mapping = {'Low risk': 0, 'Mid risk': 1, 'High risk': 2}\n",
    "    data['RiskLevel'] = data['RiskLevel'].map(risk_mapping)\n",
    "    \n",
    "    # Handle any remaining unmapped or missing values by filling with 'Low'\n",
    "    if data['RiskLevel'].isnull().sum() > 0:\n",
    "        data['RiskLevel'] = data['RiskLevel'].fillna(0)  # Default to 'Low'\n",
    "    \n",
    "    # Separate features (X) and target (y)\n",
    "    X = data[['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate']]\n",
    "    y = data['RiskLevel']\n",
    "    \n",
    "    return X, y\n",
    "\n",
    "# Step 2: Machine Learning Model Training\n",
    "def train_model(X, y):\n",
    "    # Split the dataset into training and testing sets\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "    \n",
    "    # Train the Random Forest model\n",
    "    model = RandomForestClassifier(random_state=42)\n",
    "    model.fit(X_train, y_train)\n",
    "    \n",
    "    # Evaluate the model (optional for debugging)\n",
    "    y_pred = model.predict(X_test)\n",
    "    accuracy = accuracy_score(y_test, y_pred)\n",
    "    return model, accuracy\n",
    "\n",
    "# Streamlit App\n",
    "def main():\n",
    "    st.title(\"Maternal Health Risk Predictor\")\n",
    "    \n",
    "    # File upload\n",
    "    uploaded_file = st.file_uploader(r\"C:\\Users\\Asus\\Desktop\\SDP\\Maternal Health Risk Data Set.csv\")\n",
    "\n",
    "    \n",
    "    if uploaded_file is not None:\n",
    "        # Preprocess the data\n",
    "        X, y = preprocess_data(uploaded_file)\n",
    "        \n",
    "        # Train the model\n",
    "        model, accuracy = train_model(X, y)\n",
    "        \n",
    "        st.success(f\"Model trained successfully with an accuracy of {accuracy:.2f}\")\n",
    "        \n",
    "        st.subheader(\"Enter patient details:\")\n",
    "        \n",
    "        # Input fields\n",
    "        age = st.number_input(\"Age\", min_value=10, max_value=100, value=25, step=1)\n",
    "        systolic_bp = st.number_input(\"SystolicBP\", min_value=50, max_value=200, value=120, step=1)\n",
    "        diastolic_bp = st.number_input(\"DiastolicBP\", min_value=30, max_value=150, value=80, step=1)\n",
    "        bs = st.number_input(\"Blood Sugar (BS)\", min_value=0.0, max_value=10.0, value=4.5, step=0.1)\n",
    "        body_temp = st.number_input(\"Body Temperature\", min_value=35.0, max_value=42.0, value=37.0, step=0.1)\n",
    "        heart_rate = st.number_input(\"Heart Rate\", min_value=40, max_value=200, value=75, step=1)\n",
    "        \n",
    "        # Predict button\n",
    "        if st.button(\"Predict Risk Level\"):\n",
    "            # Create a dataframe for the input\n",
    "            user_input = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]],\n",
    "                                      columns=['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate'])\n",
    "            \n",
    "            # Predict risk level\n",
    "            risk_level_num = model.predict(user_input)[0]\n",
    "            risk_mapping = {0: \"Low Risk\", 1: \"Mid Risk\", 2: \"High Risk\"}\n",
    "            risk_level = risk_mapping[risk_level_num]\n",
    "            \n",
    "            st.success(f\"Predicted Risk Level: {risk_level}\")\n",
    "\n",
    "# Run the app\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd9f5dcf-1e59-4566-8381-4b9793d5485e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}