# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GlobalReachConnectionRequest(Model):
    """GlobalReachConnectionRequest.

    :param id:
    :type id: str
    :param key:
    :type key: str
    :param network:
    :type network: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'network': {'key': 'network', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, key: str=None, network: str=None, **kwargs) -> None:
        super(GlobalReachConnectionRequest, self).__init__(**kwargs)
        self.id = id
        self.key = key
        self.network = network
