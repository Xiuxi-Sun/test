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
module: azure_rm_expressroutecircuit
version_added: '2.9'
short_description: Manage Azure ExpressRouteCircuit instance.
description:
  - 'Create, update and delete instance of Azure ExpressRouteCircuit.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  circuit_name:
    description:
      - The name of the express route circuit.
      - The name of express route circuit.
      - The name of the circuit.
    required: true
    type: str
  sku:
    description:
      - The SKU.
    type: dict
    suboptions:
      name:
        description:
          - The name of the SKU.
        type: str
      tier:
        description:
          - The tier of the SKU.
        type: str
        choices:
          - Standard
          - Premium
          - Basic
          - Local
      family:
        description:
          - The family of the SKU.
        type: str
        choices:
          - UnlimitedData
          - MeteredData
  allow_classic_operations:
    description:
      - Allow classic operations.
    type: bool
  circuit_provisioning_state:
    description:
      - The CircuitProvisioningState state of the resource.
    type: str
  service_provider_provisioning_state:
    description:
      - The ServiceProviderProvisioningState state of the resource.
    type: str
    choices:
      - NotProvisioned
      - Provisioning
      - Provisioned
      - Deprovisioning
  authorizations:
    description:
      - The list of authorizations.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      authorization_key:
        description:
          - The authorization key.
        type: str
      authorization_use_status:
        description:
          - The authorization use status.
        type: str
        choices:
          - Available
          - InUse
  peerings:
    description:
      - The list of peerings.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      peering_type:
        description:
          - The peering type.
        type: str
        choices:
          - AzurePublicPeering
          - AzurePrivatePeering
          - MicrosoftPeering
      state:
        description:
          - The peering state.
        type: str
        choices:
          - Disabled
          - Enabled
      azure_asn:
        description:
          - The Azure ASN.
        type: integer
      peer_asn:
        description:
          - The peer ASN.
        type: integer
      primary_peer_address_prefix:
        description:
          - The primary address prefix.
        type: str
      secondary_peer_address_prefix:
        description:
          - The secondary address prefix.
        type: str
      primary_azure_port:
        description:
          - The primary port.
        type: str
      secondary_azure_port:
        description:
          - The secondary port.
        type: str
      shared_key:
        description:
          - The shared key.
        type: str
      vlan_id:
        description:
          - The VLAN ID.
        type: integer
      microsoft_peering_config:
        description:
          - The Microsoft peering configuration.
        type: dict
        suboptions:
          advertised_public_prefixes:
            description:
              - The reference to AdvertisedPublicPrefixes.
            type: list
          advertised_communities:
            description:
              - The communities of bgp peering. Specified for microsoft peering.
            type: list
          legacy_mode:
            description:
              - The legacy mode of the peering.
            type: integer
          customer_asn:
            description:
              - The CustomerASN of the peering.
            type: integer
          routing_registry_name:
            description:
              - The RoutingRegistryName of the configuration.
            type: str
      stats:
        description:
          - The peering stats of express route circuit.
        type: dict
        suboptions:
          primarybytes_in:
            description:
              - The Primary BytesIn of the peering.
            type: integer
          primarybytes_out:
            description:
              - The primary BytesOut of the peering.
            type: integer
          secondarybytes_in:
            description:
              - The secondary BytesIn of the peering.
            type: integer
          secondarybytes_out:
            description:
              - The secondary BytesOut of the peering.
            type: integer
      gateway_manager_etag:
        description:
          - The GatewayManager Etag.
        type: str
      route_filter:
        description:
          - The reference to the RouteFilter resource.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      ipv6_peering_config:
        description:
          - The IPv6 peering configuration.
        type: dict
        suboptions:
          primary_peer_address_prefix:
            description:
              - The primary address prefix.
            type: str
          secondary_peer_address_prefix:
            description:
              - The secondary address prefix.
            type: str
          microsoft_peering_config:
            description:
              - The Microsoft peering configuration.
            type: dict
            suboptions:
              advertised_public_prefixes:
                description:
                  - The reference to AdvertisedPublicPrefixes.
                type: list
              advertised_communities:
                description:
                  - >-
                    The communities of bgp peering. Specified for microsoft
                    peering.
                type: list
              legacy_mode:
                description:
                  - The legacy mode of the peering.
                type: integer
              customer_asn:
                description:
                  - The CustomerASN of the peering.
                type: integer
              routing_registry_name:
                description:
                  - The RoutingRegistryName of the configuration.
                type: str
          route_filter:
            description:
              - The reference to the RouteFilter resource.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          state:
            description:
              - The state of peering.
            type: str
            choices:
              - Disabled
              - Enabled
      connections:
        description:
          - >-
            The list of circuit connections associated with Azure Private
            Peering for this circuit.
        type: list
        suboptions:
          name:
            description:
              - >-
                The name of the resource that is unique within a resource group.
                This name can be used to access the resource.
            type: str
          express_route_circuit_peering:
            description:
              - >-
                Reference to Express Route Circuit Private Peering Resource of
                the circuit initiating connection.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          peer_express_route_circuit_peering:
            description:
              - >-
                Reference to Express Route Circuit Private Peering Resource of
                the peered circuit.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          address_prefix:
            description:
              - >-
                /29 IP address space to carve out Customer addresses for
                tunnels.
            type: str
          authorization_key:
            description:
              - The authorization key.
            type: str
          ipv6_circuit_connection_config:
            description:
              - >-
                IPv6 Address PrefixProperties of the express route circuit
                connection.
            type: dict
            suboptions:
              address_prefix:
                description:
                  - >-
                    /125 IP address space to carve out customer addresses for
                    global reach.
                type: str
      peered_connections:
        description:
          - >-
            The list of peered circuit connections associated with Azure Private
            Peering for this circuit.
        type: list
        suboptions:
          name:
            description:
              - >-
                The name of the resource that is unique within a resource group.
                This name can be used to access the resource.
            type: str
          express_route_circuit_peering:
            description:
              - >-
                Reference to Express Route Circuit Private Peering Resource of
                the circuit.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          peer_express_route_circuit_peering:
            description:
              - >-
                Reference to Express Route Circuit Private Peering Resource of
                the peered circuit.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          address_prefix:
            description:
              - >-
                /29 IP address space to carve out Customer addresses for
                tunnels.
            type: str
          connection_name:
            description:
              - The name of the express route circuit connection resource.
            type: str
          auth_resource_guid:
            description:
              - >-
                The resource guid of the authorization used for the express
                route circuit connection.
            type: str
  service_key:
    description:
      - The ServiceKey.
    type: str
  service_provider_notes:
    description:
      - The ServiceProviderNotes.
    type: str
  service_provider_properties:
    description:
      - The ServiceProviderProperties.
    type: dict
    suboptions:
      service_provider_name:
        description:
          - The serviceProviderName.
        type: str
      peering_location:
        description:
          - The peering location.
        type: str
      bandwidth_in_mbps:
        description:
          - The BandwidthInMbps.
        type: integer
  express_route_port:
    description:
      - >-
        The reference to the ExpressRoutePort resource when the circuit is
        provisioned on an ExpressRoutePort resource.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  bandwidth_in_gbps:
    description:
      - >-
        The bandwidth of the circuit when the circuit is provisioned on an
        ExpressRoutePort resource.
    type: number
  gateway_manager_etag:
    description:
      - The GatewayManager Etag.
    type: str
  global_reach_enabled:
    description:
      - Flag denoting global reach status.
    type: bool
  state:
    description:
      - Assert the state of the ExpressRouteCircuit.
      - >-
        Use C(present) to create or update an ExpressRouteCircuit and C(absent)
        to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Delete ExpressRouteCircuit
      azure_rm_expressroutecircuit: 
        circuit_name: circuitName
        resource_group_name: rg1
        

    - name: Create ExpressRouteCircuit
      azure_rm_expressroutecircuit: 
        circuit_name: circuitName
        resource_group_name: rg1
        location: Brazil South
        properties:
          allow_classic_operations: false
          authorizations: []
          peerings: []
          service_provider_properties:
            bandwidth_in_mbps: 200
            peering_location: Silicon Valley
            service_provider_name: Equinix
        sku:
          family: MeteredData
          name: Standard_MeteredData
          tier: Standard
        

    - name: Create ExpressRouteCircuit on ExpressRoutePort
      azure_rm_expressroutecircuit: 
        circuit_name: expressRouteCircuit1
        resource_group_name: rg1
        location: westus
        properties:
          bandwidth_in_gbps: 10
          express_route_port:
            id: >-
              /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/expressRoutePorts/portName
        sku:
          family: MeteredData
          name: Premium_MeteredData
          tier: Premium
        

'''

RETURN = '''
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
    - A unique read-only string that changes whenever the resource is updated.
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
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
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
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
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
    - The identifier of the circuit traffic. Outer tag for QinQ encapsulation.
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

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMExpressRouteCircuit(AzureRMModuleBaseExt):
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
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['Standard',
                                 'Premium',
                                 'Basic',
                                 'Local']
                    ),
                    family=dict(
                        type='str',
                        disposition='family',
                        choices=['UnlimitedData',
                                 'MeteredData']
                    )
                )
            ),
            allow_classic_operations=dict(
                type='bool',
                disposition='/allow_classic_operations'
            ),
            circuit_provisioning_state=dict(
                type='str',
                disposition='/circuit_provisioning_state'
            ),
            service_provider_provisioning_state=dict(
                type='str',
                disposition='/service_provider_provisioning_state',
                choices=['NotProvisioned',
                         'Provisioning',
                         'Provisioned',
                         'Deprovisioning']
            ),
            authorizations=dict(
                type='list',
                disposition='/authorizations',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    authorization_key=dict(
                        type='str',
                        disposition='authorization_key'
                    ),
                    authorization_use_status=dict(
                        type='str',
                        disposition='authorization_use_status',
                        choices=['Available',
                                 'InUse']
                    )
                )
            ),
            peerings=dict(
                type='list',
                disposition='/peerings',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    peering_type=dict(
                        type='str',
                        disposition='peering_type',
                        choices=['AzurePublicPeering',
                                 'AzurePrivatePeering',
                                 'MicrosoftPeering']
                    ),
                    state=dict(
                        type='str',
                        disposition='state',
                        choices=['Disabled',
                                 'Enabled']
                    ),
                    azure_asn=dict(
                        type='integer',
                        disposition='azure_asn'
                    ),
                    peer_asn=dict(
                        type='integer',
                        disposition='peer_asn'
                    ),
                    primary_peer_address_prefix=dict(
                        type='str',
                        disposition='primary_peer_address_prefix'
                    ),
                    secondary_peer_address_prefix=dict(
                        type='str',
                        disposition='secondary_peer_address_prefix'
                    ),
                    primary_azure_port=dict(
                        type='str',
                        disposition='primary_azure_port'
                    ),
                    secondary_azure_port=dict(
                        type='str',
                        disposition='secondary_azure_port'
                    ),
                    shared_key=dict(
                        type='str',
                        disposition='shared_key'
                    ),
                    vlan_id=dict(
                        type='integer',
                        disposition='vlan_id'
                    ),
                    microsoft_peering_config=dict(
                        type='dict',
                        disposition='microsoft_peering_config',
                        options=dict(
                            advertised_public_prefixes=dict(
                                type='list',
                                disposition='advertised_public_prefixes',
                                elements='str'
                            ),
                            advertised_communities=dict(
                                type='list',
                                disposition='advertised_communities',
                                elements='str'
                            ),
                            legacy_mode=dict(
                                type='integer',
                                disposition='legacy_mode'
                            ),
                            customer_asn=dict(
                                type='integer',
                                disposition='customer_asn'
                            ),
                            routing_registry_name=dict(
                                type='str',
                                disposition='routing_registry_name'
                            )
                        )
                    ),
                    stats=dict(
                        type='dict',
                        disposition='stats',
                        options=dict(
                            primarybytes_in=dict(
                                type='integer',
                                disposition='primarybytes_in'
                            ),
                            primarybytes_out=dict(
                                type='integer',
                                disposition='primarybytes_out'
                            ),
                            secondarybytes_in=dict(
                                type='integer',
                                disposition='secondarybytes_in'
                            ),
                            secondarybytes_out=dict(
                                type='integer',
                                disposition='secondarybytes_out'
                            )
                        )
                    ),
                    gateway_manager_etag=dict(
                        type='str',
                        disposition='gateway_manager_etag'
                    ),
                    route_filter=dict(
                        type='dict',
                        disposition='route_filter',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    ipv6_peering_config=dict(
                        type='dict',
                        disposition='ipv6_peering_config',
                        options=dict(
                            primary_peer_address_prefix=dict(
                                type='str',
                                disposition='primary_peer_address_prefix'
                            ),
                            secondary_peer_address_prefix=dict(
                                type='str',
                                disposition='secondary_peer_address_prefix'
                            ),
                            microsoft_peering_config=dict(
                                type='dict',
                                disposition='microsoft_peering_config',
                                options=dict(
                                    advertised_public_prefixes=dict(
                                        type='list',
                                        disposition='advertised_public_prefixes',
                                        elements='str'
                                    ),
                                    advertised_communities=dict(
                                        type='list',
                                        disposition='advertised_communities',
                                        elements='str'
                                    ),
                                    legacy_mode=dict(
                                        type='integer',
                                        disposition='legacy_mode'
                                    ),
                                    customer_asn=dict(
                                        type='integer',
                                        disposition='customer_asn'
                                    ),
                                    routing_registry_name=dict(
                                        type='str',
                                        disposition='routing_registry_name'
                                    )
                                )
                            ),
                            route_filter=dict(
                                type='dict',
                                disposition='route_filter',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            state=dict(
                                type='str',
                                disposition='state',
                                choices=['Disabled',
                                         'Enabled']
                            )
                        )
                    ),
                    connections=dict(
                        type='list',
                        disposition='connections',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            express_route_circuit_peering=dict(
                                type='dict',
                                disposition='express_route_circuit_peering',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            peer_express_route_circuit_peering=dict(
                                type='dict',
                                disposition='peer_express_route_circuit_peering',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            address_prefix=dict(
                                type='str',
                                disposition='address_prefix'
                            ),
                            authorization_key=dict(
                                type='str',
                                disposition='authorization_key'
                            ),
                            ipv6_circuit_connection_config=dict(
                                type='dict',
                                disposition='ipv6_circuit_connection_config',
                                options=dict(
                                    address_prefix=dict(
                                        type='str',
                                        disposition='address_prefix'
                                    )
                                )
                            )
                        )
                    ),
                    peered_connections=dict(
                        type='list',
                        updatable=False,
                        disposition='peered_connections',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            express_route_circuit_peering=dict(
                                type='dict',
                                disposition='express_route_circuit_peering',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            peer_express_route_circuit_peering=dict(
                                type='dict',
                                disposition='peer_express_route_circuit_peering',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            address_prefix=dict(
                                type='str',
                                disposition='address_prefix'
                            ),
                            connection_name=dict(
                                type='str',
                                disposition='connection_name'
                            ),
                            auth_resource_guid=dict(
                                type='str',
                                disposition='auth_resource_guid'
                            )
                        )
                    )
                )
            ),
            service_key=dict(
                type='str',
                disposition='/service_key'
            ),
            service_provider_notes=dict(
                type='str',
                disposition='/service_provider_notes'
            ),
            service_provider_properties=dict(
                type='dict',
                disposition='/service_provider_properties',
                options=dict(
                    service_provider_name=dict(
                        type='str',
                        disposition='service_provider_name'
                    ),
                    peering_location=dict(
                        type='str',
                        disposition='peering_location'
                    ),
                    bandwidth_in_mbps=dict(
                        type='integer',
                        disposition='bandwidth_in_mbps'
                    )
                )
            ),
            express_route_port=dict(
                type='dict',
                disposition='/express_route_port',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            bandwidth_in_gbps=dict(
                type='number',
                disposition='/bandwidth_in_gbps'
            ),
            gateway_manager_etag=dict(
                type='str',
                disposition='/gateway_manager_etag'
            ),
            global_reach_enabled=dict(
                type='bool',
                disposition='/global_reach_enabled'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.circuit_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCircuit, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                         supports_check_mode=True,
                                                         supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.express_route_circuits.create_or_update(resource_group_name=self.resource_group_name,
                                                                                circuit_name=self.circuit_name,
                                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCircuit instance.')
            self.fail('Error creating the ExpressRouteCircuit instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.express_route_circuits.delete(resource_group_name=self.resource_group_name,
                                                                      circuit_name=self.circuit_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCircuit instance.')
            self.fail('Error deleting the ExpressRouteCircuit instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.express_route_circuits.get(resource_group_name=self.resource_group_name,
                                                                   circuit_name=self.circuit_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExpressRouteCircuit()


if __name__ == '__main__':
    main()
