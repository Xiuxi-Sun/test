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
module: azure_rm_virtualmachinescalesetvmruncommand_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetVMRunCommand info.
description:
  - Get info of VirtualMachineScaleSetVMRunCommand.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_scale_set_name:
    description:
      - The name of the VM scale set.
    required: true
    type: str
  instance_id:
    description:
      - The instance ID of the virtual machine.
    required: true
    type: str
  run_command_name:
    description:
      - The name of the virtual machine run command.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get VirtualMachineScaleSet VM run commands.
      azure_rm_virtualmachinescalesetvmruncommand_info: 
        instance_id: '0'
        resource_group_name: myResourceGroup
        run_command_name: myRunCommand
        vm_scale_set_name: myvmScaleSet
        

    - name: List run commands in Vmss instance.
      azure_rm_virtualmachinescalesetvmruncommand_info: 
        instance_id: '0'
        resource_group_name: myResourceGroup
        vm_scale_set_name: myvmScaleSet
        

'''

RETURN = '''
virtual_machine_scale_set_vmrun_commands:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineScaleSetVMRunCommand and the values are the facts for that
    VirtualMachineScaleSetVMRunCommand.
  returned: always
  type: complex
  contains:
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
    source:
      description:
        - The source of the run command script.
      returned: always
      type: dict
      sample: null
      contains:
        script:
          description:
            - Specifies the script content to be executed on the VM.
          returned: always
          type: str
          sample: null
        script_uri:
          description:
            - Specifies the script download location.
          returned: always
          type: str
          sample: null
        command_id:
          description:
            - Specifies a commandId of predefined built-in script.
          returned: always
          type: str
          sample: null
    parameters:
      description:
        - The parameters used by the script.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The run command parameter name.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The run command parameter value.
          returned: always
          type: str
          sample: null
    protected_parameters:
      description:
        - The parameters used by the script.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The run command parameter name.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The run command parameter value.
          returned: always
          type: str
          sample: null
    async_execution:
      description:
        - >-
          Optional. If set to true, provisioning will complete as soon as the
          script starts and will not wait for script to complete.
      returned: always
      type: bool
      sample: null
    run_as_user:
      description:
        - Specifies the user account on the VM when executing the run command.
      returned: always
      type: str
      sample: null
    run_as_password:
      description:
        - >-
          Specifies the user account password on the VM when executing the run
          command.
      returned: always
      type: str
      sample: null
    timeout_in_seconds:
      description:
        - The timeout in seconds to execute the run command.
      returned: always
      type: integer
      sample: null
    output_blob_uri:
      description:
        - >-
          Specifies the Azure storage blob where script output stream will be
          uploaded.
      returned: always
      type: str
      sample: null
    error_blob_uri:
      description:
        - >-
          Specifies the Azure storage blob where script error stream will be
          uploaded.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    instance_view:
      description:
        - The virtual machine run command instance view.
      returned: always
      type: dict
      sample: null
      contains:
        execution_state:
          description:
            - Script execution status.
          returned: always
          type: str
          sample: null
        execution_message:
          description:
            - Communicate script configuration errors or execution messages.
          returned: always
          type: str
          sample: null
        exit_code:
          description:
            - Exit code returned from script execution.
          returned: always
          type: integer
          sample: null
        output:
          description:
            - Script output stream.
          returned: always
          type: str
          sample: null
        error:
          description:
            - Script error stream.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - Script start time.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - Script end time.
          returned: always
          type: str
          sample: null
        statuses:
          description:
            - The resource status information.
          returned: always
          type: list
          sample: null
          contains:
            code:
              description:
                - The status code.
              returned: always
              type: str
              sample: null
            level:
              description:
                - The level code.
              returned: always
              type: sealed-choice
              sample: null
            display_status:
              description:
                - The short localizable label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed status message, including for alerts and error
                  messages.
              returned: always
              type: str
              sample: null
            time:
              description:
                - The time of the status.
              returned: always
              type: str
              sample: null
    value:
      description:
        - The list of run commands
      returned: always
      type: list
      sample: null
      contains:
        source:
          description:
            - The source of the run command script.
          returned: always
          type: dict
          sample: null
          contains:
            script:
              description:
                - Specifies the script content to be executed on the VM.
              returned: always
              type: str
              sample: null
            script_uri:
              description:
                - Specifies the script download location.
              returned: always
              type: str
              sample: null
            command_id:
              description:
                - Specifies a commandId of predefined built-in script.
              returned: always
              type: str
              sample: null
        parameters:
          description:
            - The parameters used by the script.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The run command parameter name.
              returned: always
              type: str
              sample: null
            value:
              description:
                - The run command parameter value.
              returned: always
              type: str
              sample: null
        protected_parameters:
          description:
            - The parameters used by the script.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The run command parameter name.
              returned: always
              type: str
              sample: null
            value:
              description:
                - The run command parameter value.
              returned: always
              type: str
              sample: null
        async_execution:
          description:
            - >-
              Optional. If set to true, provisioning will complete as soon as
              the script starts and will not wait for script to complete.
          returned: always
          type: bool
          sample: null
        run_as_user:
          description:
            - >-
              Specifies the user account on the VM when executing the run
              command.
          returned: always
          type: str
          sample: null
        run_as_password:
          description:
            - >-
              Specifies the user account password on the VM when executing the
              run command.
          returned: always
          type: str
          sample: null
        timeout_in_seconds:
          description:
            - The timeout in seconds to execute the run command.
          returned: always
          type: integer
          sample: null
        output_blob_uri:
          description:
            - >-
              Specifies the Azure storage blob where script output stream will
              be uploaded.
          returned: always
          type: str
          sample: null
        error_blob_uri:
          description:
            - >-
              Specifies the Azure storage blob where script error stream will be
              uploaded.
          returned: always
          type: str
          sample: null
        instance_view:
          description:
            - The virtual machine run command instance view.
          returned: always
          type: dict
          sample: null
          contains:
            execution_state:
              description:
                - Script execution status.
              returned: always
              type: str
              sample: null
            execution_message:
              description:
                - Communicate script configuration errors or execution messages.
              returned: always
              type: str
              sample: null
            exit_code:
              description:
                - Exit code returned from script execution.
              returned: always
              type: integer
              sample: null
            output:
              description:
                - Script output stream.
              returned: always
              type: str
              sample: null
            error:
              description:
                - Script error stream.
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - Script start time.
              returned: always
              type: str
              sample: null
            end_time:
              description:
                - Script end time.
              returned: always
              type: str
              sample: null
            statuses:
              description:
                - The resource status information.
              returned: always
              type: list
              sample: null
              contains:
                code:
                  description:
                    - The status code.
                  returned: always
                  type: str
                  sample: null
                level:
                  description:
                    - The level code.
                  returned: always
                  type: sealed-choice
                  sample: null
                display_status:
                  description:
                    - The short localizable label for the status.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      The detailed status message, including for alerts and
                      error messages.
                  returned: always
                  type: str
                  sample: null
                time:
                  description:
                    - The time of the status.
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - The uri to fetch the next page of run commands.
      returned: always
      type: str
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


class AzureRMVirtualMachineScaleSetVMRunCommandInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str',
                required=True
            ),
            instance_id=dict(
                type='str',
                required=True
            ),
            run_command_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.run_command_name = None
        self.expand = None

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
        super(AzureRMVirtualMachineScaleSetVMRunCommandInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None and
            self.run_command_name is not None):
            self.results['virtual_machine_scale_set_vmrun_commands'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None):
            self.results['virtual_machine_scale_set_vmrun_commands'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vmrun_commands.get(resource_group_name=self.resource_group_name,
                                                                                     vm_scale_set_name=self.vm_scale_set_name,
                                                                                     instance_id=self.instance_id,
                                                                                     run_command_name=self.run_command_name,
                                                                                     expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vmrun_commands.list(resource_group_name=self.resource_group_name,
                                                                                      vm_scale_set_name=self.vm_scale_set_name,
                                                                                      instance_id=self.instance_id,
                                                                                      expand=self.expand)
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
    AzureRMVirtualMachineScaleSetVMRunCommandInfo()


if __name__ == '__main__':
    main()
