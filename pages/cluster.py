import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import ast

def show_wordcloud():
    st.subheader("Wordcloud of the tweets")
    # create a slider
    df = pd.read_csv('New Data/whoosh finale.csv')
    cluster = st.slider('Select a cluster', 3, 10)

    # show the wordcloud based on the value of the slide bar, automatically update
    wc = WordCloud(
        width=800,
        height=400,
        max_words=200,
        background_color='black',  # set background color to black
        colormap='twilight',  # use the twilight color map
        contour_width=3,  # add a contour around the wordcloud
        contour_color='steelblue',  # set the contour color
        random_state=42  # set a fixed random state for reproducibility
    )

    # generate the wordcloud
    n = "cluster_" + str(cluster)

    for i in range(0, cluster):

        st.subheader("Cluster " + str(i))
        cluster_tweets = df.loc[df[n] == i]['sanitized_tweet']
        tweet_list = []
        for tweet in cluster_tweets:
            try:
                tweet_list.extend(ast.literal_eval(tweet))
            except ValueError:
                pass
        wc.generate(' '.join(tweet_list))
        fig, ax = plt.subplots()
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        print("\n")
        # get the top 5 dominant words for the cluster
        words = ' '.join(tweet_list).split()
        word_count = Counter(words)
        top_words = word_count.most_common(5)
        st.write("Top 5 dominant words for Cluster " + str(i) + ":")
        data = {"Words": [], "Time of Appearance": []}
        for word, count in top_words:
            data["Words"].append(word)
            data["Time of Appearance"].append(count)
        st.table(data)


df = pd.read_csv('New Data/whoosh finale.csv')
st.title("Demo Klustering Cuitan Whoosh 🐦")
show_wordcloud()