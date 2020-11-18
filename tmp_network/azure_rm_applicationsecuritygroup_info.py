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
module: azure_rm_applicationsecuritygroup_info
version_added: '2.9'
short_description: Get ApplicationSecurityGroup info.
description:
  - Get info of ApplicationSecurityGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  application_security_group_name:
    description:
      - The name of the application security group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get application security group
      azure_rm_applicationsecuritygroup_info: 
        application_security_group_name: test-asg
        resource_group_name: rg1
        

    - name: List all application security groups
      azure_rm_applicationsecuritygroup_info: 

    - name: List load balancers in resource group
      azure_rm_applicationsecuritygroup_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
application_security_groups:
  description: >-
    A list of dict results where the key is the name of the
    ApplicationSecurityGroup and the values are the facts for that
    ApplicationSecurityGroup.
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
          The resource GUID property of the application security group resource.
          It uniquely identifies a resource, even if the user changes its name
          or migrate the resource across subscriptions or resource groups.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the application security group resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A list of application security groups.
      returned: always
      type: list
      sample: null
    next_link:
      description:
        - The URL to get the next set of results.
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


class AzureRMApplicationSecurityGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            application_security_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.application_security_group_name = None

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
        super(AzureRMApplicationSecurityGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.application_security_group_name is not None):
            self.results['application_security_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['application_security_groups'] = self.format_item(self.list())
        else:
            self.results['application_security_groups'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.application_security_groups.get(resource_group_name=self.resource_group_name,
                                                                        application_security_group_name=self.application_security_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.application_security_groups.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.application_security_groups.list_all()
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
    AzureRMApplicationSecurityGroupInfo()


if __name__ == '__main__':
    main()
