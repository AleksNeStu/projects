import json

import settings
from client import AllegroClient


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# Chrome
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
# driver = webdriver.Chrome(options=chrome_options)


# Example
def get_orders():
    allegro = AllegroClient(
        client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET,
        sandbox=False)
    # e.g. use refresh auth tokens from auth_resp
    auth_resp = allegro.sign_in()
    # https://developer.allegro.pl/tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR
    target_path = "/order/carriers"
    # target_path = "/order/events"
    res = allegro._get(target_path)
    return json.dumps(res)

if __name__ == "__main__":
    orders = json.dumps(get_orders())
    print(orders)