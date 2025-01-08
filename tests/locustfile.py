from locust import HttpUser, SequentialTaskSet, task, between
import urllib3


class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):

        urllib3.disable_warnings()

        # wait_time = between(1, 5)

        @task
        def mainPage(self):
            self.client.get("/")

        @task
        def vinPage(self):
            self.client.get("/vin", verify=False)

        @task
        def newsPage(self):
            self.client.get("/news", verify=False)
        @task
        def companyPage(self):
            self.client.get("/company", verify=False)

        @task
        def pagesPage(self):
            self.client.get("https://av.by/pages/info", verify=False)

        @task
        def carsPage(self):
            self.client.get("https://cars.av.by/", verify=False)

