from collections import defaultdict
import random


SUMMER = 0b1000
FALL = 0b0100
WINTER = 0b0010
SPRING = 0b0001
REGULAR = FALL | WINTER | SPRING
ALL = SUMMER | REGULAR


classes = set()


class Class:

    def __init__(self, name, units=4, quarters=REGULAR):
        self.name = name
        self.units = units
        self.quarters = quarters
        self.prereqs = set()
        self.coreqs = set()
        classes.add(self)

    def prereq(self, c):
        if c not in classes:
            raise Exception('Class not in available classes')
        self.prereqs.add(c)

    def coreq(self, c):
        if c not in classes:
            raise Exception('Class not in available classes')
        self.coreqs.add(c)


def build_schedule(template=None, packing=10, max_units=(18, 18, 18), years=4, summers=False):
    if template is None:
        template = []
        for i in range(years):
            template.append([[] for j in range(4 if summers else 3)])
    final_schedule = None
    while final_schedule is None:
        schedule = [[list(i) for i in j] for j in template]
        weights = remove_taken(compute_weights(), schedule)
        final_schedule = test_schedule(schedule, weights, packing, max_units, summers)
    return final_schedule


def compute_weights():
    weights = defaultdict(int)
    for c in classes:
        weights[c] += 1
        compute_weight(weights, c)
    actual_weights = []
    for c in weights:
        actual_weights += [c] * weights[c]
    return actual_weights


def compute_weight(weights, c, coreq=False):
    for prereq in c.prereqs:
        weights[prereq] += 6 if coreq else 8
        compute_weight(weights, prereq, coreq)
    for coreq_ in c.coreqs:
        weights[coreq_] += 2 if coreq else 4
        compute_weight(weights, coreq_, True)


def remove_taken(weights, schedule):
    for year in schedule:
        for term in year:
            for c in term:
                weights = list(filter(lambda x: x != c, weights))
    return weights


def test_schedule(schedule, weights, packing, max_units, summers):
    taken = set()
    for year in schedule:
        for date, term in enumerate(year):
            tries = 0
            while sum_units(term) < max_units[date]:
                tries += 1
                if tries >= packing:
                    break
                if not weights:
                    break
                new_class = random.choice(weights)
                if not is_offered(new_class, date, summers) or new_class.prereqs & taken != new_class.prereqs:
                    continue
                if new_class.units + sum_units(term) > max_units[date]:
                    continue
                term.append(new_class)
                weights = list(filter(lambda x: x != new_class, weights))
            for c in term:
                taken.add(c)
    if check_schedule(schedule, max_units) and not weights:
        return schedule


def is_offered(c, date, summers):
    if summers:
        quarter = [SUMMER, FALL, WINTER, SPRING][date]
    else:
        quarter = [FALL, WINTER, SPRING][date]
    return quarter & c.quarters


def sum_units(term):
    units = 0
    for c in term:
        units += c.units
    return units


def check_schedule(schedule, max_units):
    taken = set()
    for year in schedule:
        for date, term in enumerate(year):
            if sum_units(term) > max_units[date]:
                return False
            for c in term:
                if c.prereqs & taken != c.prereqs:
                    return False
            for c in term:
                taken.add(c)
            for c in term:
                if c.coreqs & taken != c.coreqs:
                    return False
    return True


def print_schedule(schedule):
    for y, year in enumerate(schedule, 1):
        print('Year {}'.format(y))
        for term in year:
            for course in term:
                print(course.name, end=', ')
            print('UNITS: {}'.format(sum_units(term)))
        print()