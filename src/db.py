from astrapy import DataAPIClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

ENDPOINT = "https://81f32063-1f98-4cb8-9179-13aa5629b55d-us-east-2.apps.astra.datastax.com" #os.getenv("ASTRA_ENDPOINT")
TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

@st.cache_resource()
def get_db():
    client = DataAPIClient(TOKEN)
    db = client.get_database_by_api_endpoint(ENDPOINT)
    return db

db = get_db()

collection_names = ["personal_data", "notes"]

for collection in collection_names:
    try:
        db.create_collection(collection)
    except Exception as e:
        pass

personal_data_collection = db.get_collection("personal_data")
notes_collection = db.get_collection("notes")
