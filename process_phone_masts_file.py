import csv
import pprint

from collections import Counter
from datetime import datetime


class ProcessMobilePhoneMasts(object):
    def __init__(self):
        self.data = self.get_data_from_file()
        self.pp = pprint.PrettyPrinter(indent=4)

    def get_data_from_file(self):
        with open('Mobile_Phone_Masts.csv', 'r') as csv_data_file:
            csv_data = csv.DictReader(csv_data_file)
            return [row for row in csv_data]

    def solve_first_task(self):
        sorted_data = sorted(self.data, key=lambda element: float(element['Current Rent']))
        return sorted_data[:5]

    def solve_second_task(self):
        filtered_data = [row for row in self.data if row['Lease Years'] == '25']
        total_rent = sum([float(row['Current Rent']) for row in filtered_data])
        return filtered_data, total_rent

    def solve_third_task(self):
        return Counter([row['Tenant Name'] for row in self.data])

    def solve_fourth_task(self):
        date_format = "%d %b %Y"
        start = datetime.strptime('01 Jun 1999', date_format).date()
        end = datetime.strptime('31 Aug 2007', date_format).date()
        data = []
        for row in self.data:
            row_date = datetime.strptime(row['Lease Start Date'], date_format).date()
            if start < row_date < end:
                row = row.copy()
                row['Lease Start Date'] = row_date.strftime("%d/%m/%Y")
                data.append(row)
        return data

    def print_first_solution(self):
        result = self.solve_first_task()
        print('Solution for first task:')
        self.pp.pprint(result)

    def print_second_solution(self):
        filtered_data, total_rent = self.solve_second_task()
        print('Solution for second task:')
        print(f'Total rent: {total_rent}')
        self.pp.pprint(filtered_data)

    def print_third_solution(self):
        result = self.solve_third_task()
        print('Solution for third task:')
        self.pp.pprint(result)

    def print_fourth_solution(self):
        result = self.solve_fourth_task()
        print('Solution for fourth task:')
        self.pp.pprint(result)


def run_script():
    selected = input(
        'Select which of the solutions would you like to print out.\n'
        'Choices are:\n'
        '1 - first task\n'
        '2 - second task\n'
        '3 - third task\n'
        '4 - fourth task\n'
        'Enter will print them all.\n'
    )
    processor = ProcessMobilePhoneMasts()
    choices_switch = {
        '1': processor.print_first_solution,
        '2': processor.print_second_solution,
        '3': processor.print_third_solution,
        '4': processor.print_fourth_solution,
    }
    if selected and selected in choices_switch.keys():
        choices_switch[selected]()
    elif not selected:
        for solution in choices_switch.values():
            solution()
    else:
        print(f'Sorry but "{selected}" is not a valid choice.')


if __name__ == "__main__":
    run_script()
