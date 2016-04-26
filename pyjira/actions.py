import pyjira.api as _api
import json as _json


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
