
import helper as h
from time_range import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Friend:
    all_busy_minutes_range: ClassVar[list] = []
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self,obj:TimeRange):
        self.busy_time_ranges.append(obj)
        #Add the minutes range object to a class attribute
        Friend.all_busy_minutes_range.append(obj.minutes_range)


# f1 = Friend('Jim')
# f1.add_busy_range(TimeRange(start_time= "09:00",end_time= "17:00"))
# f1.add_busy_range(TimeRange(start_time='18:00',end_time="23:00"))
# print(f1.busy_time_ranges)

# print(f1)