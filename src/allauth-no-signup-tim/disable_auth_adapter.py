from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class DisableSignupAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, req):
        return False

class EnableSocialSignupAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, req, socialaccount):
        return True
