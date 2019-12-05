import requests  # HTTP request simulator library
from bs4 import BeautifulSoup as bs  # a library that helps to parse the response we get from the server
# to simulate browser actions
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

company_url = 'https://vangogh.lviv.ua/'


def vangogh_site_parse(company_url, headers):
    session = requests.Session()  # we create the illusion of user continuity working
    request = session.get(company_url, headers=headers)  # to simulate opening a page in a browser
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')  # to provide a readable server response
        result = create_dict_with_info_from_site(soup)
        return result
    else:
        return f'Error: {request.status_code}'


def create_dict_with_info_from_site(soup):
    vangog_dict = {'company_name': parse_name(soup),
                   'href': company_url,
                   'styles': parse_styles(soup),
                   'prices': parse_prices(soup),
                   'address': parse_address(soup)}
    return vangog_dict


def parse_name(soup):
    company_name = soup.find('title').text
    return company_name


def parse_styles(soup):
    styles_list = []
    style_divs = soup.find_all('div', attrs={'class': 'problems_list_item design_text design_rest'
                                                      '_colors_border_nh design_rest_colors_border_nh-bf two_items'})
    for div in style_divs:
        style = div.find('strong').text
        styles_list.append(style)
    styles = '\n'.join(styles_list)
    return styles


def parse_prices(soup):
    prices = soup.find('div', attrs={'class': 'row design_inner_title_middle bg_reverce_color_col'}).text.strip('\n')
    return prices


def parse_address(soup):
    address_div = soup.find('div', attrs={'class': 'address'})
    address = address_div.find('p').text
    return address


if __name__ == '__main__':
    result = vangogh_site_parse(company_url, headers)
    print(result)
