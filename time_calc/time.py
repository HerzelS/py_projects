def add_time(start, duration, day = False):
    """The function adds duration time to the start time and return the result"""

    day_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    day_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    am_pm = {'AM':'PM', 'PM': 'AM'}


    # index and strip white space for the 'hour' and 'minute' hands of the start time
    hour_hand = start[:start.index(":")].strip()
    minute_hand = start[start.index(":")+ 1:-3].strip()


    # get the time_stamp AM/PM
    if 'AM' in start:
        time_stamp = "AM"
    if 'PM' in start:
        time_stamp = "PM"


    # index and strip white space for the 'hour' and 'minute' hands of the duration period
    duration_hours = duration[:duration.index(":")].strip()
    duration_minutes = duration[duration.index(":") +1:].strip()

    minutes_start = int(minute_hand) # minutes at minute hand
    hour_current = int(hour_hand) # hours at hour hand
    starting_minutes = int(hour_hand) * 60 + int(minute_hand) # convert everything to minutes

    duration_hours_actual = int(duration_hours) # actual duration hours
    minutes_actual = int(duration_minutes) # actual duration minutes
    minutes_duration = int(duration_hours) * 60 + int(duration_minutes) # combined minutes duration (hours and mintes)
    total_minutes = int(minutes_start) + int(minutes_actual)


    # Calculate the number of days
    cumulative_minutes = starting_minutes + minutes_duration
    days =  cumulative_minutes // 1440

    # Add munutes on the hour
    minutes_future = minutes_start + minutes_actual
    if total_minutes >= 60:
        hour_current += 1
        minutes_future = cumulative_minutes % 60

    # Adding hour on the hour
    final_hours = (hour_current + duration_hours_actual) % 12
    time_stamp_change = int((hour_current + duration_hours_actual) / 12)

    final_hours = final_hours = 12 if final_hours == 0 else final_hours
    minutes_future = minutes_future if minutes_future > 9 else '0' + str(minutes_future)

    if time_stamp == 'PM' and hour_current + (duration_hours_actual // 12 ) >= 12:
        days += 1
    elif time_stamp == 'PM' and time_stamp_change >=1:
        days += 1
        
    time_stamp = am_pm[time_stamp] if time_stamp_change % 2 == 1 else time_stamp

    new_time = f'{final_hours}:{minutes_future} {time_stamp}'
    
    # Add days - this is working now
    if day:
        day = day.lower()
        index = int((day_index[day]) + days) % 7
        new_day = day_of_week_array[index]
        new_time += ', ' + new_day 

    if days == 1:
       new_time = f'{new_time} (next day)'
    elif days == days > 1:
       new_time = f'{new_time} ({str(days)} days later)'
    elif days == 0:
       new_time = new_time

    return new_time

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)

print(add_time('11:43 PM', '24:20', 'tueSday'))