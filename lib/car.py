class Car():

    def __init__(self):
        self.front = []
        self.back = []

    def add(self, data):
        if "front" in data["position"]: 
            self.front.append(data) 
        else: 
            self.back.append(data)

    def list_of(self):
        return self.front, self.back