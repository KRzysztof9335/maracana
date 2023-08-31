"""This module contains all info to scrap data from flashscore.com
User should provide team name
For provided team


"""
from dataclasses import dataclass
import logging
from bs4 import BeautifulSoup
from typing import Dict, List, Any, Set
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import re
import time

from models import Incident, Summary, Match
from consts import SCRAP_LIMIT, TODAY

URL_FLASHSCORE = "https://www.flashscore.com"

@dataclass
class Fixture:
    "Describes FlashScore Fixture"
    id_flash: str
    date: str  # dd.mm.yy
    home: str
    away: str
    status: str = "Ongoing"


def sanitize_next_fixtures(fixtures: List[Any]) -> List[Fixture]:
    out: List[Fixture] = []
    prev_month = -1
    year_swap = False

    for idx, fixture in enumerate(fixtures):
        if idx >= SCRAP_LIMIT:
            break

        id_flash = fixture.attrs["id"].replace("g_1_", "")
        team_away = fixture.find("div", {"class": "event__participant event__participant--away"}).text
        team_home = fixture.find("div", {"class": "event__participant event__participant--home"}).text
        date = fixture.find("div", {"class": "event__time"}).text

        month_current = int(date.split('.')[1])
        if month_current >= prev_month:
            prev_month = month_current
        else:
            year_swap = True

        year = int(TODAY.strftime("%y"))
        if year_swap:
            year += 1

        date = re.sub(r"(\d+)\.(\d+).", rf"\1.\2.{year}", date)

        out.append(Fixture(id_flash, date, team_home, team_away))
    return out


def get_next_fixtures(driver: webdriver.Firefox, league: str) -> List[Fixture]:
    driver.get(f"{URL_FLASHSCORE}/football/{league}/fixtures/")  # Add protection if league does not exist
    soup = BeautifulSoup(driver.page_source, "html.parser")
    raw = soup.find_all("div", {"id": re.compile("g_1_.*")})
    return sanitize_next_fixtures(raw)


def wait_for_window(driver: webdriver.Firefox, vars: Dict[str, str], timeout: float = 2):
    time.sleep(round(timeout / 1000))
    wh_now = driver.window_handles
    wh_then = vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()

def scrap_country(country: str) -> None:
    "Scrap "




def scrap_match(source: str) -> Dict[str, Summary]:
    stats = Summary()
    soup = BeautifulSoup(source, "html.parser")
    divs: List[Any] = soup.find_all("div", {"class": "smv__participantRow"})

    for div in divs:
        minute = div.find("div", {"class": "smv__timeBox"}).text
        team = "away" if "smv__awayParticipant" in div.__repr__() else "home"  # Use Enum
        player = ""  # TODO: Later
        incident = Incident(player, minute)

        if "card-ico yellowCard-ico" in div.find('svg').__repr__():
            stats.cards_y.append(incident)
            continue

        if "card-ico redCard-ico" in div.find('svg').__repr__():
            stats.cards_r.append(incident)
            continue

        if div.find("div", {"class": re.compile("smv__incident(Home|Away)Score")}):
            stats.goals.append(incident)
            continue

        # Just ignore substitutions
        if div.find("div", {"class": re.compile("smv__incidentSubOut")}):
            continue

        else:
            logging.warning(f"Do not know how to handle div {div.find('div')}")


    return stats


def scrap_single_match(driver: webdriver.Firefox):
    driver.get("https://www.flashscore.pl/mecz/tfllZ3UL/#/szczegoly-meczu/szczegoly-meczu")
    # Use beautiful soap to scrap page content to get all events
    match_starts = Match("T1", "t2")

    scrap_match(driver.page_source)
    pass


SCRAPPED: Set[str] = set()

def scrape_team():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    vars = {}
    vars["window_handles"] = driver.window_handles
    vars["window_main"] = driver.window_handles[0]
    driver.get("https://www.flashscore.pl/")
    driver.find_element(By.CSS_SELECTOR, ".searchIcon").click()
    driver.find_element(By.CSS_SELECTOR, ".searchInput__input").click()
    driver.find_element(By.CSS_SELECTOR, ".searchInput__input").send_keys("Bayern Monachium")  # type: ignore
    driver.find_element(By.CSS_SELECTOR, ".searchResult:nth-child(1) > .searchResult__participantName").click()
    driver.find_element(By.ID, "li2").click()  # li2 -> results

    # driver.get("https://www.flashscore.pl/druzyna/bayern/nVp0wiqd/wyniki/")
    # wait for page to load
    matches = driver.find_elements(By.CSS_SELECTOR, "div[class^='event__match']")

    for event in matches:
        ActionChains(driver).move_to_element(event).click().perform()  # type: ignore
        vars[event.text] = wait_for_window(driver, vars, 1000)
        driver.switch_to.window(vars[event.text])  # type:ignore
        if not event.text in SCRAPPED:
        # do something with fixtures
            scrap_single_match()
        driver.quit()
        driver.switch_to.window(vars["window_main"])  # type:ignore

        driver.quit()



if __name__ == "__main__":
    scrap_single_match()


