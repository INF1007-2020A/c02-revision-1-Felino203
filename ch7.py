"""
Exemple des notions du chapitre 7.
"""


from chatbot import *
from twitch_bot import *


def build_say_hi_callback(bot, message):
	# TODO: Créer et retourner une fonction qui prend un paramètre (ignoré).
	#       Cette fonction envoie `message` dans le chat à l'aide de la méthode `send_privmsg` du paramètre `bot`.
	def callback(*args):
		bot.send_privmsg(message)
	return callback

def run_ch7_example():
	bot = TwitchBot("logs")
	callback = build_say_hi_callback(bot, "hi :)")
	bot.register_command("say_hi", callback)
	bot.connect_and_join("oauth:wnx097lzj4xqz2gueeokfni73dbdo8", "Felino203", "chosson")
	bot.run()


