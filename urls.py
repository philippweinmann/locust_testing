from enum import Enum


class HivebuyUrls(Enum):
    AUTH_URL = "auth/"
    USER_URL = "company/user/"
    PUR_URL = "company/purchase-request/"
    POLL_URL = "company/request-for-proposal-board/"
    PUR_ORDERS_URL = "company/purchase-order/"


class DashboardUrls(Enum):
    __order__ = 'PURCHASE_REQUESTS DEPARTMENT DASHBOARD_PUR_1 PUR_O MEMBERS USER ME INVOICE_PUR_O'
    PURCHASE_REQUESTS = "company/purchase-request/?actionRequired=true&pageSize=3&requestedBy=248c8c5d-a1d3-4da7-8cba" \
                        "-749335e17925&ordering=-requested_at"
    DEPARTMENT = "company/department/"
    DASHBOARD_PUR_1 = "company/my-purchase-request/?pageSize=8"
    PUR_O = "company/purchase-order/?page=1&pageSize=5&ordering=&actionRequired=true&hideClosed=true"
    MEMBERS = "company/members/?image=true"
    USER = "company/user/"
    ME = "users/me/"
    INVOICE_PUR_O = "company/invoice-purchase-orders/?actionRequired=true&pageSize=3&requestedBy=248c8c5d-a1d3-4da7" \
                    "-8cba-749335e17925&ordering=-requested_at"


class ConnectionUrls(Enum):
    LOCALHOST = "http://127.0.0.1:8000/api/"
    STAGING = "https://backend.staging.hivebuy.de/api/"


class NoImagesUrls(Enum):
    PAYMENT_METHODS = "company/payment-method/"
