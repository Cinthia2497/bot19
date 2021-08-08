import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('1941862638:AAF29urXiEblvYv61UkZmMEnykzje_4FzjA') 
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['hola']) 
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id,  "HOLA, Envia metros para ver formula Metros a Centímetros \n Envia o Kilómetros para ver formula Kilómetros a Metros \n Envia millas para ver formula Millas a Kilómetros \n Envia pie para ver formula Pie a Pulgadas \n ")
    print("Mandaron formula")

@bot.message_handler(commands=["metros","metro"]) 
def Metros(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 metro es 100 centímetros (1m = 100cm)")
    print("Mandaron metro , metros")

@bot.message_handler(commands=["kilometros"])
def Kilómetros(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 kilómetro es 1000 metros (1km = 1000m)")
    print("Mandaron kilometros")

@bot.message_handler(commands=["millas"])
def Millas(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 milla es 1.609 kilometros")
    print("Mandaron millas")

@bot.message_handler(commands=["pie"])
def Pie(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 pie es 12.00 pulgada")
    print("Mandaron pie")

bot.polling()