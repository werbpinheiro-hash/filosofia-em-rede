import streamlit as st
from urllib.parse import quote_plus
from pathlib import Path

st.set_page_config(
    page_title="Filosofia em Rede",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f8f9fc;
    color: #202b40;
}
h1, h2, h3 {
    color: #17365d;
}
.stButton > button {
    background-color: #17365d;
    color: white;
    border-radius: 9px;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Filosofia em Rede")
st.subheader("Conhecimento além da informação")

st.write(
    "Uma plataforma educacional para pesquisar, "
    "compreender e questionar informações por meio "
    "do pensamento filosófico."
)

st.divider()

tema = st.text_input(
    "🔎 O que você deseja pesquisar?",
    placeholder="Ex.: liberdade, tecnologia, ética, política..."
)

conteudos = {
    "liberdade": {
        "conceito": (
            "A liberdade envolve a possibilidade de escolher "
            "e agir, mas também levanta questões sobre "
            "responsabilidade, autonomia e condições sociais."
        ),
        "filosofos": [
            "Jean-Paul Sartre — liberdade e responsabilidade.",
            "Immanuel Kant — autonomia e razão.",
            "Hannah Arendt — liberdade e ação política."
        ],
        "perguntas": [
            "Somos realmente livres para escolher?",
            "A sociedade limita nossa liberdade?",
            "As redes sociais influenciam nossas decisões?"
        ]
    },
    "tecnologia": {
        "conceito": (
            "A tecnologia transforma as formas de comunicação, "
            "aprendizagem, trabalho e produção do conhecimento."
        ),
        "filosofos": [
            "Michel Serres — transformações do saber.",
            "Marshall McLuhan — os meios e suas influências.",
            "Pierre Lévy — cibercultura e inteligência coletiva."
        ],
        "perguntas": [
            "Ter acesso à informação significa conhecer?",
            "A tecnologia modifica nossa maneira de pensar?",
            "A escola ainda é o principal lugar do saber?"
        ]
    },
    "ética": {
        "conceito": (
            "A ética investiga as ações humanas, os valores "
            "e os critérios utilizados para distinguir "
            "condutas justificáveis e injustificáveis."
        ),
        "filosofos": [
            "Aristóteles — virtude e vida boa.",
            "Immanuel Kant — dever e moralidade.",
            "Hans Jonas — responsabilidade e tecnologia."
        ],
        "perguntas": [
            "Toda atitude permitida é moralmente correta?",
            "Quem responde pelas consequências da tecnologia?",
            "Como agir diante de informações falsas?"
        ]
    },
    "política": {
        "conceito": (
            "A filosofia política investiga o poder, "
            "a autoridade, a justiça, o Estado "
            "e a organização da vida coletiva."
        ),
        "filosofos": [
            "Platão — justiça e organização da cidade.",
            "Aristóteles — comunidade e vida política.",
            "Michel Foucault — relações de poder."
        ],
        "perguntas": [
            "Qual é a diferença entre poder e autoridade?",
            "O poder está presente nas relações cotidianas?",
            "Como a informação influencia a democracia?"
        ]
    }
}

def links_pesquisa(assunto):
    busca = quote_plus(assunto)
    return {
        "Google Acadêmico":
            "https://scholar.google.com/scholar?q=" + busca,
        "SciELO":
            "https://search.scielo.org/?q=" + busca,
        "Portal de Periódicos CAPES":
            "https://www.periodicos.capes.gov.br/",
        "Internet Encyclopedia of Philosophy":
            "https://iep.utm.edu/"
    }

if st.button("🔍 Pesquisar", type="primary"):
    if not tema.strip():
        st.warning("Digite um assunto para pesquisar.")
    else:
        st.session_state["tema"] = tema.strip()

if "tema" in st.session_state:
    assunto = st.session_state["tema"]
    chave = assunto.lower().strip()
    dados = conteudos.get(chave)

    st.divider()
    st.header("Resultado: " + assunto)

    aba1, aba2, aba3, aba4 = st.tabs([
        "📖 Informar",
        "🧠 Compreender",
        "❓ Problematizar",
        "🔗 Fontes"
    ])

    with aba1:
        st.header("1. Informar")
        if dados:
            st.write(dados["conceito"])
        else:
            st.info(
                "Ainda não há uma explicação cadastrada "
                "para este tema. Consulte as fontes "
                "acadêmicas na quarta aba."
            )

    with aba2:
        st.header("2. Compreender")
        if dados:
            st.write("Perspectivas filosóficas:")
            for autor in dados["filosofos"]:
                st.write("• " + autor)
        else:
            st.write(
                "Pesquise diferentes autores e compare "
                "suas interpretações sobre o tema."
            )

        st.info(
            "Não basta encontrar uma resposta. "
            "É necessário compreender seus argumentos."
        )

    with aba3:
        st.header("3. Problematizar")
        if dados:
            for pergunta in dados["perguntas"]:
                st.write("❓ " + pergunta)
        else:
            st.write(
                "Quem produziu essa informação? "
                "Quais argumentos a sustentam? "
                "Existem interpretações diferentes?"
            )

        resposta = st.text_area(
            "Escreva sua reflexão:",
            key="reflexao"
        )

        if resposta:
            st.success(
                "Reflexão registrada nesta sessão. "
                "Continue desenvolvendo seus argumentos."
            )

    with aba4:
        st.header("4. Pesquisar em fontes acadêmicas")
        st.caption(
            "Os links abrem pesquisas externas. "
            "Os resultados ainda não são verificados "
            "automaticamente pela plataforma."
        )

        for nome, endereco in links_pesquisa(assunto).items():
            st.markdown(f"🔗 [{nome}]({endereco})")

st.divider()

st.header("📚 Biblioteca Filosófica")

pdf = Path("A Liberdade em Jean Paul Sartre.pdf")

if pdf.exists():
    with open(pdf, "rb") as arquivo:
        st.download_button(
            "📄 A Liberdade em Jean-Paul Sartre",
            data=arquivo.read(),
            file_name=pdf.name,
            mime="application/pdf"
        )
else:
    st.info(
        "A biblioteca poderá receber livros e "
        "materiais de estudo selecionados."
    )

st.divider()

st.caption()
    "Filosofia em Rede | Protótipo educacional "
    "| Pesquisa, pensamento crítico e conhecimento."
