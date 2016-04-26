import pyjira.api as _api
import json as _json


def get_summary(id):
    """Get summary of a ticket."""
    return _api.rest("/issue/" + str(id))
