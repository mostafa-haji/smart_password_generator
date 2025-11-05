import random
import string
def generate_password(length=12, smart_mode=True , _symbols="!@#$%^&*()_+-=[]{};:,.<>?"):
       
    """
    Generate a random password.

    Parameters:
        length (int): The desired length of the password (default: 12)
        smart_mode (bool): If True, include at least one uppercase, lowercase, digit, and symbol
        _symbols (str): Optional set of symbols to include

    Returns:
        str: A randomly generated password
    """

    if smart_mode:
        chars = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(_symbols)
        ]
    
        if (length-4)> 0:
            all_chars = string.ascii_letters + string.digits + _symbols
            chars += random.choices(all_chars, k=length - 4)
            random.shuffle(chars)
            return ''.join(chars)

        if (length-4) == 0:
            return ''.join(chars)
        else:
            return "The minimum value length 4."
    else:
        all_chars = string.ascii_letters + string.digits
        return ''.join(random.choices(all_chars, k=length))


if __name__=="__main__":
    print(generate_password())
    print(generate_password(smart_mode=False))
    print(generate_password(length=4,smart_mode=False))
    print(generate_password(length=4))