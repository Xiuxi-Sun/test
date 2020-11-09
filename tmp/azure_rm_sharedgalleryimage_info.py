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
module: azure_rm_sharedgalleryimage_info
version_added: '2.9'
short_description: Get SharedGalleryImage info.
description:
  - Get info of SharedGalleryImage.
options:
  location:
    description:
      - Resource location.
    required: true
    type: str
  gallery_unique_name:
    description:
      - The unique name of the Shared Gallery.
    required: true
    type: str
  shared_to:
    description:
      - >-
        The query parameter to decide what shared galleries to fetch when doing
        listing operations.
    type: str
    choices:
      - tenant
  gallery_image_name:
    description:
      - >-
        The name of the Shared Gallery Image Definition from which the Image
        Versions are to be listed.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery.
      azure_rm_sharedgalleryimage_info: 
        gallery_unique_name: galleryUniqueName
        location: myLocation
        

'''

RETURN = '''
shared_gallery_images:
  description: >-
    A list of dict results where the key is the name of the SharedGalleryImage
    and the values are the facts for that SharedGalleryImage.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of shared gallery images.
      returned: always
      type: list
      sample: null
      contains:
        os_type:
          description:
            - >-
              This property allows you to specify the type of the OS that is
              included in the disk when creating a VM from a managed image.
              :code:`<br>`:code:`<br>` Possible values are:
              :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
              **Linux**
          returned: always
          type: sealed-choice
          sample: null
        os_state:
          description:
            - >-
              This property allows the user to specify whether the virtual
              machines created under this image are 'Generalized' or
              'Specialized'.
          returned: always
          type: sealed-choice
          sample: null
        end_of_life_date:
          description:
            - >-
              The end of life date of the gallery image definition. This
              property can be used for decommissioning purposes. This property
              is updatable.
          returned: always
          type: str
          sample: null
        identifier:
          description:
            - This is the gallery image definition identifier.
          returned: always
          type: dict
          sample: null
          contains:
            publisher:
              description:
                - The name of the gallery image definition publisher.
              returned: always
              type: str
              sample: null
            offer:
              description:
                - The name of the gallery image definition offer.
              returned: always
              type: str
              sample: null
            sku:
              description:
                - The name of the gallery image definition SKU.
              returned: always
              type: str
              sample: null
        recommended:
          description:
            - >-
              The properties describe the recommended machine configuration for
              this Image Definition. These properties are updatable.
          returned: always
          type: dict
          sample: null
          contains:
            v_cp_us:
              description:
                - Describes the resource range.
              returned: always
              type: dict
              sample: null
              contains:
                min:
                  description:
                    - The minimum number of the resource.
                  returned: always
                  type: integer
                  sample: null
                max:
                  description:
                    - The maximum number of the resource.
                  returned: always
                  type: integer
                  sample: null
            memory:
              description:
                - Describes the resource range.
              returned: always
              type: dict
              sample: null
              contains:
                min:
                  description:
                    - The minimum number of the resource.
                  returned: always
                  type: integer
                  sample: null
                max:
                  description:
                    - The maximum number of the resource.
                  returned: always
                  type: integer
                  sample: null
        disallowed:
          description:
            - Describes the disallowed disk types.
          returned: always
          type: dict
          sample: null
          contains:
            disk_types:
              description:
                - A list of disk types.
              returned: always
              type: list
              sample: null
        hyper_v_generation:
          description:
            - >-
              The hypervisor generation of the Virtual Machine. Applicable to OS
              disks only.
          returned: always
          type: str
          sample: null
        features:
          description:
            - A list of gallery image features.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The name of the gallery image feature.
              returned: always
              type: str
              sample: null
            value:
              description:
                - The value of the gallery image feature.
              returned: always
              type: str
              sample: null
        purchase_plan:
          description:
            - >-
              Describes the gallery image definition purchase plan. This is used
              by marketplace images.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The plan ID.
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - The publisher ID.
              returned: always
              type: str
              sample: null
            product:
              description:
                - The product ID.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of shared gallery images. Call
          ListNext() with this to fetch the next page of shared gallery images.
      returned: always
      type: str
      sample: null
    unique_id:
      description:
        - The unique id of this shared gallery.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - >-
          This property allows you to specify the type of the OS that is
          included in the disk when creating a VM from a managed image.
          :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
          **Windows** :code:`<br>`:code:`<br>` **Linux**
      returned: always
      type: sealed-choice
      sample: null
    os_state:
      description:
        - >-
          This property allows the user to specify whether the virtual machines
          created under this image are 'Generalized' or 'Specialized'.
      returned: always
      type: sealed-choice
      sample: null
    end_of_life_date:
      description:
        - >-
          The end of life date of the gallery image definition. This property
          can be used for decommissioning purposes. This property is updatable.
      returned: always
      type: str
      sample: null
    identifier:
      description:
        - This is the gallery image definition identifier.
      returned: always
      type: dict
      sample: null
      contains:
        publisher:
          description:
            - The name of the gallery image definition publisher.
          returned: always
          type: str
          sample: null
        offer:
          description:
            - The name of the gallery image definition offer.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - The name of the gallery image definition SKU.
          returned: always
          type: str
          sample: null
    recommended:
      description:
        - >-
          The properties describe the recommended machine configuration for this
          Image Definition. These properties are updatable.
      returned: always
      type: dict
      sample: null
      contains:
        v_cp_us:
          description:
            - Describes the resource range.
          returned: always
          type: dict
          sample: null
          contains:
            min:
              description:
                - The minimum number of the resource.
              returned: always
              type: integer
              sample: null
            max:
              description:
                - The maximum number of the resource.
              returned: always
              type: integer
              sample: null
        memory:
          description:
            - Describes the resource range.
          returned: always
          type: dict
          sample: null
          contains:
            min:
              description:
                - The minimum number of the resource.
              returned: always
              type: integer
              sample: null
            max:
              description:
                - The maximum number of the resource.
              returned: always
              type: integer
              sample: null
    disallowed:
      description:
        - Describes the disallowed disk types.
      returned: always
      type: dict
      sample: null
      contains:
        disk_types:
          description:
            - A list of disk types.
          returned: always
          type: list
          sample: null
    hyper_v_generation:
      description:
        - >-
          The hypervisor generation of the Virtual Machine. Applicable to OS
          disks only.
      returned: always
      type: str
      sample: null
    features:
      description:
        - A list of gallery image features.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the gallery image feature.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The value of the gallery image feature.
          returned: always
          type: str
          sample: null
    purchase_plan:
      description:
        - >-
          Describes the gallery image definition purchase plan. This is used by
          marketplace images.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The plan ID.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The publisher ID.
          returned: always
          type: str
          sample: null
        product:
          description:
            - The product ID.
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


class AzureRMSharedGalleryImageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            gallery_unique_name=dict(
                type='str',
                required=True
            ),
            shared_to=dict(
                type='str',
                choices=['tenant']
            ),
            gallery_image_name=dict(
                type='str'
            )
        )

        self.location = None
        self.gallery_unique_name = None
        self.shared_to = None
        self.gallery_image_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSharedGalleryImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-30')

        if (self.location is not None and
            self.gallery_unique_name is not None and
            self.gallery_image_name is not None):
            self.results['shared_gallery_images'] = self.format_item(self.get())
        elif (self.location is not None and
              self.gallery_unique_name is not None):
            self.results['shared_gallery_images'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.shared_gallery_images.get(location=self.location,
                                                                  gallery_unique_name=self.gallery_unique_name,
                                                                  gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.shared_gallery_images.list(location=self.location,
                                                                   gallery_unique_name=self.gallery_unique_name,
                                                                   shared_to=self.shared_to)
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
    AzureRMSharedGalleryImageInfo()


if __name__ == '__main__':
    main()
