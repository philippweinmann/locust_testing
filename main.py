from locustfile import HivebuyUser
from locust import run_single_user

# for debugging purposes, activate gevent in pycharm for this to work
if __name__ == "__main__":
    run_single_user(HivebuyUser)
