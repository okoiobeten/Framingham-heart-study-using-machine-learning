import pickle
import streamlit as st

# Load the model
with open('my_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_heart_problem(features):
    try:
        return model.predict([features])[0]
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        return None

# Streamlit UI
def main():
    # Streamlit title with red color using markdown
    st.markdown("<h1 style='color: red;'>Heart Problem Prediction Using Decision Tree</h1>", unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns(2)

    # User input in the first column
    with col1:
        st.header("Patient Information")
        sysBP = st.number_input("Systolic Blood Pressure (83.5 to 295 mm Hg)", min_value=0.0, format="%.2f")
        glucose = st.number_input("Glucose Level(40 to 394 mg/dL)", min_value=0.0, format="%.2f")
        age = st.number_input("Age of Patient (32 to 72 years old)", min_value=0, step=1)
        totChol = st.number_input("Total Cholesterol Level (107 to 696 mg/dL)", min_value=0.0, format="%.2f")
        cigsPerDay = st.number_input("Number of Cigarettes Per Day (0 to 70 sticks)", min_value=0.0, format="%.2f")
        diaBP = st.number_input("Diastolic Blood Pressure (48 to 142.5 mm Hg)", min_value=0.0, format="%.2f")

    # User input in the second column
    with col2:
        st.header("Patient Attributes")
        prevalentHyp = st.radio("Is the Patient Hypertensive?", ('Yes', 'No'))
        diabetes = st.radio("Does the Patient Have Diabetes?", ('Yes', 'No'))
        BPMeds = st.radio("Is the Patient on Blood Pressure Medication?", ('Yes', 'No'))
        male = st.radio("Gender", ('Male', 'Female'))

    # Convert binary/categorical inputs to numerical
    prevalentHyp = 1 if prevalentHyp == 'Yes' else 0
    diabetes = 1 if diabetes == 'Yes' else 0
    BPMeds = 1 if BPMeds == 'Yes' else 0
    male = 1 if male == 'Male' else 0

    # Submit button
    if st.button("Predict Heart Problem"):
        prediction = predict_heart_problem([sysBP, glucose, age, totChol, cigsPerDay, diaBP, prevalentHyp, diabetes, BPMeds, male])
        if prediction is not None:
            if prediction == 1:
                st.success("The patient is likely to have a heart problem within the next 10 years.")
            else:
                st.success("The patient is unlikely to have a heart problem within the next 10 years.")

    # Footer with red background and white text
    st.markdown(
        "<div style='background-color: red; color: white; text-align: center; padding: 10px;'>"
        "This project was developed using Jupyter Notebook and Spyder IDE by Tosin"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
