import streamlit as st

st.set_page_config(
    page_title="Filosofia em Rede",
    page_icon="📚"
)

st.title("📚 Filosofia em Rede")
st.subheader("Conhecimento além da informação")

st.write(
    "Um espaço de pesquisa, reflexão crítica "
    "e aprofundamento filosófico."
)

pesquisa = st.text_input("O que você deseja pesquisar?")

if st.button("Pesquisar"):
    if pesquisa.strip():
        st.info(f"Você pesquisou: {pesquisa}")
        st.write("Em breve: fontes confiáveis e reflexões filosóficas.")
    else:
        st.warning("Digite um assunto para pesquisar.")
