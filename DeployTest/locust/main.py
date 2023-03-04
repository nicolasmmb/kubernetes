from locust import HttpUser, task, between


class QuickStartTester(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/all_env_vars")

    # @task
    # def timer(self):
    #     self.client.get("/timer?interval=5")
