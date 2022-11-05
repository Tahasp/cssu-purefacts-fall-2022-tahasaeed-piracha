import csv
import random

"""
 Problem: Given a set A of points in a 2D space (input.csv - see attached),
 select an N number of random Representative Points from this set such that
 they best "cover" the shape of the point set (as opposed to its density).
Output should be the source code and 5 separate output.csv files where N = 10, 25, 63, 159, 380.
"""

""" Function to read the input data and give a set of tuple which are the points"""
with open('input.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    all_points = set()
    for row in reader:
        all_points.add((int(row[0]), int(row[1])))

all_points_lst = list(all_points)  # list of all the points.


def dist_to_center(a: (int, int), b: (int, int)):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 1 / 2


""" Idea is to make circle around a base point and then eliminate points in that square and move on to the
next circle repeating the process until circles with no points but the centre remain.
To make sure we get the right amount of points i.e, n I would automate it to increase or decrese
the radius of the circle by small amounts to get to desired n."""


def circle_around_em(t: [(int, int)], radius: int):
    refine_lst = t.copy()
    base_point = all_points_lst[0]

    for l in all_points_lst:
        if dist_to_center(base_point, l) < radius:
            refine_lst.remove(l)

        base_point = refine_lst[random.randint(0, len(refine_lst))]
        
    return refine_lst


""" Final three cases in which either we have removed too many or too less circle points.
"""


def final_rinse(q: [(int, int)], n: int, radius: int):
    while len(q) != n:
        if len(q) < n:
            q = circle_around_em(q, radius + 1)

        elif len(q) > n:
            q = circle_around_em(q, radius - 1)

    return q


"""Function to write the output csv for selected n."""
with open('output0.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    result_points = set()
    sel = final_rinse(all_points_lst, 10, 100)
    for j in sel:
        row = j[0], j[1]
        writer.writerow(row)

if __name__ == '__main__.py':
    pass
