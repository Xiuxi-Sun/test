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
module: azure_rm_virtualmachineextensionimage
version_added: '2.9'
short_description: Manage Azure VirtualMachineExtensionImage instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineExtensionImage.'
options:
  location:
    description:
      - The name of a supported Azure region.
    required: true
    type: str
  publisher_name:
    description:
      - undefined
    required: true
    type: str
  type:
    description:
      - undefined
    required: true
    type: str
  version:
    description:
      - undefined
    required: true
    type: str
  state:
    description:
      - Assert the state of the VirtualMachineExtensionImage.
      - >-
        Use C(present) to create or update an VirtualMachineExtensionImage and
        C(absent) to delete it.
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
'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
operating_system:
  description:
    - The operating system this extension supports.
  returned: always
  type: str
  sample: null
compute_role:
  description:
    - The type of role (IaaS or PaaS) this extension supports.
  returned: always
  type: str
  sample: null
handler_schema:
  description:
    - >-
      The schema defined by publisher, where extension consumers should provide
      settings in a matching schema.
  returned: always
  type: str
  sample: null
vm_scale_set_enabled:
  description:
    - >-
      Whether the extension can be used on xRP VMScaleSets. By default existing
      extensions are usable on scalesets, but there might be cases where a
      publisher wants to explicitly indicate the extension is only enabled for
      CRP VMs but not VMSS.
  returned: always
  type: bool
  sample: null
supports_multiple_extensions:
  description:
    - Whether the handler can support multiple extensions.
  returned: always
  type: bool
  sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachineExtensionImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            publisher_name=dict(
                type='str',
                required=True
            ),
            type=dict(
                type='str',
                required=True
            ),
            version=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.publisher_name = None
        self.type = None
        self.version = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineExtensionImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.virtual_machine_extension_images.create()
            else:
                response = self.mgmt_client.virtual_machine_extension_images.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineExtensionImage instance.')
            self.fail('Error creating the VirtualMachineExtensionImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_extension_images.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineExtensionImage instance.')
            self.fail('Error deleting the VirtualMachineExtensionImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_extension_images.get(location=self.location,
                                                                             publisher_name=self.publisher_name,
                                                                             type=self.type,
                                                                             version=self.version)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineExtensionImage()


if __name__ == '__main__':
    main()
