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
module: azure_rm_expressroutecrossconnection
version_added: '2.9'
short_description: Manage Azure ExpressRouteCrossConnection instance.
description:
  - 'Create, update and delete instance of Azure ExpressRouteCrossConnection.'
options:
  resource_group_name:
    description:
      - The name of the resource group (peering location of the circuit).
      - The name of the resource group.
    required: true
    type: str
  cross_connection_name:
    description:
      - >-
        The name of the ExpressRouteCrossConnection (service key of the
        circuit).
      - The name of the ExpressRouteCrossConnection.
    required: true
    type: str
  express_route_circuit:
    description:
      - The ExpressRouteCircuit.
    type: dict
    suboptions:
      id:
        description:
          - Corresponding Express Route Circuit Id.
        type: str
  service_provider_provisioning_state:
    description:
      - >-
        The provisioning state of the circuit in the connectivity provider
        system.
    type: str
    choices:
      - NotProvisioned
      - Provisioning
      - Provisioned
      - Deprovisioning
  service_provider_notes:
    description:
      - Additional read only notes set by the connectivity provider.
    type: str
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
      gateway_manager_etag:
        description:
          - The GatewayManager Etag.
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
  state:
    description:
      - Assert the state of the ExpressRouteCrossConnection.
      - >-
        Use C(present) to create or update an ExpressRouteCrossConnection and
        C(absent) to delete it.
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
    - name: UpdateExpressRouteCrossConnection
      azure_rm_expressroutecrossconnection: 
        cross_connection_name: <circuitServiceKey>
        resource_group_name: CrossConnection-SiliconValley
        properties:
          service_provider_provisioning_state: NotProvisioned
        

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
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
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
    - The provisioning state of the circuit in the connectivity provider system.
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


class AzureRMExpressRouteCrossConnection(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cross_connection_name=dict(
                type='str',
                required=True
            ),
            express_route_circuit=dict(
                type='dict',
                disposition='/express_route_circuit',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            service_provider_provisioning_state=dict(
                type='str',
                disposition='/service_provider_provisioning_state',
                choices=['NotProvisioned',
                         'Provisioning',
                         'Provisioned',
                         'Deprovisioning']
            ),
            service_provider_notes=dict(
                type='str',
                disposition='/service_provider_notes'
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
                    gateway_manager_etag=dict(
                        type='str',
                        disposition='gateway_manager_etag'
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
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cross_connection_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCrossConnection, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.express_route_cross_connections.create_or_update(resource_group_name=self.resource_group_name,
                                                                                         cross_connection_name=self.cross_connection_name,
                                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCrossConnection instance.')
            self.fail('Error creating the ExpressRouteCrossConnection instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.express_route_cross_connections.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCrossConnection instance.')
            self.fail('Error deleting the ExpressRouteCrossConnection instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.express_route_cross_connections.get(resource_group_name=self.resource_group_name,
                                                                            cross_connection_name=self.cross_connection_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExpressRouteCrossConnection()


if __name__ == '__main__':
    main()
