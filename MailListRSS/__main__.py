from argparse import ArgumentParser
from . import MailListRSS
from yaml import safe_load

argument_setup = ArgumentParser()
argument_setup.add_argument("-c", "--config", default="config.yaml")
arguments = argument_setup.parse_args()

configuration = safe_load(open(arguments.config))

mailListRSS = MailListRSS(configuration)
