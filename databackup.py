import datetime as dt
import json
import csv


def input_num(prompt):
    """
    when the input must be an int
    :param prompt: how you want to ask for the int
    :return: an int
    """
    b = None
    while b is None:
        try:
            b = int(input(prompt))
        except ValueError:
            print("Please enter a number")
    return b


def input_employee():
    """
    this function will take text input and will make an employee dictionary for one person.
    :return: a dict with lots of stuff in it.
    """
    emp = dict()
    emp['first_name'] = input("Please enter first name: ").capitalize()
    emp['last_name'] = input("Please enter last name: ").capitalize()
    while "dob" not in emp:
        try:
            day = input_num("What is the day of your birthday?")
            month = input_num("What is the month of your birthday?(as a number)")
            year = input_num("What is the year of your birthday?")
            emp["dob"] = dt.date(year=year, month=month, day=day).isoformat()
        except ValueError:
            print("Something went wrong lets try entering the date again.")
    emp['email'] = "{}.{}{:2}@company.com".format(
                    emp['last_name'], emp['first_name'], str(year)[-2:])
    return emp


def main():
    commands = {
        "help": "Dsiplays a list of commands.",
        "add": "allows the input of an employee (not saved yet but able to be saved)",
        "lodcsv": "loads employee information to a csv file",
        "savcsv": "saves any changes to a csv file",
        "lodjson": "loads employee information to a json file",
        "savjson": "saves any changes in employee information to a json file",
        "see": "prints out list of employees to console",
        "exit": "closes the program.",
    }
    json_path = "employee_info/employees.json"
    csv_path = "employee_info/employees.csv"
    header = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'dob': 'dob',
        'email': 'email',
    }
    employees = []
    while True:
        command = input("What do ya want to do today?(type help for a list of commands): \n").lower()
        print("Running:", command)
        if command == "exit":
            break
        if command == "help":
            print("Command\t\tDescription")
            for cmd in commands:
                print("{}\t\t{}".format(cmd, commands[cmd]))
                continue
        if command == "add":
            employees.append(input_employee())
            continue
        if command == "savcsv":
            with open(csv_path, "w+", newline='') as f:
                if not employees:
                    w = csv.DictWriter(f, [])
                    w.writerows(employees)
                    continue
                w = csv.DictWriter(f, list(header.keys()))
                w.writerows([header]+employees)
            continue

        if command == "lodcsv":
            with open(csv_path, "r") as f:
                w = csv.DictReader(f)
                employees = []
                for row in w:
                    employees.append(row)
            continue
        if command == "savjson":
            with open(json_path, "w+") as f:
                json.dump(employees, f, indent=2)
            continue

        if command == "lodjson":
            with open(json_path, "r") as f:
                employees = json.load(f)
            continue
        if command == "see":
            print("Employees:")
            for item in employees:
                print(item)
            print()
            continue


if __name__ == "__main__":
    main()
