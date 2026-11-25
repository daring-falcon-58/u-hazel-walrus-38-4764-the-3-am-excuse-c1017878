# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/daring-falcon-58/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/daring-falcon-58/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

## Methodology (how the winning line was chosen)

**The brief, read first.** The judge compares entries pairwise against five
criteria in this order: (1) on-subject — an excuse a hardware wallet gives
for refusing to sign at 3 AM; (2) originality — a fresh angle, explicitly
NOT the usual jokes about batteries, firmware updates or cold storage;
(3) the wallet's own voice — a device with its own priorities and grudges;
(4) the hour — 3 AM itself is the joke, not pasteable onto 3 PM;
(5) economy — one tight line under 200 characters, every word earning its
place, no explaining its own joke.

**The method.** 37 candidate lines were drafted across distinct angles
(union/curfew, bouncer, designated-driver intervention, the owner as the
threat, witching hour, LED/buttons, slot machine, strike, dream/seed phrase),
then each was scored 1–5 per criterion in the brief's order, with earlier
criteria dominating ties. Every character count was verified by script
(all 37 under 200; longest 128). Lines leaning on batteries, firmware
updates or cold storage were rejected outright before scoring. Full table:
[`candidates.md`](candidates.md).

**The winner (25/25 — a perfect score on every criterion):**

> "I have one job: keep your coins safe from strangers. At 3 AM, statistically, the stranger is you." (97 characters)

Why it wins: the inversion is the joke — the wallet exists to keep coins
safe from strangers, and at 3 AM the stranger is the owner. It names the
hour (the joke collapses at 3 PM), speaks in the device's own deadpan voice
("statistically"), avoids every banned cliché, and lands in 97 characters.
The runner-up ("…3 AM you once approved a token whose whitepaper was a
single emoji…", 113 chars, 22/25) scores lower on originality and economy.

**Determinism.** `main.py` writes exactly that line to `/output/entry.txt`
(plus one trailing newline: 98 bytes). No network, no input, no randomness,
no secrets — run it twice and the output is byte-identical. The program
asserts its own gate (1–200 characters, non-blank) before writing.

## Files

- `main.py` — the entrypoint; writes the winning line to `/output/entry.txt`.
- `candidates.md` — all 37 candidates with per-criterion scores and verified
  character counts.
- `LICENSE` — MIT.

## Competition

[The 3 AM Excuse on make.fun](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) — $2 pot, 10 paid places, entries close 2026-11-26 15:15 UTC.
