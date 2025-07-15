# functions declaration in python is and passing values in functions can be any data type
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

# functions with default value
def defaultParamValue(val = 'Philippines'):
    print(val)

defaultParamValue("Norway")
defaultParamValue()

# return value in functions
def sampleReturnPower(x):
    return x ** 2

newX = sampleReturnPower(4)
print(newX)
print(sampleReturnPower(34))

# positional only args disallows kwargs uses ,/
def disAllowKwargs(x,y,z,/):
    print(x,y,z)
disAllowKwargs(x= 4,z=5,y = 8) # error positional args

# keyword only args on the other hand uses *,

def disAllowPosArgs(*,x):
    print(x)
disAllowPosArgs(23) # error keyword args only

# combining the two args
# any args before the ,/ are positional while after the *, are keyword only
def combinedRulesArgs(x,y,/,*,z):
    print(x,y,z)

combinedRulesArgs(34,5,z = 7)

# recursion is when the function is called itself with certain condition to stop unless it would be infinite
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# result above would be 1 3 6 10 15 21
# result = k + tri_recursion(k - 1)
# result = 1 + 0 = 1 where this is the last recursion call since k > 0
# result = 2 + 1 = 3
# result = 3 + 3 = 6
# result = 4 + 6 = 10
# result = 5 + 10 = 15
# result = 6 + 15 = 21 initial call since k = 6