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
module: azure_rm_virtualmachinesize_info
version_added: '2.9'
short_description: Get VirtualMachineSize info.
description:
  - Get info of VirtualMachineSize.
options:
  location:
    description:
      - The location upon which virtual-machine-sizes is queried.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
virtual_machine_sizes:
  description: >-
    A list of dict results where the key is the name of the VirtualMachineSize
    and the values are the facts for that VirtualMachineSize.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of virtual machine sizes.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the virtual machine size.
          returned: always
          type: str
          sample: null
        number_of_cores:
          description:
            - The number of cores supported by the virtual machine size.
          returned: always
          type: integer
          sample: null
        os_disk_size_in_mb:
          description:
            - 'The OS disk size, in MB, allowed by the virtual machine size.'
          returned: always
          type: integer
          sample: null
        resource_disk_size_in_mb:
          description:
            - >-
              The resource disk size, in MB, allowed by the virtual machine
              size.
          returned: always
          type: integer
          sample: null
        memory_in_mb:
          description:
            - >-
              The amount of memory, in MB, supported by the virtual machine
              size.
          returned: always
          type: integer
          sample: null
        max_data_disk_count:
          description:
            - >-
              The maximum number of data disks that can be attached to the
              virtual machine size.
          returned: always
          type: integer
          sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineSizeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            )
        )

        self.location = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineSizeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.location is not None):
            self.results['virtual_machine_sizes'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_sizes.list(location=self.location)
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
    AzureRMVirtualMachineSizeInfo()


if __name__ == '__main__':
    main()
