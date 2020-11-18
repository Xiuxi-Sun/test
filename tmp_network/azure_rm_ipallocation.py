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
module: azure_rm_ipallocation
version_added: '2.9'
short_description: Manage Azure IpAllocation instance.
description:
  - 'Create, update and delete instance of Azure IpAllocation.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  ip_allocation_name:
    description:
      - The name of the IpAllocation.
    required: true
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
  subnet:
    description:
      - The Subnet that using the prefix of this IpAllocation resource.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  virtual_network:
    description:
      - The VirtualNetwork that using the prefix of this IpAllocation resource.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  type_properties_type:
    description:
      - The type for the IpAllocation.
    type: str
    choices:
      - Undefined
      - Hypernet
  prefix:
    description:
      - The address prefix for the IpAllocation.
    type: str
  prefix_length:
    description:
      - The address prefix length for the IpAllocation.
    type: integer
  prefix_type:
    description:
      - The address prefix Type for the IpAllocation.
    type: str
    choices:
      - IPv4
      - IPv6
  ipam_allocation_id:
    description:
      - The IPAM allocation ID.
    type: str
  allocation_tags:
    description:
      - IpAllocation tags.
    type: dictionary
  state:
    description:
      - Assert the state of the IpAllocation.
      - >-
        Use C(present) to create or update an IpAllocation and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Delete IpAllocation
      azure_rm_ipallocation: 
        ip_allocation_name: test-ipallocation
        resource_group_name: rg1
        

    - name: Create IpAllocation
      azure_rm_ipallocation: 
        ip_allocation_name: test-ipallocation
        resource_group_name: rg1
        location: centraluseuap
        properties:
          allocation_tags:
            vnet_id: >-
              /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/HypernetVnet1
          prefix: 3.2.5.0/24
          type: Hypernet
        

'''

RETURN = '''
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
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
  sample: null
subnet:
  description:
    - The Subnet that using the prefix of this IpAllocation resource.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
virtual_network:
  description:
    - The VirtualNetwork that using the prefix of this IpAllocation resource.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
type_properties_type:
  description:
    - The type for the IpAllocation.
  returned: always
  type: str
  sample: null
prefix:
  description:
    - The address prefix for the IpAllocation.
  returned: always
  type: str
  sample: null
prefix_length:
  description:
    - The address prefix length for the IpAllocation.
  returned: always
  type: integer
  sample: null
prefix_type:
  description:
    - The address prefix Type for the IpAllocation.
  returned: always
  type: str
  sample: null
ipam_allocation_id:
  description:
    - The IPAM allocation ID.
  returned: always
  type: str
  sample: null
allocation_tags:
  description:
    - IpAllocation tags.
  returned: always
  type: dictionary
  sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMIpAllocation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            ip_allocation_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            subnet=dict(
                type='dict',
                updatable=False,
                disposition='/subnet',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            virtual_network=dict(
                type='dict',
                updatable=False,
                disposition='/virtual_network',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            type_properties_type=dict(
                type='str',
                disposition='/type_properties_type',
                choices=['Undefined',
                         'Hypernet']
            ),
            prefix=dict(
                type='str',
                disposition='/prefix'
            ),
            prefix_length=dict(
                type='integer',
                disposition='/prefix_length'
            ),
            prefix_type=dict(
                type='str',
                disposition='/prefix_type',
                choices=['IPv4',
                         'IPv6']
            ),
            ipam_allocation_id=dict(
                type='str',
                disposition='/ipam_allocation_id'
            ),
            allocation_tags=dict(
                type='dictionary',
                disposition='/allocation_tags'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.ip_allocation_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIpAllocation, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.ip_allocations.create_or_update(resource_group_name=self.resource_group_name,
                                                                        ip_allocation_name=self.ip_allocation_name,
                                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IpAllocation instance.')
            self.fail('Error creating the IpAllocation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.ip_allocations.delete(resource_group_name=self.resource_group_name,
                                                              ip_allocation_name=self.ip_allocation_name)
        except CloudError as e:
            self.log('Error attempting to delete the IpAllocation instance.')
            self.fail('Error deleting the IpAllocation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.ip_allocations.get(resource_group_name=self.resource_group_name,
                                                           ip_allocation_name=self.ip_allocation_name,
                                                           expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIpAllocation()


if __name__ == '__main__':
    main()
