from flask import Flask, request
from fbmq import Page, Attachment, QuickReply, Buttons
import apiai
import json
app=Flask(__name__)

page=Page(page_access_token='EAAa7BshAslQBAAm0V8gZCA9dwlFjZC5bD5YYkhasmZBZC0nO2CMLV1K9aJY5r9VTFa6slwBQLGb1su8vhyoOLldsqKeYddHw7lP34fGJRHbWi0LXKotZCSKzP1djDp1FzR4X5oMmJk4iCYvIp60Ab5JVtMAIJGK1rScZAb4Caws78K2ueQdbEl')

def getAnswer(inputs):
    marvin=apiai.ApiAI(client_access_token='46139b1275564b1a8664f120e261fd17')
    req=marvin.text_request()
    req.lang='en'
    req.session_id='tom'
    req.query=inputs
    return json.loads(req.getresponse().read().decode('utf-8'))

@app.route('/bot',methods=['POST'])
def handle_webhook():
    page.handle_webhook(request.get_data(as_text=True))
    return 'ok'

@page.handle_message
def message_handler(event):
    sender_id = event.sender_id
    messages = event.message_text
    print(messages)
    print('\t'+sender_id)
    answer=getAnswer(messages)
    my_reply=answer['result']['fulfillment']['speech']
    if my_reply is None or my_reply=="":
       my_reply="Sorry"
    page.send(recipient_id=sender_id,message=my_reply)


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

