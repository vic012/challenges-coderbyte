import re


class ValidationUsername:

    def __init__(self, strParam: str) -> None:
        self._str_param = strParam

    def _validate_length(self) -> bool:
        # ----> Rule 1: The username is between 4 and 25 characters
        # It cannot be less than 4 or greater than 25 characters.
        # If so, the username is invalid, then return "false"
        return bool(len(self._str_param) < 4 or len(self._str_param) > 25)

    def _validate_start_with_letter(self) -> bool:
        # ----> Rule 2: It must start with a letter
        start_letter = self._str_param[0] # Get the first letter
        start_letter_result = re.match(r'[a-zA-Z]', start_letter)
        return bool(start_letter_result)

    def _validate_character(self) -> bool:
        # ----> Rule 3: It can only contain letters, numbers, and the underscore character.
        # We will to check if the text have this pattern
        result_pattern = re.match(r'^[a-zA-Z0-9_]+$', self._str_param)
        # If the pattern is not matched, the strParam is invalid
        return bool(result_pattern)

    def _validate_cannot_end_with_underscore(self) -> bool:
        # ----> Rule 4
        # It cannot end with an underscore character.
        return self._str_param.endswith("_")

    @property
    def result_validation(self) -> str:

        validate_length = self._validate_length()
        if validate_length is True:
            return "false"

        validate_start_with_letter = self._validate_start_with_letter()
        if validate_start_with_letter is False:
            return "false"

        validate_character = self._validate_character()
        if validate_character is False:
            return "false"

        validate_cannot_end_with_underscore = self._validate_cannot_end_with_underscore()
        if validate_cannot_end_with_underscore is True:
            return "false"

        # All rules passed, the username is valid
        return "true"


def CodelandUsernameValidation(strParam):

    validate_username = ValidationUsername(strParam)
    return validate_username.result_validation


# keep this function call here 
print(CodelandUsernameValidation(input()))