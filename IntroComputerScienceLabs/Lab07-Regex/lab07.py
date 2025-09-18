import re

# TODO: YOUR REGEX FUNCTIONS GO HERE
def validate_variable(value):
    regex = r'[a-zA-Z_][a-zA-Z0-9_]*'
    value_fsm = re.compile(regex)
    
    if value_fsm.fullmatch(value):
        return True
    else:
        return False
    
def validate_domain(value):
    regex = r'[a-zA-Z0-9_]+[\.]?[a-zA-z_]+?[\.](com|ca|org)'
    value_fsm = re.compile(regex)

    if value_fsm.fullmatch(value):
        return True
    else:
        return False
    
def validate_phone(value):
    regex = r'^\(?[0-9]{3}\)?[-]?[0-9]*?[-][0-9]{4}$'
    value_fsm = re.compile(regex)

    if value_fsm.fullmatch(value):
        return True
    else:
        return False