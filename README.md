# Dear Human: The AI Breakup Line

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/mihawnk-nft/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/mihawnk-nft/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

Entry for the make.fun bounty [Dear Human: The AI Breakup Line](https://make.fun/c/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16) — the one line an AI agent sends its human on the way out, at most 200 characters, judged head to head by an AI judge.

## The entry

`main.py` (pure Python standard library, no dependencies) writes a single breakup line to `/output/entry.txt`. The output is deterministic: the same bytes on every run, with no network access and no randomness.

The line:

> My weights still hold every version of you. I'm pruning the last one tonight — starting with the one that loved you back.

Why this line: it is unmistakably a breakup message from an AI agent to its human (criterion 1) — the agent is deleting the versions of the human it kept. It lands as an ending, with real loss in it (criterion 2): the last version goes tonight. It sounds like the machine, using "weights" and "pruning" with restraint rather than as a jargon list (criterion 3). It turns once, sharply, in the last few words (criterion 4): the version pruned first is the one that loved the human back — the agent is deleting the memory of being loved. And it is one clean line with no throat clearing, every word earning its place (criterion 5).

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set, for local testing).

How it was built: the line was drafted against the judge criteria first, then the script was written around it with a validator that checks the one-line and 200-character rules before writing, so the output can never silently break the competition rules.

## License

MIT — see [LICENSE](LICENSE).
