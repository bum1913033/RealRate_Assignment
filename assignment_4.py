import re

def create_variable_name(string):
    # Extract the last word separated by a comma, or the first word separated by a slash
    if ',' in string:
        last_word = re.findall('\s*,\s*([^,]*)\s*$', string)[-1]
    elif '/' in string:
        last_word = re.split('\s*/\s*', string)[0]
    else:
        last_word = string
    
    # Split the last word on whitespace characters
    words = re.split('\s+', last_word.strip())
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    # Remove certain words from the start of the variable name
    while words and words[0] in ['of', 'which', 'and', 'or']:
        words.pop(0)
    
    # Capitalize first letter of each word except the first
    words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    # Join words and remove underscores
    variable_name = ''.join(words).replace('_', '')
    
    # Ensure the variable name starts with a letter or underscore
    if not re.match('^[a-zA-Z_]', variable_name):
        variable_name = '_' + variable_name
        
    # Check if the variable name is a Python keyword and add an underscore if necessary
    keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
                'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import',
                'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
                'True', 'try', 'while', 'with', 'yield']
    if variable_name in keywords:
        variable_name += '_'
    
    return variable_name

input_string_1 = "Equity, foreign, currency translation difference"
variable_name_1 = create_variable_name(input_string_1)
print(variable_name_1)

input_string_2 = "Subscribed capital / capital account / capital shares"
variable_name_2 = create_variable_name(input_string_2)
print(variable_name_2)

input_string_3 = "Other liabilities, of which social security"
variable_name_3 = create_variable_name(input_string_3)
print(variable_name_3)
