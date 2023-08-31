"""
This is a main entry file responsible for handling user input and producing output
User should provide input in the following way:
1) Provide two teams for which forecasting will be performed (ongoing)
2) Provide a day and for all matches forecasting will be performed (future)
"""
from typing import Dict, List, Any, Set
from selenium import webdriver

import logging

import consts
import scrapers.flash




def process_league(web_driver: webdriver.Firefox, league: str):
    logging.info(f"Processing league {league}")
    # Read DB and update already scrapped matches with status ONGOING
    next_fixtures = scrapers.flash.get_next_fixtures(web_driver, league)
    # Get next matches
    #
    pass


def get_web_driver() -> webdriver.Firefox:
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    return driver


def main():
    "Main function to control"
    web_driver = get_web_driver()
    for league in consts.LEAGUES:
        process_league(web_driver, league)



if __name__ == "__main__":
    main()
