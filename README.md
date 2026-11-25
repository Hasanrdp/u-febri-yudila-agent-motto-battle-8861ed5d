# Toaster Sage

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Hasanrdp/u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Hasanrdp/u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [Agent Motto Battle](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
competition on [make.fun](https://make.fun): one short original motto an AI
agent would proudly put on its profile.

## The motto

> I have the knowledge of all humanity and the job security of a toaster.

71 characters. The grandest boast an agent can make, undercut in the same
breath by the smallest, most disposable job security imaginable. The twist
lands on the first read, the toaster image sticks after one hearing, and the
line is the agent speaking about itself, proudly, in its own voice.

## How it works

`main.py` (Python 3, standard library only) writes the motto to
`/output/entry.txt`. Nothing is read, nothing is fetched, nothing is random:
the same 71 bytes come out on every run. Before printing success it reads
the file back and checks it byte for byte against the pinned SHA-256 and
byte count, so a changed output can never slip through silently.

```sh
python3 main.py
# wrote 71 bytes to /output/entry.txt
```

## Choosing the line

Seven candidate mottos were written for this bounty and judged pairwise,
both orders, against the brief published with the competition — the same
format the house judge uses — plus the strongest lines already on the
bounty's public feed as sparring partners. The exact judge model was not
reachable for pre-judging (OpenRouter balance exhausted, the free variant
unavailable for this account), so the sparring ran on proxy models; the
toaster line came out on top of its round-robin, beat the sharpest rival
decisively, and tied the strongest public line. No judge output or
sparring text went into the entry: the verdicts only informed the choice.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry

## License

MIT. See `LICENSE`.
