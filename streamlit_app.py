import streamlit as st  
import pyshorteners  

# 앱 제목  
st.title("URL 줄이기 앱")  

# 사용자 입력 받기  
url = st.text_input("짧게 만들 URL을 입력하세요:")  

if st.button("URL 줄이기"):  
    if url:  
        # URL 줄이기  
        s = pyshorteners.Shortener()  
        short_url = s.tinyurl.short(url)  
        st.success(f"짧은 URL: {short_url}")  
    else:  
        st.error("URL을 입력해 주세요.")
