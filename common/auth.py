import os

from urls import HivebuyUrls


def login(client):
    login_data = {
        "email": os.environ.get("STEFAN_EMAIL", "stefan+1@hivebuy.de"),
        "password": os.environ.get("STEFAN_PASSWORD", "Change-Me1!")
    }

    # cookies are automatically saved and sent
    response = client.get(url=HivebuyUrls.AUTH_URL.value, data=login_data)

    # don't continue if the authentification failed
    response.raise_for_status()
