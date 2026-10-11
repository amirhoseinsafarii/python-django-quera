import requests


def find_category(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Bad Request"

        data = response.json()
        if not data:
            return "I can't recognize it"

        categories = {d["category"] for d in data}
        if len(categories) != 1:
            return "I can't recognize it"
        else:
            return categories.pop()

    except:
        return "Bad Request"
