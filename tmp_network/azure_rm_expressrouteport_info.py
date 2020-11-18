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
module: azure_rm_expressrouteport_info
version_added: '2.9'
short_description: Get ExpressRoutePort info.
description:
  - Get info of ExpressRoutePort.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  express_route_port_name:
    description:
      - The name of ExpressRoutePort.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ExpressRoutePortGet
      azure_rm_expressrouteport_info: 
        express_route_port_name: portName
        resource_group_name: rg1
        

    - name: ExpressRoutePortListByResourceGroup
      azure_rm_expressrouteport_info: 
        resource_group_name: rg1
        

    - name: ExpressRoutePortList
      azure_rm_expressrouteport_info: 

'''

RETURN = '''
express_route_ports:
  description: >-
    A list of dict results where the key is the name of the ExpressRoutePort and
    the values are the facts for that ExpressRoutePort.
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
    identity:
      description:
        - 'The identity of ExpressRoutePort, if configured.'
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - >-
              The type of identity used for the resource. The type
              'SystemAssigned, UserAssigned' includes both an implicitly created
              identity and a set of user assigned identities. The type 'None'
              will remove any identities from the virtual machine.
          returned: always
          type: sealed-choice
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user identities associated with resource. The user
              identity dictionary key references will be ARM resource ids in the
              form:
              '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
          returned: always
          type: dictionary
          sample: null
    peering_location:
      description:
        - >-
          The name of the peering location that the ExpressRoutePort is mapped
          to physically.
      returned: always
      type: str
      sample: null
    bandwidth_in_gbps:
      description:
        - Bandwidth of procured ports in Gbps.
      returned: always
      type: integer
      sample: null
    provisioned_bandwidth_in_gbps:
      description:
        - Aggregate Gbps of associated circuit bandwidths.
      returned: always
      type: number
      sample: null
    mtu:
      description:
        - Maximum transmission unit of the physical port pair(s).
      returned: always
      type: str
      sample: null
    encapsulation:
      description:
        - Encapsulation method on physical ports.
      returned: always
      type: str
      sample: null
    ether_type:
      description:
        - Ether type of the physical port.
      returned: always
      type: str
      sample: null
    allocation_date:
      description:
        - >-
          Date of the physical port allocation to be used in Letter of
          Authorization.
      returned: always
      type: str
      sample: null
    links:
      description:
        - The set of physical links of the ExpressRoutePort resource.
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
    circuits:
      description:
        - >-
          Reference the ExpressRoute circuit(s) that are provisioned on this
          ExpressRoutePort resource.
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
    provisioning_state:
      description:
        - The provisioning state of the express route port resource.
      returned: always
      type: str
      sample: null
    resource_guid:
      description:
        - The resource GUID property of the express route port resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of ExpressRoutePort resources.
      returned: always
      type: list
      sample: null
      contains:
        identity:
          description:
            - 'The identity of ExpressRoutePort, if configured.'
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - >-
                  The type of identity used for the resource. The type
                  'SystemAssigned, UserAssigned' includes both an implicitly
                  created identity and a set of user assigned identities. The
                  type 'None' will remove any identities from the virtual
                  machine.
              returned: always
              type: sealed-choice
              sample: null
            user_assigned_identities:
              description:
                - >-
                  The list of user identities associated with resource. The user
                  identity dictionary key references will be ARM resource ids in
                  the form:
                  '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
              returned: always
              type: dictionary
              sample: null
        peering_location:
          description:
            - >-
              The name of the peering location that the ExpressRoutePort is
              mapped to physically.
          returned: always
          type: str
          sample: null
        bandwidth_in_gbps:
          description:
            - Bandwidth of procured ports in Gbps.
          returned: always
          type: integer
          sample: null
        encapsulation:
          description:
            - Encapsulation method on physical ports.
          returned: always
          type: str
          sample: null
        links:
          description:
            - The set of physical links of the ExpressRoutePort resource.
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
        circuits:
          description:
            - >-
              Reference the ExpressRoute circuit(s) that are provisioned on this
              ExpressRoutePort resource.
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


class AzureRMExpressRoutePortInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            express_route_port_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.express_route_port_name = None

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
        super(AzureRMExpressRoutePortInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.express_route_port_name is not None):
            self.results['express_route_ports'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['express_route_ports'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['express_route_ports'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.express_route_ports.get(resource_group_name=self.resource_group_name,
                                                                express_route_port_name=self.express_route_port_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.express_route_ports.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.express_route_ports.list()
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
    AzureRMExpressRoutePortInfo()


if __name__ == '__main__':
    main()
