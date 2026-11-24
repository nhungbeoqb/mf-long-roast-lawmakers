#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Chosen line (v2, revised): same escalation, plus a petty bureaucratic
deadline — "preferably before lunch" — so the punch lands on the
lawmaker treating his own incompetence as his staff's urgent task.
"""

import os

ENTRY = (
    "The senator who wrote the AI safety bill still emails his staff "
    "a Word file called FINAL_final_v7 and asks them to print it, "
    "sign it, scan it back, and explain why the PDF button keeps "
    "hiding from him, preferably before lunch."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
