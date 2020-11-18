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
module: azure_rm_bastionhost_info
version_added: '2.9'
short_description: Get BastionHost info.
description:
  - Get info of BastionHost.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  bastion_host_name:
    description:
      - The name of the Bastion Host.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Bastion Host
      azure_rm_bastionhost_info: 
        bastion_host_name: bastionhosttenant'
        resource_group_name: rg1
        

    - name: List all Bastion Hosts for a given subscription
      azure_rm_bastionhost_info: 

    - name: List all Bastion Hosts for a given resource group
      azure_rm_bastionhost_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
bastion_hosts:
  description: >-
    A list of dict results where the key is the name of the BastionHost and the
    values are the facts for that BastionHost.
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
              Name of the resource that is unique within a resource group. This
              name can be used to access the resource.
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
    value:
      description:
        - List of Bastion Hosts in a resource group.
      returned: always
      type: list
      sample: null
      contains:
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
                  Name of the resource that is unique within a resource group.
                  This name can be used to access the resource.
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


class AzureRMBastionHostInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            bastion_host_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.bastion_host_name = None

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
        super(AzureRMBastionHostInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.bastion_host_name is not None):
            self.results['bastion_hosts'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['bastion_hosts'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['bastion_hosts'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.bastion_hosts.get(resource_group_name=self.resource_group_name,
                                                          bastion_host_name=self.bastion_host_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.bastion_hosts.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.bastion_hosts.list()
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
    AzureRMBastionHostInfo()


if __name__ == '__main__':
    main()
