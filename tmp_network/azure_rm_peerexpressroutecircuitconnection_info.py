#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_peerexpressroutecircuitconnection_info
version_added: '2.9'
short_description: Get PeerExpressRouteCircuitConnection info.
description:
  - Get info of PeerExpressRouteCircuitConnection.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  circuit_name:
    description:
      - The name of the express route circuit.
      - The name of the circuit.
    required: true
    type: str
  peering_name:
    description:
      - The name of the peering.
    required: true
    type: str
  connection_name:
    description:
      - The name of the peer express route circuit connection.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: PeerExpressRouteCircuitConnectionGet
      azure_rm_peerexpressroutecircuitconnection_info: 
        circuit_name: ExpressRouteARMCircuitA
        connection_name: 60aee347-e889-4a42-8c1b-0aae8b1e4013
        peering_name: AzurePrivatePeering
        resource_group_name: rg1
        

    - name: List Peer ExpressRouteCircuit Connection
      azure_rm_peerexpressroutecircuitconnection_info: 
        circuit_name: ExpressRouteARMCircuitA
        peering_name: AzurePrivatePeering
        resource_group_name: rg1
        

'''

RETURN = '''
peer_express_route_circuit_connections:
  description: >-
    A list of dict results where the key is the name of the
    PeerExpressRouteCircuitConnection and the values are the facts for that
    PeerExpressRouteCircuitConnection.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the resource.
      returned: always
      type: str
      sample: null
    express_route_circuit_peering:
      description:
        - >-
          Reference to Express Route Circuit Private Peering Resource of the
          circuit.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    peer_express_route_circuit_peering:
      description:
        - >-
          Reference to Express Route Circuit Private Peering Resource of the
          peered circuit.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    address_prefix:
      description:
        - /29 IP address space to carve out Customer addresses for tunnels.
      returned: always
      type: str
      sample: null
    circuit_connection_status:
      description:
        - Express Route Circuit connection state.
      returned: always
      type: str
      sample: null
    connection_name:
      description:
        - The name of the express route circuit connection resource.
      returned: always
      type: str
      sample: null
    auth_resource_guid:
      description:
        - >-
          The resource guid of the authorization used for the express route
          circuit connection.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the peer express route circuit connection
          resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - >-
          The global reach peer circuit connection associated with Private
          Peering in an ExpressRoute Circuit.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        express_route_circuit_peering:
          description:
            - >-
              Reference to Express Route Circuit Private Peering Resource of the
              circuit.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        peer_express_route_circuit_peering:
          description:
            - >-
              Reference to Express Route Circuit Private Peering Resource of the
              peered circuit.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        address_prefix:
          description:
            - /29 IP address space to carve out Customer addresses for tunnels.
          returned: always
          type: str
          sample: null
        connection_name:
          description:
            - The name of the express route circuit connection resource.
          returned: always
          type: str
          sample: null
        auth_resource_guid:
          description:
            - >-
              The resource guid of the authorization used for the express route
              circuit connection.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPeerExpressRouteCircuitConnectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            circuit_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
                type='str',
                required=True
            ),
            connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.circuit_name = None
        self.peering_name = None
        self.connection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPeerExpressRouteCircuitConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.circuit_name is not None and
            self.peering_name is not None and
            self.connection_name is not None):
            self.results['peer_express_route_circuit_connections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.circuit_name is not None and
              self.peering_name is not None):
            self.results['peer_express_route_circuit_connections'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.peer_express_route_circuit_connections.get(resource_group_name=self.resource_group_name,
                                                                                   circuit_name=self.circuit_name,
                                                                                   peering_name=self.peering_name,
                                                                                   connection_name=self.connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.peer_express_route_circuit_connections.list(resource_group_name=self.resource_group_name,
                                                                                    circuit_name=self.circuit_name,
                                                                                    peering_name=self.peering_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
                result.append(tmp.as_dict())
            return result


def main():
    AzureRMPeerExpressRouteCircuitConnectionInfo()


if __name__ == '__main__':
    main()
