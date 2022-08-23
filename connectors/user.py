import requests

from connectors.base import BaseConnector
#from apps.core_gateway.models.site_configuration import SiteConfiguration


class UserConnector(BaseConnector):
    """
    Connector to API source_data
    """

    def __init__(self, params):
        super(UserConnector, self).__init__(
            params
        )

    def get_user_data(self, **kwargs):
        url = str(self.base_url) + str('users/')
        try:
            result = requests.get(url, params=self.params)
            if result.status_code != 200:
                if result.status_code == 401:
                    status, response = self.getAuth()
                    if status == 200:
                        self.get_users()
                    return status, {'errors': [{
                        'message': 'error auth core',
                        'code': status
                    }]}
                return result.status_code, result.json()
            return result.status_code, result.json()
        except ConnectionError:
            return 400, {'errors': [{
                'message': 'Error connection',
                'code': 400
            }]}
        except Exception:
            return 400, {'errors': [{
                'message': 'Error in core',
                'code': 400
            }]}