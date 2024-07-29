import pandas as pd
import streamlit as st
from streamlit_carousel import carousel


st.set_page_config(page_title='Prediksi Harga Properti', page_icon='🏠', initial_sidebar_state='collapsed')


# Read Data utama
properti = pd.read_csv('data_input/properti_jual.csv')

test_items = [
    dict(
        title="Data Overview",
        text=" ",
        img="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1415&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    ),
    dict(
        title="Data Prediction",
        text=" ",
        img="https://plus.unsplash.com/premium_photo-1661881801573-6506e682cbd6?q=80&w=1429&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    ),
]

carousel(items=test_items, width=0.8)


# Footer
footer_content = """
---

© 2024 Dwi Gustin Nurdialit
"""
st.markdown(f"<h1 style='text-align: center;'>{footer_content}</h1>", unsafe_allow_html=True)