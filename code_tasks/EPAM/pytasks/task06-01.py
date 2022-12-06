#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task06-01:
# Create method for creating new type with special behaviour (mixins).

# Example:
# python
#  class Creature(object):
#      def __init__(self, genus):
#          self.genus = genus
#      def sound(self, msg):
#          print "{0}: {1}".format(self.genus, msg)
# 
# 	class Man(Creature):
#      def __init__(self, name):
#          super(Man, self).__init__("man")
#          self.name = name
# 
#  class SingMixin(object):
#      def sing(self):
#          self.sound('La la li la, la la la!')
# 
#  man = Man('Yury')
#  # I cannot sing!
#  man.sing()
# Traceback (most recent call last):
#   File "", line 20, in <module>
#     man.sing()
# AttributeError: 'Man' object has no attribute 'sing'
#  Singner = Man.make_with_mixin(SingMixin)
#  pavel = Singner("Pavel")
#  pavel.sing()
# man: La la li la, la la la!

# Addition info:

# added
class NewClass(type):
    # Create method for creating new type with special behaviour (mixins)
    def make_with_mixin(cls, name):
        # cls:            <class '__main__.Man'>
        # cls.__bases__:  (<class '__main__.Creature'>,)  # (<class '__main__.x'>, <class '__main__.y'>)
        # name:           <class '__main__.SingMixin'>
        while name not in cls.__bases__: # class.__bases__ - The tuple of base classes of a class object.
            cls.__bases__ = cls.__bases__+(name,) # (<class '__main__.Creature'>, <class '__main__.SingMixin'>)
        return cls # <class '__main__.Man'>

class Creature(object):
    def __init__(self, genus):
        self.genus = genus
    def sound(self, msg):
        print '{0}: {1}'.format(self.genus, msg)

class Man(Creature):
    __metaclass__ = NewClass #added
    def __init__(self, name):
        super(Man, self).__init__('man')
        self.name = name

class SingMixin(object):
    def sing(self):
        self.sound('La la li la, la la la!')

if __name__ == '__main__':
    man = Man('Aleks')
    Singner = Man.make_with_mixin(SingMixin)
    Aleks = Singner('Aleks')
    Aleks.sing()