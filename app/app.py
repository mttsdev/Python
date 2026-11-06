import streamlit as st
import pandas as pd
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

st.set_page_config(
    page_title="Chat Operadora Cartão"
    page_icon="💳"
    layout="centered"
)

st.title(" Chatbot Atendimento - Operadora de Cartão")