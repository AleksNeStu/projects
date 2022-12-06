"""Garbage collection."""

a = 40
b = a
c = [b] # Create object <40>
# Increase ref. count of <40>
# Increase ref. count of <40>

del a
b = 100
c[0] = -1 # Decrease ref. count of <40>
# Decrease ref. count of <40>
# Decrease ref. count of <40>