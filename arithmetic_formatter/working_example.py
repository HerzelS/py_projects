def add_time(start, duration, day=False):
    day_of_week_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    day_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    duration_split = duration.partition(':')
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[2])

    start_split = start.partition(':')
    start_minutes_split = start_split[2].partition(' ')
    start_hours = int(start_split[0])
    start_minutes = int(start_minutes_split[0])
    am_or_pm = start_minutes_split[2]
    am_and_pm_flip = {'AM': 'PM', 'PM': 'AM'}

    amount_of_days = int(duration_hours / 24)
                         
    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes % 60
    
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12)  
    end_hours = (start_hours + duration_hours) % 12
    
    end_minutes = end_minutes if end_minutes > 9 else '0' + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    
    if am_or_pm == 'PM' and start_hours + (duration_hours // 12) >= 12 :
        amount_of_days += 1
    elif am_or_pm == 'PM' and amount_of_am_pm_flips >= 1:
        amount_of_days += 1

    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm
    
    return_time = str(end_hours) + ':' + str(end_minutes) + ' ' + am_or_pm
    
    if day:
        day = day.lower()
        index = int((day_of_week_index[day]) + amount_of_days) % 7
        new_day = day_of_week_array[index]
        return_time += ', ' + new_day

    if amount_of_days == 1:
        print (return_time + ' ' + '(next day)')
    elif amount_of_days > 1:
        print( return_time + ' (' + str(amount_of_days) + ' days later)')
    elif amount_of_days == 0:
        print(return_time)

add_time('6:30 PM', '3:30', 'Monday')


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

    starting_minutes = int(hour_hand) * 60 + int(minute_hand)
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


    
    # Add days - this is working now
    if day:
        day = day.lower()
        index = int((day_index[day]) + days)
        new_day = day_of_week_array[index]


    time_now = f'{time_notation_hour}, {time_notation_minutes} {time_stamp}' 
 #   actual_hour_on_day =  cumulative_minutes // days To calculate hour on day


    #print(cumulative_minutes)
    #print(days)
    #print(hours_future)
    #print(minutes_future)
    print(minu)
    print(hour_current)
    print(duration_hours)
    print(end_hours)
    #print(new_day)

    #print(actual_hour_on_day)


    #return new_time

add_time("04:00 PM", '4:05', 'Monday')