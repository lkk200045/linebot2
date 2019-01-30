#SDK 載入LINE SDK
import requests

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    ImageSendMessage,LocationMessage,TemplateSendMessage, ButtonsTemplate, URITemplateAction,
    PostbackTemplateAction, MessageTemplateAction, CarouselTemplate, CarouselColumn, ConfirmTemplate
)

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
}

params ={
    # Query parameter
    'q': '我愛你',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}


app = Flask(__name__)

line_bot_api = LineBotApi('/sjBLgjHsNZhdsV+Xy9pXu7rPIrErYLvvbLfVOEYDyaiH3IEVROEnEYrMkPF+BuGCFjbTu3HSfTSUfVTJz6rLIWluhYeZp7v5FKZa94SF7pkcCPvY7El21pJuki1kpg5gl8QLxtGEfhtSutfmxdgUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba4bdf20d14b1338b998a01491aa691f')


headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
}

def luis(query):
    params['q'] = query
    if query == "我要找工作":
        a ='我要找工作'
        return a
    elif query == "台北" :
        a ='台北'
        return a
    elif query == "依選擇職務類型"  :
        a = '依選擇職務類型'
        return a
    elif query == "依地區選擇"  :
        a = '依地區選擇'
        return a
    elif query == "依工作性質選擇"  :
        a = '依工作性質選擇'
        return a
    elif query == "資訊軟體系統類"  :
        a = '資訊軟體系統類'
        return a
    elif query == "104人力銀行"  :
        a = '104人力銀行'
        return a
    else :
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
        result = r.json()
        a = result['topScoringIntent']['intent']
        return a    

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = luis(event.message.text)
    if a =='告白':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:告白 回應:我不愛妳'))
    elif a=='聊天':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:聊天 回應:我不想聊天'))
    elif a=='例外':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:例外 回應:我聽不懂耶'))
    elif a=='詢問':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:詢問 回應:歡迎光臨'))
    elif a=='誇獎':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:誇獎 回應:我會不好意思耶'))
    elif a=='問候':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:問候 回應:你好喔'))
    elif a == "我要找工作" :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='依選擇職務類型',
                        text='依選擇職務類型'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://static.104.com.tw/104main/jb/area/manjb/home/img/main/a6374579f23c233eb7e46fb4119c3a6d.jpg',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='依地區選擇',
                        text='依地區選擇'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://static.104.com.tw/104main/jb/area/manjb/home/img/main/4ee93b21011279ea8e005b6c32c6b0ca.jpg',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='依工作性質選擇',
                        text='依工作性質選擇'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif a=='依選擇職務類型' :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    URITemplateAction(
                        label='經營/人資類',
                        uri='https://www.104.com.tw/jobs/search/?cat=2001000000&jobsource=joblist_a_date&ro=0'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    URITemplateAction(
                        label='行銷/企劃/專案管理類',
                        uri='https://www.104.com.tw/jobs/search/?ro=0&jobcat=2004000000&order=2&asc=0&scstrict=0&scneg=1&page=1&mode=s&jobsource=joblist_a_date'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='資訊軟體系統類',
                        text='資訊軟體系統類'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='研發相關類',
                        text='研發相關類'
                    )
                ]
            ),
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='其他職類',
                        text='其他職類'
                    )
                ]
            ), 
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

    elif a=='依地區選擇' :
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                title='請選擇所在城市',
                text='歡迎光臨',
                actions=[
                MessageTemplateAction(
                    label='台北', text='台北'
                    ),
                MessageTemplateAction(
                    label='高雄', text='高雄'
                    ),
                MessageTemplateAction(
                    label='台南', text='台南'
                    ),
                MessageTemplateAction(
                    label='台中', text='台中'
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)

    elif a =='台北' :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='資訊軟體系統類',
                        text='資訊軟體系統類'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='研發相關類',
                        text='研發相關類'
                    )
                ]
            ),
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='104人力銀行',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='其他職類',
                        text='其他職類'
                    )
                ]
            ), 
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

    elif a =='資訊軟體系統類' :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='海悅廣告股份有限公司',
                    text='工作經歷:兩年以上，薪水面議',
                    actions=[
                    URITemplateAction(
                        label='數據分析師',
                        uri='https://www.104.com.tw/job/?jobno=6fehp&jobsource=joblist_a_date'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='耐能智慧股份有限公司',
                    text='工作經歷:五年以上，薪水面議',
                    actions=[
                    URITemplateAction(
                        label='Software Engineer',
                        uri='https://www.104.com.tw/job/?jobno=6eol2&jobsource=joblist_a_date'
                    )
                ]
            ),
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='一零四資訊科技股份有限公司',
                    text='工作經歷:不拘，薪水7萬以上',
                    actions=[
                    URITemplateAction(
                        label='Java 全端軟體工程師',
                        uri='https://www.104.com.tw/job/?jobno=6cds0&jobsource=joblist_a_date'
                    )
                ]
            ),  
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='更多工作',
                    text='自行參考',
                    actions=[
                    URITemplateAction(
                        label='更多工作',
                        uri='https://www.104.com.tw/jobs/search/?area=6001001000&cat=2007000000&jobsource=joblist_a_date&ro=0'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

    elif a =='104人力銀行' :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='一零四資訊科技股份有限公司',
                    text='工作經歷:五年以上，薪水面議',
                    actions=[
                    URITemplateAction(
                        label='投資專案經理',
                        uri='https://www.104.com.tw/job/?jobno=4py9s&jobsource=hotjob_chr'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='一零四資訊科技股份有限公司',
                    text='工作經歷:三年以上，薪水面議',
                    actions=[
                    URITemplateAction(
                        label='PHP 全端軟體工程師',
                        uri='https://www.104.com.tw/job/?jobno=63s4m&jobsource=hotjob_chr'
                    )
                ]
            ),
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='一零四資訊科技股份有限公司',
                    text='工作經歷:不拘，薪水7萬以上',
                    actions=[
                    URITemplateAction(
                        label='Java 全端軟體工程師',
                        uri='https://www.104.com.tw/job/?jobno=6cds0&jobsource=joblist_a_date'
                    )
                ]
            ),  
            CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='更多工作',
                    text='自行參考',
                    actions=[
                    URITemplateAction(
                        label='更多工作',
                        uri='https://www.104.com.tw/jobs/search/?keyword=104%E4%BA%BA%E5%8A%9B%E9%8A%80%E8%A1%8C&jobsource=2018indexpoc&ro=0&order=1'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

    else :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:不明 回應:可以請你換句話說嗎?'))
       
if __name__ == "__main__":
    app.run()