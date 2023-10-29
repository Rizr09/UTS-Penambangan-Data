import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('New Data/whoosh finale.csv')

st.title("Sentimen Analisis Cuitan Whoosh Menggunakan InSet Lexicon 👿")

sentiment_counts = df['sentiment'].value_counts()
sentiment_df = pd.DataFrame({'sentiment': sentiment_counts.index, 'count': sentiment_counts.values})
# sentiment_df.set_index('sentiment', inplace=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("Data-data di atas telah kami skoring sentimen analisisnya menggunakan teknik lexico-based approach. Dataset word dan weight yang kami gunakan berasal dari Indonesia Sentiment (InSet) Lexicon. Berikut adalah hasil yang kami peroleh:")
# tampilkan dataframe sentiment_df dengan font center
st.markdown("<br><center>" + sentiment_df.to_html() + "</center><br>", unsafe_allow_html=True)

# tampilkan image img/distribution.png
st.image("img/distribution.png")

st.markdown("<br>", unsafe_allow_html=True)