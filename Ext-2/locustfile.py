from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    # Указываем Minikube URL в переменной host
    host = "http://127.0.0.1:56615"
    
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")