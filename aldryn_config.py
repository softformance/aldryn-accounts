# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from aldryn_client import forms


class Form(forms.BaseForm):

    use_profile_apphooks = forms.CheckboxField(
        "Use profile app hooks",
        help_text=("Plug aldryn profile views as an app hook."
                   "If not checked - you need to add aldryn-accounts urls"
                   "to your project core urls manually."),
        required=False,
        initial=True,
    )
    open_signup = forms.CheckboxField(
        "Signup is open",
        help_text=("whether any user may signup. If set to False only "
                   "users with an invite code may sign up."),
        required=False,
        initial=True,
    )
    notify_password_change = forms.CheckboxField(
        "Notify password change",
        help_text=("whether a confirmation email should be sent out "
                   "whenever the password is changed"),
        required=False,
        initial=True,
    )
    password_change_redirect_url = forms.CharField(
        "Password change redirect url",
        help_text=(
            "Where to redirect users after a successful changed password. "
            "Leave empty for default."),
        required=False,
        initial='',
    )
    email_confirmation_email = forms.CheckboxField(
        "send confirmation email",
        help_text=(
            "Whether to send out a confirmation email when a user signs up"),
        required=False,
        initial=True,
    )
    email_confirmation_expire_days = forms.NumberField(
        "Email confirmation expires after, days",
        help_text="How long a confirmation email code is valid.",
        min_value=1,
        max_value=9999,
        initial=3,
    )
    restore_password_raise_validation_error = forms.CheckboxField(
        "Restore password raise validation error",
        help_text=(
            "Whether to raise validation error when user resotres password."),
        required=False,
        initial=True,
    )
    user_display_fallback_to_username = forms.CheckboxField(
        "User display name fallback to username",
        help_text=(
            "Whether to fallback to username when displaying a user."),
        required=False,
        initial=False,
    )
    user_display_fallback_to_pk = forms.CheckboxField(
        "User display fallback to pk",
        help_text=(
            "Whether to fallback to user id when displaying a user."),
        required=False,
        initial=False,
    )
    login_redirect_url = forms.CharField(
        "Login redirect url",
        help_text=(
            "Where to redirect users after a successful login. "
            "Warning! Should be a valid url, otherwise you will get "
            "404 errors."),
        required=True,
        initial='/',
    )
    signup_redirect_url = forms.CharField(
        "Signup redirect url",
        help_text=(
            "Where to redirect users after a sign up, Use view name from urls. "
            "please make sure that this view can be reversed, "
            "include namespace if needed."),
        required=True,
        initial='accounts_profile',
    )
    display_email_notifications = forms.CheckboxField(
        "Display not confirmed emails notification",
        help_text=(
            "Whether to display not confirmed emails notification on "
            "the top of the page."),
        required=False,
        initial=True,
    )
    display_password_notifications = forms.CheckboxField(
        "Display 'password not set' notification",
        help_text=(
            "Whether to display 'password not set' notification on "
            "the top of the page."),
        required=False,
        initial=True,
    )

    def to_settings(self, data, settings):
        settings['ALDRYN_ACCOUNTS_USE_PROFILE_APPHOOKS'] = data['use_profile_apphooks']
        settings['ALDRYN_ACCOUNTS_OPEN_SIGNUP'] = data['open_signup']
        settings['ALDRYN_ACCOUNTS_NOTIFY_PASSWORD_CHANGE'] = data['notify_password_change']
        settings['ALDRYN_ACCOUNTS_PASSWORD_CHANGE_REDIRECT_URL'] = data['password_change_redirect_url']
        settings['ALDRYN_ACCOUNTS_EMAIL_CONFIRMATION_EMAIL'] = data['email_confirmation_email']
        settings['ALDRYN_ACCOUNTS_EMAIL_CONFIRMATION_EXPIRE_DAYS'] = data['email_confirmation_expire_days']
        settings['ALDRYN_ACCOUNTS_RESTORE_PASSWORD_RAISE_VALIDATION_ERROR'] = data['restore_password_raise_validation_error']
        settings['ALDRYN_ACCOUNTS_USER_DISPLAY_FALLBACK_TO_USERNAME'] = data['user_display_fallback_to_username']
        settings['ALDRYN_ACCOUNTS_USER_DISPLAY_FALLBACK_TO_PK'] = data['user_display_fallback_to_pk']
        settings['ALDRYN_ACCOUNTS_LOGIN_REDIRECT_URL'] = data['login_redirect_url']
        settings['ALDRYN_ACCOUNTS_SIGNUP_REDIRECT_URL'] = data['signup_redirect_url']
        settings['ALDRYN_ACCOUNTS_DISPLAY_EMAIL_NOTIFICATION'] = data['display_email_notifications']
        settings['ALDRYN_ACCOUNTS_DISPLAY_PASSWORD_NOTIFICATION'] = data['display_password_notifications']

        # setup accounts login features and other urls
        # we have to specify those urls because add-on urls
        settings['LOGIN_URL'] = '/login/'
        settings['LOGOUT_URL'] = '/logout/'
        settings['ADDON_URLS'].append('aldryn_accounts.urls')
        settings['ADDON_URLS_I18N'].append('aldryn_accounts.urls_i18n')
        return settings