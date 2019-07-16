# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.private_cloud_operations import PrivateCloudOperations
from .operations.cluster_operations import ClusterOperations
from . import models


class VirtustreamClientConfiguration(AzureConfiguration):
    """Configuration for VirtustreamClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The unique identifier for a Microsoft Azure
     subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'http://localhost'

        super(VirtustreamClientConfiguration, self).__init__(base_url)

        self.add_user_agent('virtustreamclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class VirtustreamClient(SDKClient):
    """API for managing Virtustream Private Clouds through Azure.

    :ivar config: Configuration for client.
    :vartype config: VirtustreamClientConfiguration

    :ivar private_cloud: PrivateCloud operations
    :vartype private_cloud: vendored_sdks.operations.PrivateCloudOperations
    :ivar cluster: Cluster operations
    :vartype cluster: vendored_sdks.operations.ClusterOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The unique identifier for a Microsoft Azure
     subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = VirtustreamClientConfiguration(credentials, subscription_id, base_url)
        super(VirtustreamClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-09-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.private_cloud = PrivateCloudOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cluster = ClusterOperations(
            self._client, self.config, self._serialize, self._deserialize)