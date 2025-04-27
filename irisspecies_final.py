import streamlit as st
import pickle



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



def predict_material(h,t,d,y):
    loaded_model = pickle.load(open('mini_project_model.pkl','rb'))
    new_data = [[float(h),float(t),float(d),float(y)]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('Material Selection')
    st.image('app.png')
    hardness = get_hardness()
    toughness = get_toughness()
    density = get_density()
    yield_stress = get_yield_stress()
   
    st.write("The parameters you entered are: ")
    st.write("HARDNESS ", hardness)
    st.write("TOUGHNESS ", toughness)
    st.write("DENSITY ", density)
    st.write("YIELD STRESS", yield_stress)
    
    



if st.button("Predict"):
    predict_material(hardness, toughness, density, yield_stress)
    
