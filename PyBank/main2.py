import sys
import csv


def main():
    months = []
    total_revenue = []

    with open(r'C:\Users\Dolly\PythonHomework\Python-Challenge\PyBank\Resources\budget_data.csv', 'r') as csvfile:
        budget_reader = csv.DictReader(csvfile, delimiter=',')
        for row in budget_reader:
            months.append(row['Date'])
            total_revenue.append((row['Date'], int(row['Profit/Losses'])))

    print('Financial Analysis')
    print('------------------------------------')
    print('Total Months: {}'.format(len(months)))
    print('Total: ${:,.2f}'.format(sum([i[1] for i in total_revenue])))
    print('Average Change: ${:,.2f}'.format(
        sum([i[1] for i in total_revenue]) / len(total_revenue)))

    minimum = min([i[1] for i in total_revenue])
    maximum = max([i[1] for i in total_revenue])

    for date, value in total_revenue:
        if value == minimum:
            min_date = date
        if value == maximum:
            max_date = date

    print('Greatest Increase in Profits: {} (${})'.format(max_date, maximum))
    print('Greatest Decrease in Profits: {} (${})'.format(min_date, minimum))
    return 0


if __name__ == '__main__':
    sys.exit(main())
