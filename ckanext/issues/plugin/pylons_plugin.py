import ckan.plugins as plugins
from ckan.plugins import toolkit
import logging
log = logging.getLogger(__name__)


class IssuesMixinPlugin(plugins.SingletonPlugin):
    '''ODM issue extension'''
    implements(p.IRoutes, inherit=True)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, '../templates')
        toolkit.add_public_directory(config, '../public/css')
        toolkit.add_resource('../public/scripts', 'ckanext_issues')

    # IRoutes
    def before_map(self, map):
        from ckan.config.routing import SubMapper

        with SubMapper(map, controller='ckanext.issues.controller:IssueController') as m:
            m.connect('issues_home', '/dataset/:package_id/issues', action='home_view', ckan_icon='warning')
            m.connect('issues_new', '/dataset/:package_id/issues/new',
                      action='new')
            m.connect('issues_edit', '/dataset/:package_id/issues/:id/edit',
                      action='edit')
            m.connect('issues_delete', '/dataset/:dataset_id/issues/:issue_id/delete',
                      action='delete')
            m.connect('issues_assign',
                      '/dataset/:dataset_id/issues/:issue_id/assign',
                      action='assign')
            m.connect('issues_comments', '/dataset/:package_id/issues/:id/comments',
                      action='comments')
            m.connect('issues_report_abuse',
                      '/dataset/:dataset_id/issues/:issue_id/report_abuse',
                      action='report_abuse'),
            m.connect('issues_reset_spam_state',
                      '/dataset/:dataset_id/issues/:issue_id/reset_spam_state',
                      action='reset_spam_state'),
            m.connect('issues_comment_report_abuse',
                      '/dataset/:dataset_id/issues/:issue_id/comment/:comment_id/report_abuse',
                      action='report_comment_abuse'),
            m.connect('issues_comment_reset_spam_state',
                      '/dataset/:dataset_id/issues/:issue_id/comment/:comment_id/reset_spam_state',
                      action='reset_comment_spam_state'),
            # This is not available - not sure why this is added
            #m.connect('add_issue_with_resource', '/dataset/:package_id/issues/new/:resource_id', action='add')
            m.connect('issues_show', '/dataset/:package_id/issues/:id', action='show_view')
            # Broken: m.connect('all_issues_page', '/issues', action='all_issues_page')
            m.connect('publisher_issue_page', '/publisher/issues/:publisher_id', action='publisher_issue_page')

        return map
