class RecentCount:
    def __init__(self):
        self.time = []

    def ping(self, t):
        self.time.append(t)
        while self.time[0] < t - 3000:
            self.time.pop(0)
        return len(self.time)
