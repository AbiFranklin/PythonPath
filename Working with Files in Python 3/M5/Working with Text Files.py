def read_text(fn):
    with open(fn) as f:
        return print(f.read())
    
def read_line_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end=' ')


def write_text(fn, text):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(text)

def append_text(fn, text):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(text)

# read_text('./Working with Files in Python 3/files_to_read/backup.py')
# read_line_by_line('./Working with Files in Python 3/files_to_read/backup.py')
write_text('./Working with Files in Python 3/files_to_read/test.txt', 'Hello, World!')
read_text('./Working with Files in Python 3/files_to_read/test.txt')
append_text('./Working with Files in Python 3/files_to_read/test.txt', 'Appending this line.')
read_text('./Working with Files in Python 3/files_to_read/test.txt')
read_line_by_line('./Working with Files in Python 3/files_to_read/test.txt')