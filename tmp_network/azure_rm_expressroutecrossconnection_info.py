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
module: azure_rm_expressroutecrossconnection_info
version_added: '2.9'
short_description: Get ExpressRouteCrossConnection info.
description:
  - Get info of ExpressRouteCrossConnection.
options:
  resource_group_name:
    description:
      - The name of the resource group.
      - The name of the resource group (peering location of the circuit).
    type: str
  cross_connection_name:
    description:
      - >-
        The name of the ExpressRouteCrossConnection (service key of the
        circuit).
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ExpressRouteCrossConnectionList
      azure_rm_expressroutecrossconnection_info: 

    - name: ExpressRouteCrossConnectionListByResourceGroup
      azure_rm_expressroutecrossconnection_info: 
        resource_group_name: CrossConnection-SiliconValley
        

    - name: GetExpressRouteCrossConnection
      azure_rm_expressroutecrossconnection_info: 
        cross_connection_name: <circuitServiceKey>
        resource_group_name: CrossConnection-SiliconValley
        

'''

RETURN = '''
express_route_cross_connections:
  description: >-
    A list of dict results where the key is the name of the
    ExpressRouteCrossConnection and the values are the facts for that
    ExpressRouteCrossConnection.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of ExpressRouteCrossConnection resources.
      returned: always
      type: list
      sample: null
      contains:
        express_route_circuit:
          description:
            - The ExpressRouteCircuit.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Corresponding Express Route Circuit Id.
              returned: always
              type: str
              sample: null
        service_provider_provisioning_state:
          description:
            - >-
              The provisioning state of the circuit in the connectivity provider
              system.
          returned: always
          type: str
          sample: null
        service_provider_notes:
          description:
            - Additional read only notes set by the connectivity provider.
          returned: always
          type: str
          sample: null
        peerings:
          description:
            - The list of peerings.
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
            gateway_manager_etag:
              description:
                - The GatewayManager Etag.
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
                          The communities of bgp peering. Specified for
                          microsoft peering.
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
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    primary_azure_port:
      description:
        - The name of the primary port.
      returned: always
      type: str
      sample: null
    secondary_azure_port:
      description:
        - The name of the secondary port.
      returned: always
      type: str
      sample: null
    s_tag:
      description:
        - The identifier of the circuit traffic.
      returned: always
      type: integer
      sample: null
    peering_location:
      description:
        - The peering location of the ExpressRoute circuit.
      returned: always
      type: str
      sample: null
    bandwidth_in_mbps:
      description:
        - The circuit bandwidth In Mbps.
      returned: always
      type: integer
      sample: null
    express_route_circuit:
      description:
        - The ExpressRouteCircuit.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Corresponding Express Route Circuit Id.
          returned: always
          type: str
          sample: null
    service_provider_provisioning_state:
      description:
        - >-
          The provisioning state of the circuit in the connectivity provider
          system.
      returned: always
      type: str
      sample: null
    service_provider_notes:
      description:
        - Additional read only notes set by the connectivity provider.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the express route cross connection resource.
      returned: always
      type: str
      sample: null
    peerings:
      description:
        - The list of peerings.
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
        gateway_manager_etag:
          description:
            - The GatewayManager Etag.
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


class AzureRMExpressRouteCrossConnectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            cross_connection_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cross_connection_name = None

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
        super(AzureRMExpressRouteCrossConnectionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.cross_connection_name is not None):
            self.results['express_route_cross_connections'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['express_route_cross_connections'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['express_route_cross_connections'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_cross_connections.get(resource_group_name=self.resource_group_name,
                                                                            cross_connection_name=self.cross_connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.express_route_cross_connections.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_cross_connections.list()
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
    AzureRMExpressRouteCrossConnectionInfo()


if __name__ == '__main__':
    main()
