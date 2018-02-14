import sys

tots = ['rf_total', 'sf_total', 'foac_total', 'fh_total', 'f_total',
        's_total', 'toac_total', 'tp_total', 'op_total', 'nothing_total']

possible_hands = ['a royal flush', 'a straight flush', 'four of a kind', 'a full house',
                  'a flush', 'a straight', 'three of a kind', 'two pairs', 'one pair', 'nothing']

total = {'rf_total': 0,
         'sf_total': 0,
         'foac_total': 0,
         'fh_total': 0,
         'f_total': 0,
         's_total': 0,
         'toac_total': 0,
         'tp_total': 0,
         'op_total': 0,
         'nothing_total': 0}


def find_best_hand(number):
    j = 9
    while j >= 0:
        total[tots[(9 - int(number))]] += 1
        j = j - 1

    return total


def main():
    num_lines = 0
    for line in sys.stdin:
        line = line.strip().split(',')
        totals = find_best_hand(line[-1])
        num_lines = num_lines + 1

    i = 9
    while i >= 0:
        print('The probability of {} is {:.4f}%'.format(
            possible_hands[i], (totals[tots[i]] / num_lines) * 10))
        i = i - 1

if __name__ == '__main__':
    main()
