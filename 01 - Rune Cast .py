import random
print("Take a few moments to close your eyes, relax, and breathe.")
input("Press Enter")
print("Take a few more moments to relax and focus on your question.\nIn the next line you will be asked how many runes"
      "you wish to draw. Contemplate that now. Remember to breathe.")
input("Press Enter")

draw = int(input("How many runes do you wish to draw?_"))
print("--------------------------------------------------------------")
f = open("01 - Rune Cast.txt", "w+")

Runes = ["Fehu\n - (F: Domestic cattle, wealth.) Possessions won or earned, earned income, luck. Abundance, financial\n"
         "strength in the present or near future. Sign of hope and plenty, success and happiness. Social success.\n"
         "Energy, foresight, fertility, creation/destruction (becoming).",

         "Uruz\n - (U: Auroch, a wild ox.) Physical strength and speed, untamed potential. A time of great energy and health.\n "
         "Freedom, energy, action, courage, strength, tenacity, understanding, wisdom.\n "
         "Sudden or unexpected changes (usually for the better). Sexual desire, masculine potency.\n"
         "The shaping of power and pattern, formulation of the self. ",

         "Thurisaz\n - (TH: Thorn or a Giant.) Reactive force, directed force of destruction and defense, conflict.\n"
         "Instinctual will, vital eroticism, regenerative catalyst. A tendency toward change. Catharsis, purging, cleansing fire.\n"
         "Male sexuality, fertilization. (Thorr, the Thunder god, was of Giant stock.)\n",

         "Ansuz\n - (A: The As, ancestral god, i.e. Odin.) A revealing message or insight, communication.\n"
         "Signals, inspiration, enthusiasm, speech, true vision, power of words and naming.\n"
         "Blessings, the taking of advice. Good health, harmony, truth, wisdom.\n",

         "Raidho\n - (R: Wagon or chariot.) Travel, both in physical terms and those of lifestyle direction.\n"
         "A journey, vacation, relocation, evolution, change of place or setting. Seeing a larger perspective.\n"
         "Seeing the right move for you to make and deciding upon it. Personal rhythm, world rhythm, dance of life.\n",

         "Kenaz\n - (K: Beacon or torch.) Vision, revelation, knowledge, creativity, inspiration, technical ability.\n"
         "Vital fire of life, harnessed power, fire of transformation and regeneration. Power to create your own\n"
         "reality, the power of light. Open to new strength, energy, and power now. Passion, sexual love. Kenaz\n",

         "Gebo\n -  (G: Gift.) Gifts, both in the sense of sacrifice and of generosity, indicating balance. All matters\n "
         "in relation to exchanges, including contracts, personal relationships and partnerships.",

         "Wunjo\n - (W or V: Joy.) Joy, comfort, pleasure. Fellowship, harmony, prosperity. Ecstasy, glory, spiritual\n "
         "reward, but also the possibility of going 'over the top'. If restrained, the meaning is general success and \n"
         "recognition of worth.",

         "Hagalaz\n - (H: Hail.) Wrath of nature, destructive, uncontrolled forces, especially the weather, or within \n"
         "the unconscious. Tempering, testing, trial. Controlled crisis, leading to completion, inner harmony.\n ",

         "Naudhiz\n - (N: Need.) Delays, restriction. Resistance leading to strength, innovation, need-fire \n("
         "self-reliance). Distress, confusion, conflict, and the power of will to overcome them. Endurance, survival,\n "
         "determination. A time to exercise patience. Recognition of one's fate. Major self-initiated change. Face\n "
         "your fears.",

         "Isa\n - (I: Ice.) A challenge or frustration. Psychological blocks to thought or activity, including \n"
         "grievances. Standstill, or a time to turn inward and wait for what is to come, or to seek clarity. This\n "
         "rune reinforces runes around it.",

         "Jera\n -  (J or Y: A year, a good harvest.) The results of earlier efforts are realized. A time of peace and \n"
         "happiness, fruitful season. It can break through stagnancy. Hopes and expectations of peace and prosperity. \n"
         "The promise of success earned. Life cycle, cyclical pattern of the universe. Everything changes,\n"
         "in its own time.",

         "Eihwaz\n -  (EI: Yew tree.) Strength, reliability, dependability, trustworthiness. Enlightenment, endurance.\n "
         "Defense, protection. The driving force to acquire, providing motivation and a sense of purpose. Indicates \n"
         "that you have set your sights on a reasonable target and can achieve your goals. An honest man who can be \n"
         "relied upon.",

         "Perdhro\n -  (P: Lot cup, vagina.) Uncertain meaning, a secret matter, a mystery, hidden things and occult\n "
         "abilities. Initiation, knowledge of one's destiny, knowledge of future matters, determining the future or\n "
         "your path. Pertaining to things feminine, feminine mysteries including female fertility, and vagina. Good\n "
         "lot, fellowship and joy. Evolutionary change.",

         "Elhaz\n - (Z or -R: Elk, protection.) Protection, a shield. The protective urge to shelter oneself or others.\n "
         "Defense, warding off of evil, shield, guardian. Connection with the gods, awakening, higher life. It can be\n "
         "used to channel energies appropriately. Follow your instincts. Keep hold of success or maintain a position \n"
         "won or earned.",

         "Sowilo\n - (S: The sun.) Success, goals achieved, honor. The life-force, health. A time when power will be\n "
         "available to you for positive changes in your life, victory, health, and success. Contact between the\n "
         "higher self and the unconscious. Wholeness, power, elemental force, sword of flame, cleansing fire.",

         "Teiwaz\n - (T: Tyr, the sky god.) Honor, justice, leadership and authority. Analysis, rationality. Knowing\n "
         "where one's true strengths lie. Willingness to self-sacrifice. Victory and success in any competition or in \n"
         "legal matters.",

         "Berkana\n - (B: Berchta, the birch-goddess.) Birth, general fertility, both mental and physical and personal\n "
         "growth, liberation. Regenerative power and light of spring, renewal, promise of new beginnings, new growth.\n "
         "Arousal of desire. A love affair or new birth. The prospering of an enterprise or venture.",

         "Ehwaz\n - (E: Horse, two horses.) Transportation. May represent a horse, car, plane, boat or other vehicle.\n "
         "Movement and change for the better. Gradual development and steady progress are indicated. Harmony, "
         "teamwork, trust, loyalty. An ideal marriage or partnership. Confirmation beyond doubt the meanings of the\n "
         "runes around it.",

         "Mannaz\n - (M: Man, mankind.) The Self; the individual or the human race. Your attitude toward others and\n "
         "their attitudes towards you. Friends and enemies, social order. Intelligence, forethought, create, skill,\n "
         "ability. Divine structure, intelligence, awareness. Expect to receive some sort of aid or cooperation now.\n",
         

         "Laguz\n - (L: Water, or a leek.) Flow, water, sea, a fertility source, the healing power of renewal. Life \n"
         "energy and organic growth. Imagination and psychic matters. Dreams, fantasies, mysteries, the unknown,\n "
         "the hidden, the deep, the underworld. Success in travel or acquisition, but with the possibility of loss.",

         "Ingwaz\n - (NG: Ing, the earth god.) Male fertility, gestation, internal growth. Common virtues,\n "
         "common sense, simple strengths, family love, caring, human warmth, the home. Rest stage, a time of relief,\n "
         "of no anxiety. A time when all loose strings are tied and you are free to move in a new direction. Listen\n "
         "to yourself.",

         "Dagaz\n - (D: Day or dawn.) Breakthrough, awakening, awareness. Daylight clarity as opposed to nighttime\n "
         "uncertainty. A time to plan or embark upon an enterprise. The power of change directed by your own will, \n"
         "transformation. Hope/happiness, the ideal. Security and certainty. Growth and release. Balance point, \n"
         "the place where opposites meet.",

         "Othala\n - (O: Ancestral property.) Inherited property or possessions, a house, a home. What is truly \n"
         "important to one. Group order, group prosperity. Land of birth, spiritual heritage, experience and \n"
         "fundamental values. Aid in spiritual and physical journeys. Source of safety, increase and abundance.\n "
         ]

Runes_Reversed = ["Fehu\n - (F: Domestic cattle, wealth.) "
         "Fehu Reversed or Merkstave: Loss of personal\n"
         "property, esteem, or something that you put in effort to keep. It indicates some sort of failure. Greed,\n"
         "burnout, atrophy, discord. Cowardice, stupidity, dullness, poverty, slavery, bondage.",

         "Uruz\n - (U: Auroch, a wild ox.)"
         "Uruz Reversed or Merkstave: Weakness, obsession, misdirected force, domination by others. Sickness, inconsistency, ignorance.\n"
         "Lust, brutality, rashness, callousness, violence.",

         "Thurisaz\n - (TH: Thorn or a Giant.)"
         "Thurisaz Reversed or Merkstave: Danger, defenselessness, compulsion, betrayal, dullness.\n"
         "Evil, malice, hatred, torment, spite, lies. A bad man or woman. Rape?\n",

         "Ansuz\n - (A: The As, ancestral god, i.e. Odin.)"
         "Ansuz Reversed or Merkstave: Misunderstanding, delusion, manipulation by others, boredom. Vanity and grandiloquence.\n"
         "(Odin is a mighty, but duplicitous god. He always has his own agenda.)",

         "Raidho\n - (R: Wagon or chariot.)"
         "Raidho Reversed or Merkstave: Crisis, rigidity, stasis, injustice, irrationality. Disruption, dislocation, demotion, delusion, possibly a death.",

         "Kenaz\n - (K: Beacon or torch.)"
         "Reversed or Merkstave: Disease, breakup, instability, lack of creativity. Nakedness, exposure\n "
         "loss of illusion and false hope.",

         "Gebo\n -  (G: Gift.)"
         "Gebo cannot be reversed, but may lie in opposition): Greed, loneliness, dependence, over-sacrifice. \n"
         "Obligation, toll, privation, bribery.",

         "Wunjo\n - (W or V: Joy.)"
         "Wunjo Reversed or Merkstave: Stultification, sorrow, strife, alienation. Delirium,\n "
         "intoxication, possession by higher forces, impractical enthusiasm. Raging frenzy, berzerker.",

         "Hagalaz\n - (H: Hail.)"
         "Hagalaz Merkstave (Hagalaz cannot be reversed, but may lie in opposition): Natural disaster, catastrophe.\n "
         "Stagnation, loss of power. Pain, loss, suffering, hardship, sickness, crisis.\n",

         "Naudhiz\n - (N: Need.)" 
        "Nauthiz Reversed or Merkstave: Constraint of freedom, distress, toil, drudgery,\n "
         "laxity. Necessity, extremity, want, deprivation, starvation, need, poverty, emotional hunger.\n",

         "Isa\n - (I: Ice.) Isa Merkstave (Isa cannot be reversed, but may lie in opposition): \n"
         "Ego-mania, dullness, blindness, dissipation. Treachery, illusion, deceit, betrayal, guile, stealth, ambush,\n "
         "plots.",

         "Jera\n -  (J or Y: A year, a good harvest.) Jera Merkstave (Jera cannot be reversed, but may lie in opposition): Sudden setback, \n"
         "reversals. A major change, repetition, bad timing, poverty, conflict.",

         "Eihwaz\n -  (EI: Yew tree.) Eihwaz Reversed or Merkstave: Confusion, destruction, dissatisfaction, weakness.\n",

         "Perdhro\n -  (P: Lot cup, vagina.) Perthro Reversed or Merkstave: Addiction, stagnation, \n"
         "loneliness, malaise.",

         "Elhaz\n - (Z or -R: Elk, protection.) Algiz Reversed: or Merkstave: Hidden danger, consumption by divine forces, loss of divine \n"
         "link. Taboo, warning, turning away, that which repels.",

         "Sowilo\n - (S: The sun.)"
         "Merkstave (Sowilo cannot be reversed, but may lie in opposition): False goals, bad counsel, false success,\n "
         "gullibility, loss of goals. Destruction, retribution, justice, casting down of vanity. Wrath of god.\n",

         "Teiwaz\n - (T: Tyr, the sky god.) Tiwaz Reversed or Merkstave: One's energy and creative flow are blocked. Mental paralysis, \n"
         "over-analysis, over-sacrifice, injustice, imbalance. Strife, war, conflict, failure in competition.\n "
         "Dwindling passion, difficulties in communication, and possibly separation.",

         "Berkana\n - (B: Berchta, the birch-goddess.) Berkano Reversed \n"
         "or Merkstave: Family problems and or domestic troubles. Anxiety about someone close to you. Carelessness, \n"
         "abandon, loss of control. Blurring of consciousness, deceit, sterility, stagnation.",

         "Ehwaz\n - (E: Horse, two horses.) Ehwaz Reversed or Merkstave: This is not really a negative rune. A change is perhaps\n "
         "craved. Feeling restless or confined in a situation. Reckless haste, disharmony, mistrust, betrayal.\n",

         "Mannaz\n - (M: Man, mankind.)" "Mannaz Reversed or Merkstave: Depression, mortality, blindness, self-delusion. Cunning, slyness, \n"
         "manipulation, craftiness, calculation. Expect no help now.",

         "Laguz\n - (L: Water, or a leek.)"
         "Laguz Reversed or Merkstave: An indication of a period of confusion in your life. You may be making wrong\n "
         "decisions and poor judgements. Lack of creativity and feelings of being in a rut. Fear, circular motion,\n "
         "avoidance, withering. Madness, obsession, despair, perversity, sickness, suicide.",

         "Ingwaz\n - (NG: Ing, the earth god.) Ingwaz Merkstave (Ingwaz cannot be reversed, but may lie in opposition): Impotence, \n"
         "movement without change. Production, toil, labor, work.",

         "Dagaz\n - (D: Day or dawn.) Dagaz Merkstave (Dagaz cannot be reversed, but may lie in opposition): A\n "
         "completion, ending, limit, coming full circle. Blindness, hopelessness.",

         "Othala\n - (O: Ancestral property.)"
         "Othala Reversed or Merkstave: Lack of customary order, totalitarianism, slavery, poverty, homelessness. Bad \n"
         "karma, prejudice, clannishness, provincialism. What a man is bound to."]





Alignment = ["Up-Right", "Reversed"]

while (draw != 0):
    x = random.randint(0, 1)
    y = random.randint(0, 23)

    f.write("\n--------------------------------------------------------\n")
    f.write(Alignment[x])
    print(Alignment[x])
    f.write("\n")
    if (x == 0):
        f.write(Runes[y])
        print(Runes[y])
    elif (x == 1):
        f.write(Runes_Reversed[y])
        print(Runes_Reversed[y])
    draw = draw - 1
    f.write("\n--------------------------------------------------------\n")


f.close()
input("Press ENTER to exit. Your reading has been saved to the a text file in the same folder")