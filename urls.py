from enum import Enum


class HivebuyUrls(Enum):
    AUTH_URL = "api/auth/"
    USER_URL = "api/company/user/"
    PUR_URL = "api/company/purchase-request/"


class ConnectionUrls(Enum):
    LOCALHOST = "http://127.0.0.1:8000/"
    STAGING = "https://backend.staging.hivebuy.de/api/"
