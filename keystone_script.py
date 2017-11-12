"""
script test - keystone federated.
"""
import logging
import sys
import requests
from mechanize import Browser

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import ssl
# https://dnaeon.github.io/disable-python-ssl-verification/
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


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

def submit_form(response):
    browser = Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    browser.open(response.url)
    browser.select_form(nr = 0)
    browser.form['username'] = USERNAME
    browser.form['password'] = PASSWORD
    browser.submit() 

    url_principal = browser.geturl()
    browser.open(url_principal)
    browser.select_form(nr = 0)
    print browser.response().read()
    browser.submit() 

    return browser 

def get_projects(token):
    headers = {'X-Auth-token': token}
    url = "http://10.7.49.47:5000/v3/OS-FEDERATION/projects"
    response = requests.get(url=url, verify=False, headers=headers)
    if response.status_code in (201, 200):
        logging.debug(" ### URL ### : " + response.url)
        return response
    else:
        logging.warning('ERROR (GET PROJECTS): ' + response.text)

def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))

if __name__ == "__main__":
    r = get_idp("http://10.7.49.47:5000", 'myidp', 'mapped')  
    # import pdb; pdb.set_trace()
    r = submit_form(r) 
    print r.response().read()

