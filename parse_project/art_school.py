import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

company_url = 'http://artschoollviv.info/'


def art_school_site_parse(company_url, headers):
    session = requests.Session()
    request = session.get(company_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        result = create_dict_with_info_from_site(soup)
        return result
    else:
        return f'Error: {request.status_code}'


def create_dict_with_info_from_site(soup):
    art_school_dict = {'company_name': parse_name(soup),
                       'href': company_url,
                       'styles': parse_styles(soup),
                       'prices': parse_prices(soup),
                       'address': parse_address(soup)}
    return art_school_dict


def parse_name(soup):
    company_name = soup.find('p', {'id': 'u8724-2'}).text
    return company_name


def parse_styles(soup):
    div_ids = ['u2261-4', 'u2262-4', 'u2263-4', 'u2264-4', 'u2273-4', 'u2274-4', 'u11567-4']
    styles = ''
    for div_id in div_ids:
        style = soup.find('div', {'id': div_id}).text.lstrip()
        styles += style
    return styles


def parse_prices(soup):
    price_1 = soup.find('h2', {'id': 'u2920-3'}).text
    price_2 = soup.find('span', {'id': 'u2920-4'}).text
    prices = price_1 + ' ' + price_2
    prices = prices[0] + prices[1:].lower()
    return prices


def parse_address(soup):
    address_list = []
    address_div = soup.find('div', {'data-muse-uid': 'U2926'})
    address_elements = address_div.find_all('p')
    for address_element in address_elements:
        address_list.append(address_element.text.lstrip())
    address = '\n'.join(address_list)
    return address


if __name__ == '__main__':
    result = art_school_site_parse(company_url, headers)
    print(result)
