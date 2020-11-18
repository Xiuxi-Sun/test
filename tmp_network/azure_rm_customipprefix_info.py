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
module: azure_rm_customipprefix_info
version_added: '2.9'
short_description: Get CustomIPPrefix info.
description:
  - Get info of CustomIPPrefix.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  custom_ip_prefix_name:
    description:
      - The name of the custom IP prefix.
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
    - name: Get custom IP prefix
      azure_rm_customipprefix_info: 
        custom_ip_prefix_name: test-customipprefix
        resource_group_name: rg1
        

    - name: List all custom IP prefixes
      azure_rm_customipprefix_info: 

    - name: List resource group Custom IP prefixes
      azure_rm_customipprefix_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
custom_ipprefixes:
  description: >-
    A list of dict results where the key is the name of the CustomIPPrefix and
    the values are the facts for that CustomIPPrefix.
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
    zones:
      description:
        - >-
          A list of availability zones denoting the IP allocated for the
          resource needs to come from.
      returned: always
      type: list
      sample: null
    cidr:
      description:
        - >-
          The prefix range in CIDR notation. Should include the start address
          and the prefix length.
      returned: always
      type: str
      sample: null
    commissioned_state:
      description:
        - The commissioned state of the Custom IP Prefix.
      returned: always
      type: str
      sample: null
    public_ip_prefixes:
      description:
        - The list of all referenced PublicIpPrefixes.
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
        - The resource GUID property of the custom IP prefix resource.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the custom IP prefix resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of Custom IP prefixes that exists in a resource group.
      returned: always
      type: list
      sample: null
      contains:
        zones:
          description:
            - >-
              A list of availability zones denoting the IP allocated for the
              resource needs to come from.
          returned: always
          type: list
          sample: null
        cidr:
          description:
            - >-
              The prefix range in CIDR notation. Should include the start
              address and the prefix length.
          returned: always
          type: str
          sample: null
        commissioned_state:
          description:
            - The commissioned state of the Custom IP Prefix.
          returned: always
          type: str
          sample: null
        public_ip_prefixes:
          description:
            - The list of all referenced PublicIpPrefixes.
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


class AzureRMCustomIPPrefixInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            custom_ip_prefix_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.custom_ip_prefix_name = None
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
        super(AzureRMCustomIPPrefixInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.custom_ip_prefix_name is not None):
            self.results['custom_ipprefixes'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['custom_ipprefixes'] = self.format_item(self.list())
        else:
            self.results['custom_ipprefixes'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.custom_ipprefixes.get(resource_group_name=self.resource_group_name,
                                                              custom_ip_prefix_name=self.custom_ip_prefix_name,
                                                              expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.custom_ipprefixes.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.custom_ipprefixes.list_all()
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
    AzureRMCustomIPPrefixInfo()


if __name__ == '__main__':
    main()
