"""
Program: Customer.py
Author:  Luke Xiong
Date: 7/12/2020

This program is a Customer class with exceptions
"""
class Customer:
    #constructor
    def __init__(self, cid, last_name, first_name, phone_number=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        num_characters = set("1234567890-")
        num1_characters = set('1234567890')
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise ValueError
        if phone_number and not num_characters.issuperset(phone_number):
            raise ValueError
        if cid and not num1_characters.issuperset((cid)):
            raise ValueError
        self.customer_id = cid
        self.last_name = last_name #last_name - required string
        self.first_name = first_name #first_name - required string
        self.phone_number = phone_number #phone_number - required string
        #self.address = address #address - required: string
    #getters
    def get_customer_id(self):
        return self._customer_id

    def get_last_name(self):
        return self._last_name

    def get_first_name(self, fname):
        return self._first_name

    #def get_address(self, address):
        #return self._address

    #def get_phone(self, phone):
        #return self._phone
    #setters
    def set_customer_id(self, cid):
        self.customer_id = cid

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone
    #method
    def add_item(self):
        #display that returns a string of the customer object
        #return self.customer_id
        pass
    #display for printing
    def display(self):
        #return self.customer_id + '\n' + self.first_name + '\n' + self.last_name + '\n' + self.phone + '\n' + self.address
        return 'Customer ID: ' + str(self.customer_id) + '\n' + self.first_name + ' ' + self.last_name + '\n' + self.phone_number

    def __str__(self):
        return (self.customer_id, self.first_name, self.last_name, self.phone_number)
        #return cust

    def __repr__(self):
        return (self.customer_id, self.first_name, self.last_name, self.phone_number)

#driver
if __name__=='__main__':
    customer1 = Customer('123', 'Johnson', 'Mike', '515-123-4444')
    print(customer1.display())

try:
    customer2 = Customer('12a', 'Johnson', 'Mike', '515-123-4444')
    print(customer2.display())
except ValueError:
    print("Invalid Customer ID")
try:
    customer3 = Customer('123', '678', 'Mike', '515-123-4444')
    print(customer3.display())
except ValueError:
    print("Invalid Last Name")
try:
    customer4 = Customer('123', 'Johnson', '789', '515-123-4444')
    print(customer4.display())
except ValueError:
    print("Invalid First Name")
try:
    customer5 = Customer('324', 'Joe', 'Keri', '555-111-999P')
    print(customer5.display())
except ValueError:
    print('Invalid Phone Number')


#Which method raised the exception? The constructor or the display()? Include in your comments which one!
#the constructor caused the exception because it is missing the required arguments.
