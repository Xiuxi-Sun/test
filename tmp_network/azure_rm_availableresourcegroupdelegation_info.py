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
module: azure_rm_availableresourcegroupdelegation_info
version_added: '2.9'
short_description: Get AvailableResourceGroupDelegation info.
description:
  - Get info of AvailableResourceGroupDelegation.
options:
  location:
    description:
      - The location of the domain name.
    required: true
    type: str
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get available delegations in the resource group
      azure_rm_availableresourcegroupdelegation_info: 
        location: westcentralus
        resource_group_name: rg1
        

'''

RETURN = '''
available_resource_group_delegations:
  description: >-
    A list of dict results where the key is the name of the
    AvailableResourceGroupDelegation and the values are the facts for that
    AvailableResourceGroupDelegation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - An array of available delegations.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the AvailableDelegation resource.
          returned: always
          type: str
          sample: null
        id:
          description:
            - A unique identifier of the AvailableDelegation resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
        service_name:
          description:
            - The name of the service and resource.
          returned: always
          type: str
          sample: null
        actions:
          description:
            - The actions permitted to the service upon delegation.
          returned: always
          type: list
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


class AzureRMAvailableResourceGroupDelegationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            )
        )

        self.location = None
        self.resource_group_name = None

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
        super(AzureRMAvailableResourceGroupDelegationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.location is not None and
            self.resource_group_name is not None):
            self.results['available_resource_group_delegations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.available_resource_group_delegations.list(location=self.location,
                                                                                  resource_group_name=self.resource_group_name)
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
    AzureRMAvailableResourceGroupDelegationInfo()


if __name__ == '__main__':
    main()
