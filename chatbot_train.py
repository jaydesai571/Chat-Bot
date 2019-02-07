from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os


bot = ChatBot('Bot')
# bot.(ListTrainer)

trainer = ListTrainer(bot)

for files in os.listdir('C:/Users/jaydesai571/Desktop/jay/Devepolment/Chat bot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data = open('C:/Users/jaydesai571/Desktop/jay/Devepolment/Chat bot/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
	trainer.train(data)

while True:
	message = input('You:')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot :', reply)	
	if message.strip() == 'Bye':
		print('ChatBot : Bye')
		break