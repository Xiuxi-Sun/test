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
module: azure_rm_firewallpolicyrulecollectiongroup
version_added: '2.9'
short_description: Manage Azure FirewallPolicyRuleCollectionGroup instance.
description:
  - >-
    Create, update and delete instance of Azure
    FirewallPolicyRuleCollectionGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  firewall_policy_name:
    description:
      - The name of the Firewall Policy.
    required: true
    type: str
  rule_collection_group_name:
    description:
      - The name of the FirewallPolicyRuleCollectionGroup.
    required: true
    type: str
  name:
    description:
      - >-
        The name of the resource that is unique within a resource group. This
        name can be used to access the resource.
    type: str
  priority:
    description:
      - Priority of the Firewall Policy Rule Collection Group resource.
    type: integer
  rule_collections:
    description:
      - Group of Firewall Policy rule collections.
    type: list
    suboptions:
      rule_collection_type:
        description:
          - The type of the rule collection.
        required: true
        type: str
        choices:
          - FirewallPolicyNatRuleCollection
          - FirewallPolicyFilterRuleCollection
      name:
        description:
          - The name of the rule collection.
        type: str
      priority:
        description:
          - Priority of the Firewall Policy Rule Collection resource.
        type: integer
  state:
    description:
      - Assert the state of the FirewallPolicyRuleCollectionGroup.
      - >-
        Use C(present) to create or update an FirewallPolicyRuleCollectionGroup
        and C(absent) to delete it.
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
    - name: Delete FirewallPolicyRuleCollectionGroup
      azure_rm_firewallpolicyrulecollectiongroup: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        

    - name: Create FirewallPolicyNatRuleCollectionGroup
      azure_rm_firewallpolicyrulecollectiongroup: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        properties:
          priority: 100
          rule_collections:
            - action:
                type: DNAT
              name: Example-Nat-Rule-Collection
              priority: 100
              rule_collection_type: FirewallPolicyNatRuleCollection
              rules:
                - destination_addresses:
                    - 152.23.32.23
                  destination_ports:
                    - '8080'
                  ip_protocols:
                    - TCP
                    - UDP
                  name: nat-rule1
                  rule_type: NatRule
                  source_addresses:
                    - 2.2.2.2
                  source_ip_groups: []
                  translated_fqdn: internalhttp.server.net
                  translated_port: '8080'
        

    - name: Create FirewallPolicyRuleCollectionGroup
      azure_rm_firewallpolicyrulecollectiongroup: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        properties:
          priority: 100
          rule_collections:
            - action:
                type: Deny
              name: Example-Filter-Rule-Collection
              priority: 100
              rule_collection_type: FirewallPolicyFilterRuleCollection
              rules:
                - destination_addresses:
                    - '*'
                  destination_ports:
                    - '*'
                  ip_protocols:
                    - TCP
                  name: network-rule1
                  rule_type: NetworkRule
                  source_addresses:
                    - 10.1.25.0/24
        

    - name: Create FirewallPolicyRuleCollectionGroup With IpGroups
      azure_rm_firewallpolicyrulecollectiongroup: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        properties:
          priority: 110
          rule_collections:
            - action:
                type: Deny
              name: Example-Filter-Rule-Collection
              rule_collection_type: FirewallPolicyFilterRuleCollection
              rules:
                - destination_ip_groups:
                    - >-
                      /subscriptions/subid/providers/Microsoft.Network/resourceGroup/rg1/ipGroups/ipGroups2
                  destination_ports:
                    - '*'
                  ip_protocols:
                    - TCP
                  name: network-1
                  rule_type: NetworkRule
                  source_ip_groups:
                    - >-
                      /subscriptions/subid/providers/Microsoft.Network/resourceGroup/rg1/ipGroups/ipGroups1
        

    - name: Create FirewallPolicyRuleCollectionGroup With Web Categories
      azure_rm_firewallpolicyrulecollectiongroup: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        properties:
          priority: 110
          rule_collections:
            - action:
                type: Deny
              name: Example-Filter-Rule-Collection
              rule_collection_type: FirewallPolicyFilterRuleCollection
              rules:
                - description: Deny inbound rule
                  name: rule1
                  protocols:
                    - port: 443
                      protocol_type: Https
                  rule_type: ApplicationRule
                  source_addresses:
                    - 216.58.216.164
                    - 10.0.0.0/24
                  web_categories:
                    - Hacking
        

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
    - >-
      The name of the resource that is unique within a resource group. This name
      can be used to access the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
  sample: null
type:
  description:
    - Rule Group type.
  returned: always
  type: str
  sample: null
priority:
  description:
    - Priority of the Firewall Policy Rule Collection Group resource.
  returned: always
  type: integer
  sample: null
rule_collections:
  description:
    - Group of Firewall Policy rule collections.
  returned: always
  type: list
  sample: null
  contains:
    rule_collection_type:
      description:
        - The type of the rule collection.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the rule collection.
      returned: always
      type: str
      sample: null
    priority:
      description:
        - Priority of the Firewall Policy Rule Collection resource.
      returned: always
      type: integer
      sample: null
provisioning_state:
  description:
    - >-
      The provisioning state of the firewall policy rule collection group
      resource.
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


class AzureRMFirewallPolicyRuleCollectionGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            firewall_policy_name=dict(
                type='str',
                required=True
            ),
            rule_collection_group_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            priority=dict(
                type='integer',
                disposition='/priority'
            ),
            rule_collections=dict(
                type='list',
                disposition='/rule_collections',
                elements='dict',
                options=dict(
                    rule_collection_type=dict(
                        type='str',
                        disposition='rule_collection_type',
                        choices=['FirewallPolicyNatRuleCollection',
                                 'FirewallPolicyFilterRuleCollection'],
                        required=True
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    priority=dict(
                        type='integer',
                        disposition='priority'
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
        self.firewall_policy_name = None
        self.rule_collection_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFirewallPolicyRuleCollectionGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.firewall_policy_rule_collection_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                                                firewall_policy_name=self.firewall_policy_name,
                                                                                                rule_collection_group_name=self.rule_collection_group_name,
                                                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FirewallPolicyRuleCollectionGroup instance.')
            self.fail('Error creating the FirewallPolicyRuleCollectionGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.firewall_policy_rule_collection_groups.delete(resource_group_name=self.resource_group_name,
                                                                                      firewall_policy_name=self.firewall_policy_name,
                                                                                      rule_collection_group_name=self.rule_collection_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the FirewallPolicyRuleCollectionGroup instance.')
            self.fail('Error deleting the FirewallPolicyRuleCollectionGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.firewall_policy_rule_collection_groups.get(resource_group_name=self.resource_group_name,
                                                                                   firewall_policy_name=self.firewall_policy_name,
                                                                                   rule_collection_group_name=self.rule_collection_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFirewallPolicyRuleCollectionGroup()


if __name__ == '__main__':
    main()
