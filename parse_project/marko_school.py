import requests
from bs4 import BeautifulSoup as bs
import re

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

company_url = 'http://www.markoart-school.com.ua/'
master_klasy_url = 'http://www.markoart-school.com.ua/majster-klasy/'
address_url = 'http://www.markoart-school.com.ua/kontakty/'


def marko_school_site_parse(master_klasy_url, headers):
    session = requests.Session()
    request = session.get(master_klasy_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        result = create_dict_with_info_from_site(soup)
        return result
    else:
        return f'Error: {request.status_code}'


def create_dict_with_info_from_site(soup):
    marko_school_dict = {'company_name': parse_name(soup),
                         'href': company_url,
                         'styles': parse_styles(soup),
                         'prices': parse_prices(soup),
                         'address': parse_address(address_url, headers)}
    return marko_school_dict


def parse_name(soup):
    company_name = soup.find('a', attrs={'class': 'site-title site-logo-text'}).text
    return company_name


def parse_styles(soup):
    styles_list = []
    styles = soup.find_all('h3')
    for style in styles:
        one_style = style.text
        one_style = one_style.upper()
        one_style = one_style[0] + one_style[1:].lower()
        styles_list.append(one_style)
    styles = '\n'.join(styles_list)
    return styles


def parse_prices(soup):
    prices_list = []
    prices_res_list = []
    prices = soup.find_all('p', attrs={'class': 'elementor-image-box-description'})
    for price in prices:
        one_price = price.text.replace('\n', ' ')
        prices_list.append(one_price)
    for i in range(len(prices_list)):
        prices_elem = re.findall(r'Тривалість.+', prices_list[i])
        prices_fin_elem = ' '.join(prices_elem)
        prices_res_list.append(prices_fin_elem)
    prices_fin = '\n'.join(prices_res_list)
    return prices_fin


def parse_address(address_url, headers):
    session = requests.Session()
    request = session.get(address_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')

        address = soup.find('p', attrs={'style': 'text-align: center;'}).text
        return address


if __name__ == '__main__':
    result = marko_school_site_parse(master_klasy_url, headers)
    print(result)
