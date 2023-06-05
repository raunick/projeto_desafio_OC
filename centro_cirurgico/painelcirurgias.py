import streamlit as st
import pandas as pd

pasta = 'data/'
def map_alta_liberada(valor):
    if valor == "Sim":
        return "📝"
    else:
        return "🏥"


def map_risco_paciente(valor):
    if valor == "Alto":
        return "🤕"
    elif valor == "Médio":
        return "🤒"
    else:
        return "🙂"



# estiliza as células com valores iguais a 2

def color_by_age(age):
    if age > 70:
        return "🟠"
    else:
        return ""


def load_data():
    df = pd.read_csv(f"{pasta}centro_cir.csv")
    df["Alta Liberada "] = df["Alta Liberada"].apply(map_alta_liberada)
    df = df.drop(columns=["Alta Liberada"])
    df["Risco Cirúrgico "] = df["Risco Cirúrgico"].apply(map_risco_paciente)
    df = df.drop(columns=["Risco Cirúrgico"])
    # df["Ex Pendente "] = df["Ex Pendente"].apply(map_exame_pendente)
    # df = df.drop(columns=["Ex Pendente"])
    # df["Interconsulta "] = df["Interconsulta"].apply(map_interconsulta_pendente)
    # df = df.drop(columns=["Interconsulta"])
    # aplica a função color_by_age na coluna 'Idade'
    # df["70+ "] = df["Idade"].apply(color_by_age)

    return df

def mostrar_paciente():
    # Cria um botão para atualizar a página
    if st.button("Atualizar"):
        st.experimental_rerun()
    df = load_data()
    st.title("Painel Cirurgico")
    st.write("Lista de pacientes")
    print(df)
    st.dataframe(df)

def atualizar():
    if st.button("Atualizar"):
        st.experimental_rerun()


def painel_cirurgico():
    # opções do menu
    opcao = st.sidebar.selectbox(
        "Selecione uma opção:",
        ["Painel Cirurgico", "Painel de Pendencias"],
    )

    # condições para cada opção do menu
    if opcao == "Painel Cirurgico":
        mostrar_paciente()
    elif opcao == "Painel de Pendencias":
        st.write("# 🚧EM DESENVOLVIMENTO🚧")
