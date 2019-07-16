# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MoveResourceRequest(Model):
    """MoveResourceRequest.

    :param target_resource_group:
    :type target_resource_group: str
    :param resources:
    :type resources: list[str]
    """

    _attribute_map = {
        'target_resource_group': {'key': 'targetResourceGroup', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(MoveResourceRequest, self).__init__(**kwargs)
        self.target_resource_group = kwargs.get('target_resource_group', None)
        self.resources = kwargs.get('resources', None)