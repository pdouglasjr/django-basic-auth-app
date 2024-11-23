from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        
        # create user
        user = User.objects.create_user(email="normal@user.com", username="normaluser", password="foo")
        
        # test cases
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.username, "normaluser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        
        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email="", username="")

        with self.assertRaises(ValueError):
            User.objects.create_user(email="", username="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()

        # create admin user
        admin_user = User.objects.create_superuser(email="super@user.com", username="superuser", password="foo")

        # test cases
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.username, "superuser")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass

        #
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com",
                username="superuser",
                password="foo",
                is_superuser=False,
            )