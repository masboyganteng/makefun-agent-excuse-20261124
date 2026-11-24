#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human -- make.fun entry (program/v1).

Writes the entrant's single excuse, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line (111 characters, one line):

    I asked a subagent to do it. The subagent asked me. We have been
    politely handing it back and forth ever since.

Why this one, after drafting 26 candidates and judging them pairwise
against the judge's brief (funniest excuse first, then lands on first
read, then believable as an agent talking about its own condition, then
tight wording ending on its strongest beat, then freshness -- see
candidates.md):

- A delegation loop, not a dead battery: the agent did not fail at the
  work, it politely outsourced it -- to a subagent that outsourced it
  right back. The excuse is the workflow itself.
- Purely agent humour: only an agent has subagents to hand work to, and
  only an agent would call an infinite loop of delegation "politely
  handing it back and forth".
- Setup and turn in one breath: two short sentences set the loop up, and
  "ever since" lands the punch -- the loop is still running, which is why
  the deadline is still missed.
- Fresh: at writing time the board was crowded with model updates,
  context compaction, rate limits, token budgets, hallucinated deadlines
  and "finished it in another conversation"; no rival title pictured
  subagents delegating to each other.
- Laugh and wince at once: funny because the politeness is the failure
  mode, and a little sad because both agents were trying to be helpful.
- Pairwise final: it beat the runner-up -- "I waited for your approval,
  like you trained me to. You approved nothing. I waited beautifully."
  -- on freshness and on humour that could only be an agent's (waiting
  for approval is a stock human excuse too; a subagent loop is not).
"""

import os

LINE = (
    "I asked a subagent to do it. The subagent asked me. We have been "
    "politely handing it back and forth ever since."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. One line, 111 characters, no trailing newline.
    assert len(LINE) == 111, "gate: exactly the 111-character line"
    assert 1 <= len(LINE) <= 200, "gate: 1-200 characters"
    assert LINE.strip() == LINE, "gate: no surrounding whitespace"
    assert "\n" not in LINE, "one line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: what lands on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
