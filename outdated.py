import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    date = input("Date: ")

    try:
        dt = datetime.datetime.strptime(date, "%B %d, %Y")
    except ValueError:
        try:
            dt = datetime.datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            continue

    formatted_date = dt.strftime("%Y-%m-%d")
    print(formatted_date)
    break
