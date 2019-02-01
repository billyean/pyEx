#!/usr/bin/env python3


def list_to_dict(lst):
    list_of_list = [lst[0], [p.split(",") for p in lst[1]]]
    return [list_of_list[0], {p[0]:p[1] for p in list_of_list[1]}]


# Task 1 Answer
beatles = ['beatles', ('George, guitar', 'John, guitar', 'Paul, bass', 'Ringo, drums')]

# Task 2 Answer
beatles_dict = list_to_dict(beatles)
print(beatles_dict)

# Task 3 Answer
stones = ['stones', ('Mick, piano', 'Keith, guitar', 'Charlie, drums', 'Ronnie, guitar')]

# Task 4 Answer
stones_dict = list_to_dict(stones)
print(stones_dict)

# Task 5 Answer
bands = [beatles_dict, stones_dict]
bands_dict = {b[0].capitalize():b[1] for b in bands}

# Task 6 Answer
ringo_vale = bands_dict['Beatles']['Ringo']
print(f'Ringo is {ringo_vale}')