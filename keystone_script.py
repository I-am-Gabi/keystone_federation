"""
script test - keystone federated.
"""
import logging
import pdb
# import pdb; pdb.set_trace()
import sys
import requests
from mechanize import Browser

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(filename='logs/federation.log', level=logging.DEBUG)

USERNAME = "developer"
PASSWORD = "developerpass"

def get_idp(keystone_url, idp_id, protocol_id):
    """
    Get the idp page to login.
    """
    url = keystone_url + '/v3/OS-FEDERATION/identity_providers/{}/protocols/{}/auth'.format(idp_id, protocol_id) 
    response = requests.get(url=url, verify=False)
    if response.status_code in (201, 200): 
        return response
    else:
        print('ERROR (GET IDP): ' + response.text)

def submit_form_mechanize(response):
    br = mechanize.Browser()
    br.open(response.url)
    browser.select_form(nr = 0)
    browser.form['username'] = USERNAME
    browser.form['password'] = PASSWORD
    browser.submit()

def submit_form(response): 
    name = "developer"
    password = "developerpass" 

    payload = {'username': name, 'password': password}
    r = requests.post(response.url, payload, cookies=response.cookies) 
    return r 

def get_projects(token):
    headers = {'X-Auth-token': token}
    url = "https://10.7.49.47:5000/v3/OS-FEDERATION/projects"
    response = requests.get(url=url, verify=False, headers=headers)
    if response.status_code in (201, 200):
        logging.debug(" ### URL ### : " + response.url)
        return response
    else:
        logging.warning('GET PROJECTS ### ' + response.text)

def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))

if __name__ == "__main__":
    r = get_idp("https://10.7.49.47:5000", 'myidp', 'mapped') 

    # print r.headers['Set-Cookie'].split('PHPSESSID=')[1].split(';')[0]
    # print r.cookies
    r = submit_form(r) 
    # dump(r)
    print r.headers
    print r.content
    print r.cookies
    print r.url
    # print r.

