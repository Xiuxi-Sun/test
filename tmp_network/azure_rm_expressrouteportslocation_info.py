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
module: azure_rm_expressrouteportslocation_info
version_added: '2.9'
short_description: Get ExpressRoutePortsLocation info.
description:
  - Get info of ExpressRoutePortsLocation.
options:
  location_name:
    description:
      - Name of the requested ExpressRoutePort peering location.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ExpressRoutePortsLocationList
      azure_rm_expressrouteportslocation_info: 

    - name: ExpressRoutePortsLocationGet
      azure_rm_expressrouteportslocation_info: 
        location_name: locationName
        

'''

RETURN = '''
express_route_ports_locations:
  description: >-
    A list of dict results where the key is the name of the
    ExpressRoutePortsLocation and the values are the facts for that
    ExpressRoutePortsLocation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of all ExpressRoutePort peering locations.
      returned: always
      type: list
      sample: null
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null
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
    address:
      description:
        - Address of peering location.
      returned: always
      type: str
      sample: null
    contact:
      description:
        - Contact details of peering locations.
      returned: always
      type: str
      sample: null
    available_bandwidths:
      description:
        - The inventory of available ExpressRoutePort bandwidths.
      returned: always
      type: list
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the express route port location resource.
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


class AzureRMExpressRoutePortsLocationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str'
            )
        )

        self.location_name = None

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
        super(AzureRMExpressRoutePortsLocationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.location_name is not None):
            self.results['express_route_ports_locations'] = self.format_item(self.get())
        else:
            self.results['express_route_ports_locations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_ports_locations.get(location_name=self.location_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_ports_locations.list()
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
    AzureRMExpressRoutePortsLocationInfo()


if __name__ == '__main__':
    main()
