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
module: azure_rm_expressrouteserviceprovider_info
version_added: '2.9'
short_description: Get ExpressRouteServiceProvider info.
description:
  - Get info of ExpressRouteServiceProvider.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List ExpressRoute providers
      azure_rm_expressrouteserviceprovider_info: 

'''

RETURN = '''
express_route_service_providers:
  description: >-
    A list of dict results where the key is the name of the
    ExpressRouteServiceProvider and the values are the facts for that
    ExpressRouteServiceProvider.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of ExpressRouteResourceProvider resources.
      returned: always
      type: list
      sample: null
      contains:
        peering_locations:
          description:
            - A list of peering locations.
          returned: always
          type: list
          sample: null
        bandwidths_offered:
          description:
            - A list of bandwidths offered.
          returned: always
          type: list
          sample: null
          contains:
            offer_name:
              description:
                - The OfferName.
              returned: always
              type: str
              sample: null
            value_in_mbps:
              description:
                - The ValueInMbps.
              returned: always
              type: integer
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


class AzureRMExpressRouteServiceProviderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


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
        super(AzureRMExpressRouteServiceProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        else:
            self.results['express_route_service_providers'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_service_providers.list()
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
    AzureRMExpressRouteServiceProviderInfo()


if __name__ == '__main__':
    main()
