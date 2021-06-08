from ckanext.issues import model as issue_model
from ckan.tests import factories, helpers

import factory


class Issue(factory.Factory):

    title = 'Test issue'
    description = 'Some description'

    class Meta:
        model = issue_model.Issue

    @classmethod
    def _build(cls, target_class, *args, **kwargs):
        raise NotImplementedError(".build() isn't supported in CKAN")

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        if args:
            assert False, "Positional args aren't supported, use keyword args."

        context = {'user': factories._get_action_user_name(kwargs)}

        # issue_create is so badly behaved I'm doing this for now
        data_dict = dict(**kwargs)
        data_dict.pop('user', None)

        issue_dict = helpers.call_action('issue_create',
                                         context=context,
                                         **data_dict)
        return issue_dict


class IssueComment(factory.Factory):

    class Meta:
        model = issue_model.IssueComment

    comment = 'some comment'

    @classmethod
    def _build(cls, target_class, *args, **kwargs):
        raise NotImplementedError(".build() isn't supported in CKAN")

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        if args:
            assert False, "Positional args aren't supported, use keyword args."

        context = {'user': factories._get_action_user_name(kwargs)}
        issue_comment_dict = helpers.call_action('issue_comment_create',
                                                 context=context,
                                                 **kwargs)
        return issue_comment_dict


class Dataset(factories.Dataset):

    @classmethod
    def _add_mandatory_fields(cls, data_dict):
        """
        Add additional dataset arguments
        :return:
        """
        _mandatory_fields = {
            "notes_translated": {"en": "test"},
            "odm_spatial_range": "km"
        }
        for k, val in _mandatory_fields.items():
            data_dict[k] = data_dict.get(k, val)
        return data_dict

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        if args:
            assert False, "Positional args aren't supported, use keyword args."

        context = {"user": factories._get_action_user_name(kwargs)}
        kwargs = cls._add_mandatory_fields(kwargs)
        dataset_dict = helpers.call_action(
            "package_create", context=context, **kwargs
        )
        return dataset_dict

