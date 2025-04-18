import hashlib
from functools import lru_cache

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Hash a password using SHA256 and a strong password hash e.g. bcrypt.

    Args:
        password (str): the password to hash

    Returns:
        str: the hashed password

    """
    return pwd_context.hash(password)


def verify_password(incoming_password: str, existing_password: str) -> bool:
    """Safely compare two strings using SHA256 and a strong password hash e.g. bcrypt.

    Args:
        incoming_password (str): the password to check
        existing_password (str): the password to check against

    Returns:
        bool: True if the passwords match, False otherwise
    """
    return verify_hashs(
        hashlib.sha256(incoming_password.encode()).hexdigest(),
        hashlib.sha256(existing_password.encode()).hexdigest(),
    )


@lru_cache
def verify_hashs(incoming_hash: str, existing_hash: str) -> bool:
    """Compare two hashs using a slow hash algorithm and a cache.

    The cache will speed up repeated password checks (e.g. the correct credentials), but sill slow
    down brute force attacks. To prevent timing attacks of the caching layer, an other hash
    function must be used before the caching layer.

    Args:
        incoming_hash (str): the hash to check
        existing_hash (str): the hash to check against

    Returns:
        bool: True if the hashs match, False otherwise
    """
    return pwd_context.verify(incoming_hash, get_password_hash(existing_hash))
