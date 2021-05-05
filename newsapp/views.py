from django.shortcuts import render
from newsapi import NewsApiClient
from .models import *
from datetime import date
today = date.today()
date_today = today.strftime("%Y-%m-%d")
newsapi = NewsApiClient(api_key ='d6b5ab7f2c144ca1926003fcd0ef88ef')
# Create your views here. 
def entertainment(request):
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
        return render(request, 'entertain.html', context ={"mylist":mylist,"mylist2":mylist2})
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
        return render(request, 'entertain.html', context ={"mylist":mylist,"mylist2":mylist2})
def business(request):
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
        return render(request, 'business.html', context ={"mylist":mylist,"mylist2":mylist2})
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
        return render(request, 'business.html', context ={"mylist":mylist,"mylist2":mylist2})

def technology(request):
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
        return render(request, 'technology.html', context ={"mylist":mylist,"mylist2":mylist2})
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
        return render(request, 'technology.html', context ={"mylist":mylist,"mylist2":mylist2})

def general(request):
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
        return render(request, 'general.html', context ={"mylist":mylist,"mylist2":mylist2})
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
        return render(request, 'general.html', context ={"mylist":mylist,"mylist2":mylist2})

def sports(request):
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
        return render(request, 'sports.html', context ={"mylist":mylist,"mylist2":mylist2})
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
        return render(request, 'sports.html', context ={"mylist":mylist,"mylist2":mylist2})

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