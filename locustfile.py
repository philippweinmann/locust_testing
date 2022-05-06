from locust import HttpUser, task
import os

class HivebuyUser(HttpUser):
    localhost = 'http://127.0.0.1:8000/'
    host = localhost
    min_wait = 1000
    max_wait = 2000

    def on_start(self):
        login_data = {
            "email": os.environ.get("STEFAN_EMAIL"),
            "password": os.environ.get("STEFAN_PASSWORD")
        }

        response = self.client.get(url="api/auth/", data=login_data)
        self.cookie_jar = response.cookies

    @task
    def hello_world(self):
        user_url = "api/company/user/"
        self.client.get(url=user_url, cookies=self.cookie_jar)

        pur_url = "api/company/purchase-request/"
        self.client.get(url=pur_url, cookies=self.cookie_jar)
