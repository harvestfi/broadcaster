import requests


class EthparserAPI:

    ethparser_url = ""

    def __init__(self, ethparser_url) -> None:
        self.ethparser_url = ethparser_url

    def get_hardwork_history(self, from_date, to_date) -> str:
        payload = {"from": from_date, "to": to_date}
        r = requests.get(
            self.ethparser_url + "/api/transactions/history/hardwork", params=payload
        )
        return r.json()
