from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from .models import *
from datetime import date
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
today = date.today()
date_today = today.strftime("%Y-%m-%d")
newsapi = NewsApiClient(api_key ='d6b5ab7f2c144ca1926003fcd0ef88ef')
# Create your views here. 
def entertainment(request):
    name=request.user.get_username()
    obj=entertain_news.objects.filter(Date_Published=str(date_today))
    if list(obj)==[] :
        top = newsapi.get_top_headlines(category='entertainment',country='in')
        top2 = newsapi.get_top_headlines(category='entertainment')
        l = top['articles']+top2['articles']
        desc,news,img,url,date =[],[],[],[],[]
        for i in range(len(l)):
            f = l[i]
            new1 = entertain_news(News_Name=f['title'], News_Info=f['description'],Destination_Image=f['urlToImage'],Date_Published=f['publishedAt'][0:10],News_Url=f['url'],News_Content=f['content'])
            new1.save()
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
            date.append(f['publishedAt'][0:10])
        mylist = zip(news[:10], desc[:10], img[:10],url[:10])
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'entertain.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
    else:
        obj=entertain_news.objects.filter(Date_Published=str(date_today)).values()
        desc,news,url,img,date =[],[],[],[],[]
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
        mylist = zip(news[:10], desc[:10], img[:10],url[:10])
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'entertain.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
def business(request):
    name=request.user.get_username()
    obj=business_news.objects.filter(Date_Published=str(date_today))
    if list(obj)==[] :
        top = newsapi.get_top_headlines(category='business',country='in')
        top2 = newsapi.get_top_headlines(category='business')
        l = top['articles']+top2['articles']
        desc,news,img,url,date =[],[],[],[],[]
        for i in range(len(l)):
            f = l[i]
            new1 = business_news(News_Name=f['title'], News_Info=f['description'],Destination_Image=f['urlToImage'],Date_Published=f['publishedAt'][0:10],News_Url=f['url'],News_Content=f['content'])
            new1.save()
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
            date.append(f['publishedAt'][0:10])
        mylist = zip(news[:10], desc[:10], img[:10],url[:10])
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'business.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
    else:
        obj=business_news.objects.filter(Date_Published=str(date_today)).values()
        desc,news,url,img,date =[],[],[],[],[]
        id1,num=[],0
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
            num+=1
            a="modelId"+str(num)
            id1.append(a)
        mylist = zip(news[:10], desc[:10], img[:10],url[:10],id1)
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'business.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})

def technology(request):
    name=request.user.get_username()
    obj=technology_news.objects.filter(Date_Published=str(date_today))
    x=5
    if list(obj)==[] :
        top = newsapi.get_top_headlines(category='technology',country='in')
        top2 = newsapi.get_top_headlines(category='technology')
        l = top['articles']+top2['articles']
        desc,news,img,url,date =[],[],[],[],[]
        id1=[]
        for i in range(len(l)):
            f = l[i]
            new1 = technology_news(News_Name=f['title'], News_Info=f['description'],Destination_Image=f['urlToImage'],Date_Published=f['publishedAt'][0:10],News_Url=f['url'],News_Content=f['content'])
            new1.save()
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
            date.append(f['publishedAt'][0:10])
            a="modelId"+str(i+1)
            id1.append(a)

        mylist = zip(news[x:], desc[x:], img[x:],url[x:],id1)
        slide=["slide1","slide2","slide3","slide4","slide5"]
        slide1=["s1","s2","s3","s4","s5"]
        mylist2 = zip(news[:x], desc[:x], img[:x],url[:x],slide,slide1)
        return render(request, 'technology.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
    else:
        obj=technology_news.objects.filter(Date_Published=str(date_today)).values()
        desc,news,url,img,date =[],[],[],[],[]
        id1,num=[],0
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
            num+=1
            a="modelId"+str(num)
            id1.append(a)
        mylist = zip(news[x:], desc[x:], img[x:],url[x:],id1)
        slide=["slide1","slide2","slide3","slide4","slide5"]
        slide1=["s1","s2","s3","s4","s5"]
        mylist2 = zip(news[:x], desc[:x], img[:x],url[:x],slide,slide1)
        return render(request, 'technology.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})

def general(request):
    name=request.user.get_username()
    obj=general_news.objects.filter(Date_Published=str(date_today))
    if list(obj)==[] :
        top = newsapi.get_top_headlines(category='general',country='in')
        top2 = newsapi.get_top_headlines(category='general')
        l = top['articles']+top2['articles']
        desc,news,img,url,date =[],[],[],[],[]
        for i in range(len(l)):
            f = l[i]
            new1 = general_news(News_Name=f['title'], News_Info=f['description'],Destination_Image=f['urlToImage'],Date_Published=f['publishedAt'][0:10],News_Url=f['url'],News_Content=f['content'])
            new1.save()
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
            date.append(f['publishedAt'][0:10])
        mylist = zip(news[:10], desc[:10], img[:10],url[:10])
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'general.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
    else:
        obj=general_news.objects.filter(Date_Published=str(date_today)).values()
        desc,news,url,img,date =[],[],[],[],[]
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
        mylist = zip(news[:10], desc[:10], img[:10],url[:10])
        mylist2 = zip(news[10:], desc[10:], img[10:],url[10:],date[10:])
        return render(request, 'general.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})

def sports(request):
    name=request.user.get_username()
    obj=sports_news.objects.filter(Date_Published=str(date_today))
    x=5
    if list(obj)==[] :
        top = newsapi.get_top_headlines(category='sports',country='in')
        top2 = newsapi.get_top_headlines(category='sports')
        l = top['articles']+top2['articles']
        desc,news,img,url,date =[],[],[],[],[]
        id1=[]
        for i in range(len(l)):
            f = l[i]
            new1 = sports_news(News_Name=f['title'], News_Info=f['description'],Destination_Image=f['urlToImage'],Date_Published=f['publishedAt'][0:10],News_Url=f['url'],News_Content=f['content'])
            new1.save()
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
            url.append(f['url'])
            date.append(f['publishedAt'][0:10])
            a="modelId"+str(i+1)
            id1.append(a)

        mylist = zip(news[x:], desc[x:], img[x:],url[x:],id1)
        slide=["slide1","slide2","slide3","slide4","slide5"]
        slide1=["s1","s2","s3","s4","s5"]
        mylist2 = zip(news[:x], desc[:x], img[:x],url[:x],slide,slide1)
        return render(request, 'sports.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})
    else:
        obj=sports_news.objects.filter(Date_Published=str(date_today)).values()
        desc,news,url,img,date =[],[],[],[],[]
        id1,num=[],0
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
            num+=1
            a="modelId"+str(num)
            id1.append(a)
        mylist = zip(news[x:], desc[x:], img[x:],url[x:],id1)
        slide=["slide1","slide2","slide3","slide4","slide5"]
        slide1=["s1","s2","s3","s4","s5"]
        mylist2 = zip(news[:x], desc[:x], img[:x],url[:x],slide,slide1)
        return render(request, 'sports.html', context ={"mylist":mylist,"mylist2":mylist2,"name":name})

def date_fetch(request):
    if request.method == 'POST':
        x=10
        date_today=request.POST["date"]
        if request.POST["action"]=="Technology":
            obj=technology_news.objects.filter(Date_Published=str(date_today)).values()
            pg="technology.html"
            x=5
        elif request.POST["action"]=="sports":
            obj=sports_news.objects.filter(Date_Published=str(date_today)).values()
            pg="sports.html"
        elif request.POST["action"]=="general":
            obj=general_news.objects.filter(Date_Published=str(date_today)).values()
            pg="general.html"
        elif request.POST["action"]=="business":
            obj=business_news.objects.filter(Date_Published=str(date_today)).values()
            pg="business.html"
        else:
            obj=entertain_news.objects.filter(Date_Published=str(date_today)).values()
            pg='entertain.html'

        desc,news,url,img,date =[],[],[],[],[]
        id1,num=[],0
        for i in list(obj):
            news.append(i['News_Name'])
            desc.append(i['News_Info'])
            img.append(i['Destination_Image'])
            url.append(i['News_Url'])
            date.append(i['Date_Published'])
            num+=1
            a="modelId"+str(num)
            id1.append(a)
        if request.POST["action"]=="Technology" or request.POST["action"]=="business" or request.POST["action"]=="sports" :
            mylist = zip(news[x:], desc[x:], img[x:],url[x:],id1)
            slide=["slide1","slide2","slide3","slide4","slide5"]
            slide1=["s1","s2","s3","s4","s5"]
            mylist2 = zip(news[:x], desc[:x], img[:x],url[:x],slide,slide1)
        else:
            mylist = zip(news[:x], desc[:x], img[:x],url[:x])
            mylist2 = zip(news[x:], desc[x:], img[x:],url[x:],date[x:])
        return render(request, pg, context ={"mylist":mylist,"mylist2":mylist2})


def read_article(file_name):
    article = file_name.split(".")
    sentences = []

    for sentence in article:
        sen = sentence.strip()
        sentences.append(sen.replace("[^a-zA-Z]", " ").split(" "))
        print(sentences[len(sentences) - 1])
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

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                sentences[idx1], sentences[idx2], stop_words
            )

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words("english")
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences = read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank_numpy(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True
    )

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    return ". ".join(summarize_text),ranked_sentence
def index2(request):
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
    answer, ranked = generate_summary(sentence)
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
        return redirect(general)
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form})

def index(request):
    return render(request,'index3.html')
