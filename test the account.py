import telepot

bot = telepot.Bot('337709071:AAFzJ37j0xGsgDHh5enploqAmKayxZkSrF4')
print(bot.getMe())
bot.setWebhook(('https://bot.khashtamov.com/planet/bot/{bot_token}/'.format(bot_token=bot_token)))

