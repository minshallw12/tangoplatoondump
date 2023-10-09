class Users:

    def __init__(self, name, email, drivers):
        self.name = name
        self.email = email
        self.drivers = drivers

    def __str__(self) -> str:
        return f"{self.name} Dunder"


will = Users("Will", "will@will.com", "UP15123451")
andrew = Users("Andrew", "Andrew@gmail.com", "RF2305979")

print(will)
print(andrew.email)