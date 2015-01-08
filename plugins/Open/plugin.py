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

class Open(callbacks.Plugin):
    """.open and .close give the status of the stuttgart hackerspace
    reads http://shackspace.de/sopen/text/en"""

    def __init__(self, irc):
        self.__parent = super(Open, self)
        self.__parent.__init__(irc)

    def open(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is open
        """
        status = urlopen("http://shackspace.de/sopen/text/en").read()
        
        if "open" in status:
            irc.reply("shack is closed", prefixNick=False)
        elif "closed" in status:
            irc.reply("shack is not closed", prefixNick=False)
          
    open = wrap(open)

    def close(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is closed
        """
        irc.reply("You do not have permissions to close this hackerspace. This incident will be reported.", prefixNick=True)


    close = wrap(close)

    def is_open(self):
        return "open" in urlopen("http://shackspace.de/sopen/text/en").read()
        

Class = Open


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
