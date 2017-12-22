# ============================================================================
# FILE: sfservices.py
# AUTHOR: Rafał Toboła
# License: MIT license
# ============================================================================

from .base import Base

from os.path import exists
from subprocess import Popen, PIPE
import json


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sfservices'
        self.mark = '[SF]'
        self.filetypes = ['php']

        self.__cache = []

    def on_init(self, context):
        self.__make_cache(context)

    def on_event(self, context):
        self.__make_cache(context)

    def gather_candidates(self, context):
        return sorted(list(set(self.__cache)))

    def __make_cache(self, context):

        if exists('./app/console'):
            cmd = 'php ./app/console debug:container --format=json | grep -v \'//\''
        elif exists('./bin/console'):
            cmd = 'php ./bin/console debug:container --format=json | grep -v \'//\''
        else:
            return []

        output,error = Popen(cmd, shell=True, executable='/bin/bash', stdout=PIPE, stderr=PIPE).communicate()

        contdbg = json.loads(output)

        for sname in contdbg['definitions']:
            self.__cache.append(sname)
        for sname in contdbg['aliases']:
            self.__cache.append(sname)

        return self.__cache
