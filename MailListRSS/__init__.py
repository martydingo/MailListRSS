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
        # messages = (
        #     self.client.users[self.configuration["inbox"]]
        #     .messages.get()
        #     # .filter("ccRecipients/any(i:i ')")
        #     .filter("startswith(subject, '[DNSOP]')")
        #     .top(1)
        #     .execute_query()
        # )
        # messages = (
        #     self.client.users[self.configuration["inbox"]]
        #     .mail_folders[
        #         "AAMkADcxYzY4ODFkLTY1MDYtNGMyNi04MmNmLTg4YTU0Mjg3OGJmYgAuAAAAAABiSP8jCFYLSZrBWYpeHWpYAQBbd8M1_CGsQ63mmDqKE8XTAAPDml8ZAAA="
        #     ]
        #     .child_folders.get_all()
        #     .execute_query()
        # )
        messages = (
            self.client.users[self.configuration["inbox"]]
            .mail_folders[
                "AAMkADcxYzY4ODFkLTY1MDYtNGMyNi04MmNmLTg4YTU0Mjg3OGJmYgAuAAAAAABiSP8jCFYLSZrBWYpeHWpYAQBbd8M1_CGsQ63mmDqKE8XTAAPDml8aAAA="
            ]
            .messages.get()
            .execute_query()
        )

        print(messages.to_json())
