import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 Streamlit 애플리케이션입니다.")

number = st.slider("숫자를 선택하세요", 0, 100)
st.write(f"선택한 숫자는 {number}입니다.")
