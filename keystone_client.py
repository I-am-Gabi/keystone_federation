from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

import logging
import sys
logging.basicConfig(filename='logs/keystone.log', level=logging.DEBUG)


KEYSTONE_ENDPOINT = "https://10.7.49.47:5000/v3"

def auth_keystone():
	logging.debug('authentication keystone')
	auth = v3.Password(auth_url=KEYSTONE_ENDPOINT, 
		username="admin", 
		password="admin", 
		project_name="admin", 
		user_domain_id="bea2ef5b95c54584947a43ab53f1e3ba", 
		project_domain_id="bea2ef5b95c54584947a43ab53f1e3ba")

	sess = session.Session(auth=auth, verify=False) 
	keystone = client.Client(session=sess, version=(3,))  
	return keystone, sess


def get_projects_list(keystone):
	return keystone.projects.list()

def get_unscoped_token(session):
	get_auth_data(session, auth, headers)

def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))

if __name__ == "__main__":
	ks, session = auth_keystone()
	get_projects_list(ks)
	
# tive que add controller aos meus hosts