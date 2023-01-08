# def deprecation_warning():
#     print("""

# =============================================================================
# *** DEPRECATION WARNING ***

# Insert here you message

# Please update any scripts/automation you have to append the `-c v1` option,
# which is available now.

# =============================================================================

#     """)


# deprecation_warning()

# import re
# import sys

# PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
# project_name = "{{cookiecutter.project}}"
# if not re.match(PROJECT_NAME_REGEX, project_name):
#     print(
#         "ERROR: The project name (%s) is not a valid Python module name. Please do not use a _ and use - instead"
#         % project_name
#     )
#     # Exit to cancel project
#     sys.exit(1)

# DIRECTORY_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
# directory_name = "{{cookiecutter.directory_name}}"
# if not re.match(DIRECTORY_NAME_REGEX, directory_name):
#     print(
#         "ERROR: The directory name (%s) is not a valid Python module name. Please do not use a - and use _ instead"
#         % directory_name
#     )
#     # Exit to cancel project
#     sys.exit(1)