import re


def validate_email(email: str) -> bool:
    pattern = r'^[A-Za-z0-9_.]+@[A-Za-z0-9]+\.[A-Za-z]{3}$'
    return bool(re.fullmatch(pattern, email))
    
    

def validate_phone(number: str) -> bool:
    pattern = r'^(09\d{9}|\+989\d{9}|00989\d{9})$'
    return bool(re.fullmatch(pattern, number))
