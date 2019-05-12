The Repository contains 3 files:

1) rbac_user.py - This file is used to create new users and assign them different roles like Admin,Manager etc. A user can be assigned multiple roles.
Contains 3 functions:
1) get_roles(): Tells the roles a particular user has.
2) add_roles(list_of_role_names_to_add) : Adds the provided list of role_names to the user object.
3) remove_roles(list_of_role_names_to_remove) : Removes the role_names provided in the list from the user object.
				  
2) rbac_actions.py - This file is used to specify the actions that a particular role can perform. For eg. Admin can perform Read,Write and Delete
Contains 2 functions:
1) add_action_types(list_of_action_types,list_of_role_names,resource) - Associates action with the rolename and helps us store which roles can perform which actions.
2) action_allowed(action_type,role_name,resource) - Tells whether a particular action can be performed by a role or not.

3) Notebook.ipynb - This is a python notebook that demonstrates the code in action. 
