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
module: azure_rm_applicationgatewayprivatelinkresource_info
version_added: '2.9'
short_description: Get ApplicationGatewayPrivateLinkResource info.
description:
  - Get info of ApplicationGatewayPrivateLinkResource.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  application_gateway_name:
    description:
      - The name of the application gateway.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists all private link resources on application gateway
      azure_rm_applicationgatewayprivatelinkresource_info: 
        application_gateway_name: appgw
        resource_group_name: rg1
        

'''

RETURN = '''
application_gateway_private_link_resources:
  description: >-
    A list of dict results where the key is the name of the
    ApplicationGatewayPrivateLinkResource and the values are the facts for that
    ApplicationGatewayPrivateLinkResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of private link resources of an application gateway.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Name of the private link resource that is unique within an
              Application Gateway.
          returned: always
          type: str
          sample: null
        required_members:
          description:
            - Required member names of private link resource.
          returned: always
          type: list
          sample: null
        required_zone_names:
          description:
            - Required DNS zone names of the the private link resource.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - URL to get the next set of results.
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


class AzureRMApplicationGatewayPrivateLinkResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            application_gateway_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.application_gateway_name = None

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
        super(AzureRMApplicationGatewayPrivateLinkResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.application_gateway_name is not None):
            self.results['application_gateway_private_link_resources'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.application_gateway_private_link_resources.list(resource_group_name=self.resource_group_name,
                                                                                        application_gateway_name=self.application_gateway_name)
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
    AzureRMApplicationGatewayPrivateLinkResourceInfo()


if __name__ == '__main__':
    main()
