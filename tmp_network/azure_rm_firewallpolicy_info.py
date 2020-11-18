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
module: azure_rm_firewallpolicy_info
version_added: '2.9'
short_description: Get FirewallPolicy info.
description:
  - Get info of FirewallPolicy.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  firewall_policy_name:
    description:
      - The name of the Firewall Policy.
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get FirewallPolicy
      azure_rm_firewallpolicy_info: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        

    - name: List all Firewall Policies for a given resource group
      azure_rm_firewallpolicy_info: 
        resource_group_name: rg1
        

    - name: List all Firewall Policies for a given subscription
      azure_rm_firewallpolicy_info: 

'''

RETURN = '''
firewall_policies:
  description: >-
    A list of dict results where the key is the name of the FirewallPolicy and
    the values are the facts for that FirewallPolicy.
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
        - The identity of the firewall policy.
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
    rule_collection_groups:
      description:
        - List of references to FirewallPolicyRuleCollectionGroups.
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
        - The provisioning state of the firewall policy resource.
      returned: always
      type: str
      sample: null
    base_policy:
      description:
        - The parent firewall policy from which rules are inherited.
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
    firewalls:
      description:
        - >-
          List of references to Azure Firewalls that this Firewall Policy is
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
    child_policies:
      description:
        - List of references to Child Firewall Policies.
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
    threat_intel_mode:
      description:
        - The operation mode for Threat Intelligence.
      returned: always
      type: str
      sample: null
    threat_intel_whitelist:
      description:
        - ThreatIntel Whitelist for Firewall Policy.
      returned: always
      type: dict
      sample: null
      contains:
        ip_addresses:
          description:
            - List of IP addresses for the ThreatIntel Whitelist.
          returned: always
          type: list
          sample: null
        fqdns:
          description:
            - List of FQDNs for the ThreatIntel Whitelist.
          returned: always
          type: list
          sample: null
    dns_settings:
      description:
        - DNS Proxy Settings definition.
      returned: always
      type: dict
      sample: null
      contains:
        servers:
          description:
            - List of Custom DNS Servers.
          returned: always
          type: list
          sample: null
        enable_proxy:
          description:
            - Enable DNS Proxy on Firewalls attached to the Firewall Policy.
          returned: always
          type: bool
          sample: null
        require_proxy_for_network_rules:
          description:
            - FQDNs in Network Rules are supported when set to true.
          returned: always
          type: bool
          sample: null
    intrusion_detection:
      description:
        - The configuration for Intrusion detection.
      returned: always
      type: dict
      sample: null
      contains:
        mode:
          description:
            - Intrusion detection general state.
          returned: always
          type: str
          sample: null
        configuration:
          description:
            - Intrusion detection configuration properties.
          returned: always
          type: dict
          sample: null
          contains:
            signature_overrides:
              description:
                - List of specific signatures states.
              returned: always
              type: list
              sample: null
              contains:
                id:
                  description:
                    - Signature id.
                  returned: always
                  type: str
                  sample: null
                mode:
                  description:
                    - The signature state.
                  returned: always
                  type: str
                  sample: null
            bypass_traffic_settings:
              description:
                - List of rules for traffic to bypass.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the bypass traffic rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the bypass traffic rule.
                  returned: always
                  type: str
                  sample: null
                protocol:
                  description:
                    - The rule bypass protocol.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses or ranges for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_addresses:
                  description:
                    - List of destination IP addresses or ranges for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_ports:
                  description:
                    - List of destination ports or ranges.
                  returned: always
                  type: list
                  sample: null
                source_ip_groups:
                  description:
                    - List of source IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_ip_groups:
                  description:
                    - List of destination IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
    transport_security:
      description:
        - TLS Configuration definition.
      returned: always
      type: dict
      sample: null
      contains:
        certificate_authority:
          description:
            - The CA used for intermediate CA generation.
          returned: always
          type: dict
          sample: null
          contains:
            key_vault_secret_id:
              description:
                - >-
                  Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or
                  'Certificate' object stored in KeyVault.
              returned: always
              type: str
              sample: null
            name:
              description:
                - Name of the CA certificate.
              returned: always
              type: str
              sample: null
    sku:
      description:
        - The Firewall Policy SKU.
      returned: always
      type: dict
      sample: null
      contains:
        tier:
          description:
            - Tier of Firewall Policy.
          returned: always
          type: str
          sample: null
    value:
      description:
        - List of Firewall Policies in a resource group.
      returned: always
      type: list
      sample: null
      contains:
        identity:
          description:
            - The identity of the firewall policy.
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
        rule_collection_groups:
          description:
            - List of references to FirewallPolicyRuleCollectionGroups.
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
        base_policy:
          description:
            - The parent firewall policy from which rules are inherited.
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
        firewalls:
          description:
            - >-
              List of references to Azure Firewalls that this Firewall Policy is
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
        child_policies:
          description:
            - List of references to Child Firewall Policies.
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
        threat_intel_mode:
          description:
            - The operation mode for Threat Intelligence.
          returned: always
          type: str
          sample: null
        threat_intel_whitelist:
          description:
            - ThreatIntel Whitelist for Firewall Policy.
          returned: always
          type: dict
          sample: null
          contains:
            ip_addresses:
              description:
                - List of IP addresses for the ThreatIntel Whitelist.
              returned: always
              type: list
              sample: null
            fqdns:
              description:
                - List of FQDNs for the ThreatIntel Whitelist.
              returned: always
              type: list
              sample: null
        dns_settings:
          description:
            - DNS Proxy Settings definition.
          returned: always
          type: dict
          sample: null
          contains:
            servers:
              description:
                - List of Custom DNS Servers.
              returned: always
              type: list
              sample: null
            enable_proxy:
              description:
                - Enable DNS Proxy on Firewalls attached to the Firewall Policy.
              returned: always
              type: bool
              sample: null
            require_proxy_for_network_rules:
              description:
                - FQDNs in Network Rules are supported when set to true.
              returned: always
              type: bool
              sample: null
        intrusion_detection:
          description:
            - The configuration for Intrusion detection.
          returned: always
          type: dict
          sample: null
          contains:
            mode:
              description:
                - Intrusion detection general state.
              returned: always
              type: str
              sample: null
            configuration:
              description:
                - Intrusion detection configuration properties.
              returned: always
              type: dict
              sample: null
              contains:
                signature_overrides:
                  description:
                    - List of specific signatures states.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    id:
                      description:
                        - Signature id.
                      returned: always
                      type: str
                      sample: null
                    mode:
                      description:
                        - The signature state.
                      returned: always
                      type: str
                      sample: null
                bypass_traffic_settings:
                  description:
                    - List of rules for traffic to bypass.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - Name of the bypass traffic rule.
                      returned: always
                      type: str
                      sample: null
                    description:
                      description:
                        - Description of the bypass traffic rule.
                      returned: always
                      type: str
                      sample: null
                    protocol:
                      description:
                        - The rule bypass protocol.
                      returned: always
                      type: str
                      sample: null
                    source_addresses:
                      description:
                        - List of source IP addresses or ranges for this rule.
                      returned: always
                      type: list
                      sample: null
                    destination_addresses:
                      description:
                        - >-
                          List of destination IP addresses or ranges for this
                          rule.
                      returned: always
                      type: list
                      sample: null
                    destination_ports:
                      description:
                        - List of destination ports or ranges.
                      returned: always
                      type: list
                      sample: null
                    source_ip_groups:
                      description:
                        - List of source IpGroups for this rule.
                      returned: always
                      type: list
                      sample: null
                    destination_ip_groups:
                      description:
                        - List of destination IpGroups for this rule.
                      returned: always
                      type: list
                      sample: null
        transport_security:
          description:
            - TLS Configuration definition.
          returned: always
          type: dict
          sample: null
          contains:
            certificate_authority:
              description:
                - The CA used for intermediate CA generation.
              returned: always
              type: dict
              sample: null
              contains:
                key_vault_secret_id:
                  description:
                    - >-
                      Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or
                      'Certificate' object stored in KeyVault.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - Name of the CA certificate.
                  returned: always
                  type: str
                  sample: null
        sku:
          description:
            - The Firewall Policy SKU.
          returned: always
          type: dict
          sample: null
          contains:
            tier:
              description:
                - Tier of Firewall Policy.
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


class AzureRMFirewallPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            firewall_policy_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.firewall_policy_name = None
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
        super(AzureRMFirewallPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.firewall_policy_name is not None):
            self.results['firewall_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['firewall_policies'] = self.format_item(self.list())
        else:
            self.results['firewall_policies'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.firewall_policies.get(resource_group_name=self.resource_group_name,
                                                              firewall_policy_name=self.firewall_policy_name,
                                                              expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.firewall_policies.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.firewall_policies.list_all()
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
    AzureRMFirewallPolicyInfo()


if __name__ == '__main__':
    main()
