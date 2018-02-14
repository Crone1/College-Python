import sys

disqualified_p_name = []
p_name = []
p_points = []


def find_length_longest_name(people_and_scores):
    longest = ''
    for line in people_and_scores:
        tokens = line.strip().split()
        name = ' '.join(tokens[:-19])
        if len(name) > len(longest):
            longest = name

    return len(longest)


def find_disqualified(name, scores):
    for score in scores:
        if not score.strip().isdigit() and score.strip() != 'X':
            disqualified_p_name.append(name)
            return ''

    return 'not empty'


def order_lists(pars, indexes, scores):
    indexes = [int(x) for x in indexes]

    hole_pars = [int(pars) for _, pars, _ in sorted(
        zip(indexes, pars, scores))]

    people_scores = [scores for _, _, scores in sorted(
        zip(indexes, pars, scores))]

    return [hole_pars, people_scores]


def find_pars(players_par, pars):
    while players_par:
        i = 0
        while i < int(players_par) and i < 18:
            pars[i] = pars[i] + 1
            i = i + 1

        if i < int(players_par):
            players_par = int(players_par) - 18

        else:
            players_par = 0

    return pars


def stableford_score(pars, scores):
    points = 0
    i = 0
    while i < len(pars):
        if scores[i] != 'X' and 2 - (int(scores[i]) - int(pars[i])) > 0:
            points = points + 2 - (int(scores[i]) - int(pars[i]))
        i = i + 1

    return points


def main():
    lines = sys.stdin.readlines()
    pars = lines[0].strip().split()
    indexes = lines[1].strip().split()
    people_and_scores = lines[2:]

    for line in people_and_scores:
        tokens = line.strip().split()
        name = ' '.join(tokens[:-19])
        players_par = tokens[-19].strip()
        scores = tokens[-18:]

        if find_disqualified(name, scores):
            [par, score] = order_lists(pars, indexes, scores)
            new_par = find_pars(players_par, par)
            points = stableford_score(new_par, score)
            p_name.append(name)
            p_points.append(points)

    if p_name:
        players_points = [p_points for p_points, _ in sorted(zip(p_points, p_name))][
            ::-1]

        players_name = [p_name for _, p_name in sorted(zip(p_points, p_name))][
            ::-1]

        i = 0
        while i < len(players_name):
            print('{:>{}s} : {:>2}'.format(
                players_name[i], find_length_longest_name(people_and_scores), players_points[i]))
            i = i + 1

    for person in disqualified_p_name:
        print('{:>{}s} : Disqualified'.format(
            person, find_length_longest_name(people_and_scores)))

if __name__ == '__main__':
    main()
