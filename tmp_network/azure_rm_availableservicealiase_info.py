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
module: azure_rm_availableservicealiase_info
version_added: '2.9'
short_description: Get AvailableServiceAliase info.
description:
  - Get info of AvailableServiceAliase.
options:
  location:
    description:
      - The location.
    required: true
    type: str
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get available service aliases
      azure_rm_availableservicealiase_info: 
        location: westcentralus
        

    - name: Get available service aliases in the resource group
      azure_rm_availableservicealiase_info: 
        location: westcentralus
        resource_group_name: rg1
        

'''

RETURN = '''
available_service_aliases:
  description: >-
    A list of dict results where the key is the name of the
    AvailableServiceAliase and the values are the facts for that
    AvailableServiceAliase.
  returned: always
  type: complex
  contains:
    value:
      description:
        - An array of available service aliases.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the service alias.
          returned: always
          type: str
          sample: null
        id:
          description:
            - The ID of the service alias.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the resource.
          returned: always
          type: str
          sample: null
        resource_name:
          description:
            - The resource name of the service alias.
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


class AzureRMAvailableServiceAliaseInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str'
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
        super(AzureRMAvailableServiceAliaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.location is not None):
            self.results['available_service_aliases'] = self.format_item(self.list_by_resource_group())
        elif (self.location is not None):
            self.results['available_service_aliases'] = self.format_item(self.list())
        return self.results

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.available_service_aliases.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                                         location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.available_service_aliases.list(location=self.location)
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
    AzureRMAvailableServiceAliaseInfo()


if __name__ == '__main__':
    main()
