from more_itertools import unique_everseen
with open('schools_data__completed_backup.csv', 'r') as f, open('schools_data__completed_333.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))
