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

import random

class Insult(callbacks.Plugin):
    """Add the help for "@plugin help Insult" here
    This should describe *how* to use this plugin."""

    def __init__(self, irc):
        self.__parent = super(Insult, self)
        self.__parent.__init__(irc)

    def insult(self, irc, msg, args, nick):
        """<nick>

        insults the given nick
        """

        irc.reply(nick + ", " + self.get_insult(), prefixNick=False)

    insult = wrap(insult, ['nickInChannel'])


    def get_insult(self):
        return "thou art a " + random.choice(adjective_1) + " " + \
        random.choice(adjective_2) + " " + random.choice(noun) + "!"

Class = Insult


# insults are taken from http://www.pangloss.com/seidel/shake_rule.html
adjective_1 = [
  "artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered",
  "clouted", "craven", "currish", "dankish", "dissembling", "droning",
  "errant", "fawning", "fobbing", "froward", "frothy", "gleeking", "goatish",
  "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded",
  "lumpish", "mammering", "mangled", "mewling", "paunchy", "pribbling",
  "puking", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy",
  "spleeny", "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed",
  "villainous", "warped", "wayward", "weedy", "yeasty",
    ]

adjective_2 = [
  "base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained",
  "clapper-clawed", "clay-brained", "common-kissing", "crook-pated",
  "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted",
  "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed",
  "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping",
  "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed",
  "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered",
  "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep", "pox-marked",
  "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne",
  "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited",
  "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten"
    ]

noun = [
  "apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear",
  "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb",
  "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench",
  "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard",
  "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster",
  "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant",
  "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock",
  "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal",
  "whey-face", "wagtail"
    ]

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
