import csv
import requests
import favicon

headers = {'User-agent': 'Mozilla/5.0'}


def get_icon(url, row, index, writer, out_file):
    icons = favicon.get(url)
    print(icons)
    print('INDEX***', index)
    for n, i in enumerate(icons):
        response = requests.get(i.url, stream=True, headers=headers)
        if response.status_code != 200 or i.url.endswith('.com/') or i.url.endswith('.com') or i.url.endswith('.edu/')\
                or i.url.endswith('.edu'):
            continue
        name = i.url.split('/')[-1]
        if name.__contains__('?'):
            name = name.split('?')[0]
        print(name)
        with open('fbs_fcs_missing/{}_{}.{}'.format(index, index, name), 'wb') as image:
            for chunk in response.iter_content(1024):
                image.write(chunk)
        row.append('{}_{}.{}'.format(index, index, name))
        writer.writerow(row)
        out_file.flush()
        break


with open('fbs_fcs_missing.csv', 'r') as f, open('fbs_fcs_missing_data_favicon.csv', 'w') as out_file:
    reader = csv.reader(f)
    writer = csv.writer(out_file)
    for index, row in enumerate(reader):
        # index += 500

        # if index == 0:
        #     row.append('Primary Icon')
        #     writer.writerow(row)
        #     out_file.flush()
        #     continue
        # if index > 923:
        # else:
        print(index)
        try:
            if row[12].endswith('.edu/') or row[12].endswith('.edu'):
                url_string = row[11]
                url = '{}{}'.format('http://', url_string)
                print('IF URL :', url)
            elif row[11].endswith('.edu/') or row[11].endswith('.edu'):
                url_string = row[12]
                url = '{}{}'.format('http://', url_string)
                print('ELIF URL :', url)
            else:
                url_string = row[11]
                url = '{}{}'.format('http://', url_string)
                print('ELSE URL :', url)
            get_icon(url, row, index, writer, out_file)

        except Exception as e:
            print(str(e))
            print(row)
            try:
                if row[11] == url.replace('http://',''):
                    url_string = row[12]
                    url = '{}{}'.format('http://', url_string)
                else:
                    url_string = row[11]
                    url = '{}{}'.format('http://', url_string)

                get_icon(url, row, index, writer, out_file)
            except:
                row.append('')
                writer.writerow(row)
                out_file.flush()
            continue
out_file.close()
f.close()
