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
module: azure_rm_ipgroup_info
version_added: '2.9'
short_description: Get IpGroup info.
description:
  - Get info of IpGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  ip_groups_name:
    description:
      - The name of the ipGroups.
    type: str
  expand:
    description:
      - >-
        Expands resourceIds (of Firewalls/Network Security Groups etc.) back
        referenced by the IpGroups resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get_IpGroups
      azure_rm_ipgroup_info: 
        ip_groups_name: ipGroups1
        resource_group_name: myResourceGroup
        

    - name: ListByResourceGroup_IpGroups
      azure_rm_ipgroup_info: 
        resource_group_name: myResourceGroup
        

    - name: List_IpGroups
      azure_rm_ipgroup_info: 

'''

RETURN = '''
ip_groups:
  description: >-
    A list of dict results where the key is the name of the IpGroup and the
    values are the facts for that IpGroup.
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
    provisioning_state:
      description:
        - The provisioning state of the IpGroups resource.
      returned: always
      type: str
      sample: null
    ip_addresses:
      description:
        - IpAddresses/IpAddressPrefixes in the IpGroups resource.
      returned: always
      type: list
      sample: null
    firewalls:
      description:
        - >-
          List of references to Firewall resources that this IpGroups is
          associated with.
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
    firewall_policies:
      description:
        - >-
          List of references to Firewall Policies resources that this IpGroups
          is associated with.
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
    value:
      description:
        - The list of IpGroups information resources.
      returned: always
      type: list
      sample: null
      contains:
        ip_addresses:
          description:
            - IpAddresses/IpAddressPrefixes in the IpGroups resource.
          returned: always
          type: list
          sample: null
        firewalls:
          description:
            - >-
              List of references to Firewall resources that this IpGroups is
              associated with.
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
        firewall_policies:
          description:
            - >-
              List of references to Firewall Policies resources that this
              IpGroups is associated with.
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


class AzureRMIpGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            ip_groups_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.ip_groups_name = None
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
        super(AzureRMIpGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.ip_groups_name is not None):
            self.results['ip_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['ip_groups'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['ip_groups'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.ip_groups.get(resource_group_name=self.resource_group_name,
                                                      ip_groups_name=self.ip_groups_name,
                                                      expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.ip_groups.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.ip_groups.list()
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
    AzureRMIpGroupInfo()


if __name__ == '__main__':
    main()
