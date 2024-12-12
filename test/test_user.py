


from app.models.models import User
import unittest

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User(username="testuser", email="test@example.com", password="securepassword")

    def test_email_is_valid(self):
        self.user.email = "test@example.com"
        self.assertIn("@", self.user.email)
        self.assertIn(".", self.user.email)

    def test_email_is_invalid(self):
        self.user.email = "invalid-email"
        self.assertNotIn("@", self.user.email)
        self.assertNotIn(".", self.user.email)

if __name__ == "__main__":
    unittest.main()
