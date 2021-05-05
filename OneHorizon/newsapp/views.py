from django.shortcuts import render, redirect

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def read_article(file_name):
    article = file_name.split(".")
    sentences = []

    for sentence in article:
        sen = sentence.strip()
        sentences.append(sen.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                sentences[idx1], sentences[idx2], stop_words
            )

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words("english")
    summarize_text = []

    sentences = read_article(file_name)

    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    print(sentence_similarity_martix)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank_numpy(sentence_similarity_graph)
    for i in sentence_similarity_graph.edges(data=True):
        print(i)
    ranked_sentence = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True
    )

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    return ". ".join(summarize_text), ranked_sentence


def index(request):
    name = request.user.get_username()
    return render(request, "index.html", {"name": name})


def business(request):
    return render(request, "business.html")


def travel(request):
    return render(request, "travel.html")


def natural(request):
    return render(request, "natural.html")


def summary(request):
    button = request.POST["b1"]
    sentence = request.POST["comment"]
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(sentence)
    negative = sentiment["neg"]
    neutral = sentiment["neu"]
    positive = sentiment["pos"]
    compound = sentiment["compound"]
    if compound >= 0.05:
        result = "The news article is positive"

    elif compound <= -0.05:
        result = "The news article is negative"

    else:
        result = "The news article is neutral"
    answer, ranked = generate_summary(sentence, 3)
    score = []
    sent = []
    for i in ranked:
        score.append(i[0])
        sent.append(" ".join(i[1]))
    rk = zip(score, sent)
    return render(
        request,
        "result.html",
        {
            "positive": positive,
            "neutral": neutral,
            "negative": negative,
            "compound": compound,
            "result": result,
            "summary": answer,
            "rank": rk,
        },
    )


from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form})

