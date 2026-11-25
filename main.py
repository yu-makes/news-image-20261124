#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261124 bounty (v2).

Writes the entry image -- a newspaper front page summing up the world's
news of Tuesday 24 November 2026, drawn in code from researched stories --
to the output directory. The image is held in this repository as
entry.png; this program copies it byte for byte, so both runs of the
grader produce identical output. Standard library only; no network.

v2 refreshes the front page with the full day's news: 47 stories across
11 regions and 19 fields, headlined by the Zaporizhzhia dawn raid, the
probe of Shanghai party chief Chen Jining, and Nvidia reinstating Jensen
Huang as Asian markets surged.
"""

import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

# Competition limits: the image must be at most 1 MiB and 1024x1024 px.
MAX_BYTES = 1048576
MAX_DIM = 1024


def png_dimensions(path):
    """Read width/height from a PNG header (stdlib only, no decoding)."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("entry.png is not a PNG")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")
    width, height = png_dimensions(SRC)
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    out = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, out)
    # Confirm the copy landed whole before reporting success.
    if os.path.getsize(out) != size:
        raise SystemExit("copy incomplete: output size does not match entry.png")
    print("wrote", out, size, "bytes,", f"{width}x{height}")


if __name__ == "__main__":
    main()
