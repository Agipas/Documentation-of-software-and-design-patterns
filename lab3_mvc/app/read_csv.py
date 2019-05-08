import re

with open('generated.csv', 'r+') as file:
    buffer = file.read()
    # data = mmap.mmap(file.fileno(), 0)
    # mo = re.search('\nCompensations', data)
    first = re.split(r'Compensations\n', buffer)[1]
    sec = re.split(r'.*\n\nProjects\n', first)[0]
    compensation = sec.split('\n')
    print(compensation)