class Record:
    def __init__(self, position1, position2, date, tyre_tread, tyre_depth):
        self.position1 = position1
        self.position2 = position2
        self.date = date
        self.tyre_tread = tyre_tread
        self.tyre_depth = tyre_depth

    def format(self):
        return {"position": f"{self.position1}, {self.position2}", "date": f"{self.date}", "tyre tread": f"{self.tyre_tread}", "tyre depth": f"{self.tyre_depth}"}
