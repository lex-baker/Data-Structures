class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Write a function that provides an efficient look up of whether the user is in a group.

#This function is assuming that being a user of a sub group makes them a user of the group
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for u in group.get_users():
        if user == u:
            return True
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(is_user_in_group("sub_child_user", sub_child)) # True
print(is_user_in_group("sub_child_user", child)) # True
print(is_user_in_group("sub_child_user", parent)) # True
print(is_user_in_group("_user", parent)) # False

print()
# Test Case 2
sub_group = Group("Group 1")
group = Group("Group 2")
super_group = Group("Group 3")
super_group.add_group(group)
group.add_group(sub_group)
sub_group.add_user("Sub_Group_User")
group.add_user("Group_User")
super_group.add_user("Super_Group_User")

print(is_user_in_group("Sub_Group_User", sub_group)) # True
print(is_user_in_group("Sub_Group_User", super_group)) # True

print(is_user_in_group("Group_User", sub_group)) # False
print(is_user_in_group("Group_User", super_group)) # True

print(is_user_in_group("Super_Group_User", group)) # False
print(is_user_in_group("Super_Group_User", super_group)) # True

# Test Case 3
previous_group = Group(0)
previous_group.add_user("User_0")
for n in range(1, 10000):
    group = Group(n)
    group.add_user("User_" + str(n))
    group.add_group(previous_group)
    previous_group = group
print(group.get_users()) # 9999
print(group.get_groups()[0].get_name()) # 9998
print(group.get_groups()[0].get_users()[0]) # User_9998