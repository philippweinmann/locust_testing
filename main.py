from locustfile import HivebuyUser
from locust import env

if __name__ == '__main__':
    environment = env.Environment()
    HivebuyUser(environment).run()
