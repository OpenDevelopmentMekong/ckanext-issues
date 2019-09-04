from ckan.lib.dictization.model_dictize import _get_members, user_list_dictize


def get_users_for_group(context, data_dict):
   context['with_capacity'] = True
   model = context['model']
   group = model.Group.get(data_dict.get('id'))
   users = user_list_dictize(_get_members(context, group, 'users'), context)

   return users
