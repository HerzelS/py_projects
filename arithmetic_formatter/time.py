def add_time(start, duration, day = ''):
    # Add duration time to the start time and return the result
    day_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    day_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time_flip = {'AM':'PM', 'PM': 'AM'}


    duration_hours = duration[:duration.index(":")].strip()
    duration_minutes = duration[duration.index(":") +1:].strip()
    hour_hand = start[:start.index(":")].strip()
    minute_hand = start[start.index(":")+ 1:-3].strip()

    minutes_start = int(minute_hand)
    starting_minutes = int(hour_hand) * 60 + int(minute_hand)
    hour_current = int(hour_hand)
    duration_hours_org = int(duration_hours)
    minutes_duration = int(duration_hours) * 60 + int(duration_minutes)
    minutes_takes = int(duration_minutes)
    total_minutes = int(minutes_start) + int(minutes_takes)


    if 'AM' in start:
        time_stamp = "AM"
    if 'PM' in start:
        time_stamp = "PM"
    
    cumulative_minutes = starting_minutes + minutes_duration
    days =  cumulative_minutes // 1440

    # Adding munutes on the hour
    minutes_future = minutes_start + minutes_takes
    if total_minutes >= 60:
        hour_current += 1
        minutes_future = cumulative_minutes % 60

    # Adding hour on the hour
    end_hours = (hour_current + duration_hours_org) % 12
    number_of_time_flips = int((hour_current + duration_hours_org) / 12)

    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    minutes_future = minutes_future if minutes_future > 9 else '0' + str(minutes_future)

    if time_stamp == 'PM' and hour_current + (duration_hours_org // 12 ) >= 12:
        days += 1
    elif time_stamp == 'PM' and number_of_time_flips >=1:
        days += 1
        
    time_stamp = time_flip[time_stamp] if number_of_time_flips % 2 == 1 else time_stamp

    new_time = f'{end_hours}:{minutes_future} {time_stamp}'
    
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


add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

a = add_time('11:43 PM', '24:20', 'tueSday')

print(a)