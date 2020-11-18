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
module: azure_rm_firewallpolicy
version_added: '2.9'
short_description: Manage Azure FirewallPolicy instance.
description:
  - 'Create, update and delete instance of Azure FirewallPolicy.'
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
  expand:
    description:
      - Expands referenced resources.
    type: str
  identity:
    description:
      - The identity of the firewall policy.
    type: dict
    suboptions:
      type:
        description:
          - >-
            The type of identity used for the resource. The type
            'SystemAssigned, UserAssigned' includes both an implicitly created
            identity and a set of user assigned identities. The type 'None' will
            remove any identities from the virtual machine.
        type: sealed-choice
      user_assigned_identities:
        description:
          - >-
            The list of user identities associated with resource. The user
            identity dictionary key references will be ARM resource ids in the
            form:
            '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        type: dictionary
  rule_collection_groups:
    description:
      - List of references to FirewallPolicyRuleCollectionGroups.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  base_policy:
    description:
      - The parent firewall policy from which rules are inherited.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  firewalls:
    description:
      - >-
        List of references to Azure Firewalls that this Firewall Policy is
        associated with.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  child_policies:
    description:
      - List of references to Child Firewall Policies.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  threat_intel_mode:
    description:
      - The operation mode for Threat Intelligence.
    type: str
    choices:
      - Alert
      - Deny
      - 'Off'
  threat_intel_whitelist:
    description:
      - ThreatIntel Whitelist for Firewall Policy.
    type: dict
    suboptions:
      ip_addresses:
        description:
          - List of IP addresses for the ThreatIntel Whitelist.
        type: list
      fqdns:
        description:
          - List of FQDNs for the ThreatIntel Whitelist.
        type: list
  dns_settings:
    description:
      - DNS Proxy Settings definition.
    type: dict
    suboptions:
      servers:
        description:
          - List of Custom DNS Servers.
        type: list
      enable_proxy:
        description:
          - Enable DNS Proxy on Firewalls attached to the Firewall Policy.
        type: bool
      require_proxy_for_network_rules:
        description:
          - FQDNs in Network Rules are supported when set to true.
        type: bool
  intrusion_detection:
    description:
      - The configuration for Intrusion detection.
    type: dict
    suboptions:
      mode:
        description:
          - Intrusion detection general state.
        type: str
        choices:
          - 'Off'
          - Alert
          - Deny
      configuration:
        description:
          - Intrusion detection configuration properties.
        type: dict
        suboptions:
          signature_overrides:
            description:
              - List of specific signatures states.
            type: list
            suboptions:
              id:
                description:
                  - Signature id.
                type: str
              mode:
                description:
                  - The signature state.
                type: str
                choices:
                  - 'Off'
                  - Alert
                  - Deny
          bypass_traffic_settings:
            description:
              - List of rules for traffic to bypass.
            type: list
            suboptions:
              name:
                description:
                  - Name of the bypass traffic rule.
                type: str
              description:
                description:
                  - Description of the bypass traffic rule.
                type: str
              protocol:
                description:
                  - The rule bypass protocol.
                type: str
                choices:
                  - TCP
                  - UDP
                  - ICMP
                  - ANY
              source_addresses:
                description:
                  - List of source IP addresses or ranges for this rule.
                type: list
              destination_addresses:
                description:
                  - List of destination IP addresses or ranges for this rule.
                type: list
              destination_ports:
                description:
                  - List of destination ports or ranges.
                type: list
              source_ip_groups:
                description:
                  - List of source IpGroups for this rule.
                type: list
              destination_ip_groups:
                description:
                  - List of destination IpGroups for this rule.
                type: list
  transport_security:
    description:
      - TLS Configuration definition.
    type: dict
    suboptions:
      certificate_authority:
        description:
          - The CA used for intermediate CA generation.
        type: dict
        suboptions:
          key_vault_secret_id:
            description:
              - >-
                Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or
                'Certificate' object stored in KeyVault.
            type: str
          name:
            description:
              - Name of the CA certificate.
            type: str
  sku:
    description:
      - The Firewall Policy SKU.
    type: dict
    suboptions:
      tier:
        description:
          - Tier of Firewall Policy.
        type: str
        choices:
          - Standard
          - Premium
  state:
    description:
      - Assert the state of the FirewallPolicy.
      - >-
        Use C(present) to create or update an FirewallPolicy and C(absent) to
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
    - name: Delete Firewall Policy
      azure_rm_firewallpolicy: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        

    - name: Create FirewallPolicy
      azure_rm_firewallpolicy: 
        firewall_policy_name: firewallPolicy
        resource_group_name: rg1
        location: West US
        properties:
          dns_settings:
            enable_proxy: true
            require_proxy_for_network_rules: false
            servers:
              - 30.3.4.5
          intrusion_detection:
            configuration:
              bypass_traffic_settings:
                - description: Rule 1
                  destination_addresses:
                    - 5.6.7.8
                  destination_ports:
                    - '*'
                  name: bypassRule1
                  protocol: TCP
                  source_addresses:
                    - 1.2.3.4
              signature_overrides:
                - id: '2525004'
                  mode: Deny
            mode: Alert
          sku:
            tier: Premium
          threat_intel_mode: Alert
          threat_intel_whitelist:
            fqdns:
              - '*.microsoft.com'
            ip_addresses:
              - 20.3.4.5
          transport_security:
            certificate_authority:
              key_vault_secret_id: 'https://kv/secret'
              name: clientcert
        tags:
          key1: value1
        

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
          The type of identity used for the resource. The type 'SystemAssigned,
          UserAssigned' includes both an implicitly created identity and a set
          of user assigned identities. The type 'None' will remove any
          identities from the virtual machine.
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


class AzureRMFirewallPolicy(AzureRMModuleBaseExt):
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
            expand=dict(
                type='str'
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    type=dict(
                        type='sealed-choice',
                        disposition='type'
                    ),
                    user_assigned_identities=dict(
                        type='dictionary',
                        disposition='user_assigned_identities'
                    )
                )
            ),
            rule_collection_groups=dict(
                type='list',
                updatable=False,
                disposition='/rule_collection_groups',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            base_policy=dict(
                type='dict',
                disposition='/base_policy',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            firewalls=dict(
                type='list',
                updatable=False,
                disposition='/firewalls',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            child_policies=dict(
                type='list',
                updatable=False,
                disposition='/child_policies',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            threat_intel_mode=dict(
                type='str',
                disposition='/threat_intel_mode',
                choices=['Alert',
                         'Deny',
                         'Off']
            ),
            threat_intel_whitelist=dict(
                type='dict',
                disposition='/threat_intel_whitelist',
                options=dict(
                    ip_addresses=dict(
                        type='list',
                        disposition='ip_addresses',
                        elements='str'
                    ),
                    fqdns=dict(
                        type='list',
                        disposition='fqdns',
                        elements='str'
                    )
                )
            ),
            dns_settings=dict(
                type='dict',
                disposition='/dns_settings',
                options=dict(
                    servers=dict(
                        type='list',
                        disposition='servers',
                        elements='str'
                    ),
                    enable_proxy=dict(
                        type='bool',
                        disposition='enable_proxy'
                    ),
                    require_proxy_for_network_rules=dict(
                        type='bool',
                        disposition='require_proxy_for_network_rules'
                    )
                )
            ),
            intrusion_detection=dict(
                type='dict',
                disposition='/intrusion_detection',
                options=dict(
                    mode=dict(
                        type='str',
                        disposition='mode',
                        choices=['Off',
                                 'Alert',
                                 'Deny']
                    ),
                    configuration=dict(
                        type='dict',
                        disposition='configuration',
                        options=dict(
                            signature_overrides=dict(
                                type='list',
                                disposition='signature_overrides',
                                elements='dict',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    ),
                                    mode=dict(
                                        type='str',
                                        disposition='mode',
                                        choices=['Off',
                                                 'Alert',
                                                 'Deny']
                                    )
                                )
                            ),
                            bypass_traffic_settings=dict(
                                type='list',
                                disposition='bypass_traffic_settings',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
                                    description=dict(
                                        type='str',
                                        disposition='description'
                                    ),
                                    protocol=dict(
                                        type='str',
                                        disposition='protocol',
                                        choices=['TCP',
                                                 'UDP',
                                                 'ICMP',
                                                 'ANY']
                                    ),
                                    source_addresses=dict(
                                        type='list',
                                        disposition='source_addresses',
                                        elements='str'
                                    ),
                                    destination_addresses=dict(
                                        type='list',
                                        disposition='destination_addresses',
                                        elements='str'
                                    ),
                                    destination_ports=dict(
                                        type='list',
                                        disposition='destination_ports',
                                        elements='str'
                                    ),
                                    source_ip_groups=dict(
                                        type='list',
                                        disposition='source_ip_groups',
                                        elements='str'
                                    ),
                                    destination_ip_groups=dict(
                                        type='list',
                                        disposition='destination_ip_groups',
                                        elements='str'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            transport_security=dict(
                type='dict',
                disposition='/transport_security',
                options=dict(
                    certificate_authority=dict(
                        type='dict',
                        disposition='certificate_authority',
                        options=dict(
                            key_vault_secret_id=dict(
                                type='str',
                                disposition='key_vault_secret_id'
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            )
                        )
                    )
                )
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    tier=dict(
                        type='str',
                        disposition='tier',
                        choices=['Standard',
                                 'Premium']
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
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFirewallPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.firewall_policies.create_or_update(resource_group_name=self.resource_group_name,
                                                                           firewall_policy_name=self.firewall_policy_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FirewallPolicy instance.')
            self.fail('Error creating the FirewallPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.firewall_policies.delete(resource_group_name=self.resource_group_name,
                                                                 firewall_policy_name=self.firewall_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the FirewallPolicy instance.')
            self.fail('Error deleting the FirewallPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.firewall_policies.get(resource_group_name=self.resource_group_name,
                                                              firewall_policy_name=self.firewall_policy_name,
                                                              expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFirewallPolicy()


if __name__ == '__main__':
    main()
