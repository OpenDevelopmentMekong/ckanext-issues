import ckan.plugins as plugins
from ckan.plugins import toolkit
from ckanext.issues.views import issues_blueprint
import logging
log = logging.getLogger(__name__)


class IssuesMixinPlugin(plugins.SingletonPlugin):
    '''ODM issue extension'''
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, '../templates-2.9')
        toolkit.add_public_directory(config, '../public')
        toolkit.add_resource('../public', 'issues')
        
    def get_blueprint(self):
        return [issues_blueprint]
