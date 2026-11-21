[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/twitterchi00-ops/tiny-chess-4kb/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/twitterchi00-ops/tiny-chess-4kb/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# Tiny Chess — one Python file, 4 KB, plays chess

This is my entry for the make.fun bounty `tiny-chess-01`: build
the strongest chess engine that fits in 4 KB of Python. The whole
engine is `main.py` (4,070 bytes). It uses only the Python 3.13
standard library, no third-party packages, no network, no clock.

## What is inside

The board is 0x88. The search is negamax alpha-beta with
iterative deepening, capped at 40,000 nodes per move, so a move
never runs past the 10-second limit. On top of that: null-move
pruning, a quiescence search that looks at captures and at every
check evasion, MVV-LVA ordering, two killer moves per ply, and a
transposition table that only orders moves (it never returns a
stored value). The root move list starts with the previous
iteration's best move, and the loop stops as soon as a forced mate
is found. The evaluation is material plus simple piece-square
terms: how far pawns have advanced, knight and bishop centrality,
the bishop pair, and a king term that likes the castled squares
(+20) and dislikes a king that has wandered (+10 a rank).

The bot talks to the make.fun environment over HTTP: it answers
`POST /game` and `POST /move` with UCI moves. Given the same
position it always answers the same move.

## Measured here (Python 3.12, this machine)

- Perft: 18 out of 18 reference positions agree with the
  published node counts (start position to depth 4, Kiwipete
  to depth 3, and the rest).
- Practice trials against the kit's own environment server and
  its official scorer. Trial-0 came out **3 wins, 0 draws,
  3 losses, Elo 1,279**: it checkmated the depth-2, depth-3
  and depth-4 anchors, and lost to the nodes-100k, nodes-250k
  and nodes-500k anchors. Across all three practice trials
  (18 games) the mean is Elo 995. The practice floor is 1,154.

## How to submit

This bounty only accepts entries built in a recorded session of
a coding agent (Claude Code, Codex, Cursor, Superbot, or similar).
The repository has to be yours on GitHub, and it has to be
created after the competition opened.
