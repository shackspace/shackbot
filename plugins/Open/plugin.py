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
    """Add the help for "@plugin help Stoll" here
    This should describe *how* to use this plugin."""

    def __init__(self, irc):
        self.__parent = super(Open, self)
        self.__parent.__init__(irc)

    def open(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is open
        """
        if "open" in self.get_shack_status():
            irc.reply("shack is open", prefixNick=False)
        else:
            irc.reply("shack is not open", prefixNick=False)

    open = wrap(open)

    def close(self, irc, msg, args):
        """takes no arguments

        tells you whether the shack is closed
        """
        if "close" in self.get_shack_status():
            irc.reply("shack is closed", prefixNick=False)
        else:
            irc.reply("shack is not closed", prefixNick=False)

    close = wrap(close)

    def get_shack_status(self):
        return urlopen("http://shackspace.de/sopen/text/en").read()
        

Class = Open


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
