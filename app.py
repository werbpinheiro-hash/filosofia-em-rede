                    )

                    st.write(
                        "📍 Consulte esta obra na biblioteca "
                        "física da escola."
                    )
        else:
            st.warning(
                "Nenhuma obra encontrada. "
                "Experimente outro tema ou autor."
            )

    st.divider()

    st.subheader("Aprofunde sua pesquisa")

    if pesquisa.strip():
        link = (
            "https://scholar.google.com/scholar?q="
            + quote_plus(pesquisa)
        )
        st.markdown(
            f"[Pesquisar no Google Acadêmico]({link})"
        )

    st.markdown(
        "[Consultar a SciELO](https://search.scielo.org/)"
    )

with aba2:
    st.header("Catálogo da biblioteca")

    st.write(
        f"Total de obras cadastradas: {len(livros)}"
    )

    for numero, livro in enumerate(livros, start=1):
        with st.expander(
            f"{numero}. {livro['titulo']}"
        ):
            st.write("**Autor:**", livro["autor"])
            st.write("**Temas:**", livro["temas"])
            st.write("**Apresentação:**", livro["resumo"])
            st.write(
                "**Problema norteador:**",
                livro["problema"]
            )
            if livro.get("A palavra do Professor"):
                st.write("**A palavra do professor:**", livro["A palavra do Professor"])

with aba3:
    st.header("Diário de reflexão filosófica")

    st.write(
        "Escolha uma obra da biblioteca e desenvolva "
        "uma reflexão a partir de sua leitura."
    )

    titulos = [livro["titulo"] for livro in livros]

    obra_escolhida = st.selectbox(
        "Selecione a obra:",
        titulos
    )

    livro_escolhido = next(
        livro for livro in livros
        if livro["titulo"] == obra_escolhida
    )

    st.info(livro_escolhido["problema"])
    if livro_escolhido.get("A palavra do Professor"):
        st.write("**A palavra do professor:**", livro_escolhido["A palavra do Professor"])

    reflexao = st.text_area(
        "Escreva sua reflexão:",
        height=200,
        placeholder=(
            "Apresente sua ideia, desenvolva argumentos "
            "e relacione sua resposta à leitura."
        )
    )

    if reflexao.strip():
        conteudo = (
            "FILOSOFIA EM REDE\n\n"
            "Obra: " + obra_escolhida + "\n\n"
            "Problema: " +
            livro_escolhido["problema"] + "\n\n"
            "Reflexão:\n" + reflexao
        )

        st.download_button(
            "📥 Baixar minha reflexão",
            data=conteudo.encode("utf-8"),
            file_name="reflexao_filosofica.txt",
            mime="text/plain"
        )

st.divider()

st.header("📂 Materiais digitais da biblioteca")

arquivos_pdf = sorted(Path(".").glob("*.pdf"))

if arquivos_pdf:
    for caminho in arquivos_pdf:
        with open(caminho, "rb") as arquivo:
            st.download_button(
                label="📄 " + caminho.name,
                data=arquivo.read(),
                file_name=caminho.name,
                mime="application/pdf",
                key="pdf_" + caminho.name
            )
else:
    st.write(
        "Nenhum PDF disponível na pasta principal."
    )

st.divider()

st.caption(
    "Filosofia em Rede | Biblioteca Filosófica Escolar | "
    "Da informação à investigação filosófica"
)

