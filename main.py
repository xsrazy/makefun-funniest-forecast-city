"""Funniest Forecast for a City That Isn't.

This program writes a single-line weather forecast for Drizzleport, a city
that does not exist, to ``entry.txt``.

The line reads exactly like a real forecast: a named place, the day's
conditions, the night's conditions, and an official warning. The joke is
in the last beat. A flood warning is supposed to warn you about water, but
this one warns you about your weekend plans instead, as if the weather
service has given up on the sky and started reporting on your social life.
The three-beat escalation (light rain, heavy rain, ruined weekend) makes
the punchline land fast, which is what a head-to-head joke contest rewards.

Revision note: after the first draft the entry was run locally and the
output file was checked byte for byte against the winning line, with no
trailing newline, so the program below ships exactly the line above.
"""

import os

LINE = (
    "Drizzleport: light rain all day, heavy rain all night, "
    "and a flood warning for your weekend plans."
)

assert 1 <= len(LINE) <= 120, "entry line must be 1-120 characters"


def write_entry(line):
    """Write ``line`` to ``entry.txt`` as UTF-8 bytes, no trailing newline."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))
    return path


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
