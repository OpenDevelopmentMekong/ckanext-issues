from ckan.lib.dictization.model_dictize import _get_members, user_list_dictize
from ckan.plugins import toolkit
import ckan.lib.helpers as h


def get_users_for_group(context, data_dict):
    context['with_capacity'] = True
    model = context['model']
    group = model.Group.get(data_dict.get('id'))
    users = user_list_dictize(_get_members(context, group, 'users'), context)

    return users


def get_request_parameter_flask_pylons_mixin(request_object, method="get"):
    """
    Conversion of request object get and post from pylons and flask
    :param request_object:
    :param method:
    :return:
    """
    if not toolkit.check_ckan_version(min_version='2.9.0'):
        return getattr(request_object, method.upper())

    new_param = dict()
    if method.upper() == "GET":
        request_params = request_object.params
    else:
        request_params = request_object.form

    for param in request_params:
        if isinstance(request_params.get(param, ''), list):
            new_param[param] = ",".join(request_params.get(param))
        else:
            new_param[param] = request_params.get(param)

    return new_param


def redirect_to_flask_pylons_mixin(pylons_route_name=None, flask_route_name=None, **kwargs):
    """
    Mixin in route names for pylons and flask.
    :param pylons_route_name: str
    :param flask_route_name: str
    :param kwargs: named arguments
    :return: redirect
    """

    if toolkit.check_ckan_version(min_version='2.9.0'):
        return toolkit.redirect_to(h.url_for(flask_route_name, **kwargs))
    else:
        return toolkit.redirect_to(h.url_for(pylons_route_name, **kwargs))
