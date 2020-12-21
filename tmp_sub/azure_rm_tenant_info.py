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
module: azure_rm_tenant_info
version_added: '2.9'
short_description: Get Tenant info.
description:
  - Get info of Tenant.
options: {}
extends_documentation_fragment:
  - azure.azcollection.azure
  - azure.azcollection.azure_tags
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: listTenants
      azure_rm_tenant_info: 

'''

RETURN = '''
    tenants:
      description: >-
        A list of dict results where the key is the name of the Tenant and the
        values are the facts for that Tenant.
      returned: always
      type: complex
      contains:
        value:
          description:
            - An array of tenants.
          returned: always
          type: list
          sample: null
        next_link:
          description:
            - The URL to use for getting the next set of results.
          returned: always
          type: str
          sample: null
    
'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.subscription import SubscriptionClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTenantInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTenantInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SubscriptionClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-06-01')

        else:
            self.results['tenants'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.tenants.list()
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
    AzureRMTenantInfo()


if __name__ == '__main__':
    main()
