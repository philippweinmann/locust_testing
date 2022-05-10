from enum import Enum


class HivebuyUrls(Enum):
    AUTH_URL = "auth/"
    USER_URL = "company/user/"
    PUR_URL = "company/purchase-request/"
    POLL_URL = "company/request-for-proposal-board/"
    PUR_ORDERS_URL = "company/purchase-order/"


class ConnectionUrls(Enum):
    LOCALHOST = "http://127.0.0.1:8000/api/"
    STAGING = "https://backend.staging.hivebuy.de/api/"
