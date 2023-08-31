"""This module contains constants that will be shared between modules"""
import datetime

DB = "test.db"

# COUNTRIES_LEAGUES = {
#     'England': 'Premier League',
#     'Spain': 'LaLiga',
#     'Italy': 'Serie A',
#     'Germany': 'Bundesliga',
#     'France':'Ligue 1',
#     'Portugal': 'Primeira Liga'}

COUNTRIES_LEAGUES = {'Germany': 'Bundesliga'}

LEAGUES = ["germany/bundesliga"]

SCRAP_LIMIT = 10  # No more matches to be scrapped at one session per league
TODAY = datetime.date.today()
# https://www.flashscore.com/football/germany/bundesliga/fixtures/
# https://www.flashscore.com/football/france/ligue-1/#/Q1sSPOn5/table/overall