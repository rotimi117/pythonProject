def generate_username(email_list):
    if "@" in email_list:
        email = email_list.split("@")[0]
        return email
    else:
        return None

email = generate_username("rotiminicol117@gmail.com")
print(email)


def username_generator(email: str):
    username = email.split("@")[0]
    return f"your username is {username}"




