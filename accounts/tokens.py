from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class EmailAuthToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.email_auth)


account_activation_token = EmailAuthToken()
