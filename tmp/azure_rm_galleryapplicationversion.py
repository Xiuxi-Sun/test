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
module: azure_rm_galleryapplicationversion
version_added: '2.9'
short_description: Manage Azure GalleryApplicationVersion instance.
description:
  - 'Create, update and delete instance of Azure GalleryApplicationVersion.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery in which the Application
        Definition resides.
    required: true
    type: str
  gallery_application_name:
    description:
      - >-
        The name of the gallery Application Definition in which the Application
        Version is to be created.
      - >-
        The name of the gallery Application Definition in which the Application
        Version is to be updated.
      - >-
        The name of the gallery Application Definition in which the Application
        Version resides.
    required: true
    type: str
  gallery_application_version_name:
    description:
      - >-
        The name of the gallery Application Version to be created. Needs to
        follow semantic version name pattern: The allowed characters are digit
        and period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - >-
        The name of the gallery Application Version to be updated. Needs to
        follow semantic version name pattern: The allowed characters are digit
        and period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
      - The name of the gallery Application Version to be retrieved.
      - The name of the gallery Application Version to be deleted.
    required: true
    type: str
  publishing_profile:
    description:
      - The publishing profile of a gallery image version.
    type: dict
    suboptions:
      source:
        description:
          - >-
            The source image from which the Image Version is going to be
            created.
        required: true
        type: dict
        suboptions:
          media_link:
            description:
              - >-
                Required. The mediaLink of the artifact, must be a readable
                storage page blob.
            required: true
            type: str
          default_configuration_link:
            description:
              - >-
                Optional. The defaultConfigurationLink of the artifact, must be
                a readable storage page blob.
            type: str
      manage_actions:
        description:
          - undefined
        type: dict
        suboptions:
          install:
            description:
              - >-
                Required. The path and arguments to install the gallery
                application. This is limited to 4096 characters.
            required: true
            type: str
          remove:
            description:
              - >-
                Required. The path and arguments to remove the gallery
                application. This is limited to 4096 characters.
            required: true
            type: str
          update:
            description:
              - >-
                Optional. The path and arguments to update the gallery
                application. If not present, then update operation will invoke
                remove command on the previous version and install command on
                the current version of the gallery application. This is limited
                to 4096 characters.
            type: str
      enable_health_check:
        description:
          - Optional. Whether or not this application reports health.
        type: bool
  expand:
    description:
      - The expand expression to apply on the operation.
    type: str
    choices:
      - ReplicationStatus
  state:
    description:
      - Assert the state of the GalleryApplicationVersion.
      - >-
        Use C(present) to create or update an GalleryApplicationVersion and
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
    - name: Create or update a simple gallery Application Version.
      azure_rm_galleryapplicationversion: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Update a simple gallery Application Version.
      azure_rm_galleryapplicationversion: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Delete a gallery Application Version.
      azure_rm_galleryapplicationversion: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

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
publishing_profile:
  description:
    - The publishing profile of a gallery image version.
  returned: always
  type: dict
  sample: null
  contains:
    source:
      description:
        - The source image from which the Image Version is going to be created.
      returned: always
      type: dict
      sample: null
      contains:
        media_link:
          description:
            - >-
              Required. The mediaLink of the artifact, must be a readable
              storage page blob.
          returned: always
          type: str
          sample: null
        default_configuration_link:
          description:
            - >-
              Optional. The defaultConfigurationLink of the artifact, must be a
              readable storage page blob.
          returned: always
          type: str
          sample: null
    manage_actions:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        install:
          description:
            - >-
              Required. The path and arguments to install the gallery
              application. This is limited to 4096 characters.
          returned: always
          type: str
          sample: null
        remove:
          description:
            - >-
              Required. The path and arguments to remove the gallery
              application. This is limited to 4096 characters.
          returned: always
          type: str
          sample: null
        update:
          description:
            - >-
              Optional. The path and arguments to update the gallery
              application. If not present, then update operation will invoke
              remove command on the previous version and install command on the
              current version of the gallery application. This is limited to
              4096 characters.
          returned: always
          type: str
          sample: null
    enable_health_check:
      description:
        - Optional. Whether or not this application reports health.
      returned: always
      type: bool
      sample: null
provisioning_state:
  description:
    - 'The provisioning state, which only appears in the response.'
  returned: always
  type: str
  sample: null
replication_status:
  description:
    - This is the replication status of the gallery image version.
  returned: always
  type: dict
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


class AzureRMGalleryApplicationVersion(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            gallery_name=dict(
                type='str',
                required=True
            ),
            gallery_application_name=dict(
                type='str',
                required=True
            ),
            gallery_application_version_name=dict(
                type='str',
                required=True
            ),
            publishing_profile=dict(
                type='dict',
                disposition='/publishing_profile',
                options=dict(
                    source=dict(
                        type='dict',
                        disposition='source',
                        required=True,
                        options=dict(
                            media_link=dict(
                                type='str',
                                disposition='media_link',
                                required=True
                            ),
                            default_configuration_link=dict(
                                type='str',
                                disposition='default_configuration_link'
                            )
                        )
                    ),
                    manage_actions=dict(
                        type='dict',
                        disposition='manage_actions',
                        options=dict(
                            install=dict(
                                type='str',
                                disposition='install',
                                required=True
                            ),
                            remove=dict(
                                type='str',
                                disposition='remove',
                                required=True
                            ),
                            update=dict(
                                type='str',
                                disposition='update'
                            )
                        )
                    ),
                    enable_health_check=dict(
                        type='bool',
                        disposition='enable_health_check'
                    )
                )
            ),
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.gallery_name = None
        self.gallery_application_name = None
        self.gallery_application_version_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryApplicationVersion, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-09-30')

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
            response = self.mgmt_client.gallery_application_versions.create_or_update(resource_group_name=self.resource_group_name,
                                                                                      gallery_name=self.gallery_name,
                                                                                      gallery_application_name=self.gallery_application_name,
                                                                                      gallery_application_version_name=self.gallery_application_version_name,
                                                                                      gallery_application_version=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryApplicationVersion instance.')
            self.fail('Error creating the GalleryApplicationVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_application_versions.delete(resource_group_name=self.resource_group_name,
                                                                            gallery_name=self.gallery_name,
                                                                            gallery_application_name=self.gallery_application_name,
                                                                            gallery_application_version_name=self.gallery_application_version_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryApplicationVersion instance.')
            self.fail('Error deleting the GalleryApplicationVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gallery_application_versions.get(resource_group_name=self.resource_group_name,
                                                                         gallery_name=self.gallery_name,
                                                                         gallery_application_name=self.gallery_application_name,
                                                                         gallery_application_version_name=self.gallery_application_version_name,
                                                                         expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryApplicationVersion()


if __name__ == '__main__':
    main()
