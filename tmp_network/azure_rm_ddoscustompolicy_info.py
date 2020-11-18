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
module: azure_rm_ddoscustompolicy_info
version_added: '2.9'
short_description: Get DdosCustomPolicy info.
description:
  - Get info of DdosCustomPolicy.
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
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get DDoS custom policy
      azure_rm_ddoscustompolicy_info: 
        ddos_custom_policy_name: test-ddos-custom-policy
        resource_group_name: rg1
        

'''

RETURN = '''
ddos_custom_policies:
  description: >-
    A list of dict results where the key is the name of the DdosCustomPolicy and
    the values are the facts for that DdosCustomPolicy.
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
    resource_guid:
      description:
        - >-
          The resource GUID property of the DDoS custom policy resource. It
          uniquely identifies the resource, even if the user changes its name or
          migrate the resource across subscriptions or resource groups.
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
          The list of public IPs associated with the DDoS custom policy
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
    protocol_custom_settings:
      description:
        - The protocol-specific DDoS policy customization parameters.
      returned: always
      type: list
      sample: null
      contains:
        protocol:
          description:
            - >-
              The protocol for which the DDoS protection policy is being
              customized.
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
              The customized DDoS protection trigger rate sensitivity degrees.
              High: Trigger rate set with most sensitivity w.r.t. normal
              traffic. Default: Trigger rate set with moderate sensitivity
              w.r.t. normal traffic. Low: Trigger rate set with less sensitivity
              w.r.t. normal traffic. Relaxed: Trigger rate set with least
              sensitivity w.r.t. normal traffic.
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


class AzureRMDdosCustomPolicyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            ddos_custom_policy_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.ddos_custom_policy_name = None

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
        super(AzureRMDdosCustomPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.ddos_custom_policy_name is not None):
            self.results['ddos_custom_policies'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.ddos_custom_policies.get(resource_group_name=self.resource_group_name,
                                                                 ddos_custom_policy_name=self.ddos_custom_policy_name)
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
    AzureRMDdosCustomPolicyInfo()


if __name__ == '__main__':
    main()
