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
module: azure_rm_webcategory_info
version_added: '2.9'
short_description: Get WebCategory info.
description:
  - Get info of WebCategory.
options:
  name:
    description:
      - The name of the azureWebCategory.
    type: str
  expand:
    description:
      - Expands resourceIds back referenced by the azureWebCategory resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Azure Web Category by name
      azure_rm_webcategory_info: 
        name: Arts
        

    - name: List all Azure Web Categories for a given subscription
      azure_rm_webcategory_info: 

'''

RETURN = '''
web_categories:
  description: >-
    A list of dict results where the key is the name of the WebCategory and the
    values are the facts for that WebCategory.
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
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    group:
      description:
        - The name of the group that the category belongs to.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of Azure Web Categories for a given Subscription.
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


class AzureRMWebCategoryInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.name = None
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
        super(AzureRMWebCategoryInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.name is not None):
            self.results['web_categories'] = self.format_item(self.get())
        else:
            self.results['web_categories'] = self.format_item(self.list_by_subscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.web_categories.get(name=self.name,
                                                           expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_subscription(self):
        response = None

        try:
            response = self.mgmt_client.web_categories.list_by_subscription()
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
    AzureRMWebCategoryInfo()


if __name__ == '__main__':
    main()
