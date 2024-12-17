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
        def ссылкаPage(self):
            self.client.get("ссылка", verify=False)

        # Задача для выбора продукта
        @task
        def ссылкаPage(self):
            self.client.get("ссылка", verify=False)
        @task
        def ссылкаPage(self):
            self.client.get("ссылка", verify=False)

        @task
        def ссылкаPage(self):
            self.client.get("ссылка", verify=False)

