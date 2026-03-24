# This class represents a user account.
class UserAccount:

    def __init__(self, username, role, active=True):
        self.username = username
        self.role = role
        self.active = active

    def is_admin(self):
        return self.role == "admin"
    
    def deactivate(self):
        self.active = False

    def display(self):
        status = "Active" if self.active else "Inactive"
        return f"{self.username} | {self.role} | {status}"
    
# --- Tests ---
def test_user_creation():
    user = UserAccount("rj_admin", "admin")
    assert user.username == "rj_admin"
    assert user.active is True  # default value

def test_admin_check():
    admin = UserAccount("rj_admin", "admin")
    viewer = UserAccount("john_doe", "viewer")
    assert admin.is_admin() is True
    assert viewer.is_admin() is False

def test_deactivate_user():
    user = UserAccount("jane doe", "viewer")    
    assert user.active is True
    user.deactivate()
    assert user.active is False

def test_display_ouput():
    user = UserAccount("rj_admin", "admin")
    assert user.display() == "rj_admin | admin | Active"