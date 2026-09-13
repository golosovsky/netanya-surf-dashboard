#!/usr/bin/env python3
"""Unit checks for Surf / SUP / Neither thresholds."""

SURF_MIN_CM = 60
SUP_MAX_CM = 20


def recommend(cm: float | None) -> str:
    if cm is None:
        return "Neither"
    if cm >= SURF_MIN_CM:
        return "Surf"
    if cm <= SUP_MAX_CM:
        return "SUP"
    return "Neither"


EXAMPLES = [
    (10, "SUP"),
    (20, "SUP"),
    (21, "Neither"),
    (40, "Neither"),
    (59, "Neither"),
    (60, "Surf"),
    (70, "Surf"),
]


def main() -> None:
    for cm, expected in EXAMPLES:
        got = recommend(cm)
        assert got == expected, f"{cm}cm → {got}, expected {expected}"
        print(f"OK  {cm:3d} cm → {got}")
    print("All threshold assertions passed.")


if __name__ == "__main__":
    main()
