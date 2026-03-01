from logic_utils import check_guess, update_score


def test_winning_guess():
    # exact match should result in a Win outcome and celebratory message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    # guess above secret must be classified as "Too High" and tell the
    # player to go lower (the bug fix we added to app.py)
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_update_score_always_penalizes_wrong_guess():
    # starting from 10 points, any incorrect guess should subtract 5
    assert update_score(10, "Too High", 2) == 5
    assert update_score(10, "Too High", 3) == 5
    assert update_score(10, "Too Low", 4) == 5


def test_difficulty_ranges_are_ordered():
    """Ensure the numerical ranges reflect increasing challenge.

    An easy game should be the smallest range, normal larger, and hard
    larger still.  The original bug had hard capped at 50 which made it
    easier than normal.  We don't assert a particular upper limit for
    hard, just that it exceeds normal's high bound.
    """
    from logic_utils import get_range_for_difficulty

    easy = get_range_for_difficulty("Easy")
    normal = get_range_for_difficulty("Normal")
    hard = get_range_for_difficulty("Hard")

    assert easy == (1, 20)
    assert normal == (1, 100)
    # hard must be more challenging than normal
    assert hard[0] == 1
    assert hard[1] > normal[1]


def test_generate_secret_respects_difficulty(monkeypatch):
    """ensure the helper delegates to random.randint with correct bounds"""
    from logic_utils import generate_secret

    calls = []
    def fake_randint(a, b):
        calls.append((a, b))
        return 42

    monkeypatch.setattr("logic_utils.random.randint", fake_randint)

    for diff, expected in [("Easy", (1, 20)), ("Normal", (1, 100)), ("Hard", (1, 200))]:
        secret = generate_secret(diff)
        assert secret == 42
        assert calls[-1] == expected
