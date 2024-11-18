import requests,bs4,telebot,os
token="5130510284:AAHzgfEhVj0Rjx4KL0TD6uIqpEjar52GZrU"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(messag):
    bot.send_message(messag.chat.id,str("Welcome {} \n send pinterest photo url to download\n copyright: @Kaero7").format(messag.chat.first_name))
@bot.message_handler(func=lambda m:True)
def go(message):
    try:
        req=requests.get(message.text)
        soup=bs4.BeautifulSoup(req.text,"html.parser")
        #searche all meta in url
        find=soup.find_all("meta")
        #try to get the photo url
        image=str(find).split(".jpg")[0]+".jpg"
        #now clean
        url=str(image).split('<meta content="')
        #the url ready
        image_url=url[len(url)-1]
        #request to the photo url
        req_image=requests.get(image_url)
        #save the photo 
        with open("image.jpg","wb") as ph:
            ph.write(req_image.content)
        #send photo te telegram
        with open("image.jpg","rb") as rbl:
            bot.send_photo(message.chat.id,rbl)
        os.remove("image.jpg")
    except:
        bot.send_message(message.chat.id,"Broken Url🔗")
bot.delete_webhook()
bot.polling()
