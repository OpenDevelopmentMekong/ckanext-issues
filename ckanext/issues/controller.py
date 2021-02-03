from ckan.lib.base import BaseController
from ckanext.issues.utils import view_functions


class IssueController(BaseController):

    def _before(self, package_id):
        return view_functions._before(package_id)

    def new(self, package_id, resource_id=None):
        return view_functions.new(package_id, resource_id)

    def show_view(self, id, package_id):
        return view_functions.show_view(id, package_id)

    def edit(self, id, package_id, resource_id=None):
        return view_functions.edit(id, package_id, resource_id)

    def home_view(self, package_id):
        return view_functions.home_view(package_id)

    def delete(self, dataset_id, issue_id):
        return view_functions.delete(dataset_id, issue_id)

    def comments(self, id, package_id):
        return view_functions.comments(id, package_id)

    def assign(self, dataset_id, issue_id):
        return view_functions.assign(dataset_id, issue_id)

    def report_abuse(self, dataset_id, issue_id):
        return view_functions.report_abuse(dataset_id, issue_id)

    def report_comment_abuse(self, dataset_id, issue_id, comment_id):
        return view_functions.report_comment_abuse(dataset_id, issue_id, comment_id)

    def reset_spam_state(self, dataset_id, issue_id):
        return view_functions.reset_spam_state(dataset_id, issue_id)

    def reset_comment_spam_state(self, dataset_id, issue_id, comment_id):
        return view_functions.reset_comment_spam_state(dataset_id, issue_id, comment_id)

    def publisher_issue_page(self, publisher_id):
        return view_functions.publisher_issue_page(publisher_id)

    def all_issues_page(self):
        return view_functions.all_issues_page()

