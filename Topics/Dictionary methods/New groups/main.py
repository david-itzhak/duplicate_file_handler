# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
opened_groups_number = int(input())
groups_dict = {groups[index]: int(input()) if index < opened_groups_number else None for index in range(len(groups))}
print(groups_dict)
