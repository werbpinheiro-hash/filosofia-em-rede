# BIBLIOTECA FILOSÓFICA ESCOLAR
st.divider()
st.header("📚 Biblioteca Filosófica Escolar")

st.write( "Encontre uma obra da biblioteca da escola "
    "para aprofundar sua investigação filosófica.")

livros = [
    {
        "titulo": "A Desobediência Civil",
        "autor": "Henry David Thoreau",
        "temas": ["liberdade", "política", "justiça", "estado"],
        "resumo": "Discute a resistência individual diante de leis injustas.",
        "problema": "Devemos obedecer a uma lei que consideramos injusta?"
    },
    {
        "titulo": "O Príncipe",
        "autor": "Nicolau Maquiavel",
        "temas": ["poder", "política", "governo", "estado"],
        "resumo": "Analisa a conquista e a manutenção do poder político.",
        "problema": "O governante pode agir contra a moral para conservar o poder?"
    },
    {
        "titulo": "Discurso sobre o Método",
        "autor": "René Descartes",
        "temas": ["conhecimento", "razão", "dúvida", "ciência"],
        "resumo": "Apresenta um método de investigação baseado na razão e na dúvida.",
        "problema": "Como podemos distinguir o conhecimento verdadeiro do falso?"
    },
    {
        "titulo": "O Mito da Caverna",
        "autor": "Platão",
        "temas": ["verdade", "educação", "conhecimento", "aparência"],
        "resumo": "Uma alegoria sobre a passagem das aparências ao conhecimento.",
        "problema": "Como saber se aquilo que vemos corresponde à realidade?"
    },
    {
        "titulo": "Sobre a Brevidade da Vida",
        "autor": "Sêneca",
        "temas": ["tempo", "vida", "felicidade", "morte"],
        "resumo": "Reflete sobre o uso do tempo e a maneira como vivemos.",
        "problema": "A vida é curta ou utilizamos mal o tempo?"
    },
    {
        "titulo": "A Ideologia Alemã",
        "autor": "Karl Marx e Friedrich Engels",
        "temas": ["sociedade", "ideologia", "trabalho", "história"],
        "resumo": "Investiga as relações entre vida material, sociedade e ideias.",
        "problema": "Como as condições materiais influenciam nossa maneira de pensar?"
    }
]

busca_livro = st.text_input(
    "🔎 Pesquise um tema na biblioteca:",
    key="busca_biblioteca"
)

if busca_livro.strip():
    termo = busca_livro.lower().strip()
    encontrados = []

    for livro in livros:
        campos = [
            livro["titulo"].lower(),
            livro["autor"].lower()
        ] + livro["temas"]

        if any(termo in campo for campo in campos):
            encontrados.append(livro)

    if encontrados:
        st.success(f"{len(encontrados)} obra(s) encontrada(s).")

        for livro in encontrados:
            with st.expander("📖 " + livro["titulo"], expanded=True):
                st.write("**Autor:**", livro["autor"])
                st.write("**Apresentação:**", livro["resumo"])
                st.write("**Problema norteador:**", livro["problema"])

                st.info(
                    "Esta obra faz parte do catálogo inicial "
                    "da biblioteca física da escola. "
                    "Consulte o exemplar para aprofundar a leitura.")
