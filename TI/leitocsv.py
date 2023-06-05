import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def ler_csv():
    # Título do aplicativo
    st.title("Análise de Dados")

    # Upload do arquivo CSV
    file = st.file_uploader("Carregar arquivo CSV", type="csv")

    if file is not None:
        # Leitura dos dados do arquivo CSV
        data = pd.read_csv(file, parse_dates=True)

        # Exibição do DataFrame
        st.subheader("DataFrame")
        st.write(data.head())
        st.write(data.describe())

        # Colunas disponíveis para seleção
        columns = data.columns.tolist()

        # Seleção das colunas para gráfico
        x_column = st.sidebar.selectbox("Eixo X", columns)
        y_column = st.sidebar.selectbox("Eixo Y", columns)

        # Seleção do tipo de gráfico (soma ou contagem)
        chart_type = st.sidebar.radio("Tipo de Gráfico", ("Soma", "Contagem"))

        # Cálculo dos valores para o gráfico
        if chart_type == "Soma":
            chart_data = data.groupby(x_column)[y_column].sum()
        else:
            chart_data = data[x_column].value_counts()

        # Plotagem do gráfico
        st.subheader("Gráfico")
        plt.barh(chart_data.index, chart_data.values)
        plt.xlabel(x_column)
        plt.ylabel("Soma" if chart_type == "Soma" else "Contagem")
        # plt.xticks(rotation=90)
        st.pyplot(plt)
        st.subheader("Gráfico 2")
        st.line_chart(chart_data)
        st.bar_chart(chart_data)


if __name__ == '__ler_csv__':
    ler_csv()