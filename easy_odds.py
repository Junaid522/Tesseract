import csv
import random
import sys
from bs4 import BeautifulSoup
import requests

session_requests = requests.session()
desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']


def random_headers():
    return {'User-Agent': random.choice(desktop_agents), }


def extract_data(page_url, output_file_name):
    try:
        result = session_requests.get(
            page_url,
            headers=random_headers(),
        )
        if result.ok and result.status_code == 200:
            table_list = []
            header_list = ['Book Maker']
            book_maker_list = []
            soup = BeautifulSoup(result.content, "lxml")
            book_maker_table = soup.find('table', attrs={'id': 'legendTable'})
            table_body = book_maker_table.find('tbody')
            all_book_maker_trs = table_body.find_all('tr')
            for row in all_book_maker_trs:
                book_maker_name = ""
                book_maker_number = ""
                book_maker_number_span = row.find('span', attrs={'class': 'racecard-number'})
                if book_maker_number_span:
                    book_maker_number = str(book_maker_number_span.text).strip()

                book_maker_name_span = row.find('span', attrs={'class': 'racecard-selection'})
                if book_maker_name_span:
                    book_maker_name = str(book_maker_name_span.text).strip()
                if book_maker_name:
                    book_maker_num_and_name = "{0} | {1}".format(book_maker_number, book_maker_name)
                    book_maker_list.append(book_maker_num_and_name)
                    print(book_maker_num_and_name)

            bets_table = soup.find('table', attrs={'id': 'betsTable'})
            bet_companies_row = bets_table.find('tr', attrs={'class': 'tr-bookmakers'})
            all_companies_headings = bet_companies_row.find_all('th')
            for company_heading in all_companies_headings:
                company_name = str(company_heading.find('span').text).strip()
                header_list.append(company_name)
                print(company_name)

            table_list.append(header_list)
            bet_data_body = bets_table.find('tbody')
            all_bet_data_rows = bet_data_body.find_all('tr')
            for i in range(len(book_maker_list)):
                row_list = [book_maker_list[i]]
                current_data_row = all_bet_data_rows[i]
                all_columns = current_data_row.find_all('td')
                for company_column in all_columns:
                    odd_div = company_column.find('div', attrs={'class': 'oddsValue'})
                    odd_value = ""
                    if odd_div:
                        odd_value = str(odd_div.text).strip()
                    else:
                        odd_value = company_column.text
                    row_list.append(odd_value)
                print(row_list)
                table_list.append(row_list)
            with open(output_file_name, "w") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerows(table_list)
                # print(table_list)

    except Exception as es:
        print(str(es))


if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print("Invalid command: Please run script command using following format")
            print("python main.py input_url output_file_name.csv")
        else:
            url = sys.argv[1]
            file_name = sys.argv[2]
            extract_data(url, file_name)
    except Exception as e:
        print(str(e))
