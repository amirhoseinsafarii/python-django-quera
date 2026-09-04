def check_registration_rules(**kwargs: str) -> list[str]:
    correct_userpass = []
    for key, value in kwargs.items():
        if value.__len__() >= 6 and not value.isdigit() and key != "quera" and key != "codecup" and key.__len__() >= 4 :
            correct_userpass.append(key) 
    return correct_userpass
