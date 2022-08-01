from datetime import datetime as dt


def time_difference(end_time):
    time_fmt = '%H:%M:%S'
    date_time_now = dt.now().strftime(time_fmt)
    difference = dt.strptime(end_time, time_fmt) - \
        dt.strptime(date_time_now, time_fmt)

    return str(difference)
