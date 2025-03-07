# -*- coding: utf-8 -*-

import streamlit as st
from transformers import pipeline

def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

st.title("📝 Générateur de résumé automatique")
st.write("Collez un texte ci-dessous et obtenez un résumé généré par IA.")

input_text = st.text_area("📄 Texte à résumer", "Collez votre texte ici...")

if st.button("✨ Générer le résumé"):
    if input_text.strip():
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.subheader("📌 Résumé généré :")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("⚠️ Veuillez entrer un texte avant de générer un résumé.")

st.markdown("---")
st.markdown("🔗 **Projet open-source** - [byuser99x](https://github.com/ton-repo)")
