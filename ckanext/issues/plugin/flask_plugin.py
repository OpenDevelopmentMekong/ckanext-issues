import ckan.plugins as plugins
from ckan.plugins import toolkit
from ckanext.issues.views import issues_blueprint
import logging
log = logging.getLogger(__name__)


class IssuesMixinPlugin(plugins.SingletonPlugin):
    '''ODM issue extension'''
    plugins.implements(plugins.IBlueprint)

    def get_blueprint(self):
        return [issues_blueprint]
