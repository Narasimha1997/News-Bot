from newsapi.articles import Articles


NEWS_API_KEY='1bae2e39f2b540f3a15dbbcb269eba9b'

def get_news(sources):
    articles=Articles(API_KEY=NEWS_API_KEY)
    info=articles.get(source=sources)
    news_array=[]
    for i in range(0,3):
        data={
        'headline':info['articles'][i]['title'],
        'body':info['articles'][i]['description'],
        'url':info['articles'][i]['url'],
        'image':info['articles'][i]['urlToImage'],
        'time':info['articles'][i]['publishedAt']
        }
        news_array.append(data)
    return news_array

def processNewsAndSend(sources):
    data=get_news(sources)
    
