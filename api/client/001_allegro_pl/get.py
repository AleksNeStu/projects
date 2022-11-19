import json

import settings
from client import AllegroClient


# Example
def get_orders():
    allegro = AllegroClient(
        client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET,
        sandbox=False)
    # e.g. use refresh auth tokens from auth_resp
    auth_resp = allegro.sign_in()
    # https://developer.allegro.pl/tutorials/jak-obslugiwac-zamowienia-GRaj0qyvwtR
    orders = allegro._get('/order/events')
    return json.dumps(orders)

print(json.dumps(get_orders()))