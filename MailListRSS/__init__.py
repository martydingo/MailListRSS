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
            .messages.get()
            .execute_query()
        )

        for message in messages:
            try:
                mailingListSubjectList = message.subject.split("[")[1].split("]")
                mailingListTopic = mailingListSubjectList[0]
                mailingListSubject = (
                    mailingListSubjectList[1].replace("Re:", "").strip()
                )
            except:
                mailingListTopic = "Unknown"
                mailingListSubject = message.subject

            id = message.webLink
            title = mailingListSubject
            subtitle = mailingListTopic
            auther = {
                "name": message.sender.emailAddress.name,
                "email": message.sender.emailAddress.address,
            }
            # print(mailingListTopic)
            # print(mailingListSubject)
