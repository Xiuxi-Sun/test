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
module: azure_rm_virtualhub_info
version_added: '2.9'
short_description: Get VirtualHub info.
description:
  - Get info of VirtualHub.
options:
  resource_group_name:
    description:
      - The resource group name of the VirtualHub.
    type: str
  virtual_hub_name:
    description:
      - The name of the VirtualHub.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: VirtualHubGet
      azure_rm_virtualhub_info: 
        resource_group_name: rg1
        virtual_hub_name: virtualHub1
        

    - name: VirtualHubListByResourceGroup
      azure_rm_virtualhub_info: 
        resource_group_name: rg1
        

    - name: VirtualHubList
      azure_rm_virtualhub_info: 

'''

RETURN = '''
virtual_hubs:
  description: >-
    A list of dict results where the key is the name of the VirtualHub and the
    values are the facts for that VirtualHub.
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
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
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
        - >-
          List of all virtual hub route table v2s associated with this
          VirtualHub.
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
    value:
      description:
        - List of VirtualHubs.
      returned: always
      type: list
      sample: null
      contains:
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
        security_provider_name:
          description:
            - The Security Provider name.
          returned: always
          type: str
          sample: null
        virtual_hub_route_table_v2_s:
          description:
            - >-
              List of all virtual hub route table v2s associated with this
              VirtualHub.
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
    next_link:
      description:
        - URL to get the next set of operation list results if there are any.
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


class AzureRMVirtualHubInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            virtual_hub_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.virtual_hub_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualHubInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.virtual_hub_name is not None):
            self.results['virtual_hubs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['virtual_hubs'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['virtual_hubs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_hubs.get(resource_group_name=self.resource_group_name,
                                                         virtual_hub_name=self.virtual_hub_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.virtual_hubs.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_hubs.list()
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
    AzureRMVirtualHubInfo()


if __name__ == '__main__':
    main()
