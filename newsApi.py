import requests
import datetime
def topHeadlines():
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=7ff7efe46da54d49b0bfb94f76891b07')
    response = requests.get(url)
    topHeadlinesOfDay = response.json()
    return topHeadlinesOfDay

def categoryNews(category):
    currentDate =  str(datetime.datetime.now().date())
    url = ('http://newsapi.org/v2/everything?q='+category+'&from='+currentDate+'&sortBy=publishedAt&apiKey=7ff7efe46da54d49b0bfb94f76891b07')
    response = requests.get(url)
    categoryNewsArticles = response.json()
    return categoryNewsArticles



