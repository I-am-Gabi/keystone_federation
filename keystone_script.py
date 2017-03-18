"""
script test - keystone federated.
"""
import logging
import sys
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(filename='logs/federation.log', level=logging.DEBUG)

def get_url_idp(keystone_url, idp, prot):
    """
    method to get unscoped token
    """
    url = keystone_url+'/v3/OS-FEDERATION/identity_providers/{}/protocols/{}/auth'.format(idp, prot)
    # cert = '/Users/gabriela/Documents/ufrn/projeto/keystone_script/certs/domain.crt'
    # key = '/Users/gabriela/Documents/ufrn/projeto/keystone_script/certs/domain.key'
    # response = requests.get(url=url, verify=False, cert=(cert, key))
    response = requests.get(url=url, verify=False)
    print response.headers
    if response.status_code in (201, 200): 
        return response.url
    else:
        print('ERROR GET URL IDP: ' + response.text)

def submit_login(url):
    """
    method to submit form
    """
    name = "developer"
    password = "developerpass"
    data = {"username" : name, "password": password}
    response = requests.post(url, data=data)
    print response.status_code

def get_projects(token):
    headers = {'X-Auth-token': token}
    url = "https://10.7.49.47:5000/v3/OS-FEDERATION/projects"
    response = requests.get(url=url, verify=False, headers=headers)
    if response.status_code in (201, 200):
        logging.debug(" ### URL ### : " + response.url)
        return response
    else:
        logging.warning('ORG INFO ### ' + response.text)


if __name__ == "__main__":
    # logging.debug(' ### START ###')
    url_idp = get_url_idp("https://10.7.49.47:5000", 'myidp', 'mapped')
    # print submit_login(url_idp)
    
    # token = get_projects("53fe371cd87e8ea6f398d154b11aa8dd6cdc24db")
