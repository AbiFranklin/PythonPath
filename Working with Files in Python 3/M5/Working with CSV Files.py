import csv

def read_csv_file(file_path, delimiter=','):
    """Reads a CSV file and returns its contents as a list of dictionaries."""
    with open(file_path) as csv_f:
        cnt = -1
        rows = csv.reader(csv_f, delimiter=delimiter)
        for r in rows:
            if cnt == -1:
                print(f'{" | ".join(r)}')
            else:
                print(f'{r[0]} | {r[1]} | {r[2]} | {r[3]}')
            cnt += 1
        print(f'Total rows: {cnt}')

read_csv_file('./Working with Files in Python 3/files_to_read/names.csv', ",")

def write_csv_file(fn, header, row):
    """Writes a single row to a CSV file."""
    with open(fn, 'w', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

write_csv_file('./Working with Files in Python 3/files_to_read/names_output.csv',
                ['first_name', 'last_name', 'age', 'city'],
                ['John', 'Doe', '30', 'New York'])
read_csv_file('./Working with Files in Python 3/files_to_read/names_output.csv', ",")

def append_csv_file(fn, row):
    """Appends a single row to a CSV file."""
    with open(fn, 'a', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)

append_csv_file('./Working with Files in Python 3/files_to_read/names_output.csv', ['Jane', 'Smith', '25', 'Los Angeles'])
read_csv_file('./Working with Files in Python 3/files_to_read/names_output.csv', ",")
