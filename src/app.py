#!/usr/bin/python

import logging
import sys
import traceback

from const.exit_status import ExitStatus


class App:
    def __init__(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    try:
        app = App()
        app.run()
        sys.exit(ExitStatus.SUCCESS)
    except Exception:
        logging.exception(traceback.format_exc())
        sys.exit(ExitStatus.FAIL)
