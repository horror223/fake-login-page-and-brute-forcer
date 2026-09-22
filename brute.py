import page
from auth import verify_login


def brute_force():
    with open("passlist.txt", "r") as file:
        lines = file.readlines()

    username = None

    for line in lines:
        clean_line = line.strip()

        if clean_line.startswith("User:"):
            username = clean_line.removeprefix("User:").strip()

        elif clean_line.startswith("Pass:"):
            password = clean_line.removeprefix("Pass:").strip()

            print("Trying...")
            print("User:", username)
            print("Pass:", password)

            if verify_login(username, password):
                print()
                print("LOGIN FOUND")
                print("User:", username)
                print("Pass:", password)
                break

            else:
                print("Login failed")
                print()


brute_force()