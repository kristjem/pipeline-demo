import random
import datetime as dt
import requests
from setup import URL

animal_list = ["dog", "cat", "bird", "fish", "rabbit", "lizard", "frog"]

def get_random_word_from_list(word_list) -> str:
    """Returns a random word from  given list"""
    number_of_words = len(word_list)
    random_index = random.randint(0, number_of_words - 1)
    return word_list[random_index]


def post_to_webhook_site(url=URL) -> bool:
    """
    Takes a temporary URL from https://webhook.site/ and sends a POST request to it\n
    Define the URL in the setup.py file
    """
    word = get_random_word_from_list(animal_list)
    response = requests.post(url, json={"word": word, "timestamp": dt.datetime.now().isoformat()}, timeout=5)
    if response.status_code == 200:
        return True
    return False

if __name__ == "__main__":
    print(f"Hello from {__name__}")
    post_to_webhook_site()
    print(f"Please check the URL:\n{URL}")
    print("It should have received a POST request with a random word and timestamp")
    print(f"{__name__}is done executing")

