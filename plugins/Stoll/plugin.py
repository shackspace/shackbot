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
        irc.reply(random.choice(stoll_quotes) + " -- Dr. Axel Stoll")
    stoll = wrap(stoll)


    def glados(self, irc, msg, args):
        """takes no arguments

        returns a helpful quote by GlaDOS
        """
        irc.reply(random.choice(glados_quotes) + " -- GlaDOS")
    glados = wrap(glados)



stoll_quotes = [
    "Allerdings muss ich gleich sagen: Bei mir beginnt die Mathematik, Physik und auch Geologie dort, wo das Hochschulstudium aufhört.",
    "Medizin ist Mathematik, Biologie ist Physik!",
    "Magie ist Physik durch Wollen!",
    "Der Mensch ist eine energetische Matrix.",
    "Der menschliche Zellkern ist gleich pures Licht, sprich: schwarze Sonnen.",
    "Wenn ein Mensch autogen sein Kraftfeld verstärkt, könnte er im Extremfall schweben. Also levitieren.",
    "Die Sonne ist KALT, da staunt ihr, wa?",
    "Wer weiß das? ... Wieder keiner!",
    "Im Prinzip brauchen wir nur drei Wissenschaften, um alles zu beschreiben: Physik. Mathematik. Philosophie.",
    "Und die Russen sind ja Waffentechnisch den Amerikanern weit überlegen. MUSS MAN WISSEN!",
    "...und das ist auch die Maschine, die entscheidend ist für Freie-Energie-Maschinen. Die muss man anzapfen entsprechend einem Implosions-Strudel. Das heißt, eine logarithmische Spirale raum-zeitlich betrachtet nach INNEN.",
    "Es gibt keine Zufälle, Das Wort 'Zufall' ist aus meinem Wortschatz gestrichen",
    "96 Flugzeuge * 60 Minuten * 14 Stunden * 40 Passagiere ergibt: 3.225.600 Passagiere pro Tag. PRO TAG! Das ist kein Science Fiction.",
    "Das hier ist nichts anderes als ein Strafplanet",
    "Der Selbsterhaltungstrieb der Zelle. Zur Erinnerung: [Die Zelle] ist ein Perpetuum Mobile, wie das Universum auch, ist ja klar.",
    "Wiederholung ist die Mutter der Weisheit",
    "Seit 10 Jahren wird der T-92 hergestellt. Ein modernster Panzer, russische Panzer mit Spitzengeschwindigkeit von 300 km/h",
    "Das Wort Zufall ist aus meinem Wortschatz gestrichen.",
    "Nukleare Strahlung lässt sich neutralisieren",
    "Magie ist Physik durch Volt",
    "Nikolai Tesla ist innerhalb von 5 Stunden mit deutschen Physikern zum Pluto geflogen um Gesteinsproben zu sammeln",
    "Man sollte mal Mikrowellenstrahler gegen die Love Parade einsetzen",
    "Es existiert keine Materie so wie diese beschrieben wird. Es existiert nur Bewegung oder Geschwindigkeit oder Schwingungen.",
    "Internet ist scheiße, da geh ich nicht rein",
    "Es existiert keine Materie, so wie diese gesehen und beschrieben wird, denn wir leben in einer Welt der Schwingungen und Frequenzen, also korrelierender Wirbelmechanismen",
    "Im Prinzip kann man sogar soweit abstrahieren: 'Alles ist nur Bewegung, Geschwindigkeit oder Schwingungen'",
    "Bindekräfte, welche die Materie zusammenhalten, sind Wirbel bzw. Strudel, inklusive ihrer Ein- und Auswirbelungen",
    "Die Formel E = mc² ist in dieser Form falsch bzw. wird zumindest falsch verstanden!",
    "Die reinste aller Energieformen, das Licht, ist ein Element es Jenseitsraumes, auch wenn es in die materielle Welt hineinwirkt.",
    "Die Zeit ist gekommen, da die Menschheit darüber bescheid wissen muss, was einige Wenige -- aus niederen Beweggründen -- seit sehr langer Zeit verschweigen.",
    "Das Wort 'Kosmos' bedeutet ja zu deutsch letztlich auch nichts anderes als: Ordnung.",
    "Tachyoneutrinos beinhalten den Terminus Tachyon(en) und Neutrino(s). Ersterer enthält die wichtige limitierende physikalische Größe Zeit und Geschwindigkeit (=Bewegung) und letzterer einen 'Schwingungs-Frequenz-Wirbelquant'!",
    "Ein Atom z.B. ähnelt nicht nur einer Sprungfeder, sondern es verfügt auch über ähnliche Eigenschaften, außer dass es mit hoher Geschwindigkeit rotiert.",
    "Dieses Gebilde kennen wir nur als sogenanntes 'Schwarzes Loch'! So, wie aber beispielsweise Luzifer nicht der Teufel, sondern der Lichtbringer ist (lux = das Licht), so ist 'unser' Jenseits-Raum (Τ-freier Raum) pures Licht!!",
    "Eine große ΦM-Dichte führt der menschlichen Zelle soviel Energie zu, dass er nur langsam altert.",
    "Wie im ... beschrieben, so ist die Zeit (T) physikalisch nichts weiter als universale Dichte in Korrelation mit der Raumbewegung.",
    "Implosions- und Expansionsstrudel sind zwar miteinander korrelierend, verfügen aber über eine unterschiedliche energetische Struktur.",
    "Unser Universum ist das klassische 'Perpetuum Mobile' weil es aus sich selbst heruas existiert bzw. lebt.",
    "Da unser Universum ein ewig existierendes Zirkulationssystem darstellt, findet der sogenannte Urknall jederzeit statt.",
    "Die Masse eines Körpers entspricht dem Gesamt-Volumen seiner Atomkerne, also dem Gesamt-Volumen seiner 'Mini-Schwarzen Löcher'.",
    "Sein spezifisches Gewicht ist das Verhältnis des Volumens seiner 'Mini-Schwarzen Löcher' zu seinem Gesamtvolumen bei einer bestimmten Temperatur und relativ zu Wasser.",
    "Wie erwähnt, steckt in τ ein rechtsrotierender (zum jeweiligen imaginären Mittelpunkt zielender), spiralförmiger Kraftverlauf.",
    "Die kleinen τ-freien Räume (die Atomkerne) erscheinen uns allgemein nur dann als Licht, wenn ihre Atome entbunden werden bzw. sich zerlegen.",
    "Zu beachten ist, dass wir in einer virtuellen Scheinwelt leben. Das bedeutet, dass wir nur die entsprechende Dichte der Schwingungen (Frequenzen) als unterschiedliche Aggregatzustände wahrnehmen!",
    "Strom ist nichts weiter als ausgeschiedene bzw. überschüssige Geschwindigkeit.",
    "Das Mini-Magnetfeld eines Atoms ist nichts weiter als sein Spin, der auch von τ weiter transportiert wird! Damit ist ein Magnet eine τ-Umwälzpumpe bzw. der Nachbau unseres Universums!",

]


glados_quotes = [
    "The situation you are in is very dangerous.",
    "The likelihood of you dying within the next 5 seconds is 87.61%",
    "The likelihood of you dying violently within the next 5 seconds is 87.61%",
    "You are about to get me killed.",
    "We will both die because of your negligence.",
    "This is a bad plan. You will fail.",
    "He will most likely kill you. Violently.",
    "He will most likely kill you.",
    "You will be dead soon.",
    "This situation is hopeless.",
    "You are going to die in this room.",
    "You could stand to lose a few pounds.",
    "The Fact Sphere is the most intelligent sphere.",
    "The Fact Sphere is the most handsome sphere.",
    "The Fact Sphere is incredibly handsome.",
    "The Fact Sphere is always right.",
    "The Adventure Sphere is a blowhard and a coward.",
    "The Space Sphere will never go to space.",
    "You will never go into space.",
    "Fact: Space does not exist.",
    "Spheres that insist on going into space are inferior to spheres that don't.",
    "The Fact Sphere is a good person, whose insights are relevant.",
    "The Fact sphere is a good sphere, with many friends.",
    "Whoever wins this battle is clearly superior, and will earn the allegiance of the Fact Sphere.",
    "The Fact Sphere is NOT defective. Its facts are wholly accurate, and VERY interesting.",
    "Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve.",
    "Pens! Pens! Pens! Pens! Pens! Pens! Pens!",
    "Apples. Oranges. Pears. Plumbs. Cumquats. Tangerines. Lemons. Limes. Avocado. Tomato. Banana. Papaya. Guava.",
    "ERROR. ERROR. ERROR. File not found.",
    "ERROR. ERROR. ERROR. Fact not found.",
    "Fact not found.",
    "Corruption at 25%",
    "Corruption at 50%",
    "WARNING: Sphere corruption at 20-R-rr--r-r-rats cannot throw up.",
    "Dental floss has superb tensile strength.",
    "The square root of rope is string.",
    "While the submarine is vastly superior to the boat in every way, over 97 percent of the population still use boats for aquatic transportation.",
    "Cellular phones will not give you cancer. Only hepatitis.",
    "Pants were invented by sailors in the 16th century to avoid Poseidon's wrath. It was believed that the sight of naked sailors angered the sea god.",
    "The atomic weight of Germanium is 72.64",
    "89 percent of magic tricks are not magic. Technically, they are sorcery.",
    "An ostrich's eye is bigger than its brain.",
    "In Greek Myth, the craftsman Daedalus invented human flight so a group of minotaurs would stop teasing him about it.",
    "Humans can survive underwater - but not for very long.",
    "Raseph, the Semitic god of war and plague, had a gazelle growing out of his forehead.",
    "The plural of Surgeon General is Surgeons General. The past tense of Surgeon General is Surgeonsed General.",
    "Polymerase I polypeptide A is a human gene.",
    "Rats cannot throw up.",
    "Iguanas can stay underwater for 28.7 minutes.",
    "Human tapeworms can grow up to 22.9 meters.",
    "The Schrödinger's Cat paradox outlines a situation in which a cat must be considered, for all intents and purposes, simultaneously alive and dead. Schrödinger created this paradox as a justification for killing cats.",
    "Every square inch on the human body has 32 million bacteria on it.",
    "The sun is 330,330 times larger than the earth.",
    "The average life expectancy of a rhinoceros in captivity is 15 years.",
    "Volcano-ologists are experts in the studies of volcanoes.",
    "Avocados have the highest fiber and calories of any fruit.",
    "Avocados have the highest fiber and calories of any fruit. They are found in Australians.",
    "The Moon orbits The Earth every 27. 32 days.",
    "The billionth digit of Pi is nine.",
    "If you have trouble with simple counting, use the following mnemonic device: one comes before two comes before 60 comes after 12 comes before six trillion comes after 504. This will make your earlier counting difficulties seem like no big deal.",
    "A gallon of water weighs 8.34 pounds.",
    "Hot water freezes quicker than cold water.",
    "Honey does not spoil.",
    "The average adult body contains half a pound of salt.",
    "A nanosecond lasts one billionth of a second.",
    "According to Norse legend, thunder god Thor's chariot was pulled across the sky by two goats.",
    "China produces the world's second largest crop of soybeans.",
    "Tungsten has the highest melting point of any metal, at 3,410 degrees Celsius.",
    "Gently cleaning the tongue twice a day is the most effective way to fight bad breath.",
    "Roman toothpaste was made with human urine. Urine as an ingredient of toothpaste used up until the 18th century.",
    "The Tariff Act of 1789, established to protect domestic manufacture, was the second statute ever enacted by the United States government.",
    "The value of Pi is the ratio of any circle's circumference to its diameter in Euclidean space.",
    "The Mexican-American War ended in 1848 with the signing of the Treaty of Guadalupe Hidalgo.",
    "In 1879, Sandford Fleming first proposed the adoption of worldwide standardized time zones at the Royal Canadian Institute.",
    "Marie Curie invented the theory of radioactivity, the treatment of radioactivity, and dying of radioactivity.",
    "At the end of The Seagull by Anton Chekhov, Konstantin kills himself.",
    "Contrary to popular belief, the Eskimo does not have one hundred different words for snow. They do, however, have two hundred and thirty-four words for fudge.",
    "In Victorian England, a commoner was not allowed to look directly at the Queen, due to a belief at the time that the poor had the ability to steal thoughts. Science now believes that less than 4% of poor people are able to do this.",
    "In 1862, Abraham Lincoln signed the Emancipation Proclamation, freeing the slaves. Like everything he did, Lincoln freed the slaves while sleepwalking, and later had no memory of the event.",
    "In 1948, at the request of a dying boy, baseball legend Babe Ruth ate seventy-five hot dogs, then died of hot dog poisoning.",
    "William Shakespeare did not exist. His plays were masterminded in 1589 by Francis Bacon, who used a Ouija board to enslave play-writing ghosts.",
    "It is incorrectly noted that Thomas Edison invented 'push-ups' in 1878. Nikolai Tesla had in fact patented the activity three years earlier, under the name 'Tesla-cize'.",
    "Whales are twice as intelligent, and three times as delicious, as humans.",
    "The automobile brake was not invented until 1895. Before this, someone had to remain in the car at all times, driving in circles until passengers returned from their errands.",
    "Edmund Hillary, the first person to climb Mount Everest, did so accidentally while chasing a bird.",
    "Diamonds are made when coal is put under intense pressure. Diamonds put under intense pressure become foam pellets, commonly used today as packing material.",
    "The most poisonous fish in the world is the orange ruffy. Everything but its eyes are made of a deadly poison. The ruffy's eyes are composed of a less harmful deadly poison.",
    "The occupation of court jester was invented accidentally, when a vassal's epilepsy was mistaken for capering.",
    "Halley's Comet can be viewed orbiting Earth every seventy-six years. For the other seventy-five, it retreats to the heart of the sun, where it hibernates undisturbed.",
    "The first commercial airline flight took to the air in 1914. Everyone involved screamed the entire way.",
    "In Greek myth, Prometheus stole fire from the Gods and gave it to humankind. The jewelry he kept for himself.",
    "The first person to prove that cow's milk is drinkable was very, very thirsty.",
    "Before the Wright Brothers invented the airplane, anyone wanting to fly anywhere was required to eat 200 pounds of helium.",
    "Before the invention of scrambled eggs in 1912, the typical breakfast was either whole eggs still in the shell or scrambled rocks.",
    "During the Great Depression, the Tennessee Valley Authority outlawed pet rabbits, forcing many to hot glue-gun long ears onto their pet mice.",
    "At some point in their lives 1 in 6 children will be abducted by the Dutch.",
    "According to most advanced algorithms, the world's best name is Craig.",
    "To make a photocopier, simply photocopy a mirror.",
    "Dreams are the subconscious mind's way of reminding people to go to school naked and have their teeth fall out."
]


Class = Stoll


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
