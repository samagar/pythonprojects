#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Contacts App '''

class Contacts():
    def __init__(self,first,last=None,phone=None,address=None):
        self.first=first
        self.last=last
        self.phone=phone
        self.address=address
        
    def add_new(self):
        if self.first not in con_dict:
            con_dict[self.first] = {
                    "first":self.first,
                    "last":self.last,
                    "phone":self.phone,
                    "address":self.address
                    }
            msg = "\n**{0} has been added to contacts".format(self.first)
            print(msg)
        else:
            msg ="\n!!{0} exists already..can not add".format(self.first)
            print(msg)
            
    def edit_contact(self):
        print("First name can not be changed")
        ls = input("Enter updated last name\n")
        np = input("Enter updated phone #\n")
        na = input("Enter updated address\n")
        
        con_dict[self.first] = {
        "first":self.first,
        "last":ls,
        "phone":np,
        "address":na
        }
        
        print("\n!! Record Updated..Check updated record below")
        my_obj2.search_contact()
        
    def search_contact(self): 
        if self.first in con_dict:
            mylist = con_dict.get(self.first)
            print("\n** Record Found **")
            for topic, value in mylist.items():
                print(topic,":",value)
            a = input("\n1. Edit record\n2. Delete record\n3. Go Home\n")
            if a == "1":
                my_obj2.edit_contact()
            elif a =="2":
                my_obj2.del_contact()
            elif a =="3":
                return
            else:
                print("!!Invalid Entry")
        else:
            print("\n!!Record not found")
            
    def del_contact(self):
        del con_dict[self.first]
        msg = "\n**{0} has been deleted from contacts".format(self.first)
        print(msg)

# Main        
import pickle
f = open("Contacts.txt","rb")
con_dict = pickle.load(f)
# print(con_dict)

while True:
    a = input("select options \n1-Add\n2-Search\nQ-quit\n")  
    if a == "1":
        first = input("Enter first name:\n")
        last  = input("Enter last name:\n")
        phone = input("Enter Phone:\n")
        address = input("Enter address:\n")

        my_obj1 = Contacts(first,last,phone,address)
        my_obj1.add_new()

    elif a == "2":
        first = input("Enter first name:\n")
        my_obj2 = Contacts(first)
        my_obj2.search_contact()
                 
    elif a == "Q":
        print("!!Thank you..Exited")
        f = open("Contacts.txt","wb")
        pickle.dump(con_dict,f)
        break
    
    else:
        print("!!Invalid Entry")   