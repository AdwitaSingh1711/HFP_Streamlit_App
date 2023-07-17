import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('Heart_Failure_Prediction.pkl','rb'))

st.title("Comprehensive Heart Failure Prediction")

st.write("""
         We're extremely proud to see that you're taking your first step towards your heart health journey!
         
         Enter the required details in the fields below to get a respinse!
         """)

st.write("The following form acce")

def predict_hf(age,anaemia,creatinine_phosphokinase,diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine,serum_sodium,sex,smoking):
    input=np.array([[age,anaemia,creatinine_phosphokinase,diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine,serum_sodium,sex,smoking]]).astype(np.float64)
    prediction = model.predict(input)
    #pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return int(prediction)

def main():
    #st.title("Abalone Age Prediction")

    age = st.text_input("Age")
    anaemia = st.text_input("Anaemia: Yes-1, No-0")
    creatinine_phosphokinase = st.text_input("Creatinine Phophokinase Levels")
    diabetes = st.text_input("Diabetes: Yes-1, No-0")
    ejection_fraction = st.text_input("Ejection Fraction")
    high_blood_pressure = st.text_input("High Blood Pressure")
    platelets = st.text_input("Platelets")
    serum_creatinine = st.text_input("Serum Creatinine")
    serum_sodium = st.text_input("Serum Sodium")
    sex = st.text_input("Gender: Male-1, Female-0")
    smoking = st.text_input("Smoking: Yes-1, No-0 (Also, we're elated to hear this! Great job there.)")

    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> Your healthy as you can be! Go live out your days in bliss, but don't forget to eat well!</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> There is a fair chance of you expereincing heart failure in the near future. We recommend that you step back and reasses your health once.</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
       </div>
    """

    if st.button("Predict the age"):
        output = predict_hf(age,anaemia,creatinine_phosphokinase,diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine,serum_sodium,sex,smoking)
        st.success('The risk of heart failure is {}'.format(output))

        if output == 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()