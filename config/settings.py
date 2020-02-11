import os

# Build paths inside the project like this"":"" os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# API definition

APIS = {
    "account": {
        "login":"/login/mail?back_url=https%3A%2F%2Fke.youdao.com%2F%3FloginBack%3Dtrue",
        "rename":"/user/account/"
    }
}
