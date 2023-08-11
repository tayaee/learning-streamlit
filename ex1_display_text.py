import streamlit as st

st.title('텍스트 출력')
st.header('헤더 1')
st.subheader('서브헤더 1')
st.subheader('서브헤더 2')
st.header('헤더 2')
st.text('텍스트 위짓 1\n라인 2 <a href="google.com">Google</a>')
t = f'''
# One
* 마크다운 제목 1
  * 서브제목 1
  * 서브제목 3
    * 서브제목 4 <a href="google.com">Google</a>
    * 서브제목 2
'''
st.markdown(t, unsafe_allow_html=True)
st.caption("캡션")
st.latex(r"\sqrt[3]{x^3+y^3 \over 2}")
st.latex(r"\sqrt[3]{x^3+y^3 \over 2}, \log_{10} f, \sum_{k=1}^N k^2, \int_{-N}^{N} e^x\, dx")
st.latex('''f(n) = \begin{Bmatrix} x & y \\ z & v \end{Bmatrix}''')
st.latex('\oint_{C} x^3\, dx + 4y^2\, dy')
st.code('''
for i in a_list:
    print(f'i = {i})
''')
