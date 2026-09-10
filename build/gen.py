#!/usr/bin/env python3
"""Generate the static site.

Reads only build/effects.py, build/roster.py and build/builds.py. No game data files
are needed or used: every effect description on the site is our own summary.
"""
import html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import effects as E
import roster as R
from builds import BUILDS

e = html.escape
TRAIT_OF = {c[0]: c[1] for c in R.ROSTER}
STATS_OF = {c[0]: c[2:] for c in R.ROSTER}

# ---- validation: every perk a build names must have a written description ----
problems = []
for b in BUILDS:
    if b['civ'] not in TRAIT_OF:
        problems.append(f"{b['civ']}: not on the roster")
    for n, _ in b['deck'] + b['swaps']:
        if n not in E.PERKS:
            problems.append(f"{b['civ']}: no description written for {n!r}")
    if len(b['deck']) != 6:
        problems.append(f"{b['civ']}: deck has {len(b['deck'])} cards")
for n in E.PERKS:
    if n not in R.CATEGORY:
        problems.append(f"{n!r} has a description but no category")
if problems:
    print('VALIDATION FAILED'); [print(' ', p) for p in problems]; sys.exit(1)

NAV = [('index.html', 'Home'), ('builds.html', 'Builds'),
       ('perks.html', 'Perks'), ('mechanics.html', 'Mechanics')]
CUR = ' aria-current="page"'

def page(fname, title, kicker, h1, lede, body):
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, CUR if h == fname else '', e(t)) for h, t in NAV)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(lede[:180])}">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#127875;</text></svg>">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html">HADDONFIELD <span>BUILDS</span></a>
  <nav class="top-nav">{nav}</nav>
</div></header>
<section class="hero"><div class="wrap">
  <div class="kicker">{e(kicker)}</div>
  <h1>{e(h1)}</h1>
  <p class="lede">{lede}</p>
</div></section>
<main><div class="wrap">
{body}
</div></main>
<footer class="bottom"><div class="wrap">
<p>Every effect description on this site is written here. None of it is copied from the
game, and no game files, assets or data exports are distributed. Percentages are
deliberately absent: the effects are known, the magnitudes are not, and nothing on this
site invents one.</p>
<p>Fan made reference. Not affiliated with IllFonic, Compass International Pictures,
Miramax, or Universal.</p>
</div></footer>
</body>
</html>'''
    open(os.path.join(ROOT, fname), 'w', encoding='utf-8').write(doc)

def desc(name):
    return E.PERKS[name][0]

def scales(name):
    return E.PERKS[name][1]

def note(name):
    p = E.PERKS[name]
    return p[2] if len(p) > 2 else None

def flat_badge(does_scale):
    return '' if does_scale else ' <span class="flat">FLAT</span>'

# ============================ builds.html ============================
def build_section(b):
    civ = b['civ']
    tname = TRAIT_OF[civ]
    s = STATS_OF[civ]
    tag = f'<span class="tag{" alt" if b.get("alt") else ""}">{e(b["role"])}</span>'
    deck_line = ' <b>&middot;</b> '.join(e(n) for n, _ in b['deck'])
    rows = ''.join(
        f'<tr><td class="perk">{e(n)}{flat_badge(scales(n))}</td>'
        f'<td>{e(desc(n))}</td><td>{e(w)}</td></tr>' for n, w in b['deck'])
    swaps = ''.join(
        f'<li><span class="mono">{e(n)}</span> {e(w)}. '
        f'<span style="color:var(--ink-faint)">{e(desc(n))}</span></li>' for n, w in b['swaps'])
    why = ''.join(f'<p>{e(x)}</p>' for x in b['why'])
    play = ''.join(f'<li>{e(x)}</li>' for x in b['play'])
    wpn, itm, lnote = b['loadout']
    return f'''
<section class="build" id="{b['slug']}">
  <div class="build-head"><h2>{e(civ)}</h2>{tag}</div>
  <p class="bio">{e(E.BLURBS[civ])}</p>
  <p>{e(b['summary'])}</p>

  <div class="trait-box">
    <div class="label">Unique trait</div>
    <div class="tname">{e(tname)}{flat_badge(E.TRAIT_SCALES[tname])}</div>
    <div class="tdesc">{e(E.TRAITS[tname])}</div>
  </div>

  <h3>Why this character</h3>
  {why}
  <p class="count">Progressive challenges that involve Michael directly: {s[0]} of 15
  (break chase {s[1]}, damage {s[2]}, down {s[3]}, stun {s[4]},
  grab escape {s[5]}, rescue from grab {s[6]}).</p>

  <h3>The deck</h3>
  <div class="deckline">{deck_line}</div>
  <div class="tablewrap"><table>
    <thead><tr><th>Card</th><th>What it does</th><th>Why it is here</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>

  <h4>Swaps</h4>
  <ul>{swaps}</ul>

  <h3>Loadout</h3>
  <p>Starting weapon <span class="mono">{e(wpn)}</span>, starting item
  <span class="mono">{e(itm)}</span>. {e(lnote)}</p>

  <h3>How to play it</h3>
  <ol>{play}</ol>
</section>'''

jump = ''.join(f'<a href="#{b["slug"]}">{e(b["civ"].split()[0])}</a>' for b in BUILDS)
page('builds.html', 'Builds for every civilian | Haddonfield Builds',
     'Twelve civilians, twelve decks',
     'A build for every character',
     "One six card deck per civilian, each one built around what that character's "
     'unique trait does.',
     f'''
<div class="panel note">
<p>Every deck here is six cards. Your deck is a pool that in match perk rolls draw from,
so each extra card is one more thing that can come up instead of what you wanted. Six
cards you always want means every roll lands. The game caps deck size and does not
require you to fill it.</p>
</div>

<div class="jump">{jump}</div>
{''.join(build_section(b) for b in BUILDS)}

<h2>Reading the ordering</h2>
<p>The builds are ordered by how much each character's own progressive challenge tree
points them at Michael. Each civilian has fifteen challenges, and we counted the ones
that need you to act against him: downing him, damaging him, stunning him, escaping a
grab, pulling somebody else out of a grab, breaking chase, or baiting him. That measures
what the character was designed to do and says nothing about raw power. Bob leads it and
Tanya sits last, which does not make Tanya weak. It makes her a scout.</p>
''')

# ============================ perks.html ============================
cats = sorted({R.CATEGORY[n] for n in E.PERKS}, key=lambda c: list(R.CATEGORY_LABEL).index(c))
btns = ''.join(f'<button data-cat="{c}" aria-pressed="false">{e(R.CATEGORY_LABEL[c])}</button>'
               for c in cats)

def measured(n):
    v = E.VALUES.get(n)
    if not v: return '<span style="color:var(--ink-faint)">&mdash;</span>'
    return ' '.join(f'<span class="mono">{r[:4]} {p}%</span>' for r, p in v.items())

def perk_row(n):
    d, sc = E.PERKS[n][0], E.PERKS[n][1]
    nt = note(n)
    extra = f'<div style="color:var(--ink-faint);font-size:13px;margin-top:5px">{e(nt)}</div>' if nt else ''
    return (f'<tr data-cat="{R.CATEGORY[n]}" '
            f'data-text="{e((n + " " + d).lower())}">'
            f'<td class="perk">{e(n)}{flat_badge(sc)}</td>'
            f'<td>{e(d)}{extra}</td>'
            f'<td style="white-space:nowrap">{"" if not sc else measured(n)}</td></tr>')

def ladder_cell(n, t):
    v = E.VALUES[n]
    if t in v:
        return f'<td class="num" style="color:var(--pumpkin);font-weight:700">{v[t]}%</td>'
    return '<td class="num" style="color:var(--ink-faint)">&mdash;</td>'

ladder_rows = ''.join(
    '<tr><td class="perk">%s</td>%s</tr>' % (e(n), ''.join(ladder_cell(n, t) for t in R.RARITY))
    for n in sorted(E.VALUES, key=lambda x: (-len(E.VALUES[x]), x)))

deck_rows = ''.join(perk_row(n) for n in sorted(E.PERKS))
trait_rows = ''.join(
    f'<tr><td>{e(civ)}</td>'
    f'<td class="perk">{e(TRAIT_OF[civ])}{flat_badge(E.TRAIT_SCALES[TRAIT_OF[civ]])}</td>'
    f'<td>{e(E.TRAITS[TRAIT_OF[civ]])}</td></tr>'
    for civ, *_ in R.ROSTER)
spec_rows = ''.join(
    f'<tr><td class="perk">{e(k)}</td><td>{e(v)}</td></tr>' for k, v in E.SPECTATOR.items())
C = R.COUNTS

page('perks.html', 'Every perk card | Haddonfield Builds',
     f"{C['total']} perks, described in plain terms",
     'The complete perk list',
     f"All {C['deck']} deck perks, {C['traits']} unique traits and {C['spectator']} "
     'spectator perks, with what each one actually does.',
     f'''
<div class="panel note">
<p>A card marked <span class="flat">FLAT</span> does a fixed thing rather than a
percentage, so a Common copy does the same as a Legendary one and spending Perk Points
upgrading it is wasted.</p>
<p>Percentages shown in the <b>Measured</b> column were read off the cards in game. Most
cards have no figure yet, and nothing here is estimated: a blank means we have not seen
it. See the ladder below.</p>
</div>

<h2>Deck perks</h2>
<p>{C['deck']} cards you can roll, scrap, upgrade and slot into a deck.</p>
<div class="filters">
  <input type="search" id="q" placeholder="Search names and effects" aria-label="Search perks">
  <button data-cat="" aria-pressed="true">All</button>{btns}
  <span class="count" id="cnt"></span>
</div>
<div class="tablewrap"><table id="perktable">
  <thead><tr><th>Card</th><th>What it does</th><th>Measured</th></tr></thead>
  <tbody>{deck_rows}</tbody>
</table></div>

<h2>Unique traits</h2>
<p>{C['traits']} traits for {C['traits']} civilians, one each, always on, never a deck card.
Anything a guide calls a second or third trait is an ordinary deck perk the character
starts with. None of the twelve trait names appears among the {C['deck']} deck perks, so
no card duplicates a trait.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Civilian</th><th>Trait</th><th>What it does</th></tr></thead>
  <tbody>{trait_rows}</tbody>
</table></div>

<h2>Spectator perks</h2>
<p>{C['spectator']} perks you pick after you die, applied to yourself or to the player you are
watching. They cannot go in a deck. Two of them put you back in the match as an authority
figure, which is how the arrest gets the police it needs.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Perk</th><th>What it does</th></tr></thead>
  <tbody>{spec_rows}</tbody>
</table></div>

<h2>The rarity ladder</h2>
<p>Five tiers: {' &middot; '.join(R.RARITY)}.</p>
<p>{e(E.LADDER_NOTE)}</p>
<p>{e(E.LADDER_RULE)}</p>
<p class="count">Every figure below was read off a card in game. Nothing is projected.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Card</th>{''.join(f'<th>{E.NUMERALS[t]} &middot; {t}</th>' for t in R.RARITY)}</tr></thead>
  <tbody>{ladder_rows}</tbody>
</table></div>
<p>{e(E.UPGRADE_NOTE)}</p>
<p>{e(E.WHY_CURVES)}</p>
<p>None of this touches the deck size argument, which is arithmetic about draw pools and does
not care how large any individual effect turns out to be. A card you never want is a bad draw
at every tier.</p>

<h2>The perk economy</h2>
<p>There are two separate rollers and they are easy to confuse. Between matches you spend
Perk Points to add a random card to your collection, and paying more improves the rarity
odds. During a match you earn perk rolls that draw from the deck you brought and apply
whatever comes up.</p>
<p>Card upgrades are temporary, lasting a few matches, so Perk Points spent on an upgrade
are a consumable rather than an investment.</p>
<p>Deck size has a maximum and no minimum. There is a warning for going over the limit and
a counter showing how full your deck is, and nothing anywhere for a deck being too small,
incomplete, or randomly filled. Whatever number your deck screen shows is a ceiling you
are allowed to sit well under.</p>

<script>
(function () {{
  var rows = [].slice.call(document.querySelectorAll('#perktable tbody tr'));
  var btns = [].slice.call(document.querySelectorAll('.filters button'));
  var q = document.getElementById('q'), cnt = document.getElementById('cnt');
  var cat = '';
  function apply() {{
    var term = q.value.trim().toLowerCase(), n = 0;
    rows.forEach(function (r) {{
      var ok = (!cat || r.dataset.cat === cat) && (!term || r.dataset.text.indexOf(term) > -1);
      r.hidden = !ok; if (ok) n++;
    }});
    cnt.textContent = n + ' of ' + rows.length;
  }}
  btns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      cat = b.dataset.cat;
      btns.forEach(function (x) {{ x.setAttribute('aria-pressed', String(x === b)); }});
      apply();
    }});
  }});
  q.addEventListener('input', apply);
  apply();
}})();
</script>
''')
print('generated builds.html, perks.html')

# ============================ index.html ============================
roster_cards = ''.join(
    f'<a href="builds.html#{b["slug"]}">'
    f'<div class="name">{e(b["civ"])}</div>'
    f'<div class="role">{e(b["role"])}</div>'
    f'<div class="trait">{e(TRAIT_OF[b["civ"]])}. {e(E.TRAITS[TRAIT_OF[b["civ"]]])}</div></a>'
    for b in BUILDS)

FACTS = [
 ("01", "His objective is the Residents, not you",
  "Michael is scored on killing the NPC townsfolk, and the game lists killing the four "
  "player civilians as a separate objective marked optional. Yours is to get Residents "
  "out. Every second he spends chasing you is a second off his own win condition, which "
  "is why getting in his way is a real plan rather than a stunt."),
 ("02", "A deck is a pool, not a loadout",
  "During a match you earn perk rolls, and each one draws a card out of the deck you "
  "brought. Every extra card is one more thing that can come up instead of what you "
  "wanted. Six cards you always want beats fifteen where six are good."),
 ("03", "One unique trait each",
  "Twelve traits for twelve civilians. Everything else a guide calls a trait is an "
  "ordinary deck perk the character happens to start with, and none of the twelve trait "
  "names appears among the 62 deck perks."),
 ("04", "You can arrest him",
  "Detaining Michael ends the match on the spot. Police near him fill a detainment meter, "
  "flashlights fill it faster, and once it is full a knockdown opens a long hold "
  "interaction. That makes police perks, lights and Knockout worth more than they look."),
]
facts_html = ''.join(
    f'<div class="fact"><div class="n">{n}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
    for n, t, d in FACTS)
tbl = ''.join(
    f'<tr><td>{e(c[0])}</td><td class="perk">{e(c[1])}</td>'
    f'<td class="num">{c[2]}</td><td class="num">{c[3]}</td>'
    f'<td class="num">{c[4]}</td><td class="num">{c[5]}</td></tr>' for c in R.ROSTER)

page('index.html', 'Haddonfield Builds | Halloween: The Game perk decks',
     'Halloween: The Game',
     'A perk deck for every civilian',
     'Twelve six card decks, each built around what that character&rsquo;s trait does. '
     'No invented perks, and no percentages that nobody can source.',
     f'''
<h2>What drives every build</h2>
<div class="grid four">{facts_html}</div>

<h2>Pick a civilian</h2>
<p>Twelve builds, one per character, each written around what that character's trait
does rather than around a generic best perks list.</p>
<div class="roster">{roster_cards}</div>

<h2>Who the game wants fighting Michael</h2>
<p>Each civilian has fifteen progressive challenges. Counting the ones that need you to
act against Michael directly, by downing him, damaging him, stunning him, escaping a
grab, pulling somebody else out of a grab, breaking chase or baiting him, shows what
each character was designed to do. It measures intent and says nothing about power.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Civilian</th><th>Trait</th><th>vs Michael</th><th>Chase</th><th>Damage</th><th>Down</th></tr></thead>
  <tbody>{tbl}</tbody>
</table></div>
<p>Bob Simms leads it at eleven, and he is the only civilian whose tree covers all three
Stalk marker tiers alongside four combat challenges. Thomas Armitage has zero chase
challenges because Running Back makes them unnecessary: hitting Michael sheds your Stalk
tier, which is what breaking chase would have done anyway.</p>

<h2>About this site</h2>
<p>The builds come from reading what each perk and trait does and working out which
levers matter, rather than from copying a tier list. Every description here is written
for this site in plain terms. Nothing is copied from the game, and no game files, assets
or data exports are hosted or distributed.</p>
<div class="panel warn">
<p>What you will not find here is numbers. The game keeps the actual percentages behind
each effect separately from the effect itself, so the honest position is that the levers
are known and their sizes are not. If a card turns out to be worth three percent, its
place in a deck moves, and this site would be wrong about the ordering.</p>
<p>Civilian stats are absent for the same reason. The four attributes are Capability,
Athleticism, Personality and Resourcefulness, and the numbers behind them are not
something we can stand behind. The stat tables circulating online have no source, so
repeating them here would only launder a guess.</p>
</div>
''')

# ============================ mechanics.html ============================
abil_rows = ''.join(f'<tr><td class="perk">{e(n)}</td><td>{e(d)}</td></tr>' for n, d in E.ABILITIES)
SCORE_GROUPS = [
 ("Fighting him", ["Damaged Michael, at three separate sizes",
                   "Knocked him back, stunned him, disoriented him, blinded him",
                   "Downed him, and assisting somebody else's downing",
                   "Handing a Resident a weapon that they then down him with"]),
 ("Surviving him", ["Breaking chase, scored at three tiers",
                    "Struggling free of a grab, and countering one outright",
                    "Escaping the match, rated from mediocre up to perfect"]),
 ("Ending the match", ["Detaining Michael", "Helping somebody else detain him"]),
 ("Residents", ["Convincing, calming and commanding Residents and Special Targets",
                "Finding them, saving them, escorting them to an escape",
                "Skill checks during conversations, good and perfect"]),
 ("Police", ["Placing a call, rated unconvincing through very convincing",
             "Filling each of the three badge meters, and assisting on one"]),
 ("Objectives", ["Repairing the car, filling its tank, clearing escape blockers, opening an escape",
                 "Repairing comms and restoring power",
                 "Finding escape items and escape routes",
                 "Looting, healing yourself, and distracting him"]),
]
score_html = ''.join(
    f'<h4>{e(t)}</h4><ul>' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>'
    for t, items in SCORE_GROUPS)

page('mechanics.html', 'How the match works | Haddonfield Builds',
     'Stalk, Bloodthirst, detainment',
     'The systems a build has to answer to',
     'Objectives, Stalk, Bloodthirst, Shape Jump denial, the arrest, and what civilians '
     'actually score points for.',
     f'''
<h2>The objectives are not symmetric</h2>
<p>Michael is scored on killing the Residents, meaning the NPC townsfolk who live on the
map. Killing the four of you is a separate objective and the game marks it optional. Your
side is scored on getting Residents out alive, with your own escape as a secondary.</p>
<p>That asymmetry is the reason a harassment build works. Holding his attention is not a
side show, it is denial of the thing he wins with.</p>
<p>The game uses four separate words for people and they are not interchangeable.
Civilians are the four players. Residents are the townsfolk. Special Targets are priority
Residents worth more to both sides. Police are the authority figures the arrest runs on.</p>

<h2>Stalk</h2>
<p>Stalk is the resource Michael spends to kill you, and it has three tiers. Standing near
him builds it passively up to one level. Going into Killer Sense, his first person mask
view, lets him take a single target all the way to tier three, and he builds it faster by
standing still, being close, and using focus.</p>
<p>High Stalk weakens you, marks you for much longer, makes you easier to track, and pays
him a bigger score when he finishes you. The grab prompt is gated on your Stalk level, so
a civilian at tier zero is not grabbable the way a civilian at tier three is.</p>
<p>Shedding a tier scores for you at three separate levels, and most of the roster has it
as a challenge goal. Every card in the stalk category on the perks page is a way of
denying him this resource.</p>

<h2>Bloodthirst</h2>
<p>Bloodthirst is his global power meter and it also has three tiers. It fills from
stalking, grabbing, attacking, killing, and lingering over the bodies he has already made.
As it rises he gets more melee damage, faster movement in Shape Jump, shorter cooldowns,
and at the top tier access to his Bloodthirst executions. It also reveals more of his
tracking, so a high tier Michael can see where his targets are from further away.</p>
<p>It drains. Standing in light costs him tiers, taking damage costs him tiers, and being
knocked down costs him tiers. Every hit you land and every second you hold a flashlight on
him is turning his power meter down, which is why a build that harasses him is doing more
than buying time.</p>

<h2>Shape Jump and how to shut it off</h2>
<p>Shape Jump is his traversal ability. He slips into the shadows, moves invisibly and
quickly, and can pass through unlit doors. It is the single hardest thing about playing
against him, and it has three hard conditions on entering or leaving.</p>
<ul>
  <li>He cannot be standing in light.</li>
  <li>He cannot be in anybody's line of sight.</li>
  <li>Nobody can be standing too close to him.</li>
</ul>
<p>Any one of those denies it on its own. Standing in light, watching him, or simply
crowding him each work. Aura of Awareness widens the third condition, which is the
mechanical basis for body blocking as a tactic. Reality Tear is the exception and ignores
all three, so a Michael holding that ability can always break the lock once.</p>

<h2>His kit</h2>
<div class="tablewrap"><table>
  <thead><tr><th>Ability</th><th>What it does</th></tr></thead>
  <tbody>{abil_rows}</tbody>
</table></div>
<p>In melee he has a light attack, a heavy attack, and a shove. The shove stumbles people
away from him and doubles as a way to interrupt an incoming attack, which is why poise
matters to anybody planning to trade hits with him.</p>

<h2>Detainment</h2>
<p>Detaining Michael ends the match immediately, skipping every escape requirement. It
works like this.</p>
<ol>
  <li>Authority figures near him raise a detainment meter. More of them raise it faster,
      and flashlights on him raise it faster still.</li>
  <li>The meter has to be full.</li>
  <li>He then has to be knocked down.</li>
  <li>Somebody completes a long hold interaction before he recovers.</li>
</ol>
<p>It is a team play. It needs somebody on the phones bringing police, somebody holding a
light, and somebody landing the knockdown. Knockout extends the window for the last step,
and the two respawn perks are how a dead teammate comes back as the officer the whole
thing depends on. A player who has died is not out of the match, they are a component of
the win condition.</p>

<h2>Fear is a lockout</h2>
<p>Fear does not slow you down so much as switch things off. Past a threshold you cannot
use a phone and you cannot hold a conversation, both of which refuse outright rather than
degrading. Police pressure comes from phone calls, so fear reduction is an investment in
the arrest rather than a comfort pick.</p>
<p>Fear also feeds tripping, which Grave Footing reduces, and it interacts badly with
Survival Rage, which pays out only while you are terrified. Do not run Survival Rage
alongside Unphased or Wired.</p>

<h2>What civilians score for</h2>
<p>The scoring table is the clearest statement the game makes about what it wants from
you, and it is broader than most players assume.</p>
{score_html}
<p>Note how much of that is fighting him. Downing, stunning and blinding Michael are all
scored, at multiple tiers, which is why the older advice that melee is a losing trade is
wrong.</p>
''')
print('generated index.html, mechanics.html')
