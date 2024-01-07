import re

def CodelandUsernameValidation(strParam):
    # ----> Rule 1: The username is between 4 and 25 characters
    # It cannot be less than 4 or greater than 25 characters.
    # If so, the username is invalid, then return "false"
    if len(strParam) < 4 or len(strParam) > 25:
        return "false"
    # ----<

    # ----> Rule 2: It must start with a letter
    start_letter = strParam[0] # Get the first letter
    start_letter_result = re.match(r'[a-zA-Z]', start_letter)
    if not start_letter_result:
        return "false"
    # ----<

    # ----> Rule 3: It can only contain letters, numbers, and the underscore character.
    # We will to check if the text have this pattern
    result_pattern = re.match(r'^[a-zA-Z0-9_]+$', strParam)
    # If the pattern is not matched, the strParam is invalid
    if not result_pattern:
        return "false"
    # ----<

    # ----> Rule 4
    # It cannot end with an underscore character.
    if strParam.endswith("_"):
        return "false"

    # All rules passed, the username is valid
    return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))