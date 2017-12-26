"""
This KU-Regis Python code is heavily
adapted from @Mameaw14's `ku-check-grade`

The original source code can be found
at https://github.com/mameaw14/ku-check-grade/
"""

import requests
import getpass
from bs4 import BeautifulSoup

session = requests.Session()

def login(username, password):
    """
    login to KU-Regis and store the session
    """
    payload = {'form_username': username,
        'form_password': password,
        'zone': '0'
    }
    memText = session.post('https://std.regis.ku.ac.th/_Login.php',
        data = payload)
    soup = BeautifulSoup(memText.text, 'lxml')
    name = soup.find('tr', id = '3')
    if len(name) == 0:
        return False
    return True

def get_ku20_html():
    """
    Get KU20 HTML page
    """
    attr = {
        'mode': 'KU20'
    }
    headers = {
        'Referer': 'https://std.regis.ku.ac.th/_Student_Registration.php',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101'
    }
    regis = session.get('https://std.regis.ku.ac.th/_Student_RptKu.php?',
        params = attr,
        headers = headers
    )
    return regis.text
