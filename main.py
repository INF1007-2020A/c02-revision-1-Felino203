"""
Fonction principale qui roule les exemples par chapitre.
"""


import sys
import os
import argparse
import configparser
import json
import random
from collections import namedtuple
from dataclasses import dataclass

from chatbot import *
from twitch_bot import *
from ch7 import *
from ch8 import *
from ch9 import *
from ch11 import *
from my_bot import MyBot


def main():
	bot = TwitchBot("logs")
	bot.connect_and_join("oauth:wnx097lzj4xqz2gueeokfni73dbdo8", "Felino203", "chosson")
	chapter_example = "ch11"

	if chapter_example == "ch7":
		run_ch7_example()
	elif chapter_example == "ch8":
		run_ch8_example("data/config.ini", "data/quotes.json")
	elif chapter_example == "ch9":
		run_ch9_example()
	elif chapter_example == "ch11":
		run_ch11_example()

if __name__ == "__main__":
	main()
