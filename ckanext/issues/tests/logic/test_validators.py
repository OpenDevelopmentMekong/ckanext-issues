from ckan import model
from ckan.lib import search
from ckan.tests import factories, helpers
from ckanext.issues.logic import validators
from ckanext.issues.tests import factories as issue_factories
from nose.tools import assert_equals
import pytest


@pytest.mark.usefixtures("clean_db", "with_request_context")
class TestAsPackageId(object):
    def setup(self):
        self.dataset = issue_factories.Dataset()

    def test_given_name_returns_id(self):
        package_id = validators.as_package_id(self.dataset['name'], 
                                              context={
                                                  'model': model,
                                                  'session': model.Session})
        assert_equals(self.dataset['id'], package_id)

    def test_given_id_returns_id(self):
        package_id = validators.as_package_id(self.dataset['id'], 
                                              context={
                                                  'model': model,
                                                  'session': model.Session})
        assert_equals(self.dataset['id'], package_id)
