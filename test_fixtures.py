import pytest

@pytest.fixture
def sample_user():
    user = {
        "name": "RJ",
        "role": "QA Engineer",
        "experience_years": 7
    }
    return user

@pytest.fixture
def test_tools():
    return ["Playwright", "Selenium", "pytest", "AccelQ"]

def test_user_has_name(sample_user):
    assert sample_user["name"] == "RJ"

def test_user_is_experienced(sample_user):
    assert sample_user["experience_years"] >= 5

def test_playwright_in_tools(test_tools):
    assert "Playwright" in test_tools

def test_tool_count(test_tools):
    assert len(test_tools) == 4
