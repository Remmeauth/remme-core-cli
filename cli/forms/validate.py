"""
Provide implementation validation.
"""
from marshmallow import (
    Schema,
    fields,
)

from ._fields import (
    FamilyName,
    Id,
    IdList,
    Limit,
    NodeAddress,
    NodeURL,
)


class ValidationForm(Schema):
    """
    Validation form for all parameters.
    """

    address = NodeAddress(allow_none=True)
    ids = IdList(allow_none=True)
    id = Id(allow_none=True)
    start = Id(allow_none=True)
    head = Id(allow_none=True)
    limit = Limit(allow_none=True)
    family_name = FamilyName(allow_none=True)
    reverse = fields.String(allow_none=True)
    node_url = NodeURL(allow_none=True)
