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
module: azure_rm_expressroutecircuitpeering_info
version_added: '2.9'
short_description: Get ExpressRouteCircuitPeering info.
description:
  - Get info of ExpressRouteCircuitPeering.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  circuit_name:
    description:
      - The name of the express route circuit.
    required: true
    type: str
  peering_name:
    description:
      - The name of the peering.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get ExpressRouteCircuit Peering
      azure_rm_expressroutecircuitpeering_info: 
        circuit_name: circuitName
        peering_name: MicrosoftPeering
        resource_group_name: rg1
        

    - name: List ExpressRouteCircuit Peerings
      azure_rm_expressroutecircuitpeering_info: 
        circuit_name: circuitName
        resource_group_name: rg1
        

'''

RETURN = '''
express_route_circuit_peerings:
  description: >-
    A list of dict results where the key is the name of the
    ExpressRouteCircuitPeering and the values are the facts for that
    ExpressRouteCircuitPeering.
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
    peering_type:
      description:
        - The peering type.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The peering state.
      returned: always
      type: str
      sample: null
    azure_asn:
      description:
        - The Azure ASN.
      returned: always
      type: integer
      sample: null
    peer_asn:
      description:
        - The peer ASN.
      returned: always
      type: integer
      sample: null
    primary_peer_address_prefix:
      description:
        - The primary address prefix.
      returned: always
      type: str
      sample: null
    secondary_peer_address_prefix:
      description:
        - The secondary address prefix.
      returned: always
      type: str
      sample: null
    primary_azure_port:
      description:
        - The primary port.
      returned: always
      type: str
      sample: null
    secondary_azure_port:
      description:
        - The secondary port.
      returned: always
      type: str
      sample: null
    shared_key:
      description:
        - The shared key.
      returned: always
      type: str
      sample: null
    vlan_id:
      description:
        - The VLAN ID.
      returned: always
      type: integer
      sample: null
    microsoft_peering_config:
      description:
        - The Microsoft peering configuration.
      returned: always
      type: dict
      sample: null
      contains:
        advertised_public_prefixes:
          description:
            - The reference to AdvertisedPublicPrefixes.
          returned: always
          type: list
          sample: null
        advertised_communities:
          description:
            - The communities of bgp peering. Specified for microsoft peering.
          returned: always
          type: list
          sample: null
        legacy_mode:
          description:
            - The legacy mode of the peering.
          returned: always
          type: integer
          sample: null
        customer_asn:
          description:
            - The CustomerASN of the peering.
          returned: always
          type: integer
          sample: null
        routing_registry_name:
          description:
            - The RoutingRegistryName of the configuration.
          returned: always
          type: str
          sample: null
    stats:
      description:
        - The peering stats of express route circuit.
      returned: always
      type: dict
      sample: null
      contains:
        primarybytes_in:
          description:
            - The Primary BytesIn of the peering.
          returned: always
          type: integer
          sample: null
        primarybytes_out:
          description:
            - The primary BytesOut of the peering.
          returned: always
          type: integer
          sample: null
        secondarybytes_in:
          description:
            - The secondary BytesIn of the peering.
          returned: always
          type: integer
          sample: null
        secondarybytes_out:
          description:
            - The secondary BytesOut of the peering.
          returned: always
          type: integer
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the express route circuit peering resource.
      returned: always
      type: str
      sample: null
    gateway_manager_etag:
      description:
        - The GatewayManager Etag.
      returned: always
      type: str
      sample: null
    last_modified_by:
      description:
        - Who was the last to modify the peering.
      returned: always
      type: str
      sample: null
    route_filter:
      description:
        - The reference to the RouteFilter resource.
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
    ipv6_peering_config:
      description:
        - The IPv6 peering configuration.
      returned: always
      type: dict
      sample: null
      contains:
        primary_peer_address_prefix:
          description:
            - The primary address prefix.
          returned: always
          type: str
          sample: null
        secondary_peer_address_prefix:
          description:
            - The secondary address prefix.
          returned: always
          type: str
          sample: null
        microsoft_peering_config:
          description:
            - The Microsoft peering configuration.
          returned: always
          type: dict
          sample: null
          contains:
            advertised_public_prefixes:
              description:
                - The reference to AdvertisedPublicPrefixes.
              returned: always
              type: list
              sample: null
            advertised_communities:
              description:
                - >-
                  The communities of bgp peering. Specified for microsoft
                  peering.
              returned: always
              type: list
              sample: null
            legacy_mode:
              description:
                - The legacy mode of the peering.
              returned: always
              type: integer
              sample: null
            customer_asn:
              description:
                - The CustomerASN of the peering.
              returned: always
              type: integer
              sample: null
            routing_registry_name:
              description:
                - The RoutingRegistryName of the configuration.
              returned: always
              type: str
              sample: null
        route_filter:
          description:
            - The reference to the RouteFilter resource.
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
        state:
          description:
            - The state of peering.
          returned: always
          type: str
          sample: null
    express_route_connection:
      description:
        - The ExpressRoute connection.
      returned: always
      type: dict
      sample: null
    connections:
      description:
        - >-
          The list of circuit connections associated with Azure Private Peering
          for this circuit.
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
              circuit initiating connection.
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
        authorization_key:
          description:
            - The authorization key.
          returned: always
          type: str
          sample: null
        ipv6_circuit_connection_config:
          description:
            - >-
              IPv6 Address PrefixProperties of the express route circuit
              connection.
          returned: always
          type: dict
          sample: null
          contains:
            address_prefix:
              description:
                - >-
                  /125 IP address space to carve out customer addresses for
                  global reach.
              returned: always
              type: str
              sample: null
    peered_connections:
      description:
        - >-
          The list of peered circuit connections associated with Azure Private
          Peering for this circuit.
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
    value:
      description:
        - The peerings in an express route circuit.
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
        peering_type:
          description:
            - The peering type.
          returned: always
          type: str
          sample: null
        state:
          description:
            - The peering state.
          returned: always
          type: str
          sample: null
        azure_asn:
          description:
            - The Azure ASN.
          returned: always
          type: integer
          sample: null
        peer_asn:
          description:
            - The peer ASN.
          returned: always
          type: integer
          sample: null
        primary_peer_address_prefix:
          description:
            - The primary address prefix.
          returned: always
          type: str
          sample: null
        secondary_peer_address_prefix:
          description:
            - The secondary address prefix.
          returned: always
          type: str
          sample: null
        primary_azure_port:
          description:
            - The primary port.
          returned: always
          type: str
          sample: null
        secondary_azure_port:
          description:
            - The secondary port.
          returned: always
          type: str
          sample: null
        shared_key:
          description:
            - The shared key.
          returned: always
          type: str
          sample: null
        vlan_id:
          description:
            - The VLAN ID.
          returned: always
          type: integer
          sample: null
        microsoft_peering_config:
          description:
            - The Microsoft peering configuration.
          returned: always
          type: dict
          sample: null
          contains:
            advertised_public_prefixes:
              description:
                - The reference to AdvertisedPublicPrefixes.
              returned: always
              type: list
              sample: null
            advertised_communities:
              description:
                - >-
                  The communities of bgp peering. Specified for microsoft
                  peering.
              returned: always
              type: list
              sample: null
            legacy_mode:
              description:
                - The legacy mode of the peering.
              returned: always
              type: integer
              sample: null
            customer_asn:
              description:
                - The CustomerASN of the peering.
              returned: always
              type: integer
              sample: null
            routing_registry_name:
              description:
                - The RoutingRegistryName of the configuration.
              returned: always
              type: str
              sample: null
        stats:
          description:
            - The peering stats of express route circuit.
          returned: always
          type: dict
          sample: null
          contains:
            primarybytes_in:
              description:
                - The Primary BytesIn of the peering.
              returned: always
              type: integer
              sample: null
            primarybytes_out:
              description:
                - The primary BytesOut of the peering.
              returned: always
              type: integer
              sample: null
            secondarybytes_in:
              description:
                - The secondary BytesIn of the peering.
              returned: always
              type: integer
              sample: null
            secondarybytes_out:
              description:
                - The secondary BytesOut of the peering.
              returned: always
              type: integer
              sample: null
        gateway_manager_etag:
          description:
            - The GatewayManager Etag.
          returned: always
          type: str
          sample: null
        route_filter:
          description:
            - The reference to the RouteFilter resource.
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
        ipv6_peering_config:
          description:
            - The IPv6 peering configuration.
          returned: always
          type: dict
          sample: null
          contains:
            primary_peer_address_prefix:
              description:
                - The primary address prefix.
              returned: always
              type: str
              sample: null
            secondary_peer_address_prefix:
              description:
                - The secondary address prefix.
              returned: always
              type: str
              sample: null
            microsoft_peering_config:
              description:
                - The Microsoft peering configuration.
              returned: always
              type: dict
              sample: null
              contains:
                advertised_public_prefixes:
                  description:
                    - The reference to AdvertisedPublicPrefixes.
                  returned: always
                  type: list
                  sample: null
                advertised_communities:
                  description:
                    - >-
                      The communities of bgp peering. Specified for microsoft
                      peering.
                  returned: always
                  type: list
                  sample: null
                legacy_mode:
                  description:
                    - The legacy mode of the peering.
                  returned: always
                  type: integer
                  sample: null
                customer_asn:
                  description:
                    - The CustomerASN of the peering.
                  returned: always
                  type: integer
                  sample: null
                routing_registry_name:
                  description:
                    - The RoutingRegistryName of the configuration.
                  returned: always
                  type: str
                  sample: null
            route_filter:
              description:
                - The reference to the RouteFilter resource.
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
            state:
              description:
                - The state of peering.
              returned: always
              type: str
              sample: null
        connections:
          description:
            - >-
              The list of circuit connections associated with Azure Private
              Peering for this circuit.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within a resource
                  group. This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            express_route_circuit_peering:
              description:
                - >-
                  Reference to Express Route Circuit Private Peering Resource of
                  the circuit initiating connection.
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
                  Reference to Express Route Circuit Private Peering Resource of
                  the peered circuit.
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
                - >-
                  /29 IP address space to carve out Customer addresses for
                  tunnels.
              returned: always
              type: str
              sample: null
            authorization_key:
              description:
                - The authorization key.
              returned: always
              type: str
              sample: null
            ipv6_circuit_connection_config:
              description:
                - >-
                  IPv6 Address PrefixProperties of the express route circuit
                  connection.
              returned: always
              type: dict
              sample: null
              contains:
                address_prefix:
                  description:
                    - >-
                      /125 IP address space to carve out customer addresses for
                      global reach.
                  returned: always
                  type: str
                  sample: null
        peered_connections:
          description:
            - >-
              The list of peered circuit connections associated with Azure
              Private Peering for this circuit.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within a resource
                  group. This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            express_route_circuit_peering:
              description:
                - >-
                  Reference to Express Route Circuit Private Peering Resource of
                  the circuit.
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
                  Reference to Express Route Circuit Private Peering Resource of
                  the peered circuit.
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
                - >-
                  /29 IP address space to carve out Customer addresses for
                  tunnels.
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
                  The resource guid of the authorization used for the express
                  route circuit connection.
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


class AzureRMExpressRouteCircuitPeeringInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.circuit_name = None
        self.peering_name = None

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
        super(AzureRMExpressRouteCircuitPeeringInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.circuit_name is not None and
            self.peering_name is not None):
            self.results['express_route_circuit_peerings'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.circuit_name is not None):
            self.results['express_route_circuit_peerings'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuit_peerings.get(resource_group_name=self.resource_group_name,
                                                                           circuit_name=self.circuit_name,
                                                                           peering_name=self.peering_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuit_peerings.list(resource_group_name=self.resource_group_name,
                                                                            circuit_name=self.circuit_name)
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
    AzureRMExpressRouteCircuitPeeringInfo()


if __name__ == '__main__':
    main()