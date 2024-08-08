from office365.graph_client import GraphClient
from pprint import pprint


class MailListRSS:
    def __init__(self, configuration) -> None:
        method = configuration["method"]
        self.configuration = configuration[method]

        if method == "office365":
            self.__setup_office365__()
            self.__poll_office365__()

    def __setup_office365__(self):
        self.client = GraphClient.with_client_secret(
            tenant=self.configuration["tenant_id"],
            client_id=self.configuration["client_id"],
            client_secret=self.configuration["client_secret"],
        )

    def __poll_office365__(self):
        messages = (
            self.client.users[self.configuration["inbox"]]
            .mail_folders[self.configuration["folder_id"]]
            .messages.get_all()
            .execute_query()
        )

        for message in messages:
            print(message.subject)
