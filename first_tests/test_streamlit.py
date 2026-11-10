import streamlit as st

st.set_page_config(page_title="Test Streamlit")

st.title("Test de fonctionnement")
st.success("Streamlit fonctionne correctement !")

if st.button("Tester"):
    st.write("Le bouton fonctionne.")