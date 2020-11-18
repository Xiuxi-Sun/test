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
module: azure_rm_virtualhub
version_added: '2.9'
short_description: Manage Azure VirtualHub instance.
description:
  - 'Create, update and delete instance of Azure VirtualHub.'
options:
  resource_group_name:
    description:
      - The resource group name of the VirtualHub.
    required: true
    type: str
  virtual_hub_name:
    description:
      - The name of the VirtualHub.
    required: true
    type: str
  virtual_wan:
    description:
      - The VirtualWAN to which the VirtualHub belongs.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  vpn_gateway:
    description:
      - The VpnGateway associated with this VirtualHub.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  p2_s_vpn_gateway:
    description:
      - The P2SVpnGateway associated with this VirtualHub.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  express_route_gateway:
    description:
      - The expressRouteGateway associated with this VirtualHub.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  azure_firewall:
    description:
      - The azureFirewall associated with this VirtualHub.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  security_partner_provider:
    description:
      - The securityPartnerProvider associated with this VirtualHub.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  address_prefix:
    description:
      - Address-prefix for this VirtualHub.
    type: str
  route_table:
    description:
      - The routeTable associated with this virtual hub.
    type: dict
    suboptions:
      routes:
        description:
          - List of all routes.
        type: list
        suboptions:
          address_prefixes:
            description:
              - List of all addressPrefixes.
            type: list
          next_hop_ip_address:
            description:
              - NextHop ip address.
            type: str
  security_provider_name:
    description:
      - The Security Provider name.
    type: str
  virtual_hub_route_table_v2_s:
    description:
      - List of all virtual hub route table v2s associated with this VirtualHub.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      routes:
        description:
          - List of all routes.
        type: list
        suboptions:
          destination_type:
            description:
              - The type of destinations.
            type: str
          destinations:
            description:
              - List of all destinations.
            type: list
          next_hop_type:
            description:
              - The type of next hops.
            type: str
          next_hops:
            description:
              - NextHops ip address.
            type: list
      attached_connections:
        description:
          - List of all connections attached to this route table v2.
        type: list
  sku:
    description:
      - The sku of this VirtualHub.
    type: str
  bgp_connections:
    description:
      - List of references to Bgp Connections.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  ip_configurations:
    description:
      - List of references to IpConfigurations.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  virtual_router_asn:
    description:
      - VirtualRouter ASN.
    type: integer
  virtual_router_ips:
    description:
      - VirtualRouter IPs.
    type: list
  enable_virtual_router_route_propogation:
    description:
      - Flag to control route propogation for VirtualRouter hub.
    type: bool
  state:
    description:
      - Assert the state of the VirtualHub.
      - >-
        Use C(present) to create or update an VirtualHub and C(absent) to delete
        it.
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
    - name: VirtualHubPut
      azure_rm_virtualhub: 
        resource_group_name: rg1
        virtual_hub_name: virtualHub2
        

    - name: VirtualHubDelete
      azure_rm_virtualhub: 
        resource_group_name: rg1
        virtual_hub_name: virtualHub1
        

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
virtual_wan:
  description:
    - The VirtualWAN to which the VirtualHub belongs.
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
vpn_gateway:
  description:
    - The VpnGateway associated with this VirtualHub.
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
p2_s_vpn_gateway:
  description:
    - The P2SVpnGateway associated with this VirtualHub.
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
express_route_gateway:
  description:
    - The expressRouteGateway associated with this VirtualHub.
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
azure_firewall:
  description:
    - The azureFirewall associated with this VirtualHub.
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
security_partner_provider:
  description:
    - The securityPartnerProvider associated with this VirtualHub.
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
    - Address-prefix for this VirtualHub.
  returned: always
  type: str
  sample: null
route_table:
  description:
    - The routeTable associated with this virtual hub.
  returned: always
  type: dict
  sample: null
  contains:
    routes:
      description:
        - List of all routes.
      returned: always
      type: list
      sample: null
      contains:
        address_prefixes:
          description:
            - List of all addressPrefixes.
          returned: always
          type: list
          sample: null
        next_hop_ip_address:
          description:
            - NextHop ip address.
          returned: always
          type: str
          sample: null
provisioning_state:
  description:
    - The provisioning state of the virtual hub resource.
  returned: always
  type: str
  sample: null
security_provider_name:
  description:
    - The Security Provider name.
  returned: always
  type: str
  sample: null
virtual_hub_route_table_v2_s:
  description:
    - List of all virtual hub route table v2s associated with this VirtualHub.
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
    routes:
      description:
        - List of all routes.
      returned: always
      type: list
      sample: null
      contains:
        destination_type:
          description:
            - The type of destinations.
          returned: always
          type: str
          sample: null
        destinations:
          description:
            - List of all destinations.
          returned: always
          type: list
          sample: null
        next_hop_type:
          description:
            - The type of next hops.
          returned: always
          type: str
          sample: null
        next_hops:
          description:
            - NextHops ip address.
          returned: always
          type: list
          sample: null
    attached_connections:
      description:
        - List of all connections attached to this route table v2.
      returned: always
      type: list
      sample: null
sku:
  description:
    - The sku of this VirtualHub.
  returned: always
  type: str
  sample: null
routing_state:
  description:
    - The routing state.
  returned: always
  type: str
  sample: null
bgp_connections:
  description:
    - List of references to Bgp Connections.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
ip_configurations:
  description:
    - List of references to IpConfigurations.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
virtual_router_asn:
  description:
    - VirtualRouter ASN.
  returned: always
  type: integer
  sample: null
virtual_router_ips:
  description:
    - VirtualRouter IPs.
  returned: always
  type: list
  sample: null
enable_virtual_router_route_propogation:
  description:
    - Flag to control route propogation for VirtualRouter hub.
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


class AzureRMVirtualHub(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            virtual_hub_name=dict(
                type='str',
                required=True
            ),
            virtual_wan=dict(
                type='dict',
                disposition='/virtual_wan',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            vpn_gateway=dict(
                type='dict',
                disposition='/vpn_gateway',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            p2_s_vpn_gateway=dict(
                type='dict',
                disposition='/p2_s_vpn_gateway',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            express_route_gateway=dict(
                type='dict',
                disposition='/express_route_gateway',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            azure_firewall=dict(
                type='dict',
                disposition='/azure_firewall',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            security_partner_provider=dict(
                type='dict',
                disposition='/security_partner_provider',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            address_prefix=dict(
                type='str',
                disposition='/address_prefix'
            ),
            route_table=dict(
                type='dict',
                disposition='/route_table',
                options=dict(
                    routes=dict(
                        type='list',
                        disposition='routes',
                        elements='dict',
                        options=dict(
                            address_prefixes=dict(
                                type='list',
                                disposition='address_prefixes',
                                elements='str'
                            ),
                            next_hop_ip_address=dict(
                                type='str',
                                disposition='next_hop_ip_address'
                            )
                        )
                    )
                )
            ),
            security_provider_name=dict(
                type='str',
                disposition='/security_provider_name'
            ),
            virtual_hub_route_table_v2_s=dict(
                type='list',
                disposition='/virtual_hub_route_table_v2_s',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    routes=dict(
                        type='list',
                        disposition='routes',
                        elements='dict',
                        options=dict(
                            destination_type=dict(
                                type='str',
                                disposition='destination_type'
                            ),
                            destinations=dict(
                                type='list',
                                disposition='destinations',
                                elements='str'
                            ),
                            next_hop_type=dict(
                                type='str',
                                disposition='next_hop_type'
                            ),
                            next_hops=dict(
                                type='list',
                                disposition='next_hops',
                                elements='str'
                            )
                        )
                    ),
                    attached_connections=dict(
                        type='list',
                        disposition='attached_connections',
                        elements='str'
                    )
                )
            ),
            sku=dict(
                type='str',
                disposition='/sku'
            ),
            bgp_connections=dict(
                type='list',
                updatable=False,
                disposition='/bgp_connections',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            ip_configurations=dict(
                type='list',
                updatable=False,
                disposition='/ip_configurations',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            virtual_router_asn=dict(
                type='integer',
                disposition='/virtual_router_asn'
            ),
            virtual_router_ips=dict(
                type='list',
                disposition='/virtual_router_ips',
                elements='str'
            ),
            enable_virtual_router_route_propogation=dict(
                type='bool',
                disposition='/enable_virtual_router_route_propogation'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.virtual_hub_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualHub, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.virtual_hubs.create_or_update(resource_group_name=self.resource_group_name,
                                                                      virtual_hub_name=self.virtual_hub_name,
                                                                      virtual_hub_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualHub instance.')
            self.fail('Error creating the VirtualHub instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_hubs.delete(resource_group_name=self.resource_group_name,
                                                            virtual_hub_name=self.virtual_hub_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualHub instance.')
            self.fail('Error deleting the VirtualHub instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_hubs.get(resource_group_name=self.resource_group_name,
                                                         virtual_hub_name=self.virtual_hub_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualHub()


if __name__ == '__main__':
    main()
