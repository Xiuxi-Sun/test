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
module: azure_rm_firewallpolicyrulecollectiongroup_info
version_added: '2.9'
short_description: Get FirewallPolicyRuleCollectionGroup info.
description:
  - Get info of FirewallPolicyRuleCollectionGroup.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get FirewallPolicyNatRuleCollectionGroup
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        

    - name: Get FirewallPolicyRuleCollectionGroup
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        

    - name: Get FirewallPolicyRuleCollectionGroup With IpGroups
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleGroup1
        

    - name: Get FirewallPolicyRuleCollectionGroup With Web Categories
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        rule_collection_group_name: ruleCollectionGroup1
        

    - name: List all FirewallPolicyRuleCollectionGroup With Web Categories
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        

    - name: List all FirewallPolicyRuleCollectionGroups for a given FirewallPolicy
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        

    - name: List all FirewallPolicyRuleCollectionGroups with IpGroups for a given FirewallPolicy
      azure_rm_firewallpolicyrulecollectiongroup_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        

'''

RETURN = '''
firewall_policy_rule_collection_groups:
  description: >-
    A list of dict results where the key is the name of the
    FirewallPolicyRuleCollectionGroup and the values are the facts for that
    FirewallPolicyRuleCollectionGroup.
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
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
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
    value:
      description:
        - List of FirewallPolicyRuleCollectionGroups in a FirewallPolicy.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within a resource group.
              This name can be used to access the resource.
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


class AzureRMFirewallPolicyRuleCollectionGroupInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.firewall_policy_name = None
        self.rule_collection_group_name = None

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
        super(AzureRMFirewallPolicyRuleCollectionGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.firewall_policy_name is not None and
            self.rule_collection_group_name is not None):
            self.results['firewall_policy_rule_collection_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.firewall_policy_name is not None):
            self.results['firewall_policy_rule_collection_groups'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.firewall_policy_rule_collection_groups.get(resource_group_name=self.resource_group_name,
                                                                                   firewall_policy_name=self.firewall_policy_name,
                                                                                   rule_collection_group_name=self.rule_collection_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.firewall_policy_rule_collection_groups.list(resource_group_name=self.resource_group_name,
                                                                                    firewall_policy_name=self.firewall_policy_name)
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
    AzureRMFirewallPolicyRuleCollectionGroupInfo()


if __name__ == '__main__':
    main()
