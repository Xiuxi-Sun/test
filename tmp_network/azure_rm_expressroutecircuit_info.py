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
module: azure_rm_expressroutecircuit_info
version_added: '2.9'
short_description: Get ExpressRouteCircuit info.
description:
  - Get info of ExpressRouteCircuit.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  circuit_name:
    description:
      - The name of express route circuit.
      - The name of the express route circuit.
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
    - name: Get ExpressRouteCircuit
      azure_rm_expressroutecircuit_info: 
        circuit_name: circuitName
        resource_group_name: rg1
        

    - name: Get ExpressRoute Circuit Traffic Stats
      azure_rm_expressroutecircuit_info: 
        circuit_name: circuitName
        resource_group_name: rg1
        

    - name: Get ExpressRoute Circuit Peering Traffic Stats
      azure_rm_expressroutecircuit_info: 
        circuit_name: circuitName
        peering_name: peeringName
        resource_group_name: rg1
        

    - name: List ExpressRouteCircuits in a resource group
      azure_rm_expressroutecircuit_info: 
        resource_group_name: rg1
        

    - name: List ExpressRouteCircuits in a subscription
      azure_rm_expressroutecircuit_info: 

'''

RETURN = '''
express_route_circuits:
  description: >-
    A list of dict results where the key is the name of the ExpressRouteCircuit
    and the values are the facts for that ExpressRouteCircuit.
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
    sku:
      description:
        - The SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The name of the SKU.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The tier of the SKU.
          returned: always
          type: str
          sample: null
        family:
          description:
            - The family of the SKU.
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
    allow_classic_operations:
      description:
        - Allow classic operations.
      returned: always
      type: bool
      sample: null
    circuit_provisioning_state:
      description:
        - The CircuitProvisioningState state of the resource.
      returned: always
      type: str
      sample: null
    service_provider_provisioning_state:
      description:
        - The ServiceProviderProvisioningState state of the resource.
      returned: always
      type: str
      sample: null
    authorizations:
      description:
        - The list of authorizations.
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
        authorization_key:
          description:
            - The authorization key.
          returned: always
          type: str
          sample: null
        authorization_use_status:
          description:
            - The authorization use status.
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
    service_key:
      description:
        - The ServiceKey.
      returned: always
      type: str
      sample: null
    service_provider_notes:
      description:
        - The ServiceProviderNotes.
      returned: always
      type: str
      sample: null
    service_provider_properties:
      description:
        - The ServiceProviderProperties.
      returned: always
      type: dict
      sample: null
      contains:
        service_provider_name:
          description:
            - The serviceProviderName.
          returned: always
          type: str
          sample: null
        peering_location:
          description:
            - The peering location.
          returned: always
          type: str
          sample: null
        bandwidth_in_mbps:
          description:
            - The BandwidthInMbps.
          returned: always
          type: integer
          sample: null
    express_route_port:
      description:
        - >-
          The reference to the ExpressRoutePort resource when the circuit is
          provisioned on an ExpressRoutePort resource.
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
    bandwidth_in_gbps:
      description:
        - >-
          The bandwidth of the circuit when the circuit is provisioned on an
          ExpressRoutePort resource.
      returned: always
      type: number
      sample: null
    stag:
      description:
        - >-
          The identifier of the circuit traffic. Outer tag for QinQ
          encapsulation.
      returned: always
      type: integer
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the express route circuit resource.
      returned: always
      type: str
      sample: null
    gateway_manager_etag:
      description:
        - The GatewayManager Etag.
      returned: always
      type: str
      sample: null
    global_reach_enabled:
      description:
        - Flag denoting global reach status.
      returned: always
      type: bool
      sample: null
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
    value:
      description:
        - A list of ExpressRouteCircuits in a resource group.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - The SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The tier of the SKU.
              returned: always
              type: str
              sample: null
            family:
              description:
                - The family of the SKU.
              returned: always
              type: str
              sample: null
        allow_classic_operations:
          description:
            - Allow classic operations.
          returned: always
          type: bool
          sample: null
        circuit_provisioning_state:
          description:
            - The CircuitProvisioningState state of the resource.
          returned: always
          type: str
          sample: null
        service_provider_provisioning_state:
          description:
            - The ServiceProviderProvisioningState state of the resource.
          returned: always
          type: str
          sample: null
        authorizations:
          description:
            - The list of authorizations.
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
            authorization_key:
              description:
                - The authorization key.
              returned: always
              type: str
              sample: null
            authorization_use_status:
              description:
                - The authorization use status.
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
                      Reference to Express Route Circuit Private Peering
                      Resource of the circuit initiating connection.
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
                      Reference to Express Route Circuit Private Peering
                      Resource of the peered circuit.
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
                          /125 IP address space to carve out customer addresses
                          for global reach.
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
                      Reference to Express Route Circuit Private Peering
                      Resource of the circuit.
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
                      Reference to Express Route Circuit Private Peering
                      Resource of the peered circuit.
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
                      The resource guid of the authorization used for the
                      express route circuit connection.
                  returned: always
                  type: str
                  sample: null
        service_key:
          description:
            - The ServiceKey.
          returned: always
          type: str
          sample: null
        service_provider_notes:
          description:
            - The ServiceProviderNotes.
          returned: always
          type: str
          sample: null
        service_provider_properties:
          description:
            - The ServiceProviderProperties.
          returned: always
          type: dict
          sample: null
          contains:
            service_provider_name:
              description:
                - The serviceProviderName.
              returned: always
              type: str
              sample: null
            peering_location:
              description:
                - The peering location.
              returned: always
              type: str
              sample: null
            bandwidth_in_mbps:
              description:
                - The BandwidthInMbps.
              returned: always
              type: integer
              sample: null
        express_route_port:
          description:
            - >-
              The reference to the ExpressRoutePort resource when the circuit is
              provisioned on an ExpressRoutePort resource.
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
        bandwidth_in_gbps:
          description:
            - >-
              The bandwidth of the circuit when the circuit is provisioned on an
              ExpressRoutePort resource.
          returned: always
          type: number
          sample: null
        gateway_manager_etag:
          description:
            - The GatewayManager Etag.
          returned: always
          type: str
          sample: null
        global_reach_enabled:
          description:
            - Flag denoting global reach status.
          returned: always
          type: bool
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


class AzureRMExpressRouteCircuitInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            circuit_name=dict(
                type='str'
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
        super(AzureRMExpressRouteCircuitInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.circuit_name is not None and
            self.peering_name is not None):
            self.results['express_route_circuits'] = self.format_item(self.get_peering_stats())
        elif (self.resource_group_name is not None and
              self.circuit_name is not None):
            self.results['express_route_circuits'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.circuit_name is not None):
            self.results['express_route_circuits'] = self.format_item(self.get_stats())
        elif (self.resource_group_name is not None):
            self.results['express_route_circuits'] = self.format_item(self.list())
        else:
            self.results['express_route_circuits'] = self.format_item(self.list_all())
        return self.results

    def get_peering_stats(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuits.get_peering_stats(resource_group_name=self.resource_group_name,
                                                                                 circuit_name=self.circuit_name,
                                                                                 peering_name=self.peering_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuits.get(resource_group_name=self.resource_group_name,
                                                                   circuit_name=self.circuit_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_stats(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuits.get_stats(resource_group_name=self.resource_group_name,
                                                                         circuit_name=self.circuit_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuits.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.express_route_circuits.list_all()
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
    AzureRMExpressRouteCircuitInfo()


if __name__ == '__main__':
    main()
