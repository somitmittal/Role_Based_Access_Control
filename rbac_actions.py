'''Role Based Access Control System using OOPs'''

class actions:
    def __init__(self):
        self.read=[]
        self.write=[]
        self.delete=[]

    def add_action_types(self,action_types,roles,resource):
        for role in roles:
            for action in action_types:
                if action=='read':
                    can_read=(role,resource)
                    if can_read not in self.read:
                        self.read.append(can_read)
                if action=='write':
                    can_write=(role,resource)
                    if can_write not in self.write:
                        self.write.append(can_write) 
                if action=='delete':
                    can_delete=(role,resource)
                    if can_delete not in self.delete:
                        self.delete.append(can_delete)

    def action_allowed(self,action_type,role,resource):
        if action_type=='read':
            return (role,resource) in self.read
        if action_type=='write':
            return (role,resource) in self.write
        if action_type=='delete':
            return (role,resource) in self.delete