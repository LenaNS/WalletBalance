from locust import HttpUser, task, between


class WalletApiUser(HttpUser):
    wait_time = between(0.1, 2)
    min_wait = 1000
    max_wait = 2000

    @task
    def test_wallet_balance(self):
        self.client.get("/api/v1/wallets/6ea66b41-49e7-4261-8cf0-94d77000793a")

    @task
    def test_wallet_balance22(self):
        self.client.get("/api/v1/wallets/0f8c72f8-149b-4c14-ad31-1949303c633d")

