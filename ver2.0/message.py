from linebot.models import (
    TemplateSendMessage, ButtonsTemplate, PostbackAction, TextSendMessage,StickerSendMessage
)
from video import pornhub, xvideos, spankbang

def select_video_sites():
    message = TemplateSendMessage(
        alt_text="P-Bot",
        template=ButtonsTemplate(
            title="動画サイトを選んでね",
            text="動画の送信までに少々時間がかかります",            
            image_size="cover",
            actions=[
                PostbackAction(
                label='PornHub',
                text='PornHub',
                data='pornhub'
                ),
                PostbackAction(
                label='XVIDEOS',
                text='XVIDEOS',
                data='xvideos'
                ),
                PostbackAction(
                label='SpankBang',
                text='SpankBang',
                data='spankbang'
                )
            ]
        )
    )

    return message

def select_pornhub():
    ja_title, native_title, url = pornhub()
    message = TextSendMessage(
        text=f'『{ja_title}』\r\n\r\n({native_title})\r\n\r\n{url}' 
    )
    return message

def select_xvideos():
    ja_title, native_title, url = xvideos()
    message = TextSendMessage(
        text=f'『{ja_title}』\r\n\r\n({native_title})\r\n\r\n{url}'
    )
    return message

def select_xhamster():
    ja_title, native_title, url = spankbang()
    message = TextSendMessage(
        text=f'『{ja_title}』\r\n\r\n({native_title})\r\n\r\n{url}'
    )
    return message

def follow_message():
    message = TextSendMessage(
        text='P-Botを追加してくれてありがとう!!\r\n\r\n P-Botはいつでもあなたにおすすめの動画を配信します。\r\n\r\n好きな動画サイトを選ぶだけで動画が配信されます。(配信には数秒ほどかかります)'
    )
    stump = StickerSendMessage(
        package_id='446',
        sticker_id='16581248'
    )
    return message, stump