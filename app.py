
import streamlit as st
import unicodedata
from pathlib import Path
from urllib.parse import quote_plus

st.set_page_config(
    page_title="Filosofia em Rede",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Filosofia em Rede")
st.subheader("Conhecimento além da informação")

st.write(
    "Da pesquisa digital à leitura filosófica. "
    "Explore as obras disponíveis na biblioteca escolar, "
    "conheça seus autores e investigue problemas filosóficos."
)

def normalizar(texto):
    texto = str(texto).lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )

# CATÁLOGO DA BIBLIOTECA

livros = [
    {
        "titulo": "100 Minutos para Entender Nietzsche",
        "autor": "Coleção Astral Cultural",
        "temas": "Nietzsche, moral, valores, verdade, niilismo",
        "resumo": "Introdução ao pensamento de Nietzsche e sua crítica aos valores tradicionais.",
        "problema": "Como podemos questionar os valores que orientam nossa vida?"
    },
    {
        "titulo": "100 Minutos para Entender Aristóteles",
        "autor": "Coleção Astral Cultural",
        "temas": "ética, política, virtude, felicidade, lógica",
        "resumo": "Apresentação das principais ideias de Aristóteles sobre conhecimento, ética e vida coletiva.",
        "problema": "O que significa viver bem?"
    },
    {
        "titulo": "100 Minutos para Entender Platão",
        "autor": "Coleção Astral Cultural",
        "temas": "Platão, verdade, conhecimento, justiça, educação",
        "resumo": "Introdução às ideias de Platão sobre conhecimento, realidade e justiça.",
        "problema": "Aquilo que percebemos corresponde à realidade?"
    },
    {
        "titulo": "100 Minutos para Entender Jung",
        "autor": "Coleção Astral Cultural",
        "temas": "Jung, psicologia, inconsciente, identidade",
        "resumo": "Introdução às ideias de Carl Gustav Jung sobre a psique e o inconsciente.",
        "problema": "Conhecemos completamente nossa própria identidade?"
    },
    {
        "titulo": "100 Minutos para Entender Freud",
        "autor": "Coleção Astral Cultural",
        "temas": "Freud, inconsciente, desejo, comportamento",
        "resumo": "Introdução ao pensamento de Freud e à importância do inconsciente.",
        "problema": "Somos plenamente conscientes das razões de nossas escolhas?"
    },
    {
        "titulo": "100 Minutos para Entender Lacan",
        "autor": "Coleção Astral Cultural",
        "temas": "Lacan, linguagem, desejo, sujeito, psicanálise",
        "resumo": "Apresentação introdutória de conceitos associados à psicanálise lacaniana.",
        "problema": "Como a linguagem participa da formação de quem somos?"
    },
    {
        "titulo": "A Ideologia Alemã",
        "autor": "Karl Marx e Friedrich Engels",
        "temas": "ideologia, sociedade, trabalho, história, política",
        "resumo": "Investiga as relações entre condições materiais, organização social e produção das ideias.",
        "problema": "Como a sociedade influencia nossa maneira de pensar?"
    },
    {
        "titulo": "O Ente e a Essência",
        "autor": "Tomás de Aquino",
        "temas": "metafísica, existência, essência, filosofia medieval",
        "resumo": "Examina conceitos fundamentais da metafísica, especialmente ente e essência.",
        "problema": "O que significa dizer que alguma coisa existe?"
    },
    {
        "titulo": "Discurso sobre o Método",
        "autor": "René Descartes",
        "temas": "razão, dúvida, ciência, método, conhecimento",
        "resumo": "Apresenta reflexões sobre o método e a busca de conhecimentos seguros.",
        "problema": "Como distinguir uma opinião de um conhecimento fundamentado?"
    },
    {
        "titulo": "A Desobediência Civil",
        "autor": "Henry David Thoreau",
        "temas": "liberdade, justiça, estado, política, resistência",
        "resumo": "Discute a consciência individual e a resistência diante de leis injustas.",
        "problema": "É correto desobedecer a uma lei considerada injusta?"
    },
    {
        "titulo": "Carta sobre a Tolerância",
        "autor": "John Locke",
        "temas": "tolerância, religião, liberdade, política, direitos",
        "resumo": "Defende a tolerância religiosa e discute os limites da autoridade política.",
        "problema": "Como conviver com pessoas que possuem crenças diferentes?"
    },
    {
        "titulo": "Sobre Como Lidar Consigo Mesmo",
        "autor": "Arthur Schopenhauer",
        "temas": "vida, sofrimento, autoconhecimento, felicidade",
        "resumo": "Reflexões filosóficas sobre a relação do indivíduo consigo mesmo.",
        "problema": "O autoconhecimento pode nos ajudar a viver melhor?"
    },
    {
        "titulo": "Sobre a Brevidade da Vida",
        "autor": "Sêneca",
        "temas": "tempo, vida, morte, felicidade, estoicismo",
        "resumo": "Reflete sobre a maneira como utilizamos o tempo de nossa existência.",
        "problema": "A vida é curta ou desperdiçamos o tempo disponível?"
    },
    {
        "titulo": "O Mito da Caverna",
        "autor": "Platão",
        "temas": "verdade, conhecimento, aparência, educação, realidade",
        "resumo": "Alegoria que permite refletir sobre aparência, ignorância e conhecimento.",
        "problema": "Como reconhecer que nossas certezas podem estar equivocadas?"
        "A palavra do Professor": "A palavra do Professor": "No mito da caverna de Platão iremos observar o processo de descoberta de duas realidades humanas: o mundo da verdade e o mundo da ignorancia. Sua leitura propiciara a voce escolher qual mundo deve pertencer."
    },
    {
        "titulo": "Mitos Gregos",
        "autor": "Nathaniel Hawthorne",
        "temas": "mitologia, cultura, deuses, narrativa, tradição",
        "resumo": "Reconta narrativas da mitologia grega, permitindo investigar seus significados culturais.",
        "problema": "O que os mitos revelam sobre a maneira humana de compreender o mundo?"
    },
    {
        "titulo": "Édipo Rei",
        "autor": "Sófocles",
        "temas": "destino, liberdade, verdade, tragédia, responsabilidade",
        "resumo": "Tragédia grega que aborda destino, conhecimento e responsabilidade humana.",
        "problema": "Somos responsáveis por consequências que não conseguimos prever?"
    },
    {
        "titulo": "Filosofia Bantu",
        "autor": "Placide Tempels",
        "temas": "filosofia africana, cultura, existência, ontologia",
        "resumo": "Apresenta uma interpretação da ontologia bantu, cuja abordagem também pode ser analisada criticamente.",
        "problema": "Quem possui autoridade para interpretar o pensamento de outra cultura?"
    },
    {
        "titulo": "Platão e a Teoria das Ideias",
        "autor": "A confirmar no exemplar",
        "temas": "Platão, ideias, realidade, conhecimento, metafísica",
        "resumo": "Estudo introdutório sobre a teoria das Ideias de Platão.",
        "problema": "Existe uma realidade que ultrapassa aquilo que percebemos?"
    },
    {
        "titulo": "Breve História da Ciência Moderna",
        "autor": "A confirmar no exemplar",
        "temas": "ciência, história, conhecimento, método, modernidade",
        "resumo": "Estudo histórico sobre a formação e o desenvolvimento da ciência moderna.",
        "problema": "Como os critérios para produzir conhecimento científico mudaram ao longo da história?"
    },
    {
        "titulo": "O Príncipe",
        "autor": "Nicolau Maquiavel",
        "temas": "poder, política, estado, governo, autoridade",
        "resumo": "Analisa a conquista, a manutenção e os desafios do poder político.",
        "problema": "Quais limites éticos devem orientar o exercício do poder?"
    },
    {
        "titulo": "A Divina Comédia - Paraíso",
        "autor": "Dante Alighieri",
        "temas": "religião, justiça, virtude, transcendência, literatura",
        "resumo": "Parte final da jornada poética de Dante, dedicada ao Paraíso.",
        "problema": "Como diferentes concepções de justiça se relacionam com a ideia de uma vida boa?"
    },
    {
        "titulo": "A Divina Comédia - Purgatório",
        "autor": "Dante Alighieri",
        "temas": "moral, transformação, liberdade, responsabilidade, literatura",
        "resumo": "Parte da jornada de Dante que explora transformação moral e purificação.",
        "problema": "É possível transformar nossa maneira de agir e de compreender o bem?"
    },
    {
        "titulo": "Filosofia",
        "autor": "Gabriel Chalita",
        "temas": "filosofia, ética, pensamento, conhecimento, sociedade",
        "resumo": "Obra introdutória voltada ao estudo de questões e temas filosóficos.",
        "problema": "Por que precisamos filosofar sobre nossa realidade?"
    }
]

st.divider()

aba1, aba2, aba3 = st.tabs([
    "🔎 Pesquisar",
    "📚 Catálogo completo",
    "✍️ Reflexão filosófica"
])

with aba1:
    st.header("Pesquisar na biblioteca")

    pesquisa = st.text_input(
        "Digite um tema, autor ou título:",
        placeholder="Ex.: liberdade, poder, ética, Platão",
        key="pesquisa_principal"
    )

    if pesquisa.strip():
        termo = normalizar(pesquisa)

        encontrados = []

        for livro in livros:
            texto = normalizar(
                livro["titulo"] + " " +
                livro["autor"] + " " +
                livro["temas"] + " " +
                livro["resumo"]
            )

            if termo in texto:
                encontrados.append(livro)

        if encontrados:
            st.success(
                f"{len(encontrados)} obra(s) encontrada(s)."
            )

            for livro in encontrados:
                with st.expander(
                    "📖 " + livro["titulo"],
                    expanded=True
                ):
                    st.write("**Autor:**", livro["autor"])
                    st.write("**Temas:**", livro["temas"])

                    st.subheader("Apresentação da obra")
                    st.write(livro["resumo"])

                    st.subheader("Problema norteador")
                    st.info(livro["problema"])

                    st.subheader("A palavra do professor")
                    st.write(
                        "Espaço destinado à explicação "
                        "e à orientação de leitura do professor."
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
