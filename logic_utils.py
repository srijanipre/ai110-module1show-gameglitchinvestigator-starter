import random


def get_range_for_difficulty(difficulty: str):
    #FIXME: the hard difficulty was previously capped at 50, which made it easier than normal.  This is incorrect; hard should be more challenging than normal.  Adjust the upper bound to fix this bug.
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # hard should present a larger numeric span than normal; the
        # previous value of 1‑50 made the hard level easier than normal
        # and is therefore incorrect.  Use a bigger upper bound so that
        # the secret number is harder to guess.
        return 1, 200
    return 1, 100


def generate_secret(difficulty: str):
    """Pick a random secret number for the given difficulty.

    The number is drawn using :func:`random.randint` with the bounds
    returned by :func:`get_range_for_difficulty`.  Extracting this into a
    dedicated helper makes it easier to test the range logic.
    """
    low, high = get_range_for_difficulty(difficulty)
    return random.randint(low, high)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns (ok, value, error_message) tuple suitable for the app.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare ``guess`` against ``secret`` and return a 2‑tuple
    ``(outcome, message)``.

    ``outcome`` is one of "Win", "Too High" or "Too Low".  The accompanying
    hint message should align with the outcome: when the guess exceeds the
    secret the player is told to "Go LOWER!", and when it is below the secret
    they are told to "Go HIGHER!".  This corrects the reversed hints bug.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # guess too large
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # secret might be stored as string in session state; convert guess
        # to string for comparison in that case.
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # a wrong guess (Too High or Too Low) should always cost the player 5
    # points.  previously there was a parity check that rewarded even
    # attempts with +5, which caused the bug described in reflection.md.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
