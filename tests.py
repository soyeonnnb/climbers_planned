__all__ = ['tests']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['address', 'returnAddress'])
@Js
def PyJsHoisted_returnAddress_(address, this, arguments, var=var):
    var = Scope({'address':address, 'this':this, 'arguments':arguments}, var)
    var.registers(['address'])
    return var.get('address')
PyJsHoisted_returnAddress_.func_name = 'returnAddress'
var.put('returnAddress', PyJsHoisted_returnAddress_)
var.put('address', Js('서울특별시 동대문구 이문로 107'))
pass
pass


# Add lib to the module scope
tests = var.to_python()