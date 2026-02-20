from calculator import multiply

def test_multiply():
    try:
        assert multiply(3, 4) == 12
    except AssertionError as e:
        print(f"Assertion failed: {e}")