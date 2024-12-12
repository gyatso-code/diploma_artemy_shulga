from locust import HttpUser, SequentialTaskSet, task, between


class User1(HttpUser):
    @task
    def mainPage(self):
        self.client.get("/")


# Класс, определяющий пользователя
class User2(HttpUser):

    # Набор задач, выполняемых последовательно
    @task
    class SequenceOfTasks(SequentialTaskSet):
        # Время ожидания между задачами от 1 до 5 секунд
        wait_time = between(1, 5)

        # Задача для посещения главной страницы и получения записей
        @task
        def mainPage(self):
            self.client.get("/")
            self.client.get("https://api.demoblaze.com/entries")

        # Задача для выполнения входа
        @task
        def login(self):
            self.client.options("https://api.demoblaze.com/login")
            self.client.post("https://api.demoblaze.com/login", json={"username": "aaaa", "password": "YWFhYQ=="})
            self.client.options("https://api.demoblaze.com/check")
            self.client.get("https://api.demoblaze.com/entries")
            self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})

        # Задача для выбора продукта
        @task
        def clickProduct(self):
            self.client.get("/prod.html?idp_=1")
            self.client.options("https://api.demoblaze.com/check")
            self.client.options("https://api.demoblaze.com/view")
            self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/view", json={"id": "1"})


        @task
        def addToCart(self):
            self.client.options("https://api.demoblaze.com/addtocart")
            self.client.post("https://api.demoblaze.com/addtocart",
                             json={"id": "fb3d5d23-f88c-80d9-a8de-32f1b6034bfd", "cookie": "YWFhYTE2MzA5NDU=",
                                   "prod_id": 1, "flag": 'true'})

        @task
        def viewCart(self):
            self.client.get("/cart.html")
            self.client.options("https://api.demoblaze.com/check")
            self.client.options("https://api.demoblaze.com/viewcart")
            self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/viewcart", json={"cookie": "YWFhYTE2MzA5NDU=", "flag": 'true'})
            self.client.options("https://api.demoblaze.com/view")
            self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

