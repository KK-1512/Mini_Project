import streamlit as st
import pickle

# Functions to get user input
def get_hardness():
    return st.text_input("HARDNESS")

def get_toughness():
    return st.text_input("TOUGHNESS")

def get_density():
    return st.text_input("DENSITY")

def get_yield_stress():
    return st.text_input("YIELD STRESS")

# Function to make prediction
def predict_material(h, t, d, y):
    loaded_model = pickle.load(open('mini_project_model.pkl', 'rb'))
    new_data = [[float(h), float(t), float(d), float(y)]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data:")
    st.write(prediction)

# Streamlit App
st.title('Material Selection')
st.image('app.png')

hardness = get_hardness()
toughness = get_toughness()
density = get_density()
yield_stress = get_yield_stress()

st.write("The parameters you entered are:")
st.write("HARDNESS:", hardness)
st.write("TOUGHNESS:", toughness)
st.write("DENSITY:", density)
st.write("YIELD STRESS:", yield_stress)

if st.button("Predict"):
    if hardness and toughness and density and yield_stress:
        predict_material(hardness, toughness, density, yield_stress)
    else:
        st.warning("Please fill in all input fields before predicting.")

    



if st.button("Predict"):
    predict_material(hardness, toughness, density, yield_stress)
    
