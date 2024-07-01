import streamlit as st
import os
import boto3
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
MILVUS_API_KEY = os.environ.get('MILVUS_API_KEY')
MILVUS_CLUSTER_ID = os.environ.get('MILVUS_CLUSTER_ID')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_BUCKET = os.environ.get('S3_BUCKET')
FOLDER = os.environ.get('FOLDER')

s3_client = boto3.client('s3',
                         aws_access_key_id = AWS_ACCESS_KEY,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)


# pages = [
#         st.Page("./pages/youtube.py", title="Youtube link"),
#         st.Page("./pages/rag.py", title="Podcast Q&A")

#         ]

pages = {
    "Youtube link": "./pages/youtube",
    "Podcast Q&A": "./pages/rag"
}