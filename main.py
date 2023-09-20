from time_range import TimeRange
from friend import Friend
from custom_list import CustomList
import helper as h
def main():
    # available_minutes = list(range(1440))
    available_minutes = CustomList(range(1440))# this custom list created to avoid collosion when busy ranges overlap
    f1 = Friend('Jim')
    f1.add_busy_range(TimeRange(start_time='08:00',end_time='10:00'))
    f2 = Friend('Jeremy')
    f2.add_busy_range(TimeRange(start_time='08:00', end_time='14:00'))
    # for i in  range(1440):
    #     print(i)
    # iterating over a copy of list as list[:] is best way less risky
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    time_range_list = h.prettify_available_minutes(available_minutes)
    for tr in time_range_list:
        print(f" You can meet in {tr} with ")


if __name__ == "__main__":

    main()