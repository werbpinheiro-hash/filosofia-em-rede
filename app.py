            resultados.append(livro)
    return resultados


st.title("📚 Filosofia em Rede")
st.subheader("Conhecimento além da informação")
st.write("Pesquise um tema, descubra obras da biblioteca escolar e aprofunde sua reflexão filosófica.")

aba_busca, aba_biblioteca, aba_sobre = st.tabs(["🔎 Pesquisar", "📚 Biblioteca", "ℹ️ Sobre"])

with aba_busca:
    with st.form("form_busca"):
        consulta = st.text_input("Qual tema ou autor você deseja pesquisar?", placeholder="Ex.: liberdade, poder, conhecimento, Platão")
        enviado = st.form_submit_button("Pesquisar")
    if enviado:
        st.session_state["consulta"] = consulta.strip()
    termo_atual = st.session_state.get("consulta", "")
    if termo_atual:
        encontrados = pesquisar(termo_atual)
        st.markdown("### Obras relacionadas")
        if encontrados:
            st.success(f"{len(encontrados)} obra(s) encontrada(s) no catálogo inicial.")
            for livro in encontrados:
                with st.expander(f"📖 {livro['titulo']} — {livro['autor']}", expanded=True):
                    st.write("**Apresentação da obra:**", livro["apresentacao"])
                    st.write("**Problema norteador:**", livro["problema"])
                    st.info("**Explicação do professor:** espaço reservado para comentário ou áudio autoral a ser cadastrado.")
                    st.caption("Consulte o exemplar físico na biblioteca escolar para aprofundar a leitura.")
        else:
            st.warning("Nenhuma obra cadastrada para esta pesquisa. Experimente outra palavra ou consulte o catálogo.")
        st.markdown("### Aprofunde sua pesquisa")
        st.link_button("Pesquisar no Google Acadêmico", "https://scholar.google.com/scholar?q=" + __import__("urllib.parse", fromlist=["quote_plus"]).quote_plus(termo_atual))
        st.link_button("Pesquisar na SciELO", "https://search.scielo.org/?q=" + __import__("urllib.parse", fromlist=["quote_plus"]).quote_plus(termo_atual))
        st.markdown("### Sua reflexão")
        reflexao = st.text_area("O que você pensa sobre o problema apresentado?", key="reflexao_estudante")
        if reflexao.strip():
            st.download_button("Baixar minha reflexão", data=f"Tema: {termo_atual}\n\n{reflexao}", file_name="minha_reflexao.txt", mime="text/plain")

with aba_biblioteca:
    st.markdown("### Catálogo inicial da biblioteca física")
    st.caption("As obras foram cadastradas a partir da fotografia enviada. Confirme os dados bibliográficos nos exemplares antes da divulgação definitiva.")
    for livro in LIVROS:
        with st.expander(f"{livro['titulo']} — {livro['autor']}"):
            st.write(livro["apresentacao"])
            st.write("**Temas:**", ", ".join(livro["temas"]))
            st.write("**Problema norteador:**", livro["problema"])
    st.markdown("### Arquivos PDF disponíveis no projeto")
    pdfs = sorted(Path(".").glob("*.pdf"))
    if pdfs:
        for pdf in pdfs:
            with pdf.open("rb") as arquivo:
                st.download_button(f"Baixar {pdf.name}", data=arquivo.read(), file_name=pdf.name, mime="application/pdf", key=f"pdf_{pdf.name}")
    else:
        st.caption("Nenhum PDF encontrado na pasta principal do projeto.")

with aba_sobre:
    st.write("O Filosofia em Rede conecta a pesquisa digital à leitura de obras disponíveis na biblioteca física da escola.")
    st.write("**Percurso pedagógico:** informar → compreender → problematizar → consultar a obra.")
    st.info("Esta versão utiliza um catálogo local, não inteligência artificial. Os links acadêmicos abrem pesquisas externas; seus resultados não são verificados automaticamente.")

st.divider()
st.caption("Filosofia em Rede | Protótipo educacional de mediação da leitura filosófica")
