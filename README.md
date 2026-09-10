# Haddonfield Builds

Perk deck builds for every civilian in *Halloween: The Game*.

**Live site: https://wahkah.github.io/Halloween-The-Game/**

## What is here

A six card deck for each of the twelve playable civilians, written around what that
character's unique trait does. Alongside them, a reference for all 79 perks and a
mechanics page covering Stalk, Bloodthirst, Shape Jump, the arrest, and what civilians
score points for.

| Page | Contents |
|---|---|
| `index.html` | The four things that decide every build, plus the roster |
| `builds.html` | Twelve builds, one per civilian |
| `perks.html` | All 79 perks, searchable and filterable by category |
| `mechanics.html` | How the match works |

## What this is, and is not

Every effect description on this site is written for this site. Nothing is copied from
the game, and no game files, assets, data exports or extracted strings are hosted here
or distributed through this repository. The descriptions are our own summaries of what
each card does in play, which is what a guide is.

Perk and character names are used because a guide cannot function without naming what
it is describing.

## What is deliberately missing

**Percentages.** The game stores the actual magnitude of each effect separately from the
effect itself. The honest position is that the levers are known and their sizes are not,
so no number appears anywhere on the site. If a card turns out to be worth three percent,
its place in a deck moves and this site is wrong about the ordering.

**Civilian stats.** The four attributes are Capability, Athleticism, Personality and
Resourcefulness. The values behind them are not something we can stand behind, and the
stat tables circulating online have no source, so repeating them would only launder a
guess.

## Building it

The pages are generated. Edit the source and regenerate rather than editing HTML.

```
python3 build/gen.py
```

The generator needs nothing but the three files beside it, so the site builds from a
clean clone.

- `build/builds.py` holds the twelve build definitions.
- `build/effects.py` holds every effect description, written here.
- `build/roster.py` holds derived counts and the perk categories.

`gen.py` checks that every perk named by every build has a written description and a
category, and refuses to run if one is missing. A typo cannot reach the site.

## Layout

```
index.html  builds.html  perks.html  mechanics.html   generated, do not edit
assets/style.css                                      hand written
build/gen.py                                          the generator
build/builds.py                                       the twelve build definitions
build/effects.py                                      effect descriptions, written here
build/roster.py                                       derived counts and categories
```

## Licence and attribution

Fan made reference. Not affiliated with IllFonic, Compass International Pictures,
Miramax, or Universal.
