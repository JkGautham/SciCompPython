def add_time(start, duration, starting_day=None):

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_index = {day.lower(): i for i, day in enumerate(days_of_week)}
    
    def time_to_minutes(time):
        parts = time.split()
        time_parts = parts[0].split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        if parts[1] == "PM" and hours != 12:
            hours += 12
        if parts[1] == "AM" and hours == 12:
            hours = 0
        return hours * 60 + minutes

    def minutes_to_time(minutes):
        days_later = minutes // (24 * 60)
        minutes = minutes % (24 * 60)
        hours = minutes // 60
        minutes = minutes % 60
        period = "AM"
        if hours >= 12:
            period = "PM"
            if hours > 12:
                hours -= 12
        if hours == 0:
            hours = 12
        return f"{hours}:{minutes:02d} {period}", days_later

    start_minutes = time_to_minutes(start)
    duration_parts = duration.split(':')
    duration_minutes = int(duration_parts[0]) * 60 + int(duration_parts[1])

    total_minutes = start_minutes + duration_minutes
    new_time, days_later = minutes_to_time(total_minutes)

    if starting_day:
        start_day_index = days_index[starting_day.lower()]
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_part = f", {new_day}"
    else:
        day_part = ""

    if days_later == 1:
        days_later_part = " (next day)"
    elif days_later > 1:
        days_later_part = f" ({days_later} days later)"
    else:
        days_later_part = ""
    new_time = f"{new_time}{day_part}{days_later_part}"
    return new_time

