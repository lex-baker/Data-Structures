# Problem 4

I intrepreted the question as saying that users of subgroups became users of the groups above them. Therefore:

Group: Group User

Subgroup of Group: Subgroup User

The Subgroup User is a user of Group, but the Group User is not a user of Subgroup

Time complexity: where g is the total number of subgroups and u is the number of users in a group or subgroup, O(g * u)

Space complexity: where g is total number of groups and u is number of users in a group, O(g * (size of group) + u * (size of string))