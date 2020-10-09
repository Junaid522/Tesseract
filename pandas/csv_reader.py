import csv
import pandas as pd

keep_col = [
    'URL',
    'First Name',
    'Primary Surname',
    'Secondary Surname',
    'Father First Name',
    'Father Primary Surname',
    'Father Secondary Surname',
    'Mother First Name',
    'Mother Primary Surname',
    'Mother Secondary Surname',
    'Sacrament',
    'Date',
    'Comments',
    'Diocese',
    'Historical Territory',
    'Location',
    'Parish',
    'Funds'
]

# with open(r"baptism_output.csv", 'r') as f:
with open(r"baptism1.csv", 'r') as f:
    reader = csv.reader(f)
    count = 0
    reader_stack = []
    new_rows = []
    new_rows.append(keep_col)
    for row in reader:
        if row[0].__contains__('http:'):
            reader_stack.append(row)
            new_rows.append(row)
            # print(row)
            continue
        else:
            # print(row)
            if reader_stack:
                previous_item = reader_stack.pop()
                previous_item[-1] = previous_item[-1] + row[0]
                for r in range(len(row)):
                    if not r == 0:
                        previous_item.append(row[r])
                    else:
                        continue
            else:
                print('Empty')

    for row in new_rows:
        count += 1
    #     print(row)
    print('Count: ', count)

    df = pd.DataFrame(new_rows)
    df = df.drop(df.columns[[18, 19, 20, 21, 22]], axis=1)
    df.to_csv("x_bap.csv", index=False)
    # df.to_csv("x_bap1.csv", index=False)

