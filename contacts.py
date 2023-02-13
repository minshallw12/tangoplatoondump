class Create_contact_list:
    def __init__(self, name):
        self.__name = name
        self.__list = []
    def get_list(self):
        return self.__list
    def add_contact(self, name, number):
        self.__list.append({'name':name,'number':number})
    def remove_contact(self, name):
        for person in self.get_list():
            if name == person['name']:
                self.__list.pop(self.get_list().index(person))
    def find_shared_contacts(self, contact_list):
        

family = Create_contact_list('friends')
family.add_contact('Will','2083155834')
family.add_contact('Everett','20834573834')
family.add_contact('Angelina','2083373534')
family.remove_contact('Will')

work_buds = Create_contact_list('work buddies')
work_buds.add_contact('Will', '2083155834')
work_buds.add_contact('Jim', '8463158426')
work_buds.add_contact('Avi', '2083604852')

print(family.get_list())
print(work_buds.get_list())