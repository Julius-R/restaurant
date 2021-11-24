import json
from Restaurant import Restaurant as res


data = {
    'restaurants': []
}

# Testing code
test = res("Jac", "350b534")
test.add_fridge()
test.add_fridge()
test.show_all_fridges()
print("------")
test.edit_fridge()
test.show_all_fridges()
data['restaurants'].append(json.dumps(test.__dict__))

with open("restaurants.py", "w") as f:
    save_data = json.dumps(data)
    f.write(save_data)

