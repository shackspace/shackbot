# -*- coding: utf-8 -*-
###
# Copyright (c) 2013, rixx
# All rights reserved.
#
#
###

import random

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

from .stoll import stoll_quotes
from .glados import glados_quotes

class Stoll(callbacks.Plugin):
    """Add the help for "@plugin help Stoll" here
    This should describe *how* to use this plugin."""

    def __init__(self, irc):
        self.__parent = super(Stoll, self)
        self.__parent.__init__(irc)

    def stoll(self, irc, msg, args):
        """takes no arguments

        returns a helpful quote by Dr. Axel Stoll
        """
        irc.reply(random.choice(stoll_quotes) + " -- Dr. Axel Stoll(†)" ,
                prefixNick=False)
    stoll = wrap(stoll)


    def glados(self, irc, msg, args):
        """takes no arguments

        returns a helpful quote by GlaDOS
        """
        irc.reply(random.choice(glados_quotes) + " -- GlaDOS", prefixNick=False)
    glados = wrap(glados)





Class = Stoll


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
