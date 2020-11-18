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
module: azure_rm_ddoscustompolicy
version_added: '2.9'
short_description: Manage Azure DdosCustomPolicy instance.
description:
  - 'Create, update and delete instance of Azure DdosCustomPolicy.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  ddos_custom_policy_name:
    description:
      - The name of the DDoS custom policy.
    required: true
    type: str
  public_ip_addresses:
    description:
      - >-
        The list of public IPs associated with the DDoS custom policy resource.
        This list is read-only.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  protocol_custom_settings:
    description:
      - The protocol-specific DDoS policy customization parameters.
    type: list
    suboptions:
      protocol:
        description:
          - >-
            The protocol for which the DDoS protection policy is being
            customized.
        type: str
        choices:
          - Tcp
          - Udp
          - Syn
      trigger_rate_override:
        description:
          - The customized DDoS protection trigger rate.
        type: str
      source_rate_override:
        description:
          - The customized DDoS protection source rate.
        type: str
      trigger_sensitivity_override:
        description:
          - >-
            The customized DDoS protection trigger rate sensitivity degrees.
            High: Trigger rate set with most sensitivity w.r.t. normal traffic.
            Default: Trigger rate set with moderate sensitivity w.r.t. normal
            traffic. Low: Trigger rate set with less sensitivity w.r.t. normal
            traffic. Relaxed: Trigger rate set with least sensitivity w.r.t.
            normal traffic.
        type: str
        choices:
          - Relaxed
          - Low
          - Default
          - High
  state:
    description:
      - Assert the state of the DdosCustomPolicy.
      - >-
        Use C(present) to create or update an DdosCustomPolicy and C(absent) to
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
    - name: Delete DDoS custom policy
      azure_rm_ddoscustompolicy: 
        ddos_custom_policy_name: test-ddos-custom-policy
        resource_group_name: rg1
        properties: {}
        

    - name: Create DDoS custom policy
      azure_rm_ddoscustompolicy: 
        ddos_custom_policy_name: test-ddos-custom-policy
        resource_group_name: rg1
        location: centraluseuap
        properties:
          protocol_custom_settings:
            - protocol: Tcp
        

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
      The resource GUID property of the DDoS custom policy resource. It uniquely
      identifies the resource, even if the user changes its name or migrate the
      resource across subscriptions or resource groups.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the DDoS custom policy resource.
  returned: always
  type: str
  sample: null
public_ip_addresses:
  description:
    - >-
      The list of public IPs associated with the DDoS custom policy resource.
      This list is read-only.
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
protocol_custom_settings:
  description:
    - The protocol-specific DDoS policy customization parameters.
  returned: always
  type: list
  sample: null
  contains:
    protocol:
      description:
        - The protocol for which the DDoS protection policy is being customized.
      returned: always
      type: str
      sample: null
    trigger_rate_override:
      description:
        - The customized DDoS protection trigger rate.
      returned: always
      type: str
      sample: null
    source_rate_override:
      description:
        - The customized DDoS protection source rate.
      returned: always
      type: str
      sample: null
    trigger_sensitivity_override:
      description:
        - >-
          The customized DDoS protection trigger rate sensitivity degrees. High:
          Trigger rate set with most sensitivity w.r.t. normal traffic. Default:
          Trigger rate set with moderate sensitivity w.r.t. normal traffic. Low:
          Trigger rate set with less sensitivity w.r.t. normal traffic. Relaxed:
          Trigger rate set with least sensitivity w.r.t. normal traffic.
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


class AzureRMDdosCustomPolicy(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            ddos_custom_policy_name=dict(
                type='str',
                required=True
            ),
            public_ip_addresses=dict(
                type='list',
                updatable=False,
                disposition='/public_ip_addresses',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            protocol_custom_settings=dict(
                type='list',
                disposition='/protocol_custom_settings',
                elements='dict',
                options=dict(
                    protocol=dict(
                        type='str',
                        disposition='protocol',
                        choices=['Tcp',
                                 'Udp',
                                 'Syn']
                    ),
                    trigger_rate_override=dict(
                        type='str',
                        disposition='trigger_rate_override'
                    ),
                    source_rate_override=dict(
                        type='str',
                        disposition='source_rate_override'
                    ),
                    trigger_sensitivity_override=dict(
                        type='str',
                        disposition='trigger_sensitivity_override',
                        choices=['Relaxed',
                                 'Low',
                                 'Default',
                                 'High']
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
        self.ddos_custom_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDdosCustomPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.ddos_custom_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                              ddos_custom_policy_name=self.ddos_custom_policy_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DdosCustomPolicy instance.')
            self.fail('Error creating the DdosCustomPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.ddos_custom_policies.delete(resource_group_name=self.resource_group_name,
                                                                    ddos_custom_policy_name=self.ddos_custom_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the DdosCustomPolicy instance.')
            self.fail('Error deleting the DdosCustomPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.ddos_custom_policies.get(resource_group_name=self.resource_group_name,
                                                                 ddos_custom_policy_name=self.ddos_custom_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDdosCustomPolicy()


if __name__ == '__main__':
    main()
