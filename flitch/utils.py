"""This module stores helpers for flitch project"""

# Standard Library
from os import path


def path_exists(resource_path: str) -> bool:
    """Checks if path exists

    Args:
        resource_path (str): Path to a resource in filesystem

    Returns:
        bool: Boolean response
    """
    return path.exists(resource_path)


def path_is_file(resource_path: str) -> bool:
    """Checks if path is file

    Args:
        resource_path (str): Path to a resource in filesystem

    Returns:
        bool: Boolean response
    """
    return path.exists(resource_path) and path.isfile(resource_path)


def path_is_folder(resource_path: str) -> bool:
    """Checks if a path is a folder

    Args:
        resource_path (str): Path to a resource in filesystem

    Returns:
        bool: Boolean response
    """
    return path.isdir(resource_path)
