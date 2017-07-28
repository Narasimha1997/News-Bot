from fbmq import QuickReply

quickreplies=['bloomberg','cnn','business-insider','bbc-news','cnbc','hacker-news']

def get_news_quick_reply():
    return [QuickReply(title='bloomberg',payload='bloomberg'),QuickReply(title='cnn',payload='cnn'),
    QuickReply(title='business-insider',payload='business-insider'),QuickReply(title='bbc-news',payload='bbc-news'),
    QuickReply(title='cnbc',payload='cnbc'),QuickReply(title='hacker-news',payload='hacker-news')]
