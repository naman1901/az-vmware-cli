# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrivateCloud(Model):
    """PrivateCloud.

    :param provisioning_state: Possible values include: 'Succeeded', 'Failed',
     'Cancelled'
    :type provisioning_state: str or ~vendored_sdks.models.enum
    :param circuit:
    :type circuit: ~vendored_sdks.models.Circuit
    :param cluster:
    :type cluster: ~vendored_sdks.models.Cluster
    :param clusters:
    :type clusters: list[str]
    :param endpoints:
    :type endpoints: ~vendored_sdks.models.Endpoints
    :param internet_enabled:
    :type internet_enabled: bool
    :param identity_sources:
    :type identity_sources: list[~vendored_sdks.models.IdentitySource]
    :param vpc:
    :type vpc: str
    """

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'circuit': {'key': 'circuit', 'type': 'Circuit'},
        'cluster': {'key': 'cluster', 'type': 'Cluster'},
        'clusters': {'key': 'clusters', 'type': '[str]'},
        'endpoints': {'key': 'endpoints', 'type': 'Endpoints'},
        'internet_enabled': {'key': 'internetEnabled', 'type': 'bool'},
        'identity_sources': {'key': 'identitySources', 'type': '[IdentitySource]'},
        'vpc': {'key': 'vpc', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PrivateCloud, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.circuit = kwargs.get('circuit', None)
        self.cluster = kwargs.get('cluster', None)
        self.clusters = kwargs.get('clusters', None)
        self.endpoints = kwargs.get('endpoints', None)
        self.internet_enabled = kwargs.get('internet_enabled', None)
        self.identity_sources = kwargs.get('identity_sources', None)
        self.vpc = kwargs.get('vpc', None)
