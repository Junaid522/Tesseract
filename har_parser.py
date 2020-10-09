import ast
import json
import csv
from bs4 import BeautifulSoup
from haralyzer import HarParser


with open('../../Downloads/public.tableau.com_base_6.har', 'r') as f:
# with open('../../Downloads/tahir-data/public.tableau.com_two.har', 'r') as f:
# with open('../../Downloads/men_baseball/3-harib-mensbaseball.har', 'r') as f:
# with open('../../Downloads/men_baseball/13full-harib-mensbaseball.har', 'r') as f:
# with open('../../Downloads/soccer/mens_soccer_6.har', 'r') as f:
# with open('../../Downloads/soccer/mens_soccer_8.har', 'r') as f:
# with open('../../Downloads/soccer/mens_soccer_15.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))
tree_list = []
for page in har_parser.pages:
    for index, entry in enumerate(page.entries):
        if har_parser.match_request_type(entry, 'POST'):
            text_str = str(entry.get('response').get('content').get('text'))
            if text_str.__contains__('School Name:') and not text_str.__contains__('518965;'):
                data = json.loads(text_str.strip())
                # data = text_str
                # import pdb;pdb.set_trace()
                # data = text_str
                # data = ast.literal_eval(entry.get('response').get('content').get('text'))
                print(text_str)
                cmdResultList = data.get('vqlCmdResponse').get('cmdResultList')
                print(cmdResultList)
                for index, i in enumerate(cmdResultList):
                    # try:
                    dict_data = {}
                    # command_items = json.loads(i.get('commandReturn').get('tooltipText')).get('actions').get('commandItems')

                    if i.get('commandReturn'):
                        dict_data['tooltip'] = i.get('commandReturn')
                        # print(i.get('commandReturn'))
                        tooltip_text = dict_data.get('tooltip').get('tooltipText')
                        if tooltip_text:
                            tooltip_text = json.loads(tooltip_text)
                            print(tooltip_text)
                            tooltip = tooltip_text.get('htmlTooltip')
                            dict_data['tooltip'] = tooltip
                            print(tooltip)
                            command_items = tooltip_text.get('actions').get('commandItems')
                            cmd_list = []
                            for index, cmd in enumerate(command_items):
                                cmd_list.append(cmd.get('name'))
                            dict_data['links'] = cmd_list
                            tree_list.append(dict_data)
                    # except:
                    #     print('Nothing')

updated = [i for n, i in enumerate(tree_list) if i not in tree_list[n + 1:]]
data_list = []
fieldnames = []
for index, i in enumerate(updated):
    bs = BeautifulSoup(i.get('tooltip'), 'lxml')
    all_td = bs.find_all('td')
    data = {}
    data[all_td[0].text.replace(':', '')] = all_td[2].text
    data[all_td[3].text.replace(':', '')] = all_td[5].text
    data[all_td[6].text.replace(':', '')] = all_td[8].text
    data[all_td[9].text.replace(':', '')] = all_td[11].text
    data[all_td[12].text.replace(':', '')] = all_td[14].text
    data[all_td[15].text.replace(':', '')] = all_td[17].text
    data[all_td[18].text.replace(':', '')] = all_td[20].text
    data[all_td[21].text.replace(':', '')] = all_td[23].text
    data[all_td[24].text.replace(':', '')] = all_td[26].text
    data[all_td[27].text.replace(':', '')] = all_td[29].text
    data[all_td[30].text.replace(':', '')] = all_td[32].text
    data['Primary URL'] = i.get('links')[0]
    data['Secondary URL'] = i.get('links')[1]
    data_list.append(data)
    if index == 0:
        fieldnames = [all_td[0].text.replace(':', ''), all_td[3].text.replace(':', ''), all_td[6].text.replace(':', ''),
                      all_td[9].text.replace(':', ''), all_td[12].text.replace(':', ''), all_td[15].text.replace(':', ''),
                      all_td[18].text.replace(':', ''), all_td[21].text.replace(':', ''), all_td[24].text.replace(':', ''),
                      all_td[27].text.replace(':', ''),
                      all_td[30].text.replace(':', ''), 'Primary URL', 'Secondary URL']

with open('fbs_fcs_missing.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   # writer.writeheader()
    writer.writerows(data_list)
