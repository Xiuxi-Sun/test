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
module: azure_rm_natgateway_info
version_added: '2.9'
short_description: Get NatGateway info.
description:
  - Get info of NatGateway.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  nat_gateway_name:
    description:
      - The name of the nat gateway.
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get nat gateway
      azure_rm_natgateway_info: 
        nat_gateway_name: test-natGateway
        resource_group_name: rg1
        

    - name: List all nat gateways
      azure_rm_natgateway_info: 

    - name: List nat gateways in resource group
      azure_rm_natgateway_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
nat_gateways:
  description: >-
    A list of dict results where the key is the name of the NatGateway and the
    values are the facts for that NatGateway.
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
        - The nat gateway SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of Nat Gateway SKU.
          returned: always
          type: str
          sample: null
    zones:
      description:
        - >-
          A list of availability zones denoting the zone in which Nat Gateway
          should be deployed.
      returned: always
      type: list
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    idle_timeout_in_minutes:
      description:
        - The idle timeout of the nat gateway.
      returned: always
      type: integer
      sample: null
    public_ip_addresses:
      description:
        - >-
          An array of public ip addresses associated with the nat gateway
          resource.
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
    public_ip_prefixes:
      description:
        - >-
          An array of public ip prefixes associated with the nat gateway
          resource.
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
    subnets:
      description:
        - An array of references to the subnets using this nat gateway resource.
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
    resource_guid:
      description:
        - The resource GUID property of the NAT gateway resource.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the NAT gateway resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of Nat Gateways that exists in a resource group.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - The nat gateway SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of Nat Gateway SKU.
              returned: always
              type: str
              sample: null
        zones:
          description:
            - >-
              A list of availability zones denoting the zone in which Nat
              Gateway should be deployed.
          returned: always
          type: list
          sample: null
        idle_timeout_in_minutes:
          description:
            - The idle timeout of the nat gateway.
          returned: always
          type: integer
          sample: null
        public_ip_addresses:
          description:
            - >-
              An array of public ip addresses associated with the nat gateway
              resource.
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
        public_ip_prefixes:
          description:
            - >-
              An array of public ip prefixes associated with the nat gateway
              resource.
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
        subnets:
          description:
            - >-
              An array of references to the subnets using this nat gateway
              resource.
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


class AzureRMNatGatewayInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            nat_gateway_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.nat_gateway_name = None
        self.expand = None

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
        super(AzureRMNatGatewayInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.nat_gateway_name is not None):
            self.results['nat_gateways'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['nat_gateways'] = self.format_item(self.list())
        else:
            self.results['nat_gateways'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.nat_gateways.get(resource_group_name=self.resource_group_name,
                                                         nat_gateway_name=self.nat_gateway_name,
                                                         expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.nat_gateways.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.nat_gateways.list_all()
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
    AzureRMNatGatewayInfo()


if __name__ == '__main__':
    main()
