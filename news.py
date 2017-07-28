from newsapi.articles import Articles
from fbmq import Template


def get_news(sources):
    NEWS_API_KEY='1bae2e39f2b540f3a15dbbcb269eba9b'
    articles=Articles(API_KEY=NEWS_API_KEY)
    info=articles.get(source=sources)
    news_array=[]
    news_objects=[]
    for i in range(0,10):
        headline=info['articles'][i]['title']
        body=info['articles'][i]['description']
        url_web=info['articles'][i]['url']
        image=info['articles'][i]['urlToImage']
        time=info['articles'][i]['publishedAt']
        news_objects.append(Template.GenericElement(title=headline,subtitle=body,item_url=url_web,
        image_url=image,buttons=[Template.ButtonWeb(title='Open in web',url=url_web)]))
    return news_objects
