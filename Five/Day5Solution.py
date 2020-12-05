import math

seat_ids = []
def bin_search(line):
    all_rows = list(range(0,128))
    all_cols = list(range(0,8))
    for item in line:
        rows_left = (len(all_rows))
        rbreak_point = rows_left/2
        cols_left = len(all_cols)
        cbreak_point = cols_left/2
        if item == 'F':
            all_rows = all_rows[:math.floor(rbreak_point)]
        if item == 'B':
            all_rows = all_rows[math.floor(rbreak_point):]
        if item == 'L':
            all_cols = all_cols[:math.floor(cbreak_point)]
        if item == 'R':
            all_cols = all_cols[math.floor(cbreak_point):]

    s_id = all_rows[0] * 8 + all_cols[0]
    seat_ids.append(s_id)


with open('Day5_input') as file:
    for line in file:
        line = line.strip()
        bin_search(line)

seat_ids.sort()
print(seat_ids[-1])


all_rows = list(range(0,128))
all_cols = list(range(0,8))

test_seats = []
for i in all_rows:
    for n in all_cols:
       sid = i * 8 + n
       test_seats.append(sid)

test_seats.sort()
print(test_seats[-1])

missing_seats = list(set(test_seats) - set(seat_ids))
for item in missing_seats:
    if item +1 in missing_seats or item-1 in missing_seats:
        pass
    else:
        print(item)
