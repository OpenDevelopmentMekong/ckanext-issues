"""
CKAN Issue Extension
"""
from logging import getLogger
import ckan.plugins as p
from ckan.plugins import implements, toolkit
from ckanext.issues.lib import util, helpers
from ckanext.issues.model import setup as model_setup
import ckanext.issues.logic.action as action
import ckanext.issues.auth as auth

log = getLogger(__name__)


if toolkit.check_ckan_version(min_version='2.9.0'):
    from ckanext.issues.plugin.flask_plugin import IssuesMixinPlugin
else:
    from ckanext.issues.plugin.pylons_plugin import IssuesMixinPlugin


class IssuesPlugin(IssuesMixinPlugin):
    """
    CKAN Issues Extension
    """
    implements(p.IConfigurer, inherit=True)
    implements(p.ITemplateHelpers, inherit=True)
    implements(p.IConfigurable)
    implements(p.IActions)
    implements(p.IAuthFunctions)

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'issues_dataset_resources': util.dataset_resources,
            'issues_installed': lambda: True,
            'issue_count': util.issue_count,
            'issue_comment_count': util.issue_comment_count,
            'replace_url_param': helpers.replace_url_param,
            'get_issue_filter_types': helpers.get_issue_filter_types,
            'get_issues_per_page': helpers.get_issues_per_page,
            'issues_enabled': helpers.issues_enabled,
            'issues_list': helpers.issues_list,
        }

    # IConfigurable

    def configure(self, config):
        """
        Called by load_environment
        """
        model_setup()

    # IActions

    def get_actions(self):
        return dict((name, function) for name, function in action.__dict__.items() if callable(function))

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'issue_show': auth.issue_show,
            'issue_count': auth.issue_show,
            'issue_create': auth.issue_create,
            'issue_comment_create': auth.issue_comment_create,
            'issue_update': auth.issue_update,
            'issue_status_change': auth._issue_auth_status_change,
            'issue_delete': auth.issue_delete,
            'issue_report_spam': auth.issue_report_spam,
            'issue_reset_spam_state': auth.issue_reset_spam_state,
        }
