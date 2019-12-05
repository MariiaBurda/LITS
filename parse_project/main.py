import csv

from vangogh import vangogh_site_parse
from art_school import art_school_site_parse
from marko_school import marko_school_site_parse

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

vangogh_company_url = 'https://vangogh.lviv.ua/'
art_school_company_url = 'http://artschoollviv.info/'
marko_school_company_url = 'http://www.markoart-school.com.ua/majster-klasy/'


dict_with_info_from_vangogh_site = vangogh_site_parse(vangogh_company_url, headers)
dict_with_info_from_art_school_site = art_school_site_parse(art_school_company_url, headers)
dict_with_info_from_marko_school_site = marko_school_site_parse(marko_school_company_url, headers)


def write_title_in_csv():
    with open('paint_classes_lv.csv', 'w') as file:
        doc = csv.writer(file)

        doc.writerow(('Студія', 'URL', 'Стилі', 'Ціни', 'Адреса'))


def write_info_in_csv(data):
    with open('paint_classes_lv.csv', 'a') as file:
        doc = csv.writer(file)

        doc.writerow((data['company_name'],
                      data['href'],
                      data['styles'],
                      data['prices'],
                      data['address']))


if __name__ == '__main__':
    write_title_in_csv()
    write_info_in_csv(dict_with_info_from_vangogh_site)
    write_info_in_csv(dict_with_info_from_art_school_site)
    write_info_in_csv(dict_with_info_from_marko_school_site)
