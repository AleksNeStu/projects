#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

import ast
import types
import re

class DocAPI(object): # for task04-02

    # Can do it only via instance.__dict__ and owner.__dict__, but for example implemented used instance.__dict__ and read source code!!!
    # Non-data descriptor wich can provide class-level and instance-level documentation about methods and attributes

    def __get__(self, instance, owner):
        if instance:
            dict = instance.__dict__
            for dic in dict:
                print dic,':', str(type(dict[dic]))[7:-2] # get type
        doc = self.Docstrings_parser(owner.__path__)  # owner.__path__ (file with Python source code) #task04-02
        return doc

    def Docstrings_parser(self, path):

        # Python source code docstrings parser from file or string
        # To build a dict/list representaiton of only module/function/classes and then pulls textdata from their docstrings

        look_types = {ast.Module: 'Module', ast.FunctionDef: 'Function', ast.ClassDef: 'Class'}
        with open(path, 'rt') as f:
            source = f.read() # Python source code content
        def Docstrings_get(self,source):
            ast_tree = ast.parse(source)  # Parse the source into an AST node
            for node in ast.walk(ast_tree): # node = <_ast.ClassDef object at 0x7fe71ef8b2d0>, <_ast.Name object at 0x7fe71ef8ba90>
                if isinstance(node, tuple(look_types)):
                    docstring = ast.get_docstring(node) # return docstring or None after check "type" in "look_types"
                    yield (node, getattr(node, 'name', None), docstring)
        docstrings = Docstrings_get(self,source)
        for typer, name, docstring in docstrings:
            if docstring is not None and name is not None and typer is not None:
                resin = name,':', docstring # tuple
                # return str(resin).replace("'","").replace("(","").replace(")","").replace(",","")
                replaces = ("'",""), ("(",""), (")",""),(",","")
                return reduce(lambda a, item: a.replace(*item), replaces, str(resin)) # tuple to str and replace tp pretty print

class LinterMeta(type): # for task06-02

    def __new__(mcs, name, bases, attrs):

        # __new__ method is the constructor (it returns the new instance) while __init__ is just a initializer
        # mcs: <class 'miscripts.LinterMeta'> - upperattr_metaclass
        # name: Creature - future_class_name
        # bases: (<type 'object'>,) - future_class_parents
        # attrs: - future_class_attr
        # 'sound_2016': <function sound_2016 at 0x7f3e3fa3f938>
        # '__module__': '__main__'
        # '__metaclass__': <class 'miscripts.LinterMeta'>
        # '__init__': <function __init__ at 0x7fd69bf1f500>

        for attr in attrs:

            # 1 - Check if all attrubutes is formatted as snake case style
            # snake-case style:
            # contains lowercase letters [a-z] and underscores and numbers ([0-9])
            # not start/end with an underscore
            # not start with a number ([0-9])
            snake_case_style = re.compile(r'^[a-z]+([a-z\d]+_|_[a-z\d]+)+[a-z\d]+$')
            if bool(snake_case_style.search(attr)) is True:
                print '%s - the attribute has a snake-case style' % attr
            else:
                print '%s - the attribute has not a snake-case style' % attr

            # 2 - Check if all user methods do not empty docstrings
            # print attrs[attr].__doc__
            if "<type 'function'>" in str(type(attrs[attr])) and hasattr(attrs[attr], '__doc__') and attrs[attr].__doc__ is not None: # 1 variant of check type func and doctring
                print '%s - the attribute has function type and docstring: %s' % (attr,attrs[attr].__doc__)
            elif "<type 'function'>" in str(type(attrs[attr])) and hasattr(attrs[attr], '__doc__') and attrs[attr].__doc__ is None:
                print '%s - the attribute has function type and docstring: %s' % (attr, 'EMPTY')
            else:
                print '%s - the attribute has not function type' % attr

            # 3 - Check if all docstrings have one space delimeter between words
            if isinstance(attrs[attr], types.FunctionType) and attrs[attr].__doc__: # 2 variant of check type func and doctring
                if ' ' in attrs[attr].__doc__:
                    print '%s - the attribute\'s docstring have one space delimeter between words' % attr
                else:
                    print '%s - the attribute\'s docstring have more than one space delimeter between words' % attr

        # super, which will cause inheritance (create a metaclass derived from the metaclass inherited from type)
        return super(LinterMeta, mcs).__new__(mcs, name, bases, attrs)