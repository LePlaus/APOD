import requests
import streamlit as st

nasa_api = st.secrets["api_keys"]['NASA_API_KEY']
date = st.date_input("Enter the date:",max_value="today", min_value="2020-01-01")

url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api}&date={date}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
    ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url,headers=headers)
content = response.json()

date = content['date']
title = content['title']
try:
    image_url = content['hdurl']
except KeyError:
    image_url = content['url']
try:
    img_copyright = content['copyright']
except KeyError:
    pass
explanation = content['explanation']

img = requests.get(image_url)
  
with open("apod.jpg", 'wb') as image:
    image.write(img.content)

st.title(title)
# st.caption(date)
try:
    st.image("apod.jpg")
except:
    st.video(image_url)
try:
    st.caption(f"By:{img_copyright}")
except:
    pass
st.text(explanation)
