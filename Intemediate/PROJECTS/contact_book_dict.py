class ContactBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, num):
        if name in self.contacts:
            print(f'Contact {name} already exists!')
        else:
            self.contacts[name] = num
            print(f'Contact {name} added with number {num}.')
    
    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} successfully removed.')
        else:
            print(f'Contact {name} does not exist!')
    
    def update_contact(self, name, num):
        if name in self.contacts:
            self.contacts[name] = num
            print(f'Contact {name} updated with new number {num}.')
        else:
            print(f'Contact {name} does not exist!')
    
    def get_contact(self, name):
        if name in self.contacts:
            return f'Contact {name}: {self.contacts[name]}'
        else:
            return f'Contact {name} does not exist!'
    
    def list_contacts(self):
        if not self.contacts:
            return 'No contacts available.'
        return '\n'.join([f'{name}: {num}' for name, num in self.contacts.items()])
    
    def clear_contacts(self):
        self.contacts.clear()
        print('All contacts have been cleared.')
    
    def contact_exists(self, name):
        return name in self.contacts
    
    def get_all_contacts(self):
        return self.contacts.copy() 

# Demo
cb = ContactBook()
cb.add_contact('Alice', '123-456-7890')
cb.add_contact('Bob', '987-654-3210')

print(cb.list_contacts())
print(cb.get_contact('Alice'))
cb.update_contact('Alice', '111-222-3333')
print(cb.get_contact('Alice'))
cb.remove_contact('Bob')
print(cb.list_contacts())
cb.clear_contacts()
print(cb.list_contacts())