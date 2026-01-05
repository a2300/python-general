class Time:
    """Repesents the time of the day"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

        if not self.is_valid():
            raise ValueError(f'Invalid time: {self.hour:02d}:{self.minute:02d}:{self.second:02d}')

    def print_time(self):
        """Prints the time in HH:MM:SS format"""
        s = f'{self.hour:02}:{self.minute:02}:{self.second:02}'
        print(s)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
        
    def add_time(self, hours, minutes, seconds):
        duration = Time(hours, minutes, seconds)
        seconds = self.time_to_int() + duration.time_to_int()
        return Time.int_to_time(seconds)

    def is_after(self, other):
        assert self.is_valid(), 'self is not a valid Time'
        assert other.is_valid(), 'self is not a valid Time'
        
        return self.time_to_int() > other.time_to_int()
    
    def is_valid(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        if not isinstance(self.hour, int):
            return False
        if not isinstance(self.minute, int):
            return False
        return True    

    def __str__(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        return s
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)    

    @staticmethod                    
    def int_to_time(seconds):
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        
        # Handle 24-hour wrap-around
        hour = hour % 24
        return Time(hour, minute, second)    


if __name__ == "__main__":
    start = Time(9, 40, 0)
    print(start)

    duration = Time(1, 32, 0)
    end = start + duration
    print(end)

    print("Is end after start?", end.is_after(start))



