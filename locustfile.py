from locust import HttpUser, task, tag, between

from common import auth
from urls import HivebuyUrls, ConnectionUrls, DashboardUrls


class HivebuyUser(HttpUser):
    host = ConnectionUrls.LOCALHOST.value
    min_wait = 1000
    max_wait = 2000

    # limit number of requests by adding a wait time.
    wait_time = between(0.1, 0.2)

    def on_start(self):
        auth.login(self.client)


    @tag('load dashboard')
    @task
    def load_dashboard(self):
        for url in DashboardUrls:
            self.client.get(url=url.value)

