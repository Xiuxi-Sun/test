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
module: azure_rm_ipallocation_info
version_added: '2.9'
short_description: Get IpAllocation info.
description:
  - Get info of IpAllocation.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  ip_allocation_name:
    description:
      - The name of the IpAllocation.
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
    - name: Get IpAllocation
      azure_rm_ipallocation_info: 
        ip_allocation_name: test-ipallocation
        resource_group_name: rg1
        

    - name: List all IpAllocations
      azure_rm_ipallocation_info: 

    - name: List IpAllocations in resource group
      azure_rm_ipallocation_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
ip_allocations:
  description: >-
    A list of dict results where the key is the name of the IpAllocation and the
    values are the facts for that IpAllocation.
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
    subnet:
      description:
        - The Subnet that using the prefix of this IpAllocation resource.
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
    virtual_network:
      description:
        - >-
          The VirtualNetwork that using the prefix of this IpAllocation
          resource.
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
    type_properties_type:
      description:
        - The type for the IpAllocation.
      returned: always
      type: str
      sample: null
    prefix:
      description:
        - The address prefix for the IpAllocation.
      returned: always
      type: str
      sample: null
    prefix_length:
      description:
        - The address prefix length for the IpAllocation.
      returned: always
      type: integer
      sample: null
    prefix_type:
      description:
        - The address prefix Type for the IpAllocation.
      returned: always
      type: str
      sample: null
    ipam_allocation_id:
      description:
        - The IPAM allocation ID.
      returned: always
      type: str
      sample: null
    allocation_tags:
      description:
        - IpAllocation tags.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - A list of IpAllocation resources.
      returned: always
      type: list
      sample: null
      contains:
        subnet:
          description:
            - The Subnet that using the prefix of this IpAllocation resource.
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
        virtual_network:
          description:
            - >-
              The VirtualNetwork that using the prefix of this IpAllocation
              resource.
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
        type_properties_type:
          description:
            - The type for the IpAllocation.
          returned: always
          type: str
          sample: null
        prefix:
          description:
            - The address prefix for the IpAllocation.
          returned: always
          type: str
          sample: null
        prefix_length:
          description:
            - The address prefix length for the IpAllocation.
          returned: always
          type: integer
          sample: null
        prefix_type:
          description:
            - The address prefix Type for the IpAllocation.
          returned: always
          type: str
          sample: null
        ipam_allocation_id:
          description:
            - The IPAM allocation ID.
          returned: always
          type: str
          sample: null
        allocation_tags:
          description:
            - IpAllocation tags.
          returned: always
          type: dictionary
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


class AzureRMIpAllocationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            ip_allocation_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.ip_allocation_name = None
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
        super(AzureRMIpAllocationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.ip_allocation_name is not None):
            self.results['ip_allocations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['ip_allocations'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['ip_allocations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.ip_allocations.get(resource_group_name=self.resource_group_name,
                                                           ip_allocation_name=self.ip_allocation_name,
                                                           expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.ip_allocations.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.ip_allocations.list()
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
    AzureRMIpAllocationInfo()


if __name__ == '__main__':
    main()
