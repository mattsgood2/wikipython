import datetime


answer_format = "%d/%m"
link_format = "%b/%d"
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'quit' to quit." )
    if answer.upper() == 'QUIT':
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("Thats not a valid date format please try again")
