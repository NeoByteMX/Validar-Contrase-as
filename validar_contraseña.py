def validate_password(password: str) -> bool:
    """
    Validates whether a password meets the established security criteria.

    Criteria:
    - At least 8 characters in length.
    - At least one uppercase letter.
    - At least one lowercase letter.
    - At least one number.
    - At least one special symbol (@, #, $, %).
    - Does not contain disallowed symbols.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is secure.

    Raises:
        ValueError: If the password does not meet any of the criteria.
    """
    import string

    # Define allowed special symbols (excluding space)
    special_symbols = "@#$%"

    # Define all symbols that can appear in the password
    total_symbols = set(string.punctuation)

    # Symbols that are not allowed
    disallowed_symbols = total_symbols - set(special_symbols)

    # Check for minimum length
    if len(password) < 8:
        raise ValueError("The password must have at least 8 characters.")

    # Initialize flags for each criterion
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_symbol = False

    # Validate each character in the password
    for character in password:
        if character.islower():
            has_lowercase = True
        elif character.isupper():
            has_uppercase = True
        elif character.isdigit():
            has_number = True
        elif character in special_symbols:
            has_symbol = True
        elif character in disallowed_symbols:
            raise ValueError(f"The password contains a disallowed symbol: '{character}'.")

    # Check if all criteria are met
    meets_criteria = [has_uppercase, has_lowercase, has_number, has_symbol]
    if not all(meets_criteria):
        # Identify which criterion is not met to provide a specific message
        if not has_uppercase:
            raise ValueError("The password must contain at least one uppercase letter.")
        if not has_lowercase:
            raise ValueError("The password must contain at least one lowercase letter.")
        if not has_number:
            raise ValueError("The password must contain at least one number.")
        if not has_symbol:
            raise ValueError("The password must contain at least one special symbol (@, #, $, %).")

    return True

# Examples
passwords = ["password1@", "#S53uJQysbyz(wpT", "Example123", "Abc@123", "Valid#Pass1", "BadPass!"]

for pwd in passwords:
    try:
        if validate_password(pwd):
            print(f"The password '{pwd}' is secure!")
    except ValueError as error:
        print(f"Password '{pwd}': {error}")
