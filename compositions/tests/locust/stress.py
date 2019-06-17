from locust import HttpLocust, TaskSet, task


# To run those tests, first start the server, then run the command:
# locust -f stress.py --host=http://127.0.0.1:8000


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
        self.client.get('/')

    @task
    def create_composition(self):
        response = self.client.get('/create_composition')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/create_composition',
                         {'name': 'compo1'},
                         headers={'X-CSRFToken': csrftoken})


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
