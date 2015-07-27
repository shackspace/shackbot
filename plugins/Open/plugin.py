# -*- coding: utf-8 -*-
###
# Copyright (c) 2013, rixx
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

from urllib2 import urlopen
import json
import random

class Open(callbacks.Plugin):
    """.open and .close give the status of the stuttgart hackerspace
    reads http://shackspace.de/sopen/text/en"""

    def __init__(self, irc):
        self.__parent = super(Open, self)
        self.__parent.__init__(irc)
        self.dunno = ["shack is dunnolol", "I can't tell you if the shack is open or closed", \
            "shack is schroedinger's cat", "WARNING: HACKERSPACE STATE UNDEFINED", \
            "Sorry, you'll have to ask the Computer Force", "Can't help you, sorry", \
            "Old and unreliable hardware is old and unreliable; I can't help you."]

    def open(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is open
        """
        status = urlopen("http://portal.shack:8088/status").read()
        status = json.loads(status)
        
        if status['status'] == 'open':
            irc.reply("shack is open.", prefixNick=False)
        elif status['status'] == 'closed':
            irc.reply("shack is closed.", prefixNick=False)
        else:
            irc.reply(random.choice(self.dunno), prefixNick=False)
          
    open = wrap(open)

    def close(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is closed
        """
        irc.reply("You do not have permissions to close this hackerspace. This incident will be reported.", prefixNick=True)

    close = wrap(close)


Class = Open


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
