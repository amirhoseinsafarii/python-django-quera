all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    all_users[username] = {
        "age": age,
        "city": city,
        "albums": albums,
    }


def add_album(
    name: str, artist: str, genre: str, tracks: int, all_albums: dict
) -> None:
    all_albums[name] = {
        "artist": artist,
        "genre": genre,
        "tracks": tracks,
    }


def query_user_artist(
    username: str, artist: str, all_users: dict, all_albums: dict
) -> int:

    tracks = 0
    for key, value in all_users.items():
        if key == username:
            for k, v in all_albums.items():
                if v["artist"] == artist:
                    if k in value["albums"]:
                        tracks = tracks + v["tracks"]
    return print(tracks)


def query_user_genre(
    username: str, genre: str, all_users: dict, all_albums: dict
) -> int:
    pass


def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    pass


add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)
add_album("eclipse", "malmsteen", "classic", 10, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
add_album("bidad", "shajarian", "classic", 10, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_albums)
query_user_artist("SAliB", "sorena", all_users, all_albums)

query_user_artist("SAliB", "beeptunes", all_users, all_albums)
