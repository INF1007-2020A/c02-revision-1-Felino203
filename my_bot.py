"""
Un chatbot qui s'identifie et donnes des citations aléatoires.
"""

import random

from chatbot import *
from twitch_bot import *


class MyBot(TwitchBot):
	def __init__(self, logs_folder, quotes):
		super().__init__(logs_folder)
		self.quotes = quotes


	@TwitchBot.new_command
	def say_hi(self, cmd: Chatbot.Command):
		self.send_privmsg(f"The ''Yo momma'', {self.nickname}, joker himself!")




	# TODO: Ajouter une commande "say_hi" (à l'aide du décorateur TwitchBot.command) qui répond avec un message de la forme:
	#       "My name is <nom-du-bot>. You killed my father. Prepare to die.", où <nom-du-bot> est le nom du compte utilisé par le chatbot.
	#       Indice : Dans la méthode connect_and_join de TwitchBot, le nom (nickname) du bot est gardé comme attribut.
	# TODO: Ajouter une commande "quote" qui répond de trois façons selon ce qui suit le nom de la commande dans le message.
		# Si un nom de catégorie est donné (on trouve les paramètres de la commande dans cmd.params) :
			# Si la catégorie est connue, on envoie au hasard une citation venant de cette catégorie si elle est connue, sinon
			# Sinon, on envoie un message disant que la catégorie est inconnue (ex. "Unrecognized category 'la_catégorie'")
		# Si aucune catégorie n'est fournie, on choisit au hasard une catégorie puis une citation (comme dans l'exemple du chapitre 8)

	@TwitchBot.new_command
	def yo_momma(self, cmd: Chatbot.Command):
		category = cmd.params
		if category is not None:
			if category in self.quotes:
				self.send_privmsg(random.choice(self.quotes[category]))
			else:
				self.send_privmsg(f"Yo cé quoi ça... {category} ?!?!?")
		else:
			pass
