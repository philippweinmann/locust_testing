from locust import HttpUser, task, tag, between
from urls import HivebuyUrls, ConnectionUrls
import os


class HivebuyUser(HttpUser):
    host = ConnectionUrls.LOCALHOST.value
    min_wait = 1000
    max_wait = 2000

    # limit number of requests by adding a wait time.
    wait_time = between(0.5, 1)

    def on_start(self):
        login_data = {
            "email": os.environ.get("STEFAN_EMAIL", "stefan+1@hivebuy.de"),
            "password": os.environ.get("STEFAN_PASSWORD", "Change-Me1!")
        }

        # cookies are automatically saved and sent
        response = self.client.get(url=HivebuyUrls.AUTH_URL.value, data=login_data)

        # don't continue if the authentification failed
        response.raise_for_status()

    @tag('get_all_users')
    @task
    def get_users(self):
        # get users
        self.client.get(url=HivebuyUrls.USER_URL.value)

    @tag('get_all_pur')
    @task
    def get_purchase_requests(self):
        # get purchase requests
        self.client.get(url=HivebuyUrls.PUR_URL.value)


