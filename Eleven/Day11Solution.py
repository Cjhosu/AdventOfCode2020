import itertools
import copy

rows = []
with open('Day11_sample') as file:
    for line in file:
        line = line.strip()
        rows.append(line)

layout = {}
inner = {}

for i, each in enumerate(rows):
    layout['y' + str(i)] = each

for k, v in layout.items():
    seats = list(v)
    for ix, seat in enumerate(seats):
        inner['x' + str(ix)] = seat
    layout[k] = inner
    inner = {}

def adjacent_seats(yval, xval):
    y_coords  = []
    x_coords = []
    neighbors = []
    seats = []
    for i in range(int(yval[1]) -1, int(yval[1]) + 2):
        if 'y' + str(i) in layout:
            y_coords.append('y' + str(i))
    for i in range(int(xval[1]) -1, int(xval[1]) + 2):
        if 'x' + str(i) in layout[yval]:
            x_coords.append('x' + str(i))
    for element in itertools.product(y_coords, x_coords):
        neighbors.append(element)
    neighbors.remove((yval, xval))
    print(neighbors)
    for coord in neighbors:
        seats.append(layout[coord[0]][coord[1]])
    print(seats)
    if layout[yval][xval] == 'L' and all(seat != '#' for seat in seats):
        new_layout[yval][xval] = '#'
    elif  layout[yval][xval]== '#' and sum(1 for seat in seats if seat == '#') >=4:
        new_layout[yval][xval] = 'L'

    print(new_layout)

new_layout = copy.deepcopy(layout)
for each in layout:
    for k, v in layout[each].items():
        print(each, k)
        adjacent_seats(each, k)





