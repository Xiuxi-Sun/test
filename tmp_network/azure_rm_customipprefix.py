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
module: azure_rm_customipprefix
version_added: '2.9'
short_description: Manage Azure CustomIPPrefix instance.
description:
  - 'Create, update and delete instance of Azure CustomIPPrefix.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  custom_ip_prefix_name:
    description:
      - The name of the CustomIpPrefix.
      - The name of the custom IP prefix.
    required: true
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
  zones:
    description:
      - >-
        A list of availability zones denoting the IP allocated for the resource
        needs to come from.
    type: list
  cidr:
    description:
      - >-
        The prefix range in CIDR notation. Should include the start address and
        the prefix length.
    type: str
  commissioned_state:
    description:
      - The commissioned state of the Custom IP Prefix.
    type: str
    choices:
      - Provisioning
      - Provisioned
      - Commissioning
      - Commissioned
      - Decommissioning
      - Deprovisioning
  public_ip_prefixes:
    description:
      - The list of all referenced PublicIpPrefixes.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  state:
    description:
      - Assert the state of the CustomIPPrefix.
      - >-
        Use C(present) to create or update an CustomIPPrefix and C(absent) to
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
    - name: Delete custom IP prefix
      azure_rm_customipprefix: 
        custom_ip_prefix_name: test-customipprefix
        resource_group_name: rg1
        

    - name: Create custom IP prefix allocation method
      azure_rm_customipprefix: 
        custom_ip_prefix_name: test-customipprefix
        resource_group_name: rg1
        zones:
          - '1'
        location: westus
        properties:
          cidr: 0.0.0.0/24
        

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
zones:
  description:
    - >-
      A list of availability zones denoting the IP allocated for the resource
      needs to come from.
  returned: always
  type: list
  sample: null
cidr:
  description:
    - >-
      The prefix range in CIDR notation. Should include the start address and
      the prefix length.
  returned: always
  type: str
  sample: null
commissioned_state:
  description:
    - The commissioned state of the Custom IP Prefix.
  returned: always
  type: str
  sample: null
public_ip_prefixes:
  description:
    - The list of all referenced PublicIpPrefixes.
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
resource_guid:
  description:
    - The resource GUID property of the custom IP prefix resource.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the custom IP prefix resource.
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


class AzureRMCustomIPPrefix(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            custom_ip_prefix_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            cidr=dict(
                type='str',
                disposition='/cidr'
            ),
            commissioned_state=dict(
                type='str',
                disposition='/commissioned_state',
                choices=['Provisioning',
                         'Provisioned',
                         'Commissioning',
                         'Commissioned',
                         'Decommissioning',
                         'Deprovisioning']
            ),
            public_ip_prefixes=dict(
                type='list',
                updatable=False,
                disposition='/public_ip_prefixes',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.custom_ip_prefix_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCustomIPPrefix, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.custom_ipprefixes.create_or_update(resource_group_name=self.resource_group_name,
                                                                           custom_ip_prefix_name=self.custom_ip_prefix_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the CustomIPPrefix instance.')
            self.fail('Error creating the CustomIPPrefix instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.custom_ipprefixes.delete(resource_group_name=self.resource_group_name,
                                                                 custom_ip_prefix_name=self.custom_ip_prefix_name)
        except CloudError as e:
            self.log('Error attempting to delete the CustomIPPrefix instance.')
            self.fail('Error deleting the CustomIPPrefix instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.custom_ipprefixes.get(resource_group_name=self.resource_group_name,
                                                              custom_ip_prefix_name=self.custom_ip_prefix_name,
                                                              expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCustomIPPrefix()


if __name__ == '__main__':
    main()
