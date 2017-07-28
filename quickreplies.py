from fbmq import QuickReply

quickreplies=['weather_hello','LOCATION','wiki','news_hello','bloomberg','cnn','business-insider','bbc-news','cnbc','hacker-news','techcrunch','talksport','google-news','national-geographic','the-times-of-india']

def get_news_quick_reply():
    return [QuickReply(title='bloomberg',payload='bloomberg'),QuickReply(title='cnn',payload='cnn'),
    QuickReply(title='business-insider',payload='business-insider'),QuickReply(title='bbc-news',payload='bbc-news'),
    QuickReply(title='cnbc',payload='cnbc'),QuickReply(title='hacker-news',payload='hacker-news'),
    QuickReply(title='techcrunch',payload='techcrunch'),QuickReply(title='talksport',payload='talksport'),
    QuickReply(title='google-news',payload='google-news'),
    QuickReply(title='the-times-of-india',payload='the-times-of-india')]
