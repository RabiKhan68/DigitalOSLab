from logger_module import (
    log_event,
    log_warning
)

# USER ROLE DATABASE

users = {
    "admin1": "admin",
    "ali": "student",
    "guest1": "guest"
}

# GET USER ROLE

def get_role(username):
    """
    Return the role of a given user.
    """

    return users.get(username, None)

# ACCESS CONTROL FUNCTIONS

def can_read(role):
    """
    Check if the user has read permission.
    """

    return role in [
        "admin",
        "student",
        "guest"
    ]


def can_write(role):
    """
    Check if the user has write permission.
    """

    return role in [
        "admin",
        "student"
    ]


def can_delete(role):
    """
    Check if the user has delete permission.
    Only admin can delete files.
    """

    return role == "admin"

# SECURITY VIOLATION LOGGER

def log_security_violation(username, action):
    """
    Log unauthorized access attempts.
    """

    message = (
        f"SECURITY VIOLATION | "
        f"User: {username} | "
        f"Attempted Action: {action}"
    )

    print("\n========================================")
    print("           ACCESS DENIED")
    print("========================================")

    print(f"User   : {username}")

    print(f"Action : {action}")

    print("\nUnauthorized operation detected.")

    print("========================================")

    # Log warning event
    log_warning(message)

    # Console logging
    log_event(message)
