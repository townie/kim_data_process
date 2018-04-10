# process.py
from __future__ import print_function
import filecmp

DATA = 'data.txt'
OUTPUT = 'output.csv'
TEST_FIX = 'output_fixture.txt'


def test_file(actual, expected=TEST_FIX):
    out = filecmp.cmp(actual, expected)
    if out:
        print("SUCCESS: {} == {}".format(actual, expected))
    else:
        print("FAILURE: {} != {}".format(actual, expected))


# attempt 1
print('attempt 1')

output = []
with open(DATA, 'r') as finput:
    print('opeing data.txt')
    for line in finput:
        output.append([line.decode('utf-8').rstrip()])

with open(OUTPUT, 'w+') as foutput:
    print('writing output')
    for line in output:
        foutput.write("\"{}\"\n".format(''.join(line).encode('utf-8')))

test_file(OUTPUT)

print('complete')


# attempt2

print('attempt 2')

with open(DATA, 'r') as raw:
    with open(OUTPUT + '2', 'w+') as output:
        for row in raw:
            line = '\"' + ''.join(row.encode('utf-8').rstrip()) + '\"'
            print(line, file=output)

test_file(OUTPUT + '2')
