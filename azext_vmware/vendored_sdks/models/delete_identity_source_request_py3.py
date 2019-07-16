# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeleteIdentitySourceRequest(Model):
    """DeleteIdentitySourceRequest.

    :param name:
    :type name: str
    :param alias:
    :type alias: str
    :param domain:
    :type domain: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, alias: str=None, domain: str=None, **kwargs) -> None:
        super(DeleteIdentitySourceRequest, self).__init__(**kwargs)
        self.name = name
        self.alias = alias
        self.domain = domain
