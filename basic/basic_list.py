def is_on_list(days, find):
  return find in days

def get_x(days, index):
    return days[index]

def add_x(days, value):
    return days.append(value)

def remove_x(days, value):
    return days.remove(value)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)