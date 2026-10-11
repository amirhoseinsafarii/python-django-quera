import requests


def add_book(book: dict[str, str]) -> str | None:

    match book["category"]:
        case "mathematics":
            url = "http://127.0.0.1:8000/mathematics/"
        case "physics":
            url = "http://127.0.0.1:8000/physics/"
        case "chess":
            url = "http://127.0.0.1:8000/chess/"
        case _:
            return "Invalid Category"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for item in data:
            if item["name"] == book["name"]:
                return "Bad Request"

        response = requests.post(url, json=book)

    except requests.RequestException:
        return "Bad Request"
