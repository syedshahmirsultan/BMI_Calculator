import streamlit as st

st.title("Shahmir BMI Calculator")
st.write("    ")
st.write("    ")
st.header("Weight")
weight = st.number_input("\n Enter Your Weight in Kgs",step=1)
st.write("   ")
st.header("Height")
heightVal = st.radio("Select your height unit",("Feet","Centimeter","Meter"))
if heightVal == 'Feet':
    height = st.number_input("Feet")
    try:
        bmi = weight/((height*0.3048)**2)
    except:
        st.text("Enter some value")
    
elif heightVal == 'Centimeter':
    height = st.number_input("Centimeter")
    try:
        bmi = weight/(height**2)*10000
    except:
        st.text("Enter some value")
else:
    height = st.number_input('Meter')
    try:
        bmi = weight/(height**2)
    except:
        st.text("Enter some value")
        
st.write("   ")
if weight and height:
 if(st.button("Calculate BMI")):
   st.write("    ")
   st.subheader(f"Your BMI is {bmi}")
   st.write("  ")
   if(bmi < 18.5):
       st.warning("You are Underweight")
   elif(bmi > 18.5 and bmi < 25):
       st.success("Healthy Body Weight")
   elif(bmi > 25):
       st.error("You are Overweight")