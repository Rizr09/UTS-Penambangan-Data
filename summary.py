import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("Klustering Cuitan Whoosh beserta Sentimen Analisisnya 🚅")

st.write("Kami mengumpulkan cuitan mengenai Kereta Cepat Indonesia China dalam 1 bulan terakhir (25 September 2023 - 24 Oktober 2023), yakni sebanyak 6864 cuitan. Berikut adalah contoh-contoh cuitan mengenai Whoosh beserta wordcloud dari cuitan-cuitan yang telah kami ambil.")

df = pd.read_csv('New Data/whoosh finale.csv')
df.sample(5, random_state=101)
# show the sample
st.write(df[['created_at', 'full_text', 'sanitized_tweet', 'sentiment']].sample(5))

# tampilkan image img/overall_wc.png

st.image("img/overall_wc.png")
# beri keterangan gambar dengan font center
st.markdown("<center>Wordcloud dari seluruh cuitan yang kami ambil</center>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("Pembersihan data yang kami lakukan adalah sebagai berikut:")
st.write("1. Mengkonversi semua huruf menjadi huruf kecil")
st.write("2. Menghapus semua tanda baca")
st.write("3. Stemming kalimat menggunakan Sastrawi")
st.write("4. Menghapus semua kata yang tidak bermakna (stopwords)")
st.write("5. Menghapus semua kata yang dimulai dengan http, t.co, dan amp")
st.write("6. Format manual untuk beberapa kata yang menyatu seperti jakartabandung menjadi jakarta bandung")