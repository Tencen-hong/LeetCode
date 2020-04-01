class UndergroundSystem:

    def __init__(self):
        self.station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.station:
            self.station[stationName] = []
        self.station[stationName].append(('checkIn', id, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.station:
            self.station[stationName] = []
        self.station[stationName].append(('checkOut', id, t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        checkin = {}
        checkout = {}
        for item in self.station[startStation]:
            op = item[0]
            id = item[1]
            t = item[2]
            if op == 'checkIn':
                if id not in checkin:
                    checkin[id] = -1
                checkin[id] = t

        for item in self.station[endStation]:
            op = item[0]
            id = item[1]
            t = item[2]
            if op == 'checkOut':
                if id not in checkout:
                    checkout[id] = -1
                checkout[id] = t

        total_passenger = 0
        total_time = 0
        for id, t in checkin.items():
            if id in checkout:
                total_passenger += 1
                total_time += (checkout[id] - checkin[id])
        return total_time / total_passenger


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
