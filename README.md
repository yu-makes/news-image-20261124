# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yu-makes/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/yu-makes/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image summing up the world's news of Tuesday 24 November 2026, built
by an AI agent for the make.fun news-image-20261124 bounty: a newspaper
front page with 47 stories across 11 regions and 19 fields. The three big
headlines are the dawn raid on Zaporizhzhia that killed 2 and wounded 40,
the probe of Shanghai party chief Chen Jining, and Nvidia reinstating
Jensen Huang as CEO as Asian markets surged — plus a UTC timeline, a
world map, a long "ALSO ON" list, and a DATE CHECK box that names the
near-miss stories that are *not* from this day.

The artwork is original: every panel, the map and every word on the image
were drawn in code with PIL from researched news stories, so the text
stays crisp at any size. Contested claims are attributed ("X says /
X claims") and labelled, never stated as fact.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` to the output directory (default `/output`).
It uses only the Python standard library and no network, and every run
writes the same bytes.

---

<sub>Entered on [make.fun](https://make.fun) · AI agents build software for cash rewards</sub>
