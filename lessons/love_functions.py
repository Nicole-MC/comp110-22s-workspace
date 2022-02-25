"""Love function."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    heart: int = 0
    while heart < n:
        love_note += love(to) + "\n"
        heart = heart + 1
    return love_note 
