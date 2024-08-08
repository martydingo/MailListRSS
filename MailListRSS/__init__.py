from office365.graph_client import GraphClient


class MailListRSS:
    def __init__(self, configuration) -> None:
        method = configuration["method"]
        self.configuration = configuration[method]

        if method == "office365":
            self.__setup_office365__()

    def __setup_office365__(self):
        self.client = GraphClient.with_client_secret(
            tenant=self.configuration["tenant_id"]
            client_id=self.configuration["client_id"]
            client_secret=self.configuration["client_secret"]
        )
