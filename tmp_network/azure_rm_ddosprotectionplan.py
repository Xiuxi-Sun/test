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
module: azure_rm_ddosprotectionplan
version_added: '2.9'
short_description: Manage Azure DdosProtectionPlan instance.
description:
  - 'Create, update and delete instance of Azure DdosProtectionPlan.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  ddos_protection_plan_name:
    description:
      - The name of the DDoS protection plan.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  virtual_networks:
    description:
      - >-
        The list of virtual networks associated with the DDoS protection plan
        resource. This list is read-only.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  state:
    description:
      - Assert the state of the DdosProtectionPlan.
      - >-
        Use C(present) to create or update an DdosProtectionPlan and C(absent)
        to delete it.
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
    - name: Delete DDoS protection plan
      azure_rm_ddosprotectionplan: 
        ddos_protection_plan_name: test-plan
        resource_group_name: rg1
        

    - name: Create DDoS protection plan
      azure_rm_ddosprotectionplan: 
        ddos_protection_plan_name: test-plan
        resource_group_name: rg1
        location: westus
        properties: {}
        

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
resource_guid:
  description:
    - >-
      The resource GUID property of the DDoS protection plan resource. It
      uniquely identifies the resource, even if the user changes its name or
      migrate the resource across subscriptions or resource groups.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the DDoS protection plan resource.
  returned: always
  type: str
  sample: null
virtual_networks:
  description:
    - >-
      The list of virtual networks associated with the DDoS protection plan
      resource. This list is read-only.
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


class AzureRMDdosProtectionPlan(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            ddos_protection_plan_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            virtual_networks=dict(
                type='list',
                updatable=False,
                disposition='/virtual_networks',
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
        self.ddos_protection_plan_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDdosProtectionPlan, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.ddos_protection_plans.create_or_update(resource_group_name=self.resource_group_name,
                                                                               ddos_protection_plan_name=self.ddos_protection_plan_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DdosProtectionPlan instance.')
            self.fail('Error creating the DdosProtectionPlan instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.ddos_protection_plans.delete(resource_group_name=self.resource_group_name,
                                                                     ddos_protection_plan_name=self.ddos_protection_plan_name)
        except CloudError as e:
            self.log('Error attempting to delete the DdosProtectionPlan instance.')
            self.fail('Error deleting the DdosProtectionPlan instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.ddos_protection_plans.get(resource_group_name=self.resource_group_name,
                                                                  ddos_protection_plan_name=self.ddos_protection_plan_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDdosProtectionPlan()


if __name__ == '__main__':
    main()
