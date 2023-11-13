file1 = open("CTF_Challenge/picoctf/credstuff/leak/leak/usernames.txt", "r")
file2 = open("CTF_Challenge/picoctf/credstuff/leak/leak/passwords.txt", "r")

save = {}
username = file1.readline()
password = file2.readline()

while username:
    save[username[:-1]] = password[:-1]
    username = file1.readline()
    password = file2.readline()

print(save["cultiris"])
