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
module: azure_rm_expressroutelink_info
version_added: '2.9'
short_description: Get ExpressRouteLink info.
description:
  - Get info of ExpressRouteLink.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  express_route_port_name:
    description:
      - The name of the ExpressRoutePort resource.
    required: true
    type: str
  link_name:
    description:
      - The name of the ExpressRouteLink resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ExpressRouteLinkGet
      azure_rm_expressroutelink_info: 
        express_route_port_name: portName
        link_name: linkName
        resource_group_name: rg1
        

'''

RETURN = '''
express_route_links:
  description: >-
    A list of dict results where the key is the name of the ExpressRouteLink and
    the values are the facts for that ExpressRouteLink.
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
        - >-
          Name of child port resource that is unique among child port resources
          of the parent.
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
    router_name:
      description:
        - Name of Azure router associated with physical port.
      returned: always
      type: str
      sample: null
    interface_name:
      description:
        - Name of Azure router interface.
      returned: always
      type: str
      sample: null
    patch_panel_id:
      description:
        - Mapping between physical port to patch panel port.
      returned: always
      type: str
      sample: null
    rack_id:
      description:
        - Mapping of physical patch panel to rack.
      returned: always
      type: str
      sample: null
    connector_type:
      description:
        - Physical fiber port type.
      returned: always
      type: str
      sample: null
    admin_state:
      description:
        - Administrative state of the physical port.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the express route link resource.
      returned: always
      type: str
      sample: null
    mac_sec_config:
      description:
        - MacSec configuration.
      returned: always
      type: dict
      sample: null
      contains:
        ckn_secret_identifier:
          description:
            - Keyvault Secret Identifier URL containing Mac security CKN key.
          returned: always
          type: str
          sample: null
        cak_secret_identifier:
          description:
            - Keyvault Secret Identifier URL containing Mac security CAK key.
          returned: always
          type: str
          sample: null
        cipher:
          description:
            - Mac security cipher.
          returned: always
          type: str
          sample: null
        sci_state:
          description:
            - Sci mode enabled/disabled.
          returned: always
          type: str
          sample: null
    value:
      description:
        - The list of ExpressRouteLink sub-resources.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Name of child port resource that is unique among child port
              resources of the parent.
          returned: always
          type: str
          sample: null
        admin_state:
          description:
            - Administrative state of the physical port.
          returned: always
          type: str
          sample: null
        mac_sec_config:
          description:
            - MacSec configuration.
          returned: always
          type: dict
          sample: null
          contains:
            ckn_secret_identifier:
              description:
                - >-
                  Keyvault Secret Identifier URL containing Mac security CKN
                  key.
              returned: always
              type: str
              sample: null
            cak_secret_identifier:
              description:
                - >-
                  Keyvault Secret Identifier URL containing Mac security CAK
                  key.
              returned: always
              type: str
              sample: null
            cipher:
              description:
                - Mac security cipher.
              returned: always
              type: str
              sample: null
            sci_state:
              description:
                - Sci mode enabled/disabled.
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


class AzureRMExpressRouteLinkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            express_route_port_name=dict(
                type='str',
                required=True
            ),
            link_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.express_route_port_name = None
        self.link_name = None

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
        super(AzureRMExpressRouteLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.express_route_port_name is not None and
            self.link_name is not None):
            self.results['express_route_links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.express_route_port_name is not None):
            self.results['express_route_links'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_links.get(resource_group_name=self.resource_group_name,
                                                                express_route_port_name=self.express_route_port_name,
                                                                link_name=self.link_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_links.list(resource_group_name=self.resource_group_name,
                                                                 express_route_port_name=self.express_route_port_name)
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
    AzureRMExpressRouteLinkInfo()


if __name__ == '__main__':
    main()
