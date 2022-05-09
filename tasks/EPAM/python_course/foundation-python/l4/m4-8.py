"""globals() and locals()."""

q = lambda: locals()
q()

def q():
    qwert = 1
    print(locals())

q()

print(locals())
print(globals())