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
module: azure_rm_vpnsite
version_added: '2.9'
short_description: Manage Azure VpnSite instance.
description:
  - 'Create, update and delete instance of Azure VpnSite.'
options:
  resource_group_name:
    description:
      - The resource group name of the VpnSite.
    required: true
    type: str
  vpn_site_name:
    description:
      - The name of the VpnSite being retrieved.
      - The name of the VpnSite being created or updated.
      - The name of the VpnSite being deleted.
    required: true
    type: str
  virtual_wan:
    description:
      - The VirtualWAN to which the vpnSite belongs.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  device_properties:
    description:
      - The device properties.
    type: dict
    suboptions:
      device_vendor:
        description:
          - Name of the device Vendor.
        type: str
      device_model:
        description:
          - Model of the device.
        type: str
      link_speed_in_mbps:
        description:
          - Link speed.
        type: integer
  ip_address:
    description:
      - The ip-address for the vpn-site.
    type: str
  site_key:
    description:
      - The key for vpn-site that can be used for connections.
    type: str
  address_space:
    description:
      - The AddressSpace that contains an array of IP address ranges.
    type: dict
    suboptions:
      address_prefixes:
        description:
          - >-
            A list of address blocks reserved for this virtual network in CIDR
            notation.
        type: list
  bgp_properties:
    description:
      - The set of bgp properties.
    type: dict
    suboptions:
      asn:
        description:
          - The BGP speaker's ASN.
        type: integer
      bgp_peering_address:
        description:
          - The BGP peering address and BGP identifier of this BGP speaker.
        type: str
      peer_weight:
        description:
          - The weight added to routes learned from this BGP speaker.
        type: integer
      bgp_peering_addresses:
        description:
          - >-
            BGP peering address with IP configuration ID for virtual network
            gateway.
        type: list
        suboptions:
          ipconfiguration_id:
            description:
              - The ID of IP configuration which belongs to gateway.
            type: str
          default_bgp_ip_addresses:
            description:
              - >-
                The list of default BGP peering addresses which belong to IP
                configuration.
            type: list
          custom_bgp_ip_addresses:
            description:
              - >-
                The list of custom BGP peering addresses which belong to IP
                configuration.
            type: list
          tunnel_ip_addresses:
            description:
              - >-
                The list of tunnel public IP addresses which belong to IP
                configuration.
            type: list
  is_security_site:
    description:
      - IsSecuritySite flag.
    type: bool
  vpn_site_links:
    description:
      - List of all vpn site links.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      link_properties:
        description:
          - The link provider properties.
        type: dict
        suboptions:
          link_provider_name:
            description:
              - Name of the link provider.
            type: str
          link_speed_in_mbps:
            description:
              - Link speed.
            type: integer
      ip_address:
        description:
          - The ip-address for the vpn-site-link.
        type: str
      fqdn:
        description:
          - FQDN of vpn-site-link.
        type: str
      bgp_properties:
        description:
          - The set of bgp properties.
        type: dict
        suboptions:
          asn:
            description:
              - The BGP speaker's ASN.
            type: integer
          bgp_peering_address:
            description:
              - The BGP peering address and BGP identifier of this BGP speaker.
            type: str
  o365_policy:
    description:
      - Office365 Policy.
    type: dict
    suboptions:
      break_out_categories:
        description:
          - Office365 breakout categories.
        type: dict
        suboptions:
          allow:
            description:
              - Flag to control allow category.
            type: bool
          optimize:
            description:
              - Flag to control optimize category.
            type: bool
          default:
            description:
              - Flag to control default category.
            type: bool
  state:
    description:
      - Assert the state of the VpnSite.
      - >-
        Use C(present) to create or update an VpnSite and C(absent) to delete
        it.
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
    - name: VpnSiteCreate
      azure_rm_vpnsite: 
        resource_group_name: rg1
        vpn_site_name: vpnSite1
        

    - name: VpnSiteDelete
      azure_rm_vpnsite: 
        resource_group_name: rg1
        vpn_site_name: vpnSite1
        

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
virtual_wan:
  description:
    - The VirtualWAN to which the vpnSite belongs.
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
device_properties:
  description:
    - The device properties.
  returned: always
  type: dict
  sample: null
  contains:
    device_vendor:
      description:
        - Name of the device Vendor.
      returned: always
      type: str
      sample: null
    device_model:
      description:
        - Model of the device.
      returned: always
      type: str
      sample: null
    link_speed_in_mbps:
      description:
        - Link speed.
      returned: always
      type: integer
      sample: null
ip_address:
  description:
    - The ip-address for the vpn-site.
  returned: always
  type: str
  sample: null
site_key:
  description:
    - The key for vpn-site that can be used for connections.
  returned: always
  type: str
  sample: null
address_space:
  description:
    - The AddressSpace that contains an array of IP address ranges.
  returned: always
  type: dict
  sample: null
  contains:
    address_prefixes:
      description:
        - >-
          A list of address blocks reserved for this virtual network in CIDR
          notation.
      returned: always
      type: list
      sample: null
bgp_properties:
  description:
    - The set of bgp properties.
  returned: always
  type: dict
  sample: null
  contains:
    asn:
      description:
        - The BGP speaker's ASN.
      returned: always
      type: integer
      sample: null
    bgp_peering_address:
      description:
        - The BGP peering address and BGP identifier of this BGP speaker.
      returned: always
      type: str
      sample: null
    peer_weight:
      description:
        - The weight added to routes learned from this BGP speaker.
      returned: always
      type: integer
      sample: null
    bgp_peering_addresses:
      description:
        - >-
          BGP peering address with IP configuration ID for virtual network
          gateway.
      returned: always
      type: list
      sample: null
      contains:
        ipconfiguration_id:
          description:
            - The ID of IP configuration which belongs to gateway.
          returned: always
          type: str
          sample: null
        default_bgp_ip_addresses:
          description:
            - >-
              The list of default BGP peering addresses which belong to IP
              configuration.
          returned: always
          type: list
          sample: null
        custom_bgp_ip_addresses:
          description:
            - >-
              The list of custom BGP peering addresses which belong to IP
              configuration.
          returned: always
          type: list
          sample: null
        tunnel_ip_addresses:
          description:
            - >-
              The list of tunnel public IP addresses which belong to IP
              configuration.
          returned: always
          type: list
          sample: null
provisioning_state:
  description:
    - The provisioning state of the VPN site resource.
  returned: always
  type: str
  sample: null
is_security_site:
  description:
    - IsSecuritySite flag.
  returned: always
  type: bool
  sample: null
vpn_site_links:
  description:
    - List of all vpn site links.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
      returned: always
      type: str
      sample: null
    link_properties:
      description:
        - The link provider properties.
      returned: always
      type: dict
      sample: null
      contains:
        link_provider_name:
          description:
            - Name of the link provider.
          returned: always
          type: str
          sample: null
        link_speed_in_mbps:
          description:
            - Link speed.
          returned: always
          type: integer
          sample: null
    ip_address:
      description:
        - The ip-address for the vpn-site-link.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - FQDN of vpn-site-link.
      returned: always
      type: str
      sample: null
    bgp_properties:
      description:
        - The set of bgp properties.
      returned: always
      type: dict
      sample: null
      contains:
        asn:
          description:
            - The BGP speaker's ASN.
          returned: always
          type: integer
          sample: null
        bgp_peering_address:
          description:
            - The BGP peering address and BGP identifier of this BGP speaker.
          returned: always
          type: str
          sample: null
o365_policy:
  description:
    - Office365 Policy.
  returned: always
  type: dict
  sample: null
  contains:
    break_out_categories:
      description:
        - Office365 breakout categories.
      returned: always
      type: dict
      sample: null
      contains:
        allow:
          description:
            - Flag to control allow category.
          returned: always
          type: bool
          sample: null
        optimize:
          description:
            - Flag to control optimize category.
          returned: always
          type: bool
          sample: null
        default:
          description:
            - Flag to control default category.
          returned: always
          type: bool
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


class AzureRMVpnSite(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vpn_site_name=dict(
                type='str',
                required=True
            ),
            virtual_wan=dict(
                type='dict',
                disposition='/virtual_wan',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            device_properties=dict(
                type='dict',
                disposition='/device_properties',
                options=dict(
                    device_vendor=dict(
                        type='str',
                        disposition='device_vendor'
                    ),
                    device_model=dict(
                        type='str',
                        disposition='device_model'
                    ),
                    link_speed_in_mbps=dict(
                        type='integer',
                        disposition='link_speed_in_mbps'
                    )
                )
            ),
            ip_address=dict(
                type='str',
                disposition='/ip_address'
            ),
            site_key=dict(
                type='str',
                disposition='/site_key'
            ),
            address_space=dict(
                type='dict',
                disposition='/address_space',
                options=dict(
                    address_prefixes=dict(
                        type='list',
                        disposition='address_prefixes',
                        elements='str'
                    )
                )
            ),
            bgp_properties=dict(
                type='dict',
                disposition='/bgp_properties',
                options=dict(
                    asn=dict(
                        type='integer',
                        disposition='asn'
                    ),
                    bgp_peering_address=dict(
                        type='str',
                        disposition='bgp_peering_address'
                    ),
                    peer_weight=dict(
                        type='integer',
                        disposition='peer_weight'
                    ),
                    bgp_peering_addresses=dict(
                        type='list',
                        disposition='bgp_peering_addresses',
                        elements='dict',
                        options=dict(
                            ipconfiguration_id=dict(
                                type='str',
                                disposition='ipconfiguration_id'
                            ),
                            default_bgp_ip_addresses=dict(
                                type='list',
                                updatable=False,
                                disposition='default_bgp_ip_addresses',
                                elements='str'
                            ),
                            custom_bgp_ip_addresses=dict(
                                type='list',
                                disposition='custom_bgp_ip_addresses',
                                elements='str'
                            ),
                            tunnel_ip_addresses=dict(
                                type='list',
                                updatable=False,
                                disposition='tunnel_ip_addresses',
                                elements='str'
                            )
                        )
                    )
                )
            ),
            is_security_site=dict(
                type='bool',
                disposition='/is_security_site'
            ),
            vpn_site_links=dict(
                type='list',
                disposition='/vpn_site_links',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    link_properties=dict(
                        type='dict',
                        disposition='link_properties',
                        options=dict(
                            link_provider_name=dict(
                                type='str',
                                disposition='link_provider_name'
                            ),
                            link_speed_in_mbps=dict(
                                type='integer',
                                disposition='link_speed_in_mbps'
                            )
                        )
                    ),
                    ip_address=dict(
                        type='str',
                        disposition='ip_address'
                    ),
                    fqdn=dict(
                        type='str',
                        disposition='fqdn'
                    ),
                    bgp_properties=dict(
                        type='dict',
                        disposition='bgp_properties',
                        options=dict(
                            asn=dict(
                                type='integer',
                                disposition='asn'
                            ),
                            bgp_peering_address=dict(
                                type='str',
                                disposition='bgp_peering_address'
                            )
                        )
                    )
                )
            ),
            o365_policy=dict(
                type='dict',
                disposition='/o365_policy',
                options=dict(
                    break_out_categories=dict(
                        type='dict',
                        disposition='break_out_categories',
                        options=dict(
                            allow=dict(
                                type='bool',
                                disposition='allow'
                            ),
                            optimize=dict(
                                type='bool',
                                disposition='optimize'
                            ),
                            default=dict(
                                type='bool',
                                disposition='default'
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

        self.resource_group_name = None
        self.vpn_site_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVpnSite, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.vpn_sites.create_or_update(resource_group_name=self.resource_group_name,
                                                                   vpn_site_name=self.vpn_site_name,
                                                                   vpn_site_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VpnSite instance.')
            self.fail('Error creating the VpnSite instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vpn_sites.delete(resource_group_name=self.resource_group_name,
                                                         vpn_site_name=self.vpn_site_name)
        except CloudError as e:
            self.log('Error attempting to delete the VpnSite instance.')
            self.fail('Error deleting the VpnSite instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vpn_sites.get(resource_group_name=self.resource_group_name,
                                                      vpn_site_name=self.vpn_site_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVpnSite()


if __name__ == '__main__':
    main()
