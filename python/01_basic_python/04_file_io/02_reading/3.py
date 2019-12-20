headings = []
data = []
with open('3.example.csv', 'r') as fp:
    # first line has the headings so capturing
    # the headings first
    headings = fp.readline().rstrip().split(',')

    while True:
        line = fp.readline()

        if line == '':
            break
    
        # so the last item of the list has \n which can be removed using rstrip
        data.append(line.rstrip().split(','))

print(headings)
print(data)


