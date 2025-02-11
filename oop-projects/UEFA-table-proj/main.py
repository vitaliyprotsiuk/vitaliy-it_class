from scripts.game import Game
from scripts.interactive_cmd import IntCMD
from scripts.tournament import Tournament
from scripts.window import Window
from scripts.read_files import *
from tkinter import ttk

import tkinter

teams = read_teams()
games = read_games(teams)


# creating window
Window()

