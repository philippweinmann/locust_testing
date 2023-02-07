import os

from urls import HivebuyUrls


def login(client):
    login_data = {
        "email": os.environ.get("STEFAN_EMAIL"),
        "password": os.environ.get("STEFAN_PASSWORD")
    }

    # cookies are automatically saved and sent
    client.get(url=HivebuyUrls.AUTH_URL.value, data=login_data)
