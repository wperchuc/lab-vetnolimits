import streamlit as st
import pandas as pd

# config.py
import os
from dotenv import load_dotenv
from config import API_KEY, DATABASE_URL

# Load environment variables from .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('NOCODB_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

# Optional: Add validation
if not API_KEY:
    raise ValueError("NOCODB_API_KEY environment variable is not set")

st.set_page_config (page_title="Vetnolimits Lab")

st.header("Vetnolimits Lab")
st.subheader("Twoja pomoc w diagnostyce różnicowej")

st.write("Wybierz parametr i jego stan, aby zobaczyć sugerowane diagnozy.")

