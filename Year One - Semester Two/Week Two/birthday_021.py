import sys
import calendar


def day(day, month, year):
    return calendar.weekday(year, month, day)


def sentence(number):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = days[number]
    ending = ['is fair of face.', 'is full of grace.', 'is full of woe.', 'has far to go.',
              'is loving and giving.', 'works hard for a living.', 'is fair and wise and good in every way.']
    fill_in = ending[number]

    return 'You were born on a {} and {}s child {}'.format(day, str(day) + "'", fill_in)


def main():
    birth_day = int(sys.argv[1])
    birth_month = int(sys.argv[2])
    birth_year = int(sys.argv[3])
    num = day(birth_day, birth_month, birth_year)
    print(sentence(num))


if __name__ == '__main__':
    main()
