from flask import Flask, request
from fbmq import Page, Attachment, QuickReply, Buttons, Template
import apiai
import json
import quickreplies as qr
import news
app=Flask(__name__)

page=Page(page_access_token='EAAa7BshAslQBAAm0V8gZCA9dwlFjZC5bD5YYkhasmZBZC0nO2CMLV1K9aJY5r9VTFa6slwBQLGb1su8vhyoOLldsqKeYddHw7lP34fGJRHbWi0LXKotZCSKzP1djDp1FzR4X5oMmJk4iCYvIp60Ab5JVtMAIJGK1rScZAb4Caws78K2ueQdbEl')


def handle_allActions(sender,action,ai_reply):
    if action=='action.getNews':
        smart_object=qr.get_news_quick_reply()
        page.send(recipient_id=sender, message='Choose any one of these sources:',quick_replies=smart_object)
    elif action=='smalltalk.greetings.hello':
        quickreply_mini=[QuickReply('news',payload='news_hello')]
        message_ai=ai_reply['result']['fulfillment']['speech']
        page.send(recipient_id=sender,message=message_ai+'! Click on the button below, or you can simply text What is the news?',quick_replies=quickreply_mini)
    else:
        reply=ai_reply['result']['fulfillment']['speech']
        if reply is None or reply=="":
            reply="Okay"
        page.send(recipient_id=sender,message=reply)


def getAnswer(inputs):
    marvin=apiai.ApiAI(client_access_token='46139b1275564b1a8664f120e261fd17')
    req=marvin.text_request()
    req.lang='en'
    req.session_id='tom'
    req.query=inputs
    data_di=json.loads(req.getresponse().read().decode('utf-8'))
    if 'result' in data_di:
        return data_di

@app.route('/bot',methods=['POST'])
def handle_webhook():
    page.handle_webhook(request.get_data(as_text=True))
    return 'ok'

@page.handle_message
def message_handler(event):
    sender_id = event.sender_id
    messages = event.message_text
    if message_text!="" or message_text is not None:
        answer=getAnswer(messages) mo
    if 'action' in answer['result']:
        handle_allActions(sender=sender_id, action=answer['result']['action'],ai_reply=answer)
    else:
        reply=answer['result']['fulfillment']['speech']
        if reply is None or reply=="":
            reply='Okay'
        page.send(recipient_id=sender_id,message=reply)

@page.after_send
def after_send(payload,response):
    print('complete')

@app.route('/bot', methods=['GET'])
def handle_verification():
  print("Handling Verification.")
  if request.args.get('hub.verify_token', '') == 'Hello':
    print("Verification successful!")
    return request.args.get('hub.challenge', '')
  else:
    print("Verification failed!")
    return 'Error, wrong validation token'

def store(sender,flag=False):
    sender=sender
    if flag is True:
        return sender

@page.callback(qr.quickreplies)
def callback_picked_quickreply(payload,event):
    sender_id=event.sender_id
    if payload=='news_hello':
        smart_object=qr.get_news_quick_reply()
        page.send(recipient_id=sender_id, message='Choose any one of these sources:',quick_replies=smart_object)
    else:
        news_obj=news.get_news(payload)
        page.send(sender_id,Template.Generic(news_obj))
