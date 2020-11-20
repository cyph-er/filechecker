with open('file1.txt', 'r') as file1:
    with open('file2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('Result.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)