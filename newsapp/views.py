from django.shortcuts import render
from newsapi import NewsApiClient
  
# Create your views here. 
def entertainment(request):
      
    newsapi = NewsApiClient(api_key ='d6b5ab7f2c144ca1926003fcd0ef88ef')
    top = newsapi.get_top_headlines(category='entertainment',country='in')
    top2 = newsapi.get_top_headlines(category='entertainment')
  
    l,l2 = top['articles'],top2['articles']
    desc,desc2 =[],[]
    news,news2=[],[]
    img ,img2=[],[]
    url,url2=[],[]
    date2=[]
    for i in range(10):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img,url)
    for i in range(len(l2)):
        f = l2[i]
        news2.append(f['title'])
        desc2.append(f['description'])
        img2.append(f['urlToImage'])
        url2.append(f['url'])
        date2.append(f['publishedAt'][0:10])
    mylist2 = zip(news2, desc2, img2,url2,date2)
  
    return render(request, 'entertain.html', context ={"mylist":mylist,"mylist2":mylist2})
def index2(request):
    newsapi = NewsApiClient(api_key ='60b2984d1d29423591799f1410245b84')
    top = newsapi.get_top_headlines(category="technology",language='en')
    top2 = newsapi.get_top_headlines(category="science",language='en')
    l = top['articles']+top2['articles']
    desc =[]
    news =[]
    img =[]
    lnk=[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        lnk.append(f["url"])

    mylist1 = zip(news, desc, img, lnk)

  
    return render(request, 'index2.html', context ={"mylist1":mylist1})