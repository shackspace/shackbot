# -*- coding:utf-8 -*-
###
# Copyright (c) 2014, rixx
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


from urllib2 import urlopen
from datetime import date, timedelta

class Plenum(callbacks.Plugin):
    """Add the help for "@plugin help Plenum" here
    This should describe *how* to use this plugin."""

    def __init__(self, irc):
        self.__parent = super(Plenum, self)
        self.__parent.__init__(irc)

    def plenum(self, irc, msg, args):
        """ takes no arguments

        prints date and URL of the next shackspace plenum"""
        datum = self.get_plenum_date()
        delta = (datum - date.today()).days

        if delta == 0:
            reply_string = "Heute ist Plenum!"
        else:
            reply_string = "Das nächste Plenum ist in " + str(delta) + " Tagen, "
            reply_string += "am " + datum.strftime("%d.%m.")

        irc.reply(reply_string, prefixNick=False)

    plenum = wrap(plenum)

    def plenumlink(self, irc, msg, args):
        """ takes no arguments

        prints URL to the next plenum protocol"""

        irc.reply(urlopen('http://shackspace.de/nextplenum/http300/current').geturl(),\
                  prefixNick=False)

    plenumlink = wrap(plenumlink)

    def get_plenum_date(self):
        raw = urlopen("http://shackspace.de/nextplenum/text/iso").read()[:10]
        plenum_date = date(int(raw[:4]), int(raw[5:7]), int(raw[8:10]))

        return plenum_date

Class = Plenum


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
