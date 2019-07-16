# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureClusterResponse(Model):
    """AzureClusterResponse.

    :param location:
    :type location: str
    :param name:
    :type name: str
    :param properties:
    :type properties: ~vendored_sdks.models.Cluster
    :param type:
    :type type: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'Cluster'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, name: str=None, properties=None, type: str=None, **kwargs) -> None:
        super(AzureClusterResponse, self).__init__(**kwargs)
        self.location = location
        self.name = name
        self.properties = properties
        self.type = type
