import re

def main():
    ids = []
    while True:
        mod = input("Paste mods: ")
        finder = re.compile("[0-9]+")
        id = finder.findall(mod)
        ids.append(id)
        print(ids)
        break
#Workshop ID: 2200148440

main()
