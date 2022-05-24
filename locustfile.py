from locust import HttpUser, task, tag, between

from common import auth
from urls import HivebuyUrls, ConnectionUrls, DashboardUrls, NoImagesUrls


class HivebuyUser(HttpUser):
    host = ConnectionUrls.LOCALHOST.value
    min_wait = 1000
    max_wait = 2000

    # limit number of requests by adding a wait time.
    wait_time = between(10, 20)

    def on_start(self):
        auth.login(self.client)

    @tag('load dashboard')
    @task
    def load_dashboard(self):
        for url in DashboardUrls:
            self.client.get(url=url.value)

    '''
    @tag('get payment methods')
    @task
    def load_payment_methods(self):
        self.client.get(url=NoImagesUrls.PAYMENT_METHODS.value)
    '''