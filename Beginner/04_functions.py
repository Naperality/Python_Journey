# functions declaration in python is
def myFunction(nap, num, str): # arguments/parameters are inside the parenthesis args are value params are the variables
    print(nap, num, str)

# arbitrary args a.k.a. *args are used to function without knowing how many args pass through
def sampleFunction(*args):
    print(args) # tuple not list shown

sampleFunction('Hello', 23, 45.9, 'World')

# can also send values with kwargs (key word args)
myFunction(str = 'nap', nap = 'hello', num = 23)

# if not known how many kwargs then use **kwargs and it shows as dictionary

def sampleDicArgs(**args):
    print(args)
    print(args['last'])

sampleDicArgs(last = 'Visitacion', first = 'Napoleon', age = 23)

def defaultParamValue(val = 'Philippines'):
    print(val)

defaultParamValue("Norway")
defaultParamValue()
