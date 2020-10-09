import pandas as pd

f = pd.read_csv("baptism_output.csv", low_memory=False)

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

new_f = f[keep_col].replace(to_replace=[r"\\t|\\n|\\r|\\f", "\t|\n|\r|\f"], value=[" ", " "],
                            regex=True)
# new_f = f[keep_col].replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n', ' ', regex=True)
# new_f = f[keep_col].replace({r'\\r': ' '}, regex=True)
# new_f = f[keep_col].replace('\\r', '\\n', regex=True)
# new_f = f[keep_col].replace('\\n', ' ', regex=True)
# print(f['URL':'Comments'])
# new_f = f[keep_col].replace('\\n', ' ', regex=True)
# print(new_f[['URL', 'Comments']])
# new_f = f
new_f.to_csv("x_bap.csv", index=False)
