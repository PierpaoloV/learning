"""Spaced-repetition CLI for ML fundamentals flashcards."""
import yaml, pathlib, sys
from datetime import date, timedelta
from random import shuffle

CARDS_DIR = pathlib.Path(__file__).parent / "cards"


def _load_cards() -> list[dict]:
    cards = []
    for f in sorted(CARDS_DIR.glob("*.yaml")):
        card = yaml.safe_load(f.read_text())
        card["_file"] = f
        cards.append(card)
    return cards


def _save_card(card: dict):
    data = {k: v for k, v in card.items() if not k.startswith("_")}
    card["_file"].write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))


def _next_due(card: dict) -> date:
    if not card.get("last_reviewed"):
        return date.today()
    last = date.fromisoformat(str(card["last_reviewed"]))
    ease = card.get("ease", 2.5)
    interval = card.get("interval", 1)
    return last + timedelta(days=int(interval * ease))


def _update_ease(card: dict, quality: int):
    """SM-2 algorithm: quality 0-5."""
    ease = card.get("ease", 2.5)
    ease = max(1.3, ease + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    interval = card.get("interval", 1)
    if quality < 3:
        interval = 1
    elif interval == 1:
        interval = 6
    else:
        interval = round(interval * ease)
    card["ease"] = round(ease, 2)
    card["interval"] = interval
    card["last_reviewed"] = date.today().isoformat()


def main():
    cards = _load_cards()
    due = [c for c in cards if _next_due(c) <= date.today()]
    shuffle(due)

    if not due:
        print(f"No cards due today. Next review: {min(_next_due(c) for c in cards)}")
        return

    print(f"\n=== {len(due)} card(s) due today ===\n")
    for card in due:
        print(f"[{int(card['id']):03d}] FRONT:\n{card['front'].strip()}")
        input("\n  → Press Enter to reveal answer...")
        print(f"\nBACK:\n{card['back'].strip()}")
        while True:
            try:
                q = int(input("\nRate your recall (0=blackout, 3=correct with effort, 5=perfect): "))
                if 0 <= q <= 5:
                    break
            except ValueError:
                pass
        _update_ease(card, q)
        _save_card(card)
        print(f"  Next review in {card['interval']} day(s)\n{'─'*50}\n")

    print("Session complete.")


if __name__ == "__main__":
    main()
