import streamlit as st
import joblib
MyAI = joblib.load("Data/model.pkl")
st.title("AI Page")

area = st.number_input("Area SQRT")
bedrooms = st.number_input("Bedrooms")
bathroom = st.number_input("Bathrooms")
stories = st.number_input("Stories")
house_age_years = st.number_input("house_age_years")
parking_spaces = st.number_input("parking_spaces")
distance_to_city_km = st.number_input("distance_to_city_km")
location_score = st.number_input("location_score")
furnished = st.number_input("furnished")

if st.button("Predict"):
    result = MyAI.predict([[area,bedrooms,bathroom,stories,house_age_years,parking_spaces,distance_to_city_km,location_score,furnished]])
    st.write(result)

