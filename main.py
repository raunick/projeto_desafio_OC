import streamlit as st
from TI.leitocsv import ler_csv
from TI.gestao_impressora import exibir_informacoes_impressao
from TI.gestao_impressora import obter_informacoes_impressao
from painelpa.painel import painelPA
from unidade_internacao.painelpacientes import painel_internacao
from centro_cirurgico.painelcirurgias import painel_cirurgico

def main():
    st.set_page_config(
        page_title="Projeto",
        page_icon="🏥",
    )

    st.sidebar.write("🍎 Newton v1.0")
    opcao = st.sidebar.selectbox(
        "Escolha uma opção:",
        [
            "Apresentação Projeto",
            "TI",
            "Centro Cirurgico",
            "Pronto Atendimento",
            "Unidade de Internação",
            "Faturamento",
        ],
    key='opcao')
    if opcao == "Apresentação Projeto":
        # Nome do arquivo Markdown
        arquivo_md = "projeto.md"

        # Abre o arquivo em modo de leitura
        with open(arquivo_md, "r", encoding="utf-8") as arquivo:
            # Lê o conteúdo do arquivo
            conteudo_md = arquivo.read()
            # print(conteudo_md)

        # Exibe o conteúdo na aplicação Streamlit
        st.write(conteudo_md)
    elif opcao == "TI":
        opti = st.sidebar.selectbox(
            "Escolha um Painel:", ["Gestao de Os", "Gestao de Impressora"],
        key='ti')
        st.write("# 🖥️ TI")
        st.write(f"# 🚧{opti}🚧")
        if opti == "Gestao de Os":
            st.write("OS")
            ler_csv()
        elif opti == "Gestao de Impressora":
            obter_informacoes_impressao()
            exibir_informacoes_impressao()
    elif opcao == "Centro Cirurgico":
        cc = st.sidebar.selectbox(
            "Escolha sua Setor:", [
                "Bloco Cirurgico", "Bloco Obstetrico", "Hemodinamica"])
        st.write("# 🛠 Centro Cirurgico")
        if cc == "Bloco Cirurgico":
            painel_cirurgico()
        elif cc == "Bloco Obstetrico":
            painel_cirurgico()
        else :
            st.write("# 🚧EM CRIAÇÃO🚧")
    elif opcao == "Pronto Atendimento":
        oppa = st.sidebar.selectbox(
            "Escolha um Painel:", [
                "Painel de Senhas", 
                "Painel de pendencias",
                "Inteligência Artificial",],
        key='pa')
        st.write("# 🛠 Pronto Atendimento")
        if oppa == "Painel de Senhas":
            painelPA()
        elif oppa == "Inteligência Artificial":
            # Abre o arquivo em modo de leitura
            with open("ia.md", "r", encoding="utf-8") as arquivo:
                # Lê o conteúdo do arquivo
                ia = arquivo.read()
                # print(conteudo_md)

            # Exibe o conteúdo na aplicação Streamlit
            st.write(ia)
        elif oppa == "Painel de pendencias":
            st.write("# 🚧EM CRIAÇÃO🚧")
    elif opcao == "Unidade de Internação":
        ui = st.sidebar.selectbox(
            "Escolha sua Unidade:", [
                "4º andar", "6º andar", "7º andar"])
        st.write("# Unidade de Internação")
        if ui == '4º andar':
            painel_internacao()
        else :
            st.write("# 🚧EM CRIAÇÃO🚧")
    elif opcao == "Faturamento":
        st.write("# 🛠 Faturamento")
        st.write("# 🚧EM CRIAÇÃO🚧")

if __name__ == '__main__':
    main()