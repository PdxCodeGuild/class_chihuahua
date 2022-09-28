from datetime import datetime


# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(year, month, day):
    return datetime(year, month, day)


def test_create_date():
    assert type(create_date(2021, 4, 20)) == datetime
    assert str(create_date(2021, 4, 20)) == '2021-04-20 00:00:00'


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    return int(dt.year)


def test_get_year():
    assert type(get_year(datetime(2021, 4, 20))) == int
    assert get_year(datetime(2021, 4, 20)) == 2021


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime
# Hint: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

def parse_date(date_string):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    date_month = date_string[:date_string.find(" ")]
    date_month = months[date_month]
    date_day = date_string[date_string.find(" ") + 1:date_string.find(",")]
    date_year = date_string[date_string.find(", ") + 2:]
    return datetime(int(date_year), int(date_month), int(date_day))


def test_parse_date():
    assert type(parse_date('April 20, 2021')) == datetime
    assert str(parse_date('April 20, 2021')) == '2021-04-20 00:00:00'


# Parse Datetime ===============================================================
# Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    date_month = date_string[:date_string.find(" ")]
    date_month = months[date_month]
    date_day = date_string[date_string.find(" ") + 1:date_string.find(",")]
    date_year = date_string[date_string.find(", ") + 2:date_string.find(", ") + 7]
    date_hour = date_string[date_string.find(":") - 2:date_string.find(":")]
    date_minute = date_string[date_string.find(":") + 1:date_string.find(":") + 3]
    print(date_minute)

    return datetime(int(date_year), int(date_month), int(date_day), hour=int(date_hour), minute=int(date_minute))


def test_parse_datetime():
    assert type(parse_datetime('April 20, 2021 09:30 AM')) == datetime
    assert str(parse_datetime('April 20, 2021 09:30 AM')
               ) == '2021-04-20 09:30:00'

# Format Datetime ==============================================================
# Write a function that converts the given datetime into a string


def format_datetime(dt):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    date_hour = int(dt.hour)
    suffix = ""
    if date_hour < 12:
        suffix = "AM"
    elif date_hour >= 12:
        suffix = "PM"
        date_hour -= 12
    
    date_hour = str(date_hour)
    if len(date_hour) == 1:
        date_hour = f"0{date_hour}"
    
    date_minute = str(dt.minute)
    if len(date_minute) == 1:
        date_minute = f"0{date_minute}"

    date_string = f"{months[dt.month]} {dt.day}, {dt.year} {date_hour}:{date_minute} {suffix}"
    return date_string

def test_format_datetime():
    assert type(format_datetime(datetime(2021, 4, 20, 9, 30))) == str
    assert format_datetime(datetime(2021, 4, 20, 9, 30)
                           ) == 'April 20, 2021 09:30 AM'
