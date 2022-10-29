import requests
from random import randint

BASE_URL = "https://the-dune-api.herokuapp.com/"
RANDOM_QUOTES_URL = BASE_URL + "quotes/"
RANDOM_BOOKS_URL = BASE_URL + "books/"
QUERY_PARAMS = {id: randint(1, 1000)}
QUOTES_URL = BASE_URL + "quotes/id/"
BOOKS_URL = BASE_URL + "books/id/"

def get_random(url: str, params: dict = None):
    return requests.get(url,
                        params=params if params else None,
    ).json()

def get_url(url: str, id: str):
    url = f"{url}{id}"
    return requests.get(url,
    ).json()

print(get_random(RANDOM_BOOKS_URL, QUERY_PARAMS))
print(get_url(BOOKS_URL, "11"))