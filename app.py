# ============================================
# JARVIS – IA da banda Memórias Idôneas
# Versão consultiva / híbrida
# Desenvolvido para Streamlit Cloud
# ============================================

import streamlit as st
import pandas as pd
import os

# ---------- CONFIGURAÇÃO INICIAL ----------
st.set_page_config(page_title="Jarvis – IA da banda Memórias Idôneas", layout="wide")

st.title("🎧 Jarvis – IA da banda Memórias Idôneas")
st.write("Assistente de marketing e criação de conteúdo poético-reflexivo da banda.")

# ---------- MENU LATERAL ----------
menu = st.sidebar.radio("Navegação", ["Dashboard", "Ideias Hipnóticas", "Gerador de Legendas", "Tendências", "Treinar Jarvis"])

# ---------- BASE DE DADOS LOCAL ----------
DATA_PATH = "contexto_banda.csv"

if not os.path.exists(DATA_PATH):
    pd.DataFrame(columns=["tipo", "titulo", "conteudo"]).to_csv(DATA_PATH, index=False)

# Função auxiliar para carregar e salvar contexto
def load_context():
    return pd.read_csv(DATA_PATH)

def add_context(tipo, titulo, conteudo):
    df = load_context()
    novo = pd.DataFrame([[tipo, titulo, conteudo]], columns=["tipo", "titulo", "conteudo"])
    df = pd.concat([df, novo], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

# ---------- ABA: DASHBOARD ----------
if menu == "Dashboard":
    st.header("📊 Análise geral de desempenho (modo demonstrativo)")
    st.write("Integração com Instagram e TikTok será ativada assim que as chaves de API forem configuradas.")
    st.metric("Reels analisados", 42)
    st.metric("Taxa média de engajamento", "6.8%")
    st.metric("Tendência da semana", "Histórias com emoção real")
    st.info("Jarvis está pronto para analisar dados reais assim que as chaves forem adicionadas.")

# ---------- ABA: IDEIAS HIPNÓTICAS ----------
elif menu == "Ideias Hipnóticas":
    st.header("💡 Ideias Hipnóticas")
    st.write("Sugestões automáticas baseadas nas letras e tendências.")

    st.subheader("Sugestões iniciais:")
    ideias = [
        "🎥 'O dia em que o silêncio falou mais alto' — comece com 3s de olhar fixo, depois insira o refrão.",
        "🎸 'Se você já pensou em desistir, ouve isso' — voz crua e luz baixa, sem efeitos.",
        "🕯️ 'Nem todo grito é alto' — use um take de ensaio real, com áudio ambiente.",
        "🌌 'Essa parte quase não saiu… mas era a mais verdadeira' — storytelling de bastidor.",
    ]
    for ideia in ideias:
        st.write(f"- {ideia}")

    st.success("Jarvis pode gerar novas ideias automaticamente quando conectado às métricas da banda.")

# ---------- ABA: GERADOR DE LEGENDAS ----------
elif menu == "Gerador de Legendas":
    st.header("📝 Gerador de Legendas Poéticas")
    entrada = st.text_area("Descreva o clima ou tema do vídeo (ex: recomeço, perda, fé):")
    if st.button("Gerar legenda"):
        if entrada.strip() == "":
            st.warning("Digite um tema antes de gerar.")
        else:
            legenda = f"Entre o som e o silêncio, {entrada.lower()} encontra voz. 🎶\nSalva pra ouvir quando isso bater de novo."
            st.text_area("Legenda sugerida:", legenda, height=100)

# ---------- ABA: TENDÊNCIAS ----------
elif menu == "Tendências":
    st.header("📈 Tendências e sons em alta (modo demonstrativo)")
    st.write("Integração com TikTok e Instagram será habilitada com as chaves de API.")
    st.markdown("""
    **Top sons do momento (exemplo):**
    - 🎵 'Emotional Guitar Reverb' — usado em vídeos introspectivos.
    - 🎵 'Soft Rock Outro' — tendência para reels de performance ao vivo.
    - 🎵 'Indie Fade-In' — ideal para bastidores e ensaios.
    """)

# ---------- ABA: TREINAR JARVIS ----------
elif menu == "Treinar Jarvis":
    st.header("📚 Treinar Jarvis com letras e referências")
    st.write("Envie letras, referências ou descrições que Jarvis deve conhecer.")

    tipo = st.selectbox("Tipo de conteúdo", ["Letra", "Referência", "Nota"])
    titulo = st.text_input("Título")
    conteudo = st.text_area("Conteúdo (ou cole a letra completa)")

    if st.button("Adicionar ao contexto"):
        if titulo and conteudo:
            add_context(tipo, titulo, conteudo)
            st.success(f"{tipo} '{titulo}' adicionada com sucesso!")
        else:
            st.warning("Preencha o título e o conteúdo antes de salvar.")

    st.subheader("🗂️ Contexto armazenado")
    st.dataframe(load_context())

# ---------- CONTEÚDO INICIAL PADRÃO ----------
# Adiciona letras-base se ainda não existirem
contexto = load_context()
if contexto.empty:
    letras_iniciais = [
        ("Letra", "O Que Posso Fazer", "Navegando, vou calando os erros. Confiando que tuas mãos têm o poder pra me curar."),
        ("Letra", "Suspenso", "É largando, e desatando os julgos. Que sua graça me faz livre para andar."),
        ("Letra", "Movediça", "Entre a fé e o medo, o chão se abre. Mas há um canto que me sustenta."),
    ]
    for l in letras_iniciais:
        add_context(*l)
    st.info("Letras iniciais adicionadas ao contexto.")
