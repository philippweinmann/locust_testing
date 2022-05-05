from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        login_data = {
            "email": "stefan+1@hivebuy.de",
            "password": "Change-Me1!"
        }

        response = self.client.get(url="/api/auth/", data=login_data)


if __name__ == '__main__':
    HelloWorldUser().run()
