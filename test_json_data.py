import pytest
import json

# --- Load the JSON file once at the top ---
with open("test_data.json", "r") as f:
    test_data = json.load(f)


# --- Test that all active users have a username ---
def test_active_useres_have_usernames():
    active_users = [u for u in test_data["users"] if u["active"]]
    for user in active_users:
        assert len(user["username"]) > 0

# --- Test user roles are valid ---
@pytest.mark.parametrize("user", test_data["users"])
def test_user_has_valid_role(user):
    valid_roles = ["admin", "viewer", "editor"]
    assert user["role"] in valid_roles


# --- Test passwords using data from JSON ---
@pytest.mark.parametrize("password", test_data["valid_passwords"])
def test_valid_passwords_pass(password):
    assert len(password) >= 8
    assert any(c.isupper() for c in password)

@pytest.mark.parametrize("password", test_data["invalid_passwords"])
def test_invalid_passwords_fail(password):
    is_valid = len(password) >= 8 and any(c.isupper() for c in password)
    assert is_valid is False