from ckan.plugins import toolkit
from ckanext.issues.logic.validators import (
    as_package_id,
    is_valid_sort,
    is_valid_status,
    issue_exists,
    issue_comment_exists,
)

unicode_safe = toolkit.get_validator('unicode_safe')
not_missing = toolkit.get_validator('not_missing')
ignore_missing = toolkit.get_validator('ignore_missing')
package_exists = toolkit.get_validator('package_id_or_name_exists')
resource_id_exists = toolkit.get_validator('resource_id_exists')
user_exists = toolkit.get_validator('user_id_or_name_exists')
is_natural_number = toolkit.get_validator('natural_number_validator')
is_positive_integer = toolkit.get_validator('is_positive_integer')
boolean_validator = toolkit.get_validator('boolean_validator')


def issue_create_schema():
    return {
        'title': [not_missing, unicode_safe],
        'description': [ignore_missing, unicode_safe],
        'dataset_id':[ not_missing, unicode_safe, package_exists, as_package_id],
    }

def issue_update_schema():
    return {
        'id': [not_missing, unicode_safe, issue_exists],
        'title': [ignore_missing, unicode_safe],
        'description': [ignore_missing, unicode_safe],
        'dataset_id': [ignore_missing, unicode_safe, package_exists, as_package_id],
        'resource_id': [ignore_missing, unicode_safe, resource_id_exists],
        'assignee_id': [ignore_missing, unicode_safe, user_exists],
        'status':  [ignore_missing, unicode_safe],
    }


def issue_search_schema():
    return {
        'dataset_id': [not_missing, unicode_safe, package_exists, as_package_id],
        'status': [ignore_missing, unicode_safe, is_valid_status],
        'sort': [ignore_missing, unicode_safe, is_valid_sort],
        'limit': [ignore_missing, is_natural_number],
        'offset': [ignore_missing, is_natural_number],
        'q': [ignore_missing, unicode_safe],
        'spam_state': [ignore_missing, unicode_safe],
    }


def issue_count_schema():
    return {
        'dataset_id': [not_missing, unicode_safe, package_exists, as_package_id],
        'status': [ignore_missing, unicode_safe, is_valid_status],
        'q': [ignore_missing, unicode_safe],
        'spam_state': [ignore_missing, unicode_safe],
    }


def issue_delete_schema():
    return {
        'issue_id': [not_missing, unicode_safe, issue_exists],
        'dataset_id': [not_missing, unicode_safe, package_exists, as_package_id],
    }


def issue_report_spam_schema():
    return {
        'dataset_id': [not_missing, unicode_safe, package_exists],
        'issue_id': [not_missing, unicode_safe, issue_exists],
    }


def issue_comment_report_spam_schema():
    return {
        'dataset_id': [not_missing, unicode_safe, package_exists],
        'issue_comment_id': [not_missing, unicode_safe, issue_comment_exists],
    }


def issue_home_controller_schema():
    return {
        'status': [ignore_missing, unicode_safe],
        'sort': [ignore_missing, unicode_safe ],
        'page': [ignore_missing, is_positive_integer],
        'per_page': [ignore_missing, is_positive_integer],
        'q': [ignore_missing, unicode_safe],
        'spam_state': [ignore_missing, unicode_safe],
    }


def issue_show_controller_schema():
    return {
        'id': [not_missing, unicode_safe, issue_exists],
        'dataset_id': [not_missing, unicode_safe, package_exists, as_package_id],
    }


def organization_users_autocomplete_schema():
    return {
        'q': [not_missing, unicode_safe],
        'organization_id': [not_missing, unicode_safe],
        'limit': [ignore_missing, is_positive_integer],
    }
