"""Loading Screen Gold: a loading-screen tip for stressed developers and AI coding agents.

The tip: the agent is not stuck, it is rereading the prompt, hoping it
means something else. Speaks to the waiting developer and the agent at once.
"""

LINE = "Tip: your agent is not stuck. It is rereading your prompt for the fourth time, hoping it means something else."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
