def add_time(start, duration, day = ''):
    # Add duration time to the start time and return the result
    day_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    day_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time_flip = {'AM':'PM', 'PM': 'AM'}
    time = []


    duration_hours = duration[:duration.index(":")].strip()
    duration_minutes = duration[duration.index(":") +1:].strip()
    hour_hand = start[:start.index(":")].strip()
    minute_hand = start[start.index(":")+ 1:-3].strip()



    if 'AM' in start:
        time_stamp = "AM"
    if 'PM' in start:
        time_stamp = "PM"

    time.append(hour_hand)
    time.append(minute_hand)


    hour = int(hour_hand)
    minutes = int(minute_hand)
    starting_minutes = int(hour_hand) * 60 + int(minute_hand)
    starting_hours = int(hour_hand)
    starting_minutes_org = int(minute_hand)
    duration_hours_org = int(duration_hours)
    minutes_duration = int(duration_hours) * 60 + int(duration_minutes)
    total_minutes = int(starting_minutes) + int(minutes_duration)

    hour_current = int(hour_hand)

    if starting_minutes > 720:
        time_notation_hour = starting_minutes // 60 - 12
        time_notation_minutes = starting_minutes % 60

    else:
        time_notation_hour = starting_minutes // 60
        time_notation_minutes = starting_minutes % 60

    cumulative_minutes = starting_minutes + minutes_duration
    days =  cumulative_minutes // 1440
    hours_future = cumulative_minutes // 60



    # Adding munutes on the hour
    if minutes_duration >= 60:
        hour_current += 1
        minutes_future = cumulative_minutes % 60

    # Adding hour on the hour
    end_hours = (int(hour_current) + int(duration_hours)) % 12
    number_of_time_flips = int((starting_hours + duration_hours_org) / 12)
    
    time_stamp = time_flip[time_stamp] if number_of_time_flips % 2 == 1 else time_stamp

    





    
    # Add days - this is working now
    if day:
        day = day.lower()
        index = int((day_index[day]) + days)
        new_day = day_of_week_array[index]


    time_now = f'{time_notation_hour}, {time_notation_minutes} {time_stamp}' 
 #   actual_hour_on_day =  cumulative_minutes // days To calculate hour on day

    print(f'{end_hours} : {minutes_future} {time_stamp}')
 
    #return new_time

add_time("11:00 PM", '06:05', 'Monday')