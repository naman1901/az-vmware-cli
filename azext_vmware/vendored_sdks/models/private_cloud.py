# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource import TrackedResource


class PrivateCloud(TrackedResource):
    """A private cloud resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The private cloud SKU
    :type sku: ~vendored_sdks.models.Sku
    :param properties: The properties of a private cloud resource
    :type properties: ~vendored_sdks.models.PrivateCloudProperties
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "sku": {"key": "sku", "type": "Sku"},
        "properties": {"key": "properties", "type": "PrivateCloudProperties"},
    }

    def __init__(self, **kwargs):
        super(PrivateCloud, self).__init__(**kwargs)
        self.sku = kwargs.get("sku", None)
        self.properties = kwargs.get("properties", None)
