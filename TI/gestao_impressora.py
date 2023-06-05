import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def obter_informacoes_impressao():
    # Simulação de dados de impressão para 5 impressoras diferentes
    dados_impressao = {
        'Nome da Impressora': ['PA Adulto', 'CC_AND3 B',
                               'COORD_TI C', 'FAT_Cental', 'PA Infantil'],
        'Total de Páginas Impressas': [100, 150, 80, 200, 120],
        'Nível de Toner': [75, 90, 60, 50, 70]
    }

    # Cria um DataFrame Pandas com os dados
    df_impressao = pd.DataFrame(dados_impressao)

    return df_impressao


def exibir_informacoes_impressao():
    df_impressao = obter_informacoes_impressao()

    st.title("Informações de Impressão")
    st.write(df_impressao)
    st.line_chart(df_impressao.set_index('Nome da Impressora')[
        'Total de Páginas Impressas'])
    st.line_chart(df_impressao.set_index('Nome da Impressora')[
        'Nível de Toner'])
    # Gráfico de barras do Total de Páginas Impressas
    fig, ax = plt.subplots()
    ax.bar(df_impressao['Nome da Impressora'],
           df_impressao['Total de Páginas Impressas'])
    ax.set_xlabel('Impressora')
    ax.set_ylabel('Total de Páginas Impressas')
    ax.set_title('Total de Páginas Impressas por Impressora')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Gráfico de barras do Nível de Toner
    fig2, ax2 = plt.subplots()
    ax2.bar(df_impressao['Nome da Impressora'],
            df_impressao['Nível de Toner'])
    ax2.set_xlabel('Impressora')
    ax2.set_ylabel('Nível de Toner')
    ax2.set_title('Nível de Toner por Impressora')
    plt.xticks(rotation=45)
    st.pyplot(fig2)
