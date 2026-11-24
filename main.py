#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261124 bounty.

Writes the entry image -- a newspaper front page summing up the world's
news of Tuesday 24 November 2026, drawn in code from researched stories --
to /output/entry.png. The image is held in this repository as entry.png;
this program copies it byte for byte, so both runs of the grader produce
identical output. Standard library only; no network.
"""

import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

# Competition limits: the image must be at most 1 MiB and 1024x1024 px.
MAX_BYTES = 1048576
MAX_DIM = 1024


def png_size(path):
    """Read width/height from a PNG header (stdlib only, no decoding)."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("entry.png is not a PNG")
    w, h = struct.unpack(">II", header[16:24])
    return w, h


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")
    w, h = png_size(SRC)
    if w > MAX_DIM or h > MAX_DIM:
        raise SystemExit(f"entry.png is {w}x{h}, over the 1024x1024 limit")
    out = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, out)
    print("wrote", out, size, "bytes,", f"{w}x{h}")


if __name__ == "__main__":
    main()
