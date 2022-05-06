from locust import HttpUser, task
from locust import events



class HelloWorldUser(HttpUser):
    def on_start(self):
        login_data = {
            "email": "stefan+1@hivebuy.de",
            "password": ""
        }

        response = self.client.get(url="api/auth/", data=login_data)
        self.cookie_jar = response.cookies

    @task
    def hello_world(self):
        user_url = "api/company/user/"
        self.client.get(url=user_url, cookies=self.cookie_jar)

        pur_url = "api/company/purchase-request/"
        self.client.get(url=pur_url, cookies=self.cookie_jar)
