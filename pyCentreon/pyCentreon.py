from pprint import pprint
import requests

class CentreonApi(object):


    def __init__(self, centreon_url, username, password):
        self.base_url = "{}/centreon/api/index.php".format(centreon_url)

        url = "{}?action=authenticate".format(self.base_url)
        auth_token = requests.post(url, verify=False, data={'username':username, 'password':password}).json()['authToken']
        print("Auth token: {}".format(auth_token))
        self.headers = {
            'centreon-auth-token': auth_token,
        }

    def call(self, action, object, values=False):
         
        session = requests.Session()
        session.headers.update(self.headers)

        if values is False:
            body = {
                "action": action,
                "object": object.upper(),
            }
        else:
            body = {
                "action": action,
                "object": object.upper(),
                "values": values
            }

        url = "{}?action=action&object=centreon_clapi".format(self.base_url)
        print(url)
        response = session.post(url, json=body, verify=False)
        return response.json()
