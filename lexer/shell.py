import core

while True:
    text = input("basic >")
    tokens = core.run(text)
    if tokens == []:
        continue
    print(tokens)
