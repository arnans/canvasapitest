# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://mango-cmu.instructure.com"
# Canvas API key
API_KEY = "21123~emkSDtMv6THZj0MxDAlcSnKGi7vCbv6Uam0VI1bUerOyC1xo5QL8LAnXEtWD7vpx"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(4361)   # 4361 = Embed Lab 2/66
print(course.name)

group_cat = canvas.get_group_category(category=1217)

group1count = 21
group2count = 15

for i in range(group1count):
    print("creating : Project Group 1." + str(i+1))
    group_cat.create_group(name="Project Group 1." + str(i+1))


for i in range(group2count):
    print("creating : Project Group 2." + str(i+1))
    group_cat.create_group(name="Project Group 2." + str(i+1))


# groups = group_cat.get_groups()
# print(group_cat.group_limit)

# for group in groups:
#     print(group)
#     print(group.join_level)
