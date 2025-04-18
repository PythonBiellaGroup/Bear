def fake(message: str, mooving: int = 4) -> str:
    """Encrypts a message by shifting each character by a given number of positions.

    Args:
        message (str): The message to be encrypted.
        mooving (int, optional): The number of positions to shift each character. Defaults to 4.

    Returns:
        str: The encrypted message.
    """
    # Define the caracters list to encrypt, including common accented letters
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for char in message:
        if char in characters:
            # Find the position of the char after the mooving
            new_index = (characters.index(char) + mooving) % len(characters)
            result += characters[new_index]
        else:
            # If the char is not in the list, leave it unchanged
            result += char
    return result


def unfake(message: str, mooving: int = -4) -> str:
    """Decrypts a message by shifting each character by a given amount.

    Args:
        message (str): The message to be decrypted.
        mooving (int, optional): The amount by which each character should be shifted. Defaults to -4.

    Returns:
        str: The decrypted message.
    """
    # Define the character you want to decrypt
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for char in message:
        if char in characters:
            # Find the position of the char after the mooving
            indice_nuovo = (characters.index(char) + mooving) % len(characters)
            result += characters[indice_nuovo]
        else:
            # If the char is not in the list, leave it unchanged
            result += char
    return result
