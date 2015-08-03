from datetime import datetime,timedelta

def form_entries(form):
    res={}
    for key in form:
        res[key]=form[key]
    return res

def string_to_date(date_str,date_pattern):
    return datetime.strptime(date_str,date_pattern)

def is_sunday(date):
    return date.weekday()==6

def next_sunday(date):
    delta=date.weekday()
    return date+timedelta(days=(6-delta))

def date_range_key(date_start,date_end):
    return '-'.join([str(x) for x in [date_start.year,date_start.month,date_start.day,date_end.year,date_end.month,date_end.day]])

def week_ranges(start_date,end_date):
    date_ranges=[]
    if end_date >= start_date:
        dates_left=True
        cur_start=start_date
        while dates_left:
            if is_sunday(cur_start):
                cur_end=cur_start
            else:
                cur_end=next_sunday(cur_start)
                if cur_end > end_date:
                    cur_end=end_date
                    dates_left=False
            date_ranges.append((cur_start,cur_end))
            cur_start=cur_end+timedelta(days=1)
            if cur_start > end_date:
                dates_left=False
    else:
        raise ValueError('End date cannot preceed start date')
    return date_ranges
