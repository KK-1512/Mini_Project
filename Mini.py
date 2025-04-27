import streamlit as st
import pickle
import numpy as np

class_names = {0: "AEROSPACE", 1: "AUTOMOTIVE", 2: "DOMESTIC", 3: "INDUSTRY"}

def get_hardness():
    hardness = st.text_input("HARDNESS")
    return hardness

def get_toughness():
    toughness = st.text_input("TOUGHNESS")
    return toughness

def get_density():
    density = st.text_input("DENSITY")
    return density

def get_yield_stress():
    yield_stress = st.text_input("YIELD STRESS")
    return yield_stress



def predict_apps(h,t,d,ys):
    loaded_model = pickle.load(open('mini_project_model.pkl','rb'))
    new_data = np.array([[float(h),float(t),float(d),float(ys)]])
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    predicted_class = int(prediction[0][0])
    material_name = class_names[predicted_class]

    st.success(f"Predicted Material: {material_name}")



if __name__ == "__main__":
    st.title('PREDCITION OF APPLICATION USE OF MATERIALS')
    st.image('app.png')
    hardness_value = get_hardness()
    toughness_value = get_toughness()
    density_value = get_density()
    yield_stress_value = get_yield_stress()
   
    st.write("The parameters you entered are: ")
    st.write("hardness ", hardness_value)
    st.write("toughness ", toughness_value)
    st.write("density ", density_value)
    st.write("yield stress ", yield_stress_value)
    
    



if st.button("Predict"):
    predict_apps(hardness_value,toughness_value,density_value,yield_stress_value)
