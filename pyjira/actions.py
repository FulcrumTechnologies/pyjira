import pyjira.api as _api
import json as _json


def get_issues(id, limit=50):
    """Return 50 issues for a project.
    Parameters:
    - id: id of a project.
    - limit: max number of results to be returned.
    """
    return _api.rest("/search?jql=project=" + str(id) + "&maxResults=" + str(limit))


def get_issue(id):
    """Get issue and its details.
    Parameters:
    - id: id of an issue.
    """
    return _api.rest("/issue/" + str(id))


def get_all_fields():
    """Get all existing fields."""
    return _api.rest("/field")


def get_field(id):
    """Get field and its details.
    Parameters:
    - id: id of a field.
    """
    fields = _json.loads(get_all_fields())
    for f in fields:
        if (f["id"] == str(id) or
                f["id"].replace("customfield_", "") == str(id)):
            return _json.dumps(f)


def get_issue_fields(id, field_names_enabled=True):
    """Get all fields listed for an issue.
    Parameters:
    - id: id of an issue.
    - field_names_enabled: if False, returns result with "customfield_" names.
      True by default.
    """
    issue = _json.loads(get_issue(id))

    result = {}

    for key, value in issue["fields"].items():
        if ("customfield_" in key and
                value and field_names_enabled):
            field = _json.loads(get_field(key))
            field_name = field["name"]
            result[field_name] = value
        elif value:
            result[key] = value

    return _json.dumps(result)
