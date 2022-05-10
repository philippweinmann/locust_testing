from locust import HttpUser, task, tag, between

from common import auth
from urls import HivebuyUrls, ConnectionUrls


class HivebuyUser(HttpUser):
    host = ConnectionUrls.LOCALHOST.value
    min_wait = 1000
    max_wait = 2000

    # limit number of requests by adding a wait time.
    wait_time = between(0.5, 1)

    def on_start(self):
        auth.login(self.client)

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

    @tag('get_all_polls')
    @task
    def get_purchase_requests(self):
        # get purchase requests
        self.client.get(url=HivebuyUrls.PUR_URL.value)

    @tag('get_all_po')
    @task
    def get_purchase_requests(self):
        # get purchase requests
        self.client.get(url=HivebuyUrls.PUR_ORDERS_URL.value)


