import pandas as pd
import streamlit as st
### COLOCA UM TITULO
st.title("VELOZ LOCADORA")
st.sidebar.title("VELOZ LOCADORA")
st.sidebar.image("logo.png")
### ESCREVE
st.sidebar.write("Boa Tarde. Escolha o seu carro para alugar com a melhor empresa do país")
st.markdown('---')

carros = ["Civic", "BMW", "Ford Focus", "Audi A8", "Volkswagen", "Ford Fiesta 2012"]

precos = {
    "Civic": 245,
    "BMW": 670,
    "Ford Focus": 220,
    "Audi A8": 1420,
    "Volkswagen": 180,
    "Ford Fiesta 2012": 120
}
def inicializar_estado():
    if "indice_carro" not in st.session_state:
        st.session_state.indice_carro = 0
    if "historico" not in st.session_state:
        st.session_state.historico = []

# Chamada da função no início do app
inicializar_estado()

if "indice_carro" not in st.session_state:
    st.session_state.indice_carro = 0

if "indice_carro" not in st.session_state:
    st.session_state.indice_carro = 0
if "historico" not in st.session_state:
    st.session_state.historico = []

# Layout com setas
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️"):
        st.session_state.indice_carro = (st.session_state.indice_carro - 1) % len(carros)
with col3:
    if st.button("➡️"):
        st.session_state.indice_carro = (st.session_state.indice_carro + 1) % len(carros)
carro_escolhido = carros[st.session_state.indice_carro]
diaria = precos[carro_escolhido]


st.image(f"{carro_escolhido}.png", caption=carro_escolhido)
st.markdown(f"## Você escolheu alugar: {carro_escolhido}")

gps = st.checkbox("Adicionar GPS (R$ 15 por dia)")
preco_gps = 15
seguro = st.checkbox("Adicionar seguro (R$ 30 por dia)")
lavagem = st.checkbox("Lavagem inclusa (R$ 20 fixo)")

if carro_escolhido == "Civic":
    diaria = 245

elif carro_escolhido == "BMW":
    diaria = 670

elif carro_escolhido == "Ford Focus":
    diaria = 220

elif carro_escolhido == "Audi A8":
    diaria = 1420

elif carro_escolhido == "Volkswagen":
    diaria = 180

elif carro_escolhido == "Ford Fiesta 2012":
    diaria = 120


dias = st.text_input(F"Por quantos dias você alugou o {carro_escolhido} ?")
km = st.number_input(f"Quantos km você rodou?")

if st.button("Calcular"):
    if dias.isdigit():
        dias = int(dias)
        preco_gps = 15
        preco_seguro = 30
        preco_lavagem = 20

        custo_gps = preco_gps * dias if gps else 0
        custo_seguro = preco_seguro * dias if seguro else 0
        custo_lavagem = preco_lavagem if lavagem else 0

        total_dias = diaria * dias
        total_km = km * 0.15
        aluguel = total_dias + total_km + custo_gps + custo_seguro + custo_lavagem

        extras = []
        if gps: extras.append("GPS")
        if seguro: extras.append("seguro")
        if lavagem: extras.append("lavagem")
        extras_msg = f" incluindo {', '.join(extras)}" if extras else ""


        st.success(f"Você alugou o {carro_escolhido} por {dias} dias{extras_msg}, rodou {km} km. Valor total: R$ {aluguel:.2f}")
