"""
Defining your own typed attributes
By convention, typed attributes are stored together in a container class with other attributes of the same category:
"""

from anyio import TypedAttribute, TypedAttributeSet, TypedAttributeProvider


class MyTypedAttribute:
    string_valued_attribute = TypedAttribute[str]()
    some_float_attribute = TypedAttribute[float]()

# To provide values for these attributes, implement the extra_attributes() property in your class:


class MyAttributeProvider(TypedAttributeProvider):
    def extra_attributes():
        return {
            MyTypedAttribute.string_valued_attribute: lambda: 'my attribute value',
            MyTypedAttribute.some_float_attribute: lambda: 6.492
        }

# If your class inherits from another typed attribute provider, make sure you include its attributes in the return value:

class AnotherAttributeProvider(MyAttributeProvider):
    def extra_attributes():
        return {
            **super().extra_attributes,
            MyTypedAttribute.string_valued_attribute: lambda: 'overridden attribute value'
        }