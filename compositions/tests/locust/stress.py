from locust import HttpLocust, TaskSet, task


def login(l):
    response = l.client.get('/accounts/login/')
    csrftoken = response.cookies['csrftoken']
    l.client.post('/accounts/login/',
                  {'username': 'username', 'password': 'password'},
                  headers={'X-CSRFToken': csrftoken})


class WebsiteTasks(TaskSet):
    def on_start(self):
        login(self)

    @task
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
