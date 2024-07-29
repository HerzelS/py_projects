def add_time(start, duration, DAY = ''):
    # Add duration time to the start time and return the result
    day = float(24.00)
    day_week = ['M', 'T', 'W', 'T', 'F', 'Sat', 'Sun']
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

    minutes = int(hour_hand) * 60 + int(minute_hand)
    minutes_duration = int(duration_hours) * 60 + int(duration_minutes)

    if minutes > 720:
        time_notation_hour = minutes // 60 - 12
        time_notation_minutes = minutes % 60

    else:
        time_notation_hour = minutes // 60
        time_notation_minutes = minutes % 60

    time_now = f'{time_notation_hour}, {time_notation_minutes} {time_stamp}'

    projected_time_hours = int(time_notation_hour) + int(duration_hours) # for 24 hr notation
    projected_time_minutes = int(time_notation_minutes) + int(duration_minutes)


    print(projected_time_hours)
    print(projected_time_minutes)


    #return new_time

add_time("22:45 PM", '14:05', 'mONDAY')