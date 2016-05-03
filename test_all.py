"""Script for testing the whole of pyjira."""

import pyjira
import os


def run():
    """Commence testing!"""

    # Check if variables are present
    if (not os.environ.get("PYJIRA_TEST_PROJECT") or
            not os.environ.get("PYJIRA_TEST_ISSUE") or
            not os.environ.get("PYJIRA_TEST_FIELD")):
        print ("One or more testing environment variables are not set.")

    project = os.environ["PYJIRA_TEST_PROJECT"]
    issue = os.environ["PYJIRA_TEST_ISSUE"]
    field = os.environ["PYJIRA_TEST_FIELD"]

    print ("Trying get_issues().")
    print (pyjira.get_issues(project, 5))
    print ("Trying get_issue().")
    print (pyjira.get_issue(issue))
    print ("Trying get_all_fields().")
    print (pyjira.get_all_fields())
    print ("Trying get_field().")
    print (pyjira.get_field(field))
    print ("Trying get_issue_fields().")
    print (pyjira.get_issue_fields(issue))
    print ("Trying get_issue_fields() without field names.")
    print (pyjira.get_issue_fields(issue, False))

    print ("\n\nJob\'s done.")


if __name__ == "__main__":
    run()
