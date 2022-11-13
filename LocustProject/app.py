from locust import User,task,constant



class  BipinTest(User):
    weight = 2
    wait_time = constant(4)
    @task
    def launch_site(self):
        print('launching site')

    @task
    def search(self):
        print('search')

class  BipinTest2(User):
    weight = 2
    wait_time = constant(4)
    @task
    def launch_site(self):
        print('launching site 2')

    @task
    def search(self):
        print('search 2')
