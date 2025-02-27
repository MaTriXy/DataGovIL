from ckan.lib.navl.validators import ignore_missing, not_empty, ignore, not_missing, unicode_safe
from ckan.logic.validators import name_validator, user_name_validator, \
    user_password_not_empty, user_passwords_match, ignore_not_sysadmin, \
    ignore_not_group_admin, ignore_not_package_admin, user_about_validator, \
    user_both_passwords_entered, vocabulary_id_exists

from ckan.logic import schema as ckan_schema

from ckanext.gov_theme import validators


# The main purpose of this file is to modify CKAN's user-related schemas, CKAN's default tags schema,
# and to replace the default password validators everywhere. We are also replacing
# the username validators for endpoints where username changes user to be
# allowed.


def default_user_invite_schema():
    schema = {
        'id': [ignore_missing, unicode_safe],
        'name': [not_empty, name_validator, user_name_validator, unicode_safe],
        'fullname': [ignore_missing, unicode_safe],
        'password': [validators.user_invite_password_validator, user_password_not_empty,
                     ignore_missing, unicode_safe],
        'password_hash': [ignore_missing, ignore_not_sysadmin, unicode_safe],
        'email': [not_empty, unicode_safe],
        'about': [ignore_missing, user_about_validator, unicode_safe],
        'created': [ignore],
        'openid': [ignore_missing],
        'sysadmin': [ignore_missing, ignore_not_sysadmin],
        'apikey': [ignore],
        'reset_key': [ignore],
        'activity_streams_email_notifications': [ignore_missing],
        'state': [ignore_missing],
    }
    return schema

def default_user_schema():
    schema = {
        'id': [ignore_missing, unicode_safe],
        'name': [not_empty, name_validator, user_name_validator, unicode_safe],
        'fullname': [ignore_missing, unicode_safe],
        'password': [validators.user_password_validator, user_password_not_empty,
                     ignore_missing, unicode_safe],
        'password_hash': [ignore_missing, ignore_not_sysadmin, unicode_safe],
        'email': [not_empty, unicode_safe],
        'about': [ignore_missing, user_about_validator, unicode_safe],
        'created': [ignore],
        'openid': [ignore_missing],
        'sysadmin': [ignore_missing, ignore_not_sysadmin],
        'apikey': [ignore],
        'reset_key': [ignore],
        'activity_streams_email_notifications': [ignore_missing],
        'state': [ignore_missing],
    }
    return schema


def user_new_form_schema():
    schema = default_user_schema()

    schema['password1'] = [unicode_safe, user_both_passwords_entered,
                           validators.user_password_validator, user_passwords_match]
    schema['password2'] = [unicode_safe]

    return schema


def user_edit_form_schema():
    schema = default_user_schema()

    schema['password'] = [ignore_missing]
    schema['password1'] = [ignore_missing, unicode_safe, validators.user_password_validator,
                           user_passwords_match]
    schema['password2'] = [ignore_missing, unicode_safe]

    return schema


def default_update_user_schema():
    schema = default_user_schema()

    schema['name'] = [ignore_missing, name_validator, user_name_validator,
                      unicode_safe]
    schema['password'] = [validators.user_password_validator, ignore_missing, unicode_safe]

    return schema


def default_tags_schema():
    return {
        'name': [not_missing,
                 not_empty,
                 unicode_safe,
                 ],
        'vocabulary_id': [ignore_missing,
                          unicode_safe,
                          vocabulary_id_exists],
        'revision_timestamp': [ignore],
        'state': [ignore],
        'display_name': [ignore],
    }

