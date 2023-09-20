from dataclasses import dataclass, field
import helper as h
@dataclass
class TimeRange:
    start_time : str # 00:30
    end_time : str #5:00

    start_minutes: int = field(init=False, repr=False) #30
    end_minute: int = field(init=False,repr=False) # 300

    minutes_range : range = field(init=False, repr = False)


    def __post_init__(self):
        self.start_minutes = h.timerange_to_minute(self.start_time)
        self.end_minutes = h.timerange_to_minute(self.end_time)
        self.minutes_range = range(self.start_minutes,self.end_minutes,1)


