from requests import post

while True:
    print(post("http://10.120.0.243:5000/update_command", data={"command": input("Command To Execute: ")}))
