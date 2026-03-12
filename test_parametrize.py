import pytest

# --- Basic parametrize
@pytest.mark.parametrize("number, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
])
def test_square(number, expected):
    assert number ** 2 == expected


# --- Real-world QA example: password validation ---
def is_valid_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password)

@pytest.mark.parametrize("password, expected_result", [
    ("Short1", False),      # too short
    ("alllower", False),     # no uppercase
    ("ValidPass1", True),    # valid
    ("ALLCAPS12", True),  # valid
])
def test_password_validation(password, expected_result):
    assert is_valid_password(password) == expected_result


# --- QA tool list example ---
@pytest.mark.parametrize("tool", [
    "Playwright",
    "Selenium",
    "pytest",
])
def test_tool_is_string(tool):
    assert isinstance(tool, str)
    assert len(tool) > 0
