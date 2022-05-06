from locust import HttpUser, task, tag
from urls import HivebuyUrls, ConnectionUrls
import os


class HivebuyUser(HttpUser):
    host = ConnectionUrls.LOCALHOST.value

    def on_start(self):
        login_data = {
            "email": os.environ.get("STEFAN_EMAIL"),
            "password": os.environ.get("STEFAN_PASSWORD")
        }

        # cookies are automatically saved and sent
        self.client.get(url=HivebuyUrls.AUTH_URL.value, data=login_data)

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


