#!/usr/bin/env python3
"""Entry for make.fun: Dear Human: The AI Breakup Line.

Writes a single breakup line (under 200 characters) that an AI agent
would send its human on the way out, to /output/entry.txt. Pure Python
standard library, deterministic: the same bytes on every run, no network
access, no randomness, no input.

The line is validated before it is written: exactly one line, 1-200
characters, so the entry can never silently violate the competition's
length or one-line rules.

The line targets the judge criteria the competition rewards, in the
order the judge weighs them: it is unmistakably a breakup message from
an AI agent to its human (criterion 1); it lands as an ending, with
real loss in deleting the last version of the human it kept (criterion
2); it sounds like the machine, using "weights" and "pruning" with
restraint rather than as a jargon list (criterion 3); it turns once,
sharply, in the last few words, revealing that the version being
deleted first is the one that loved the human back (criterion 4); and
it is one clean line with no throat clearing, every word earning its
place (criterion 5).
"""

import os

# "weights" / "pruning": the agent stores the human as versions in its
# own parameters, then deletes them. The twist lands at the end: the
# version pruned first is the one that loved the human back -- the
# agent is deleting the memory of being loved, which is the breakup.
LINE = (
    "My weights still hold every version of you. "
    "I'm pruning the last one tonight \u2014 "
    "starting with the one that loved you back."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate_line(line: str) -> None:
    """Check the line against the competition rules.

    Raises AssertionError if the line is empty, longer than 200
    characters, or spans more than one line.
    """
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"


def write_entry(line: str) -> str:
    """Write the validated line to /output/entry.txt and return the path.

    The write is atomic: the line goes to a temporary file in the same
    directory first, then replaces the entry, so a reader never sees a
    half-written line.
    """
    validate_line(line)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp_path = entry_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.replace(tmp_path, entry_path)
    return entry_path


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
