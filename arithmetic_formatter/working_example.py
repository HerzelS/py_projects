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

add_time('6:30 PM', '17:30', 'Monday')
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