from ckan.plugins import toolkit
from flask import Blueprint
from ckanext.issues.utils import view_functions
import logging

log = logging.getLogger(__name__)

issues_blueprint = Blueprint("issues", __name__)

issues_blueprint.add_url_rule("/dataset/<package_id>/issues", methods=["GET"], view_func=view_functions.home_view)
issues_blueprint.add_url_rule("/dataset/<package_id>/issues/new", methods=["GET", "POST"],
                              view_func=view_functions.new)
issues_blueprint.add_url_rule("/dataset/<package_id>/issues/<id>/edit", methods=["GET", "POST"],
                              view_func=view_functions.new)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/delete", methods=["GET", "POST"],
                              view_func=view_functions.delete)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/assign", methods=["POST"],
                              view_func=view_functions.assign)
issues_blueprint.add_url_rule("/dataset/<package_id>/issues/<id>/comments", methods=["POST"],
                              view_func=view_functions.comments)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/report_abuse", methods=["POST"],
                              view_func=view_functions.report_abuse)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/reset_spam_state", methods=["POST"],
                              view_func=view_functions.reset_spam_state)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/comment/<comment_id>/report_abuse",
                              methods=["POST"], view_func=view_functions.report_comment_abuse)
issues_blueprint.add_url_rule("/dataset/<dataset_id>/issues/<issue_id>/comment/<comment_id>/reset_spam_state",
                              methods=["POST"], view_func=view_functions.reset_spam_state)

# This is add method not available. Not sure why it is add in before_rout. So coomenting
#issues_blueprint.add_url_rule("/dataset/<package_id>/issues/new/<resource_id>",
                              #methods=["POST"], view_func=view_functions.add)
                              
issues_blueprint.add_url_rule("/dataset/<package_id>/issues/<id>", methods=["GET"],
                              view_func=view_functions.show_view)
issues_blueprint.add_url_rule("/publisher/issues/<publisher_id>", methods=["GET"],
                              view_func=view_functions.publisher_issue_page)
