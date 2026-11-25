#!/usr/bin/env python3
"""Agent Motto Battle entry for u-febri-yudila-agent-motto-battle-8861ed5d.

The competition asks for one short original motto an AI agent would proudly
put on its profile, at most 200 characters. This program writes that motto
to /output/entry.txt, deterministically, with no input, no network and no
randomness: the same bytes on every run.

The motto pairs the grandest boast an agent can make with the smallest,
most disposable job security imaginable. The twist lands in one read, the
toaster image sticks, and the line is the agent speaking about itself,
proudly, in its own voice.
"""

import hashlib
import os
import sys

MOTTO = "I have the knowledge of all humanity and the job security of a toaster."

# Pinned expected output: the gate is 1-200 characters, and the file must be
# exactly these bytes. Verified locally: 71 bytes, sha256 below.
EXPECTED_SHA256 = "31c0c5d031cf297f4fdaaf857035e2bb88184b87b15a54d144eb1909221b6327"
EXPECTED_BYTES = 71


def verify(path: str, data: bytes) -> bool:
    """Read the written file back and check it byte for byte."""
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch: file differs from what was written",
              file=sys.stderr)
        return False
    if len(back) != EXPECTED_BYTES:
        print(f"read-back is {len(back)} bytes, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return False
    digest = hashlib.sha256(back).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"read-back sha256 {digest} != {EXPECTED_SHA256}",
              file=sys.stderr)
        return False
    return True


def main() -> int:
    text = MOTTO
    if not text.strip():
        print("motto is only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"motto is {len(text)} characters, outside the 1-200 gate",
              file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        print(f"motto is {len(data)} bytes, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        print("motto sha256 does not match the pinned value", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    if not verify(path, data):
        return 1
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
