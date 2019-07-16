# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Endpoints(Model):
    """Endpoints.

    :param nsx_manager:
    :type nsx_manager: str
    :param vcsa:
    :type vcsa: str
    """

    _attribute_map = {
        'nsx_manager': {'key': 'nsxManager', 'type': 'str'},
        'vcsa': {'key': 'vcsa', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Endpoints, self).__init__(**kwargs)
        self.nsx_manager = kwargs.get('nsx_manager', None)
        self.vcsa = kwargs.get('vcsa', None)
