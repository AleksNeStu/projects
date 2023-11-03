#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

#Descriptor classes were created overriding:
# __set__(), __get__() and __delete__() methods of the parent class

from datetime import datetime

class NameField(object): #temp
    def __init__(self,name = None):
        self._name = name
    def __get__(self, instance, owner):
        print 'Getting name: {0}'.format(self._name)
        return self._name
    def __set__(self, instance, name):
        if type(name) is str:
            print 'Setting name: {0}'.format(name)
            self._name = name.title()
        else:
            raise TypeError('Name must be string type')
        if type(name) is str and len(name.split()) != 2:
            raise ValueError('Name must contain 2 elements: name surnamethe')
    def __delete__(self, instance):
        print 'Deleting name: {0}'.format(self._name)
        del self._name

class BirthdayField(object): #temp
    def __init__(self, birthday = None):
        self._birthday = birthday
    def __get__(self, instance, owner):
        print 'Getting birthday: {0}'.format(self._birthday)
        return self._birthday
    def __set__(self, instance, birthday):
        if type(birthday) is datetime:
            print 'Setting birthday: {0}'.format(birthday)
            self._birthday = birthday
        else:
            raise TypeError('Birthday must be datetime type')
    def __delete__(self, birthday):
        print 'Deleting birthday: {0}'.format(self._birthday)
        del self._birthday

class PhoneField(object): #temp
    def __init__(self, phone = None):
        self._phone = phone
    def __get__(self, instance, owner):
        if self._phone is None:
            print 'Getting phone: {0}'.format(self._phone)
            return self._phone
        else:
            ph = self._phone.split(' ')
            ph2 = ph[0] + ' (' + ph[1] + ') ' + ph[2][0:3] + '-' + ph[2][3:5] + '-' + ph[2][5:9]
            print 'Getting phone: {0}'.format(ph2)
            return ph2
    def __set__(self, instance, phone):
        if type(phone) is not str and phone is not None:
            raise TypeError('Phone must be datetime type')
        if len(phone) == 14:
            print 'Setting phone: {0}'.format(phone)
            self._phone = phone
        else:
            raise ValueError('Phone must be in format XXX XX XXXXXXX')
        if phone is None:
            raise ValueError('Phone cant be empty')
    def __delete__(self, phone):
        print 'Deleting phone: {0}'.format(self._phone)
        del self._phone