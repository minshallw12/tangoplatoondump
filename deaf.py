def deafGrandma():
    speech = input("HEY KID!\n>")
    cant_hear = 'abcdefghijklmnopqrstuvwxyz'
    heardIt = [char for char in speech]
    print(heardIt)
    for char in heardIt:
        if char in cant_hear:
            respond = input("WHAT?")

print(deafGrandma())        