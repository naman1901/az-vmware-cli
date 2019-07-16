# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzurePrivateCloudResponse(Model):
    """AzurePrivateCloudResponse.

    :param location:
    :type location: str
    :param name:
    :type name: str
    :param properties:
    :type properties: ~vendored_sdks.models.PrivateCloud
    :param type:
    :type type: str
    :param tags:
    :type tags: object
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'PrivateCloud'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AzurePrivateCloudResponse, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.type = kwargs.get('type', None)
        self.tags = kwargs.get('tags', None)