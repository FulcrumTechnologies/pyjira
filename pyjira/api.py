"""Functions needed to access the Jira API."""
import os
import sys

try:
    import requests
except ImportError:
    sys.stderr.write("You do not have the 'requests' module installed. "
                     "Please see http://docs.python-requests.org/en/latest/ "
                     "for more information.")
    sys.exit("Error")


requests.packages.urllib3.disable_warnings()

token = ""
user = ""
base_url = ""


def load_variables():
    """Load variables from environment variables."""

    if (not os.environ.get("PYJIRA_TOKEN") or
            not os.environ.get("PYJIRA_USER") or
            not os.environ.get("PYJIRA_ORG")):
        print ("One or more pyjira environment variables are not set. "
               "See README for directions on how to resolve this.")
        sys.exit("Error")

    global token
    global user
    global base_url
    token = os.environ["PYJIRA_TOKEN"]
    user = os.environ["PYJIRA_USER"]
    base_url = ("https://" + os.environ["PYJIRA_ORG"] + ".atlassian"
                ".net/rest/api/2")


def rest(url, req='get', data=None):
    """Main function to be called from this module.
    send a request using method 'req' and to the url. the _rest() function
    will add the base_url to this, so 'url' should be something like '/ips'.
    """
    load_variables()

    return _rest(req, base_url + url, data)


def _rest(req, url, data=None):
    """Send a rest rest request to the server."""

    if 'HTTPS' not in url.upper():
        print("Secure connection required: Please use HTTPS or https")
        return ""

    cmd = req.upper()
    if cmd != "GET" and cmd != "PUT" and cmd != "POST" and cmd != "DELETE":
        return ""

    status, body = _api_action(cmd, url, data)
    if (int(status) >= 200 and int(status) <= 226):
        return body
    else:
        return body


def _api_action(cmd, url, data=None):
    """Take action based on what kind of request is needed."""
    requisite_headers = {'Accept': 'application/json',
                         'Content-Type': 'application/json'}
    auth = (user, token)

    if cmd == "GET":
        response = requests.get(url, headers=requisite_headers, auth=auth)
    elif cmd == "PUT":
        response = requests.put(url, headers=requisite_headers, auth=auth,
                                data=data)
    elif cmd == "POST":
        response = requests.post(url, headers=requisite_headers, auth=auth,
                                 data=data)
    elif cmd == "DELETE":
        response = requests.delete(url, headers=requisite_headers, auth=auth)

    return response.status_code, response.text
