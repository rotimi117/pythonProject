class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._total_seconds = self._time_to_seconds(hour, minute, second)
    def hour(self):
        return self._total_seconds // 3600
    def hour(self, value):
        self._total_seconds = self._time_to_seconds(value, self.minute, self.second)


    def minute(self):
        return (self._total_seconds // 60) % 60


    def minute(self, value):
        self._total_seconds = self._time_to_seconds(self.hour, value, self.second)


    def second(self):
        return self._total_seconds % 60


    def second(self, value):
        self._total_seconds = self._time_to_seconds(self.hour, self.minute, value)

    def _time_to_seconds(self, hour, minute, second):
        return hour * 3600 + minute * 60 + second


t1 = Time(1, 30, 45)
print(f"Original time: {t1.hour}:{t1.minute}:{t1.second}")

t1.hour = 5
t1.minute = 20
t1.second = 10

print(f"Updated time: {t1.hour}:{t1.minute}:{t1.second}")
