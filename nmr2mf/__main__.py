"""Main application entry point."""

import os

import chromedriver_binary  # noqa
from selenium import webdriver

from .utils import get_stake

if __name__ == "__main__":
    options = webdriver.chrome.options.Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/93.0.4577.63 "
        "Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    driver.get(
        "https://moneyforward.com/accounts/show_manual/"
        f"{os.environ['MONEYFORWARD_WALLET_ID']}"
    )

    e = driver.find_element_by_link_text("メールアドレスでログイン")

    e.click()

    e = driver.find_element_by_xpath("//input[@type='email']")

    e.clear()
    e.send_keys(os.environ["MONEYFORWARD_EMAIL"])

    e = driver.find_element_by_xpath("//input[@type='submit']")

    e.click()

    e = driver.find_element_by_xpath("//input[@type='password']")

    e.clear()
    e.send_keys(os.environ["MONEYFORWARD_PASSWORD"])

    e = driver.find_element_by_xpath("//input[@type='submit']")

    e.click()

    e = driver.find_element_by_link_text("残高修正")

    e.click()

    driver.implicitly_wait(10)

    e = driver.find_element_by_xpath("//input[@id='rollover_info_value']")

    stake = get_stake()

    e.clear()
    e.send_keys(int(stake))

    e = driver.find_element_by_xpath("//form[@id='rollover_form']/div[5]/div/input")

    e.click()

    driver.implicitly_wait(10)

    driver.quit()
