class User:
    def __init__(self, roles=[]):
        self.roles = roles
        
    def get_roles(self):
        roles_copy=self.roles[:]
        return roles_copy
    
    def add_roles(self,role):
        self.roles.extend(role)

    def remove_roles(self,role_names):
        for role in role_names:
            if role in self.roles:
                self.roles.remove(role)