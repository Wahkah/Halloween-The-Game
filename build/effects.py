# Effect descriptions written for this site. These are our own summaries of what each
# card does in play, not the game's own strings. Where the in-game wording is ambiguous
# about direction or size, the entry carries a note saying so.
#
# "scales" marks a card whose strength moves with rarity. A card without it is a fixed
# mechanic, so a Common copy does the same thing as a Legendary one.

PERKS = {
 # --- stalk and stealth ---
 "Aura of Awareness":  ("Widens the area around you inside which Michael cannot enter or leave Shape Jump.", True),
 "Deaden":             ("Changes how readable the noise pings you give off are.", True,
                        "The card name and the in-game wording point in opposite directions, so treat both the size and the direction as unconfirmed until somebody tests it."),
 "Elusory":            ("Michael builds Stalk on you more slowly.", True),
 "Fade to Black":      ("Sitting in a hiding spot burns off your Stalk tiers faster.", True),
 "Fleeting Shadow":    ("You get into and out of hiding spots faster.", True),
 "Ghost":              ("Your Stalk tiers decay faster on their own.", True),
 "Lurker":             ("Standing in a stealth bush burns off Stalk and refills stamina at the same time.", False),
 "Scavenger":          ("Each press of the hiding spot rummage minigame makes more progress.", True),
 "Sixth Sense":        ("You can hear Michael breathing while he is in Shape Jump, out to a set range.", True),
 # --- combat ---
 "Brutal Cleave":      ("Your heavy melee attacks hit harder. Light attacks are unchanged.", True),
 "Contender":          ("All of your melee damage goes up.", True),
 "Deadshot":           ("Critical hits from firearms do more damage.", True),
 "Lethal Pitch":       ("Anything you throw, weapon or item, lands for more damage.", True),
 "Liquid Courage":     ("You hit harder in melee while you are drunk.", True),
 "Relentless Steel":   ("Your melee weapons lose durability more slowly, so they survive longer fights.", True),
 "Revenge":            ("Each time a Resident or civilian dies near you, your melee damage goes up. It stacks up to five times.", True),
 "Solid Foundation":   ("Raises your poise, so you are harder to stagger out of what you are doing.", True),
 "Survival Rage":      ("You hit harder in melee while you are terrified.", True),
 # --- survival ---
 "Blinding Light":     ("Blinds you land on Michael last longer.", True),
 "Dying Breath":       ("While you are on low health, you are more likely to break out of a grab.", True),
 "Glass Walker":       ("Diving through a window hurts you less.", True),
 "Grave Footing":      ("You are less likely to trip while exhausted or terrified.", True),
 "Hardened":           ("You take less damage from blunt weapons.", True),
 "Iron Ankles":        ("You take less fall damage.", True),
 "Slippery":           ("The struggle minigame you get when Michael grabs you becomes easier.", True),
 "Stubborn":           ("You move faster while wounded.", True),
 "Thick Skin":         ("You take less damage from sharp weapons.", True),
 # --- stamina and healing ---
 "Adrenaline":         ("Your stamina refills faster.", True),
 "Breakfall":          ("You recover from landing faster after a drop.", True),
 "Clotting":           ("Your health regenerates faster.", True),
 "Field Triage":       ("Sprays and med kits take less time to use, so you are exposed for less of it.", True),
 "Inspiring":          ("Residents you tell to hide get more maximum health.", True),
 "Runner's High":      ("Being exhausted slows you down less.", True),
 "Therapeutic":        ("Healing items do more when you use them on somebody else.", True),
 "Unwinded":           ("Reduces all stamina use, not just sprinting, so it applies to every action that draws on the bar.", True),
 "Wound Mender":       ("Health items restore more health.", True),
 # --- fear and intoxication ---
 "Reveler":            ("Drunk and high both last longer.", True),
 "Shield of Law":      ("You gain fear more slowly while you are close to a police officer.", True),
 "Unphased":           ("Your fear builds more slowly.", True),
 "Wired":              ("Every can of pop you drink permanently cuts the fear you take. It stacks across the match.", True),
 "Witness State":      ("While you are high, other characters within range are faintly outlined for you.", True),
 # --- police ---
 "Convincing Plea":    ("Filling the badge meter brings the next wave of police in sooner.", True),
 "Frantic":            ("Each dispatch call you finish adds more police presence than it otherwise would.", True),
 "Smooth Talker":      ("The perfect band on the dispatch call skill check gets wider.", True),
 # --- residents and followers ---
 "Guardian Shadow":    ("Residents following you take less damage.", True),
 "Panic Contagion":    ("Getting a Resident out gives you a burst of movement speed.", True),
 "Pied Piper":         ("You can have one more NPC following you than normal.", False),
 "Shared Desperation": ("Residents you hand a weapon to hit harder with it.", True),
 "Voice of Reason":    ("Residents following you gain less fear.", True),
 # --- objectives and escapes ---
 "Barricade":          ("Doors you lock take longer for Michael to break down.", True),
 "Bullet Belt":        ("Each stack of ammunition you carry holds more rounds.", True),
 "Exit Strategy":      ("You discover escape routes from further away.", True),
 "Fast Fingers":       ("You reload firearms and swap flashlight batteries faster.", False,
                        "Reload speed is a percentage in game, so this may scale with rarity even though it reads as a fixed effect here."),
 "Fated Find":         ("Hands you one escape objective item at random, chosen to be useful on the map you are on.", False),
 "Panic Drive":        ("A car takes less damage while you are the one driving it.", True),
 "Repair Expert":      ("Repairs sometimes do not consume the repair pack.", True),
 "Survival Intuition": ("One escape location is marked on your map from the start.", False),
 "Survival Skills":    ("Phones within range are outlined along with their state: ready, cooling down, or disabled.", True),
 "Trespasser":         ("You can pick a locked door open with a hold interaction, no key needed.", True),
 # --- utility ---
 "Brimstone Fuse":     ("Firecrackers you set off keep Michael disoriented for longer.", True),
 "Knockout":           ("Michael takes longer to get back up from a knockdown you contributed to.", True),
 "Silver Tongue":      ("The conversation minigame gives you more time to reach a perfect score.", True),
}
# Fast Fingers scaling: the in-game text is a percentage, so mark it as scaling.
PERKS["Fast Fingers"] = ("You reload firearms and swap flashlight batteries faster.", True)

TRAITS = {
 "Running Back":      "Any contact or physical hit you land on Michael drops your own Stalk tier. Landing a hit is what makes you harder to grab.",
 "Heavyweight":       "You get the upside of being drunk with none of the downside. No stumbling, no extra noise, less visual impairment, plus reduced fear and a melee boost.",
 "Spatial Awareness": "While you are calm, Residents within about 25 metres are marked for you through walls.",
 "Full Moon":         "Damaging and downing Michael takes more off his Bloodthirst than it would for anybody else.",
 "Popular":           "Residents following you take less damage, gain less fear, and fight harder to protect you.",
 "Hunter's Sense":    "While you are not terrified, you see faint noise pings and nearby escapes are marked, out to about 25 metres.",
 "Lone Wolf":         "Once you are the last civilian alive you get a large buff: smoother conversations, faster interactions, less fear, and the CB radio and escape items marked for you.",
 "Speed Kills":       "A repair kit substitutes for the car key when you get in and turn the engine over, though the hold takes far longer.",
 "Totally Amazing":   "The reward from the two player hiding spot lasts longer and hits harder.",
 "Dreamer":           "Residents you successfully talk to become harder for Michael to stalk, and it sticks after you walk away.",
 "Affluent Partier":  "Holding both the drunk and the high states at once adds a further melee bonus on top of whatever each is already giving you.",
 "Hi-Fi":             "A noise maker you have switched on acts as a sensor: while Michael is near one, he is outlined for you.",
}
TRAIT_SCALES = {"Running Back": False, "Heavyweight": False, "Spatial Awareness": False,
                "Hunter's Sense": False, "Lone Wolf": False, "Speed Kills": False,
                "Full Moon": True, "Popular": True, "Totally Amazing": True,
                "Dreamer": True, "Affluent Partier": True, "Hi-Fi": True}

SPECTATOR = {
 "Police Reinforcements": "Respawns you as a police officer.",
 "Loomis Reinforcements": "Respawns you as Dr. Loomis.",
 "Shotgun":               "Hands the player you are watching a shotgun.",
 "Increase Dispatch Awareness": "Nudges police presence upward.",
 "Player XP":             "Awards a small amount of experience.",
}

ABILITIES = [
 ("Killer Sense", "Drops him into a first person view from behind the mask, used to build Stalk on a chosen target accurately and to sweep the area for noise pings."),
 ("Shape Jump", "His signature traversal. He slips into the shadows and moves invisibly and quickly, including through unlit doors. He can only enter or leave it when he is out of light, unseen, and with nobody standing too close."),
 ("Shape Dash", "A burst of speed while he is in Shape Jump. It runs on three charges that have to be replenished."),
 ("Reality Tear", "Pushes him through the Shape Jump boundary in either direction no matter the circumstances, ignoring light, being watched, and even being downed. The one ability that beats every normal blocker."),
 ("Blackout", "A pulse that briefly kills power to lights, flashlights and vehicles nearby. Landlines still work."),
 ("Detection Pulse", "An expanding pulse that briefly marks people in a large radius. Anyone inside a building is not outlined individually, but the building itself gets marked."),
 ("Evil Presence", "An aura that weakens everybody near him while giving him a strong buff, useful for catching runners or fighting several people at once."),
 ("Shadow Strike", "A thrown shadow knife that slows and temporarily blinds whoever it hits."),
 ("Shape Mines", "Motion sensors he can place. Anyone who walks into one is marked and gets a jumpscare."),
 ("Teleport", "Opens a top down map view and drops him at the point he picks, unsettling anyone he lands near."),
]

# One line character descriptions, written for this site.
BLURBS = {
 "Thomas Armitage":    "A college athlete home for the weekend to visit his father. Natural leader, used to organising people under pressure.",
 "Bob Simms":          "Lynda's boyfriend. Quiet, along for the ride, and the one who went for the beer.",
 "Laurie Strode":      "The babysitter. Shy, protective, and quick on her feet when it matters.",
 "Rachel Calahan":     "Proto goth with an occult streak. Cemeteries over bowling alleys, and proud of the weirdo label.",
 "Alexis Purcell":     "Haddonfield's it girl, back from a failed run at big city modelling, working at Strode Realty.",
 "Tanya Harrison":     "Sells vinyl part time and always knows where the night is heading.",
 "Marcus Navarro":     "Newest member of a local biker gang, living on the edge of town for his grandmother's sake.",
 "Eric Dunn":          "Talks big, works at the hardware store, hunts in the woods on an ATV.",
 "Annie Brackett":     "The Sheriff's daughter, and a rebellious one.",
 "Lynda Van Der Klok": "Bold, social, unbothered by grades, and never far from a friend.",
 "Jennifer Aarons":    "Prom queen and valedictorian, happier at home with a book than out on a date.",
 "Richard Hawthorne":  "New money from California, crowned party king within a month of arriving.",
}

# Measured values, read off the cards in game. These are facts about the game rather than
# its wording, so unlike the descriptions above they are reported as observed.
#   perk -> {rarity: percentage}
VALUES = {
 "Reveler":               {"Common": 15, "Rare": 50, "Legendary": 100},
 "Voice of Reason":       {"Common": 50},
 "Shared Desperation":    {"Common": 15, "Rare": 30, "Epic": 40},
 "Exit Strategy":         {"Common": 25, "Uncommon": 35},
 "Unwinded":              {"Common": 10, "Uncommon": 15, "Legendary": 35},
 "Silver Tongue":         {"Rare": 30},
 "Slippery":              {"Common": 15, "Uncommon": 20, "Epic": 30},
 "Aura of Awareness":     {"Common": 15, "Uncommon": 20, "Rare": 25},
 "Frantic":               {"Uncommon": 25},
 "Brutal Cleave":         {"Rare": 20},
 "Grave Footing":         {"Common": 20},
 "Lethal Pitch":          {"Uncommon": 20},
 "Panic Drive":           {"Common": 20},
 "Repair Expert":         {"Common": 20},
 "Shield of Law":         {"Uncommon": 20},
 "Fade to Black":         {"Common": 15},
 "Field Triage":          {"Common": 10},
 "Glass Walker":          {"Common": 10},
 "Guardian Shadow":       {"Common": 10},
 "Hardened":              {"Common": 10},
 "Iron Ankles":           {"Common": 10},
 "Knockout":              {"Common": 10},
 "Liquid Courage":        {"Common": 5, "Uncommon": 10},
 "Smooth Talker":         {"Common": 10},
 "Stubborn":              {"Common": 10},
 "Witness State":         {"Common": 10},
 "Wound Mender":          {"Common": 5, "Uncommon": 10},
 "Adrenaline":            {"Common": 8},
 "Contender":             {"Common": 5},
 "Solid Foundation":      {"Common": 5},
 "Wired":                 {"Common": 3},
 "Panic Contagion":       {"Common": 2},
 "Elusory":               {"Common": 1},
}
METRE_VALUES = {"Witness State"}          # figure is a distance in metres, not a per cent
FLAT_CONFIRMED = {"Pied Piper": "II and V read the same",
                  "Survival Intuition": "II and III read the same as V"}
TIER_UNCONFIRMED = {"Hardened": "reported without a tier; recorded here as I"}
NUMERALS = {"Common": "I", "Uncommon": "II", "Rare": "III", "Epic": "IV", "Legendary": "V"}
LADDER_NOTE = (
 "Cards carry a numeral for their tier, I through V, matching Common through Legendary. What "
 "a tier does not do is tell you the size of an effect. Across the cards measured at tier I "
 "the figures run from 1% on Elusory to 50% on Voice of Reason, a fifty fold spread at one "
 "and the same rarity. Each card is calibrated on its own scale, so a Common of a big card "
 "beats a Legendary of a small one and the numbers cannot be compared between cards at all.")
SPREAD_NOTE = (
 "The figures are not even multiples of five. Adrenaline reads 8, Wired 3, Panic Contagion 2 "
 "and Elusory 1, which rules out the neat ladder an earlier version of this page proposed.")
SHAPE_NOTE_INTRO = ""
SHAPE_NOTE = (
 "Three of the four cards measured at more than two tiers climb five points a tier through "
 "their lower half: Slippery from I to IV, Aura of Awareness from I to III, and Unwinded from "
 "I to II. Reveler is the outlier and climbs 17.5 across the same stretch. What happens higher "
 "up is the part worth knowing, because both cards seen at V come in above where five a tier "
 "would put them. Unwinded reads 35 where five a tier gives 30, and Reveler reads 100 where "
 "its own lower rate gives 85. So the working picture is a gentle climb through the middle and "
 "a jump at the top, which would make IV to V the biggest single step on a card. That is a "
 "hypothesis drawn from two cards, and Slippery at V is the number that would test it: five a "
 "tier gives 35, and anything above that confirms the jump.")
LADDER_RULE = (
 "So a figure at one tier says nothing about the same card at another tier, and nothing at "
 "all about a different card. Only measured figures appear below. A blank is a blank and "
 "never an estimate.")
UPGRADE_NOTE = (
 "The upgrade expires after a few matches and a card can only be upgraded once, so it is a "
 "one shot buff rather than a way to climb the tiers. Rolling stays the only route to a "
 "permanently high tier copy, and paying extra on a roll improves the rarity odds.")
UPGRADE_STRATEGY = (
 "The price you pay sets the tier you land on, and 4,000 points reaches V. Since the upgrade "
 "is one shot, buying a cheaper option spends your only upgrade on a worse destination, which "
 "makes every price below the top one a trap. Either go to V or leave the card alone. "
 "Reported from play rather than measured here.")
UPGRADE_MEASURED_PRICE = (
 "Two prices have been seen. A Reveler went from III to V, two tiers, for 3,818. A Shared "
 "Desperation went from III to IV, one tier, for 3,148. Two tiers cost barely more than one, "
 "so the price is not paying for distance. It tracks the destination: reaching IV costs "
 "roughly 3,150 and reaching V roughly 3,820, whatever card you point it at and wherever it "
 "starts.")
UPGRADE_DESTINATION = (
 "Which makes the decision simple. The bill is the same for every card, so the only question "
 "is which of the cards you actually run gains the most on the way to V. Those two purchases "
 "make the point: the Reveler bought 50 points for 3,818 and the Shared Desperation bought 10 "
 "for 3,148, four times the value for a fifth more money. Going to V rather than IV costs "
 "about 20% more and is worth far more than that on any card whose curve steepens at the top.")
UPGRADE_VS_ROLL = (
 "There is a larger question underneath that one. An upgrade expires after a few matches and "
 "a roll is permanent, so 4,000 points spent upgrading is 4,000 points not spent on rolls that "
 "keep whatever they land. Nobody has published what a match pays or what a roll costs, and "
 "the official progression page gives no figures, but the comparison barely depends on them. "
 "At a hundred points a roll the upgrade costs forty rolls. Even at a thousand it costs four. "
 "Rolling wins over any horizon longer than the handful of matches an upgrade survives, which "
 "leaves the upgrade as something to spend a surplus on rather than a plan.")
UPGRADE_PRICE_TIP = (
 "An earlier version of this page suggested the quoted price told you something about the "
 "card's own curve. It does not. The price is set by the tier you are buying, so it is the "
 "same on a card that gains 50 points and one that gains 10.")
UPGRADE_RATE_NOTE = (
 "Points per tier below is how much ground a card covers between tiers, which is how much "
 "your single upgrade is worth on it. It is not a laddering plan, because there is no "
 "laddering.")
WHY_CURVES = (
 "The game's own data layout points the same way. Perk scaling lives in an asset named for a "
 "curve table, meaning a table of curves rather than one shared formula. The calibration "
 "follows the effect: a duration extension can afford to read 50% where a difficulty modifier "
 "cannot. Which also means percentages are not comparable between cards. Reveler at 50% and "
 "Slippery at 30% are measuring different things on different scales.")
