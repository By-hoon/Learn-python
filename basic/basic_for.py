import requests

while(True):
  a = input()
  arr = a.split(",")
  for i in arr:
    new_str = i.strip()
    try:
      r = requests.get(new_str)
      if r.status_code == 200:
        print(f"{new_str} is up")
      else:
        print(f"{new_str} is down")
    except:
      print(f"error {new_str} is not found")
  choice = input("Do it again? (y/n)")
  if choice == "y":
    continue
  else:
    break