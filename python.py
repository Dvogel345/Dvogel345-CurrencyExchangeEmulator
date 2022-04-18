# class Car:
# # __lt__(self,other) # <
# # __gt__(self,other) # >
# # __le__(self,other) # <=
# # __ge__(self,other) # >=
# # __eq__(self,other) # ==
# # __ne__(self,other) # !=
#
#     def __eq__(self,other): # ==
#         if self.make == other.make and self.model == other.model:
#             return True
#         else:
#             return False
#
#     def __ne__(self,other): # !=
#         if self == other:
#             return False
#         else:
#             return True
#
# car1 = Car("Hyundai","Sonata")
# car2 = Car("Hyundai","Sonata")
# car3 = Car("Honda","Accord")
# print(car1 == car2) #True (self is car1, other is car2)
# print(car1 == car3) #False (self is car1, other is car3)
# print(car2 != car3) #True (self is car2, other is car3)
class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar

  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit

  #add magic methods here
  def __repr__(self):
      # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return f"{round(self.value,2)} {self.unit}"

  def __str__(self):
      #This method returns the same value as __repr__(self).
    return f"{round(self.value,2)} {self.unit}"

  def __add__(self,other):
      # Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self.
      # If other is an int or a float, other will be treated as a USD value.
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    return Currency(x + self.value, self.unit)

  def __iadd__(self,other):
       # - This is the same as (calls) __add__(self,other) .
    return Currency.__add__(self,other)

  def __radd__(self,other):
      # - This method is similar to __add__(self,other), but occurs when an int or float tries to add a Currency object.
      # (Treat the int/float as having a USD value.)
    res = self + other
    if self.unit != "USD":
      res.changeTo("USD")
    return res

  def __sub__(self,other):
       # - All __sub__(self,other) type functions are parallel to __add__(self,other) type functions.
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    return Currency(self.value - x, self.unit)

  def __isub__(self,other):
    return Currency.__sub__(self,other)

  def __rsub__(self,other):
    res = other - self.value
    res = Currency(res,self.unit)
    if self.unit != "USD":
      res.changeTo("USD")
    return res


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2)
