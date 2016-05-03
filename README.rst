======================================
PyJira REST API wrapper
======================================

Setup
---------------

First, you're gonna want to do this:

    pip install pyjira

You're already halfway there!

Next, you need to set up your environment variables.

Go to your home directory (~/) and put this in ".pyjira":

    export PYJIRA_USER=put your username here
    export PYJIRA_TOKEN=put your password here
    export PYJIRA_ORG=put the organization name here

Next, add this to ".bash_profile", also in the home directory:

    source ~/.pyjira

On startup, these environment variables will be loaded and you will be able to
use PyJira. Woot!

Usage
---------------

To use, import like so:

    import pyjira

To get issues relating to a project:

    pyjira.get_issues("SpaceJam")  # Where "SpaceJam" is the project name

You can also limit the amount of results you get (default=50):

    pyjira.get_issues("SpaceJam", 20)  # 20 maximum results

To get a specific issue, call get_issue() with the issue's id/key:

    pyjira.get_issue("SpaceJam-931")

To get all existing fields, call get_all_fields():

    pyjira.get_all_fields()

To get a specific field:

    pyjira.get_field("customfield_90010")  # You can also just pass "90010"

To get all fields within an issue:

    pyjira.get_issue_fields("SpaceJam-931")  # Add False as a second parameter to get result with "customfield_#" field names

WIP
---------------

This project doesn't have many functions at the moment, but it will be added to
whenever a new one is needed.
