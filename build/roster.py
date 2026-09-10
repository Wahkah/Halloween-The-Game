# Derived analysis, produced once from a local parse of the game data and committed here
# so the site builds without that data present. Nothing below is game text: these are
# counts we computed and names, which a build guide cannot avoid using.
#
# Each civilian has fifteen progressive challenges. ANTI_MICHAEL counts the ones that
# require acting against Michael directly. The columns after it break that down.

# (civilian, trait, vs Michael, break chase, damage, down, stun, escape grab, rescue from grab)
ROSTER = [
    ('Bob Simms', 'Heavyweight', 11, 3, 2, 2, 0, 2, 1),
    ('Laurie Strode', 'Spatial Awareness', 9, 3, 2, 1, 1, 1, 1),
    ('Thomas Armitage', 'Running Back', 7, 0, 2, 2, 1, 1, 1),
    ('Rachel Calahan', 'Full Moon', 6, 3, 0, 0, 1, 2, 0),
    ('Alexis Purcell', 'Popular', 5, 1, 0, 0, 1, 1, 1),
    ('Eric Dunn', "Hunter's Sense", 5, 0, 3, 1, 0, 0, 1),
    ('Marcus Navarro', 'Lone Wolf', 5, 2, 1, 1, 0, 0, 0),
    ('Annie Brackett', 'Speed Kills', 4, 2, 0, 0, 0, 2, 0),
    ('Lynda Van Der Klok', 'Totally Amazing', 4, 2, 0, 0, 0, 2, 0),
    ('Jennifer Aarons', 'Dreamer', 3, 1, 0, 0, 0, 1, 0),
    ('Richard Hawthorne', 'Affluent Partier', 2, 2, 0, 0, 0, 0, 0),
    ('Tanya Harrison', 'Hi-Fi', 2, 2, 0, 0, 0, 0, 0),
]

# Our own grouping of the deck perks by what they touch.
CATEGORY = {
    'Adrenaline': 'recovery',
    'Aura of Awareness': 'stalk',
    'Barricade': 'objective',
    'Blinding Light': 'survival',
    'Breakfall': 'recovery',
    'Brimstone Fuse': 'utility',
    'Brutal Cleave': 'combat',
    'Bullet Belt': 'objective',
    'Clotting': 'recovery',
    'Contender': 'combat',
    'Convincing Plea': 'police',
    'Deaden': 'stalk',
    'Deadshot': 'combat',
    'Dying Breath': 'survival',
    'Elusory': 'stalk',
    'Exit Strategy': 'objective',
    'Fade to Black': 'stalk',
    'Fast Fingers': 'objective',
    'Fated Find': 'objective',
    'Field Triage': 'recovery',
    'Fleeting Shadow': 'stalk',
    'Frantic': 'police',
    'Ghost': 'stalk',
    'Glass Walker': 'survival',
    'Grave Footing': 'survival',
    'Guardian Shadow': 'npc',
    'Hardened': 'survival',
    'Inspiring': 'recovery',
    'Iron Ankles': 'survival',
    'Knockout': 'utility',
    'Lethal Pitch': 'combat',
    'Liquid Courage': 'combat',
    'Lurker': 'stalk',
    'Panic Contagion': 'npc',
    'Panic Drive': 'objective',
    'Pied Piper': 'npc',
    'Relentless Steel': 'combat',
    'Repair Expert': 'objective',
    'Reveler': 'fear',
    'Revenge': 'combat',
    "Runner's High": 'recovery',
    'Scavenger': 'stalk',
    'Shared Desperation': 'npc',
    'Shield of Law': 'fear',
    'Silver Tongue': 'utility',
    'Sixth Sense': 'stalk',
    'Slippery': 'survival',
    'Smooth Talker': 'police',
    'Solid Foundation': 'combat',
    'Stubborn': 'survival',
    'Survival Intuition': 'objective',
    'Survival Rage': 'combat',
    'Survival Skills': 'objective',
    'Therapeutic': 'recovery',
    'Thick Skin': 'survival',
    'Trespasser': 'objective',
    'Unphased': 'fear',
    'Unwinded': 'recovery',
    'Voice of Reason': 'fear',
    'Wired': 'fear',
    'Witness State': 'fear',
    'Wound Mender': 'recovery',
}

CATEGORY_LABEL = {'stalk': 'Stalk and stealth', 'combat': 'Combat', 'survival': 'Survival',
                  'recovery': 'Stamina and healing', 'fear': 'Fear and intoxication',
                  'police': 'Police pressure', 'npc': 'Residents and followers',
                  'objective': 'Objectives and escapes', 'utility': 'Utility'}

RARITY = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
COUNTS = {'deck': 62, 'traits': 12, 'spectator': 5, 'total': 79}
