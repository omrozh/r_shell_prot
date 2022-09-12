from requests import post

while True:
    print(post("http://139.144.67.163/update_command", data={"command": input("Command To Execute: ")}))
