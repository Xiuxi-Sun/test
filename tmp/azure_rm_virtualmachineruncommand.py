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
module: azure_rm_virtualmachineruncommand
version_added: '2.9'
short_description: Manage Azure VirtualMachineRunCommand instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineRunCommand.'
options:
  location:
    description:
      - The location upon which run commands is queried.
    type: str
  command_id:
    description:
      - The command id.
    type: str
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  vm_name:
    description:
      - >-
        The name of the virtual machine where the run command should be created
        or updated.
      - The name of the virtual machine where the run command should be updated.
      - The name of the virtual machine where the run command should be deleted.
    type: str
  run_command_name:
    description:
      - The name of the virtual machine run command.
    type: str
  source:
    description:
      - The source of the run command script.
    type: dict
    suboptions:
      script:
        description:
          - Specifies the script content to be executed on the VM.
        type: str
      script_uri:
        description:
          - Specifies the script download location.
        type: str
      command_id:
        description:
          - Specifies a commandId of predefined built-in script.
        type: str
  parameters:
    description:
      - The parameters used by the script.
    type: list
    suboptions:
      name:
        description:
          - The run command parameter name.
        required: true
        type: str
      value:
        description:
          - The run command parameter value.
        required: true
        type: str
  protected_parameters:
    description:
      - The parameters used by the script.
    type: list
    suboptions:
      name:
        description:
          - The run command parameter name.
        required: true
        type: str
      value:
        description:
          - The run command parameter value.
        required: true
        type: str
  async_execution:
    description:
      - >-
        Optional. If set to true, provisioning will complete as soon as the
        script starts and will not wait for script to complete.
    type: bool
  run_as_user:
    description:
      - Specifies the user account on the VM when executing the run command.
    type: str
  run_as_password:
    description:
      - >-
        Specifies the user account password on the VM when executing the run
        command.
    type: str
  timeout_in_seconds:
    description:
      - The timeout in seconds to execute the run command.
    type: integer
  output_blob_uri:
    description:
      - >-
        Specifies the Azure storage blob where script output stream will be
        uploaded.
    type: str
  error_blob_uri:
    description:
      - >-
        Specifies the Azure storage blob where script error stream will be
        uploaded.
    type: str
  instance_view:
    description:
      - The virtual machine run command instance view.
    type: dict
    suboptions:
      execution_state:
        description:
          - Script execution status.
        type: str
        choices:
          - Unknown
          - Pending
          - Running
          - Failed
          - Succeeded
          - TimedOut
          - Canceled
      execution_message:
        description:
          - Communicate script configuration errors or execution messages.
        type: str
      exit_code:
        description:
          - Exit code returned from script execution.
        type: integer
      output:
        description:
          - Script output stream.
        type: str
      error:
        description:
          - Script error stream.
        type: str
      start_time:
        description:
          - Script start time.
        type: str
      end_time:
        description:
          - Script end time.
        type: str
      statuses:
        description:
          - The resource status information.
        type: list
        suboptions:
          code:
            description:
              - The status code.
            type: str
          level:
            description:
              - The level code.
            type: sealed-choice
          display_status:
            description:
              - The short localizable label for the status.
            type: str
          message:
            description:
              - >-
                The detailed status message, including for alerts and error
                messages.
            type: str
          time:
            description:
              - The time of the status.
            type: str
  state:
    description:
      - Assert the state of the VirtualMachineRunCommand.
      - >-
        Use C(present) to create or update an VirtualMachineRunCommand and
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
    - name: Create or update a run command.
      azure_rm_virtualmachineruncommand: 
        resource_group_name: myResourceGroup
        run_command_name: myRunCommand
        vm_name: myVM
        

    - name: Update a run command.
      azure_rm_virtualmachineruncommand: 
        resource_group_name: myResourceGroup
        run_command_name: myRunCommand
        vm_name: myVM
        

    - name: Delete a run command.
      azure_rm_virtualmachineruncommand: 
        resource_group_name: myResourceGroup
        run_command_name: myRunCommand
        vm_name: myVM
        

'''

RETURN = '''
schema:
  description:
    - The VM run command schema.
  returned: always
  type: str
  sample: null
id:
  description:
    - |-
      The VM run command id.
      Resource Id
  returned: always
  type: str
  sample: null
os_type:
  description:
    - The Operating System type.
  returned: always
  type: sealed-choice
  sample: null
label:
  description:
    - The VM run command label.
  returned: always
  type: str
  sample: null
description:
  description:
    - The VM run command description.
  returned: always
  type: str
  sample: null
script:
  description:
    - The script to be executed.
  returned: always
  type: list
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
    type:
      description:
        - The run command parameter type.
      returned: always
      type: str
      sample: null
    default_value:
      description:
        - The run command parameter default value.
      returned: always
      type: str
      sample: null
    required:
      description:
        - The run command parameter required.
      returned: always
      type: bool
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
      Optional. If set to true, provisioning will complete as soon as the script
      starts and will not wait for script to complete.
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


class AzureRMVirtualMachineRunCommand(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str'
            ),
            command_id=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            vm_name=dict(
                type='str'
            ),
            run_command_name=dict(
                type='str'
            ),
            source=dict(
                type='dict',
                disposition='/source',
                options=dict(
                    script=dict(
                        type='str',
                        disposition='script'
                    ),
                    script_uri=dict(
                        type='str',
                        disposition='script_uri'
                    ),
                    command_id=dict(
                        type='str',
                        disposition='command_id'
                    )
                )
            ),
            parameters=dict(
                type='list',
                disposition='/parameters',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    )
                )
            ),
            protected_parameters=dict(
                type='list',
                disposition='/protected_parameters',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    value=dict(
                        type='str',
                        disposition='value',
                        required=True
                    )
                )
            ),
            async_execution=dict(
                type='bool',
                disposition='/async_execution'
            ),
            run_as_user=dict(
                type='str',
                disposition='/run_as_user'
            ),
            run_as_password=dict(
                type='str',
                disposition='/run_as_password'
            ),
            timeout_in_seconds=dict(
                type='integer',
                disposition='/timeout_in_seconds'
            ),
            output_blob_uri=dict(
                type='str',
                disposition='/output_blob_uri'
            ),
            error_blob_uri=dict(
                type='str',
                disposition='/error_blob_uri'
            ),
            instance_view=dict(
                type='dict',
                updatable=False,
                disposition='/instance_view',
                options=dict(
                    execution_state=dict(
                        type='str',
                        disposition='execution_state',
                        choices=['Unknown',
                                 'Pending',
                                 'Running',
                                 'Failed',
                                 'Succeeded',
                                 'TimedOut',
                                 'Canceled']
                    ),
                    execution_message=dict(
                        type='str',
                        disposition='execution_message'
                    ),
                    exit_code=dict(
                        type='integer',
                        disposition='exit_code'
                    ),
                    output=dict(
                        type='str',
                        disposition='output'
                    ),
                    error=dict(
                        type='str',
                        disposition='error'
                    ),
                    start_time=dict(
                        type='str',
                        disposition='start_time'
                    ),
                    end_time=dict(
                        type='str',
                        disposition='end_time'
                    ),
                    statuses=dict(
                        type='list',
                        disposition='statuses',
                        elements='dict',
                        options=dict(
                            code=dict(
                                type='str',
                                disposition='code'
                            ),
                            level=dict(
                                type='sealed-choice',
                                disposition='level'
                            ),
                            display_status=dict(
                                type='str',
                                disposition='display_status'
                            ),
                            message=dict(
                                type='str',
                                disposition='message'
                            ),
                            time=dict(
                                type='str',
                                disposition='time'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.command_id = None
        self.resource_group_name = None
        self.vm_name = None
        self.run_command_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineRunCommand, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.virtual_machine_run_commands.create_or_update(resource_group_name=self.resource_group_name,
                                                                                      vm_name=self.vm_name,
                                                                                      run_command_name=self.run_command_name,
                                                                                      run_command=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineRunCommand instance.')
            self.fail('Error creating the VirtualMachineRunCommand instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_run_commands.delete(resource_group_name=self.resource_group_name,
                                                                            vm_name=self.vm_name,
                                                                            run_command_name=self.run_command_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineRunCommand instance.')
            self.fail('Error deleting the VirtualMachineRunCommand instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_run_commands.get(location=self.location,
                                                                         command_id=self.command_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineRunCommand()


if __name__ == '__main__':
    main()
