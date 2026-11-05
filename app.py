import streamlit as st
from pathlib import Path
from urllib.parse import quote_plus
import unicodedata

st.set_page_config(page_title="Filosofia em Rede", page_icon="📚", layout="wide")


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower().strip())
    return "".join(c for c in texto if not unicodedata.combining(c))


CONTEUDOS = {
    "liberdade": {
        "conceito": "A liberdade envolve escolhas, autonomia e responsabilidade. Também depende das condições em que vivemos.",
        "autores": ["Jean-Paul Sartre: escolhas e responsabilidade.", "Immanuel Kant: autonomia da razão.", "Hannah Arendt: liberdade e ação política."],
        "questoes": ["Toda escolha é livre?", "As redes sociais influenciam nossas decisões?", "É possível ser livre sem responsabilidade?"]
    },
    "tecnologia": {
        "conceito": "As tecnologias transformam a comunicação, a aprendizagem e as formas de acesso ao conhecimento.",
        "autores": ["Michel Serres: mudanças na transmissão do saber.", "Marshall McLuhan: os meios de comunicação e seus efeitos.", "Pierre Lévy: cibercultura e inteligência coletiva."],
        "questoes": ["Informação é o mesmo que conhecimento?", "Como a tecnologia modifica a escola?", "Quem controla a informação que recebemos?"]
    },
    "etica": {
        "conceito": "A ética examina os valores, os argumentos e as consequências de nossas ações.",
        "autores": ["Aristóteles: virtudes e vida boa.", "Immanuel Kant: dever e moralidade.", "Hans Jonas: responsabilidade diante da tecnologia."],
        "questoes": ["O que torna uma ação justa?", "Compartilhar notícias sem verificar é responsável?", "Devemos pensar nas consequências futuras de nossas escolhas?"]
    },
    "politica": {
        "conceito": "A filosofia política investiga o poder, a justiça, o Estado e a convivência coletiva.",
        "autores": ["Platão: justiça e organização da cidade.", "Aristóteles: comunidade política.", "Michel Foucault: relações de poder."],
        "questoes": ["Poder e autoridade são a mesma coisa?", "Como reconhecer uma decisão justa?", "A informação influencia a democracia?"]
    },
    "conhecimento": {
        "conceito": "A teoria do conhecimento investiga como justificamos aquilo que afirmamos saber.",
        "autores": ["Platão: opinião e conhecimento.", "René Descartes: dúvida e certeza.", "David Hume: experiência e investigação."],
        "questoes": ["Como sabemos que algo é verdadeiro?", "Uma informação muito compartilhada é confiável?", "O que diferencia uma opinião de um argumento?"]
    }
}

st.title("📚 Filosofia em Rede")
st.subheader("Conhecimento além da informação")
st.write("Pesquise, compreenda, compare fontes e desenvolva seu pensamento crítico.")

with st.form("busca"):
    entrada = st.text_input("O que você deseja pesquisar?", placeholder="Ex.: liberdade, tecnologia, ética...")
    pesquisar = st.form_submit_button("🔎 Pesquisar")

if pesquisar:
    if entrada.strip():
        st.session_state["assunto"] = entrada.strip()
    else:
        st.warning("Digite um tema antes de pesquisar.")

if "assunto" in st.session_state:
    assunto = st.session_state["assunto"]
    chave = normalizar(assunto)
    dados = CONTEUDOS.get(chave)
    st.divider()
    st.header("Pesquisa: " + assunto)
    informar, compreender, problematizar, fontes = st.tabs([
        "📖 Informar", "🧠 Compreender", "❓ Problematizar", "🔗 Fontes"
    ])

    with informar:
        st.markdown("### 1. Informar")
        if dados:
            st.write(dados["conceito"])
        else:
            st.info("Este assunto ainda não está no catálogo. Consulte as fontes na última aba.")

    with compreender:
        st.markdown("### 2. Compreender")
        if dados:
            for autor in dados["autores"]:
                st.write("• " + autor)
        else:
            st.write("Compare diferentes autores e verifique como justificam suas ideias.")
        st.info("Compreender exige mais do que repetir uma informação: exige analisar seus argumentos.")

    with problematizar:
        st.markdown("### 3. Problematizar")
        perguntas = dados["questoes"] if dados else [
            "Quem produziu essa informação?",
            "Que evidências sustentam essa afirmação?",
            "Que outras interpretações são possíveis?"
        ]
        for pergunta in perguntas:
            st.write("❓ " + pergunta)
        reflexao = st.text_area("Escreva sua reflexão:", key="reflexao_aluno")
        if reflexao.strip():
            texto = "Tema: " + assunto + "\n\nReflexão:\n" + reflexao
            st.download_button("⬇️ Baixar reflexão", data=texto, file_name="reflexao_filosofica.txt", mime="text/plain")

    with fontes:
        st.markdown("### 4. Investigar as fontes")
        st.write("Acesse resultados externos e confira autoria, data e argumentos de cada publicação.")
        consulta = quote_plus(assunto)
        st.markdown("[Pesquisar no Google Acadêmico](https://scholar.google.com/scholar?q=" + consulta + ")")
        st.markdown("[Pesquisar na SciELO](https://search.scielo.org/?q=" + consulta + ")")
        st.markdown("[Portal de Periódicos CAPES](https://www.periodicos.capes.gov.br/)")
        st.caption("Os resultados externos não são avaliados automaticamente pelo aplicativo.")

st.divider()
st.header("📚 Biblioteca Filosófica")
pdfs = sorted(Path(__file__).resolve().parent.glob("*.pdf"))
if pdfs:
    for pdf in pdfs:
        with pdf.open("rb") as arquivo:
            st.download_button("📄 " + pdf.stem, data=arquivo.read(), file_name=pdf.name, mime="application/pdf", key=pdf.name)
else:
    st.info("Adicione arquivos PDF à pasta principal do repositório para aparecerem aqui.")

st.caption("Filosofia em Rede | Protótipo educacional | Pesquisa e pensamento crítico")
