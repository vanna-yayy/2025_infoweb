import streamlit as st
from retangulo import Retangulo

class RetanguloUi:
     def main():
          st.header("Cálculo com retângulo")
          base = st.text_input("Informe a base:")
          altura = st.text_input("informe a altura")
          if st.button("Calcular"):
                b = float(base)
                h = float(altura)
                r = Retangulo(b,h)
                st.write(r)
                st.write(r.calc_area())
                st.write(r.calc_diagonal())