from geopy.geocoders import Nominatim

from opencage.geocoder import OpenCageGeocode
geolocator = Nominatim(user_agent="https")

STATE_CHOICES = {'AL': 'Alabama', 'AK': 'Alaska', 'AS': 'American Samoa', 'AZ': 'Arizona', 'AR': 'Arkansas', 'AA': 'Armed Forces Americas', 'AE': 'Armed Forces Europe', 'AP': 'Armed Forces Pacific', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'MP': 'Northern Mariana Islands', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VI': 'Virgin Islands', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}


import csv
import us
long_lat_list = []
long_lat = {}
key = '9b9dbd3eb1154494b6db6f5969b2dcb5'  # get api key from:  https://opencagedata.com
# key = 'aa124a5d2a494586b470b7548898c405'  # get api key from:  https://opencagedata.com
# geocoder = OpenCageGeocode(key)
# results = geocoder.geocode('Malibu, CA')
# for r in results:
#     print(r)

with open('fbs_fcs_missing_data_favicon.csv', 'r') as f, open('fbs_fcs_missing_lat_long_1.csv', 'w') as out_file:
    reader = csv.reader(f)
    csv_writer = csv.writer(out_file)
    for index, row in enumerate(reader):
       # print(row[-6])
       #  if index == 0:
            # row.append('State')
            # row.append('State Code')
            # row.append('Updated Latitude')
            # row.append('Updated Longitude')
            # csv_writer.writerow(row)
        # if index > 933:
        # else:
        print(row[10])
        state = STATE_CHOICES.get((row[10].split(',')[1].strip()))
        city = row[10].split(',')[0].strip()
        print(city, state)
        location = geolocator.geocode(row[10].split(',')[0].strip() + ', ' + state)
        print(location.latitude, location.longitude)
        row.append(location.latitude)
        row.append(location.longitude)
        csv_writer.writerow(row)
            # print(row[-6].split(',')[1])
            # print(us.states.lookup(row[-6].split(',')[1]))
            # results = geocoder.geocode(row[-6])
            # for r in results:
            #     print(r.get('components').get('country'))
            #     if r.get('components').get('country') == 'United States of America':
            #         row.append('United States of America')
            #         row.append(r.get('components').get('state'))
            #         row.append(r.get('components').get('state_code'))
            #         row.append(r.get('geometry').get('lng'))
            #         row.append(r.get('geometry').get('lat'))
            #         csv_writer.writerow(row)
            #         break



# import csv
# data_in = 'schools_data__completed_new_34.csv'
# data_out = 'schools_data__completed_new_34_new.csv'
# with open(data_in, 'r', newline='') as in_file, open(data_out, 'w', newline='') as out_file:
#     reader = csv.reader(in_file)
#     writer = csv.writer(out_file)
#     seen = set()
#     for row in reader:
#         row = tuple(row)
#         if row in seen: continue
#         seen.add(row)
#         writer.writerow(row)

# remove duplicates from csv
# import pandas as pd
#
# df = pd.read_csv('schools_updated.csv')
# df_clean = df.drop_duplicates(subset=['School Name'], keep='last')
# print(df_clean)
#
# df_clean.to_csv('updated_csv.csv', index=False)


# import csv
# import os
#
# import favicon
# import requests
#
# import favicon
#
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# headers = {'User-Agent': user_agent}
#
# with open('schools_data__completed.csv', 'r') as f, open('updted_data_new.csv', 'w') as out_file:
#     reader = csv.reader(f)
#     writer = csv.writer(out_file)
#     for index, row in enumerate(reader):
#         if index == 0:
#             row.append('Primary Icon')
#             writer.writerow(row)
#             out_file.flush()
#             continue
#         if index < 401:
#             url = row[11]
#             if not url.startswith('http://'):
#                 url = '{}{}'.format('http://', url)
#             print(url)
#             try:
#                 # icons = favicon.get(url)
#                 icons = favicon.get(url, headers=headers, timeout=2)
#                 print('INDEX***', index)
#                 # for i in icons:
#                 response = requests.get(icons[-1].url, stream=True)
#                 name = icons[-1].url.split('/')[-1]
#                 if name.__contains__('?'):
#                     name = name.split('?')[0]
#                 print(name)
#                 if icons[-1].format:
#                     with open('tmp/{}.{}.{}'.format(index, name, icons[-1].format), 'wb') as image:
#                         for chunk in response.iter_content(1024):
#                             image.write(chunk)
#                 else:
#                     with open('tmp/{}.{}.{}'.format(index, name, '.png'), 'wb') as image:
#                         for chunk in response.iter_content(1024):
#                             image.write(chunk)
#
#                 row.append('{}.{}.{}'.format(index, name, icons[-1].format))
#                 writer.writerow(row)
#                 out_file.flush()
#             except:
#                 print('Nothing')
#                 row.append('')
#                 writer.writerow(row)
#                 out_file.flush()
#                 continue
#
# out_file.close()
# f.close()
