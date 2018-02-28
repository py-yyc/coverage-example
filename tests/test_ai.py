
import ttt


def test_create_invalid():
    try:
        ai = ttt.create_ai_for('z')
        assert False, "Should fail"
    except ValueError as e:
        assert "must be 'x' or 'o'" in str(e)

