from engine import private_api
class Checker:

    def __init__(self):
        pass

    def build(self, checker_type):
        if checker_type == 'private_api':
            return private_api.PrivateApi()