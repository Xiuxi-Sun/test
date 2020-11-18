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
module: azure_rm_bastionhost
version_added: '2.9'
short_description: Manage Azure BastionHost instance.
description:
  - 'Create, update and delete instance of Azure BastionHost.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  bastion_host_name:
    description:
      - The name of the Bastion Host.
    required: true
    type: str
  ip_configurations:
    description:
      - IP configuration of the Bastion Host resource.
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of the resource that is unique within a resource group. This
            name can be used to access the resource.
        type: str
      subnet:
        description:
          - Reference of the subnet resource.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      public_ip_address:
        description:
          - Reference of the PublicIP resource.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      private_ip_allocation_method:
        description:
          - Private IP allocation method.
        type: str
        choices:
          - Static
          - Dynamic
  dns_name:
    description:
      - FQDN for the endpoint on which bastion host is accessible.
    type: str
  state:
    description:
      - Assert the state of the BastionHost.
      - >-
        Use C(present) to create or update an BastionHost and C(absent) to
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
    - name: Delete Bastion Host
      azure_rm_bastionhost: 
        bastion_host_name: bastionhosttenant
        resource_group_name: rg1
        

    - name: Create Bastion Host
      azure_rm_bastionhost: 
        bastion_host_name: bastionhosttenant'
        resource_group_name: rg1
        properties:
          ip_configurations:
            - name: bastionHostIpConfiguration
              properties:
                public_ipaddress:
                  id: >-
                    /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/pipName
                subnet:
                  id: >-
                    /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet2/subnets/BastionHostSubnet
        

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
ip_configurations:
  description:
    - IP configuration of the Bastion Host resource.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          Name of the resource that is unique within a resource group. This name
          can be used to access the resource.
      returned: always
      type: str
      sample: null
    subnet:
      description:
        - Reference of the subnet resource.
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
    public_ip_address:
      description:
        - Reference of the PublicIP resource.
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
    private_ip_allocation_method:
      description:
        - Private IP allocation method.
      returned: always
      type: str
      sample: null
dns_name:
  description:
    - FQDN for the endpoint on which bastion host is accessible.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the bastion host resource.
  returned: always
  type: str
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


class AzureRMBastionHost(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            bastion_host_name=dict(
                type='str',
                required=True
            ),
            ip_configurations=dict(
                type='list',
                disposition='/ip_configurations',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    subnet=dict(
                        type='dict',
                        disposition='subnet',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    public_ip_address=dict(
                        type='dict',
                        disposition='public_ip_address',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    private_ip_allocation_method=dict(
                        type='str',
                        disposition='private_ip_allocation_method',
                        choices=['Static',
                                 'Dynamic']
                    )
                )
            ),
            dns_name=dict(
                type='str',
                disposition='/dns_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.bastion_host_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBastionHost, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.bastion_hosts.create_or_update(resource_group_name=self.resource_group_name,
                                                                       bastion_host_name=self.bastion_host_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the BastionHost instance.')
            self.fail('Error creating the BastionHost instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bastion_hosts.delete(resource_group_name=self.resource_group_name,
                                                             bastion_host_name=self.bastion_host_name)
        except CloudError as e:
            self.log('Error attempting to delete the BastionHost instance.')
            self.fail('Error deleting the BastionHost instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bastion_hosts.get(resource_group_name=self.resource_group_name,
                                                          bastion_host_name=self.bastion_host_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBastionHost()


if __name__ == '__main__':
    main()
