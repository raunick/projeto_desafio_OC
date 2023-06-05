import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts

info = '''Ao selecionar uma especialidade,
todos os pacientes dessa especialidade vao aparecer'''

st.set_page_config(
    page_title="Flas de pacientes",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.title('🕒 Painel de controle de tempos do PA 🏥🚑')


def adicionar_coluna_bolinha_vermelha(df):
    def verifica_tempo_espera(tempo):
        minutos = int(tempo.split(':')[0])
        if minutos > 1:
            return '🔴'
        else:
            return ''
    df['Maior espera'] = df['Tempo'].apply(verifica_tempo_espera)
    return df


def ler_csv(nome_csv, pd_):
    with open(f'{nome_csv}', encoding='utf-8') as csv_file:
        df = pd_.read_csv(csv_file)
        d = adicionar_coluna_bolinha_vermelha(df)
    return st.dataframe(d)


def ler_csv_all(nome_csv, pd_):
    with open(f'{nome_csv}', encoding='utf-8') as csv_file:
        df = pd_.read_csv(csv_file)
    return df


def grafico_velocimetro(d, key):
    options = {
        "series": [
            {
                "type": "gauge",
                "data": [{"value": d, "name": "MINUTOS"}],
                "axisLine": {
                    "lineStyle": {
                        "width": 30,
                        "color": [[0.25, "#85ba53"],
                                  [0.5, "#549fe0"],
                                  [0.75, "#f8ce55"],
                                  [1, "#eb6f70"]],
                    }
                },
                "axisLabel": {"min": 0, "max": 10, "show": False},
                "title": {"offsetCenter": [0, "70%"],
                          "textStyle": {"color": ""}},
                "detail": {
                    "fontSize": 30,
                    "fontWeight": "bolder",
                    "valueAnimation": True,
                    "formatter": f"{int(round(d[0]*0.1))} min",
                    "offsetCenter": [0, "110%"],
                    "color":""
                },
                "pointer": {"length": "80%", "width": 5},
                "itemStyle": {
                    "color": "#212529",
                    "borderColor": "#383e44",
                    "borderWidth": 2},
            }
        ]
    }
    st_echarts(options=options, height="200px", key=key)


filas = st.sidebar.selectbox(
    'Selecione uma fila:',
    ('👥 Triagem', '💻 Cadastro',
     '👨‍⚕️ Medico', '🏥 Todos', '👨‍💻 Codigo',))
filas


if filas == '🏥 Todos':
    dataTRIAGEM = [20]
    dataCADASTRO = [60]
    dataMEDICO = [90]
    col1, col2 = st.columns((7, 3))
    with col1:
        st.write("👥 Tabela Triagem:")
        ler_csv("TRIAGEM.csv", pd)
        st.write("💻 Tabela CADASTRO:")
        ler_csv("CADASTRO.csv", pd)
        st.write("👨‍⚕️ Tabela MEDICO:")
        ler_csv("MEDICO.csv", pd)
    with col2:
        grafico_velocimetro(dataTRIAGEM, key="TRIAGEM")
        grafico_velocimetro(dataCADASTRO, key="CADASTRO")
        grafico_velocimetro(dataMEDICO, key="MEDICO")
    df = ler_csv_all("filas.csv", pd)
    especialidades = np.unique(df['Especialidades'].values)
    options = st.sidebar.multiselect(
        'Escolha a Especialidade',
        especialidades,
        help=info,
        default=['CLÍNICA MÉDICA']
        )
    st.write('Especialidade selecionada:', options)
    df_filtrado = df[df['Especialidades'].isin(options)]
    st.dataframe(df_filtrado)
elif filas == '👨‍💻 Codigo':
    with open('arquivo.txt', 'r', encoding="utf-8") as f:
        codigo = f.read()
    st.code(codigo, language='python')
