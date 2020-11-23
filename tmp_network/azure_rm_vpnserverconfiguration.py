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
module: azure_rm_vpnserverconfiguration
version_added: '2.9'
short_description: Manage Azure VpnServerConfiguration instance.
description:
  - 'Create, update and delete instance of Azure VpnServerConfiguration.'
options:
  resource_group_name:
    description:
      - The resource group name of the VpnServerConfiguration.
    required: true
    type: str
  vpn_server_configuration_name:
    description:
      - The name of the VpnServerConfiguration being retrieved.
      - The name of the VpnServerConfiguration being created or updated.
      - The name of the VpnServerConfiguration being deleted.
    required: true
    type: str
  name_properties_name:
    description:
      - >-
        The name of the VpnServerConfiguration that is unique within a resource
        group.
    type: str
  vpn_protocols:
    description:
      - VPN protocols for the VpnServerConfiguration.
    type: list
  vpn_authentication_types:
    description:
      - VPN authentication types for the VpnServerConfiguration.
    type: list
  vpn_client_root_certificates:
    description:
      - VPN client root certificate of VpnServerConfiguration.
    type: list
    suboptions:
      name:
        description:
          - The certificate name.
        type: str
      public_cert_data:
        description:
          - The certificate public data.
        type: str
  vpn_client_revoked_certificates:
    description:
      - VPN client revoked certificate of VpnServerConfiguration.
    type: list
    suboptions:
      name:
        description:
          - The certificate name.
        type: str
      thumbprint:
        description:
          - The revoked VPN client certificate thumbprint.
        type: str
  radius_server_root_certificates:
    description:
      - Radius Server root certificate of VpnServerConfiguration.
    type: list
    suboptions:
      name:
        description:
          - The certificate name.
        type: str
      public_cert_data:
        description:
          - The certificate public data.
        type: str
  radius_client_root_certificates:
    description:
      - Radius client root certificate of VpnServerConfiguration.
    type: list
    suboptions:
      name:
        description:
          - The certificate name.
        type: str
      thumbprint:
        description:
          - The Radius client root certificate thumbprint.
        type: str
  vpn_client_ipsec_policies:
    description:
      - VpnClientIpsecPolicies for VpnServerConfiguration.
    type: list
    suboptions:
      sa_life_time_seconds:
        description:
          - >-
            The IPSec Security Association (also called Quick Mode or Phase 2
            SA) lifetime in seconds for a site to site VPN tunnel.
        required: true
        type: integer
      sa_data_size_kilobytes:
        description:
          - >-
            The IPSec Security Association (also called Quick Mode or Phase 2
            SA) payload size in KB for a site to site VPN tunnel.
        required: true
        type: integer
      ipsec_encryption:
        description:
          - The IPSec encryption algorithm (IKE phase 1).
        required: true
        type: str
        choices:
          - None
          - DES
          - DES3
          - AES128
          - AES192
          - AES256
          - GCMAES128
          - GCMAES192
          - GCMAES256
      ipsec_integrity:
        description:
          - The IPSec integrity algorithm (IKE phase 1).
        required: true
        type: str
        choices:
          - MD5
          - SHA1
          - SHA256
          - GCMAES128
          - GCMAES192
          - GCMAES256
      ike_encryption:
        description:
          - The IKE encryption algorithm (IKE phase 2).
        required: true
        type: str
        choices:
          - DES
          - DES3
          - AES128
          - AES192
          - AES256
          - GCMAES256
          - GCMAES128
      ike_integrity:
        description:
          - The IKE integrity algorithm (IKE phase 2).
        required: true
        type: str
        choices:
          - MD5
          - SHA1
          - SHA256
          - SHA384
          - GCMAES256
          - GCMAES128
      dh_group:
        description:
          - The DH Group used in IKE Phase 1 for initial SA.
        required: true
        type: str
        choices:
          - None
          - DHGroup1
          - DHGroup2
          - DHGroup14
          - DHGroup2048
          - ECP256
          - ECP384
          - DHGroup24
      pfs_group:
        description:
          - The Pfs Group used in IKE Phase 2 for new child SA.
        required: true
        type: str
        choices:
          - None
          - PFS1
          - PFS2
          - PFS2048
          - ECP256
          - ECP384
          - PFS24
          - PFS14
          - PFSMM
  radius_server_address:
    description:
      - >-
        The radius server address property of the VpnServerConfiguration
        resource for point to site client connection.
    type: str
  radius_server_secret:
    description:
      - >-
        The radius secret property of the VpnServerConfiguration resource for
        point to site client connection.
    type: str
  radius_servers:
    description:
      - Multiple Radius Server configuration for VpnServerConfiguration.
    type: list
    suboptions:
      radius_server_address:
        description:
          - The address of this radius server.
        required: true
        type: str
      radius_server_score:
        description:
          - The initial score assigned to this radius server.
        type: integer
      radius_server_secret:
        description:
          - The secret used for this radius server.
        type: str
  aad_authentication_parameters:
    description:
      - The set of aad vpn authentication parameters.
    type: dict
    suboptions:
      aad_tenant:
        description:
          - AAD Vpn authentication parameter AAD tenant.
        type: str
      aad_audience:
        description:
          - AAD Vpn authentication parameter AAD audience.
        type: str
      aad_issuer:
        description:
          - AAD Vpn authentication parameter AAD issuer.
        type: str
  p2_s_vpn_gateways:
    description:
      - List of references to P2SVpnGateways.
    type: list
    suboptions:
      virtual_hub:
        description:
          - The VirtualHub to which the gateway belongs.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      p2_s_connection_configurations:
        description:
          - List of all p2s connection configurations of the gateway.
        type: list
        suboptions:
          name:
            description:
              - >-
                The name of the resource that is unique within a resource group.
                This name can be used to access the resource.
            type: str
          vpn_client_address_pool:
            description:
              - >-
                The reference to the address space resource which represents
                Address space for P2S VpnClient.
            type: dict
            suboptions:
              address_prefixes:
                description:
                  - >-
                    A list of address blocks reserved for this virtual network
                    in CIDR notation.
                type: list
          routing_configuration:
            description:
              - >-
                The Routing Configuration indicating the associated and
                propagated route tables on this connection.
            type: dict
            suboptions:
              associated_route_table:
                description:
                  - >-
                    The resource id RouteTable associated with this
                    RoutingConfiguration.
                type: dict
                suboptions:
                  id:
                    description:
                      - Resource ID.
                    type: str
              propagated_route_tables:
                description:
                  - The list of RouteTables to advertise the routes to.
                type: dict
                suboptions:
                  labels:
                    description:
                      - The list of labels.
                    type: list
                  ids:
                    description:
                      - The list of resource ids of all the RouteTables.
                    type: list
                    suboptions:
                      id:
                        description:
                          - Resource ID.
                        type: str
              vnet_routes:
                description:
                  - >-
                    List of routes that control routing from VirtualHub into a
                    virtual network connection.
                type: dict
                suboptions:
                  static_routes:
                    description:
                      - List of all Static Routes.
                    type: list
                    suboptions:
                      name:
                        description:
                          - >-
                            The name of the StaticRoute that is unique within a
                            VnetRoute.
                        type: str
                      address_prefixes:
                        description:
                          - List of all address prefixes.
                        type: list
                      next_hop_ip_address:
                        description:
                          - The ip address of the next hop.
                        type: str
          enable_internet_security:
            description:
              - >-
                Flag indicating whether the enable internet security flag is
                turned on for the P2S Connections or not.
            type: bool
      vpn_gateway_scale_unit:
        description:
          - The scale unit for this p2s vpn gateway.
        type: integer
      vpn_server_configuration:
        description:
          - >-
            The VpnServerConfiguration to which the p2sVpnGateway is attached
            to.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      vpn_client_connection_health:
        description:
          - All P2S VPN clients' connection health status.
        type: dict
        suboptions:
          vpn_client_connections_count:
            description:
              - >-
                The total of p2s vpn clients connected at this time to this
                P2SVpnGateway.
            type: integer
          allocated_ip_addresses:
            description:
              - List of allocated ip addresses to the connected p2s vpn clients.
            type: list
      custom_dns_servers:
        description:
          - List of all customer specified DNS servers IP addresses.
        type: list
  state:
    description:
      - Assert the state of the VpnServerConfiguration.
      - >-
        Use C(present) to create or update an VpnServerConfiguration and
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
    - name: VpnServerConfigurationCreate
      azure_rm_vpnserverconfiguration: 
        resource_group_name: rg1
        vpn_server_configuration_name: vpnServerConfiguration1
        

    - name: VpnServerConfigurationDelete
      azure_rm_vpnserverconfiguration: 
        resource_group_name: rg1
        vpn_server_configuration_name: vpnServerConfiguration1
        

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
name_properties_name:
  description:
    - >-
      The name of the VpnServerConfiguration that is unique within a resource
      group.
  returned: always
  type: str
  sample: null
vpn_protocols:
  description:
    - VPN protocols for the VpnServerConfiguration.
  returned: always
  type: list
  sample: null
vpn_authentication_types:
  description:
    - VPN authentication types for the VpnServerConfiguration.
  returned: always
  type: list
  sample: null
vpn_client_root_certificates:
  description:
    - VPN client root certificate of VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The certificate name.
      returned: always
      type: str
      sample: null
    public_cert_data:
      description:
        - The certificate public data.
      returned: always
      type: str
      sample: null
vpn_client_revoked_certificates:
  description:
    - VPN client revoked certificate of VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The certificate name.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - The revoked VPN client certificate thumbprint.
      returned: always
      type: str
      sample: null
radius_server_root_certificates:
  description:
    - Radius Server root certificate of VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The certificate name.
      returned: always
      type: str
      sample: null
    public_cert_data:
      description:
        - The certificate public data.
      returned: always
      type: str
      sample: null
radius_client_root_certificates:
  description:
    - Radius client root certificate of VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The certificate name.
      returned: always
      type: str
      sample: null
    thumbprint:
      description:
        - The Radius client root certificate thumbprint.
      returned: always
      type: str
      sample: null
vpn_client_ipsec_policies:
  description:
    - VpnClientIpsecPolicies for VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    sa_life_time_seconds:
      description:
        - >-
          The IPSec Security Association (also called Quick Mode or Phase 2 SA)
          lifetime in seconds for a site to site VPN tunnel.
      returned: always
      type: integer
      sample: null
    sa_data_size_kilobytes:
      description:
        - >-
          The IPSec Security Association (also called Quick Mode or Phase 2 SA)
          payload size in KB for a site to site VPN tunnel.
      returned: always
      type: integer
      sample: null
    ipsec_encryption:
      description:
        - The IPSec encryption algorithm (IKE phase 1).
      returned: always
      type: str
      sample: null
    ipsec_integrity:
      description:
        - The IPSec integrity algorithm (IKE phase 1).
      returned: always
      type: str
      sample: null
    ike_encryption:
      description:
        - The IKE encryption algorithm (IKE phase 2).
      returned: always
      type: str
      sample: null
    ike_integrity:
      description:
        - The IKE integrity algorithm (IKE phase 2).
      returned: always
      type: str
      sample: null
    dh_group:
      description:
        - The DH Group used in IKE Phase 1 for initial SA.
      returned: always
      type: str
      sample: null
    pfs_group:
      description:
        - The Pfs Group used in IKE Phase 2 for new child SA.
      returned: always
      type: str
      sample: null
radius_server_address:
  description:
    - >-
      The radius server address property of the VpnServerConfiguration resource
      for point to site client connection.
  returned: always
  type: str
  sample: null
radius_server_secret:
  description:
    - >-
      The radius secret property of the VpnServerConfiguration resource for
      point to site client connection.
  returned: always
  type: str
  sample: null
radius_servers:
  description:
    - Multiple Radius Server configuration for VpnServerConfiguration.
  returned: always
  type: list
  sample: null
  contains:
    radius_server_address:
      description:
        - The address of this radius server.
      returned: always
      type: str
      sample: null
    radius_server_score:
      description:
        - The initial score assigned to this radius server.
      returned: always
      type: integer
      sample: null
    radius_server_secret:
      description:
        - The secret used for this radius server.
      returned: always
      type: str
      sample: null
aad_authentication_parameters:
  description:
    - The set of aad vpn authentication parameters.
  returned: always
  type: dict
  sample: null
  contains:
    aad_tenant:
      description:
        - AAD Vpn authentication parameter AAD tenant.
      returned: always
      type: str
      sample: null
    aad_audience:
      description:
        - AAD Vpn authentication parameter AAD audience.
      returned: always
      type: str
      sample: null
    aad_issuer:
      description:
        - AAD Vpn authentication parameter AAD issuer.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - >-
      The provisioning state of the VpnServerConfiguration resource. Possible
      values are: 'Updating', 'Deleting', and 'Failed'.
  returned: always
  type: str
  sample: null
p2_s_vpn_gateways:
  description:
    - List of references to P2SVpnGateways.
  returned: always
  type: list
  sample: null
  contains:
    virtual_hub:
      description:
        - The VirtualHub to which the gateway belongs.
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
    p2_s_connection_configurations:
      description:
        - List of all p2s connection configurations of the gateway.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        vpn_client_address_pool:
          description:
            - >-
              The reference to the address space resource which represents
              Address space for P2S VpnClient.
          returned: always
          type: dict
          sample: null
          contains:
            address_prefixes:
              description:
                - >-
                  A list of address blocks reserved for this virtual network in
                  CIDR notation.
              returned: always
              type: list
              sample: null
        routing_configuration:
          description:
            - >-
              The Routing Configuration indicating the associated and propagated
              route tables on this connection.
          returned: always
          type: dict
          sample: null
          contains:
            associated_route_table:
              description:
                - >-
                  The resource id RouteTable associated with this
                  RoutingConfiguration.
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
            propagated_route_tables:
              description:
                - The list of RouteTables to advertise the routes to.
              returned: always
              type: dict
              sample: null
              contains:
                labels:
                  description:
                    - The list of labels.
                  returned: always
                  type: list
                  sample: null
                ids:
                  description:
                    - The list of resource ids of all the RouteTables.
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
            vnet_routes:
              description:
                - >-
                  List of routes that control routing from VirtualHub into a
                  virtual network connection.
              returned: always
              type: dict
              sample: null
              contains:
                static_routes:
                  description:
                    - List of all Static Routes.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - >-
                          The name of the StaticRoute that is unique within a
                          VnetRoute.
                      returned: always
                      type: str
                      sample: null
                    address_prefixes:
                      description:
                        - List of all address prefixes.
                      returned: always
                      type: list
                      sample: null
                    next_hop_ip_address:
                      description:
                        - The ip address of the next hop.
                      returned: always
                      type: str
                      sample: null
        enable_internet_security:
          description:
            - >-
              Flag indicating whether the enable internet security flag is
              turned on for the P2S Connections or not.
          returned: always
          type: bool
          sample: null
    vpn_gateway_scale_unit:
      description:
        - The scale unit for this p2s vpn gateway.
      returned: always
      type: integer
      sample: null
    vpn_server_configuration:
      description:
        - The VpnServerConfiguration to which the p2sVpnGateway is attached to.
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
    vpn_client_connection_health:
      description:
        - All P2S VPN clients' connection health status.
      returned: always
      type: dict
      sample: null
      contains:
        vpn_client_connections_count:
          description:
            - >-
              The total of p2s vpn clients connected at this time to this
              P2SVpnGateway.
          returned: always
          type: integer
          sample: null
        allocated_ip_addresses:
          description:
            - List of allocated ip addresses to the connected p2s vpn clients.
          returned: always
          type: list
          sample: null
    custom_dns_servers:
      description:
        - List of all customer specified DNS servers IP addresses.
      returned: always
      type: list
      sample: null
etag_properties_etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
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


class AzureRMVpnServerConfiguration(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vpn_server_configuration_name=dict(
                type='str',
                required=True
            ),
            name_properties_name=dict(
                type='str',
                disposition='/name_properties_name'
            ),
            vpn_protocols=dict(
                type='list',
                disposition='/vpn_protocols',
                elements='str'
            ),
            vpn_authentication_types=dict(
                type='list',
                disposition='/vpn_authentication_types',
                elements='str'
            ),
            vpn_client_root_certificates=dict(
                type='list',
                disposition='/vpn_client_root_certificates',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    public_cert_data=dict(
                        type='str',
                        disposition='public_cert_data'
                    )
                )
            ),
            vpn_client_revoked_certificates=dict(
                type='list',
                disposition='/vpn_client_revoked_certificates',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    thumbprint=dict(
                        type='str',
                        disposition='thumbprint'
                    )
                )
            ),
            radius_server_root_certificates=dict(
                type='list',
                disposition='/radius_server_root_certificates',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    public_cert_data=dict(
                        type='str',
                        disposition='public_cert_data'
                    )
                )
            ),
            radius_client_root_certificates=dict(
                type='list',
                disposition='/radius_client_root_certificates',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    thumbprint=dict(
                        type='str',
                        disposition='thumbprint'
                    )
                )
            ),
            vpn_client_ipsec_policies=dict(
                type='list',
                disposition='/vpn_client_ipsec_policies',
                elements='dict',
                options=dict(
                    sa_life_time_seconds=dict(
                        type='integer',
                        disposition='sa_life_time_seconds',
                        required=True
                    ),
                    sa_data_size_kilobytes=dict(
                        type='integer',
                        disposition='sa_data_size_kilobytes',
                        required=True
                    ),
                    ipsec_encryption=dict(
                        type='str',
                        disposition='ipsec_encryption',
                        choices=['None',
                                 'DES',
                                 'DES3',
                                 'AES128',
                                 'AES192',
                                 'AES256',
                                 'GCMAES128',
                                 'GCMAES192',
                                 'GCMAES256'],
                        required=True
                    ),
                    ipsec_integrity=dict(
                        type='str',
                        disposition='ipsec_integrity',
                        choices=['MD5',
                                 'SHA1',
                                 'SHA256',
                                 'GCMAES128',
                                 'GCMAES192',
                                 'GCMAES256'],
                        required=True
                    ),
                    ike_encryption=dict(
                        type='str',
                        disposition='ike_encryption',
                        choices=['DES',
                                 'DES3',
                                 'AES128',
                                 'AES192',
                                 'AES256',
                                 'GCMAES256',
                                 'GCMAES128'],
                        required=True
                    ),
                    ike_integrity=dict(
                        type='str',
                        disposition='ike_integrity',
                        choices=['MD5',
                                 'SHA1',
                                 'SHA256',
                                 'SHA384',
                                 'GCMAES256',
                                 'GCMAES128'],
                        required=True
                    ),
                    dh_group=dict(
                        type='str',
                        disposition='dh_group',
                        choices=['None',
                                 'DHGroup1',
                                 'DHGroup2',
                                 'DHGroup14',
                                 'DHGroup2048',
                                 'ECP256',
                                 'ECP384',
                                 'DHGroup24'],
                        required=True
                    ),
                    pfs_group=dict(
                        type='str',
                        disposition='pfs_group',
                        choices=['None',
                                 'PFS1',
                                 'PFS2',
                                 'PFS2048',
                                 'ECP256',
                                 'ECP384',
                                 'PFS24',
                                 'PFS14',
                                 'PFSMM'],
                        required=True
                    )
                )
            ),
            radius_server_address=dict(
                type='str',
                disposition='/radius_server_address'
            ),
            radius_server_secret=dict(
                type='str',
                disposition='/radius_server_secret'
            ),
            radius_servers=dict(
                type='list',
                disposition='/radius_servers',
                elements='dict',
                options=dict(
                    radius_server_address=dict(
                        type='str',
                        disposition='radius_server_address',
                        required=True
                    ),
                    radius_server_score=dict(
                        type='integer',
                        disposition='radius_server_score'
                    ),
                    radius_server_secret=dict(
                        type='str',
                        disposition='radius_server_secret'
                    )
                )
            ),
            aad_authentication_parameters=dict(
                type='dict',
                disposition='/aad_authentication_parameters',
                options=dict(
                    aad_tenant=dict(
                        type='str',
                        disposition='aad_tenant'
                    ),
                    aad_audience=dict(
                        type='str',
                        disposition='aad_audience'
                    ),
                    aad_issuer=dict(
                        type='str',
                        disposition='aad_issuer'
                    )
                )
            ),
            p2_s_vpn_gateways=dict(
                type='list',
                updatable=False,
                disposition='/p2_s_vpn_gateways',
                elements='dict',
                options=dict(
                    virtual_hub=dict(
                        type='dict',
                        disposition='virtual_hub',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    p2_s_connection_configurations=dict(
                        type='list',
                        disposition='p2_s_connection_configurations',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vpn_client_address_pool=dict(
                                type='dict',
                                disposition='vpn_client_address_pool',
                                options=dict(
                                    address_prefixes=dict(
                                        type='list',
                                        disposition='address_prefixes',
                                        elements='str'
                                    )
                                )
                            ),
                            routing_configuration=dict(
                                type='dict',
                                disposition='routing_configuration',
                                options=dict(
                                    associated_route_table=dict(
                                        type='dict',
                                        disposition='associated_route_table',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    ),
                                    propagated_route_tables=dict(
                                        type='dict',
                                        disposition='propagated_route_tables',
                                        options=dict(
                                            labels=dict(
                                                type='list',
                                                disposition='labels',
                                                elements='str'
                                            ),
                                            ids=dict(
                                                type='list',
                                                disposition='ids',
                                                elements='dict',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    vnet_routes=dict(
                                        type='dict',
                                        disposition='vnet_routes',
                                        options=dict(
                                            static_routes=dict(
                                                type='list',
                                                disposition='static_routes',
                                                elements='dict',
                                                options=dict(
                                                    name=dict(
                                                        type='str',
                                                        disposition='name'
                                                    ),
                                                    address_prefixes=dict(
                                                        type='list',
                                                        disposition='address_prefixes',
                                                        elements='str'
                                                    ),
                                                    next_hop_ip_address=dict(
                                                        type='str',
                                                        disposition='next_hop_ip_address'
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                            enable_internet_security=dict(
                                type='bool',
                                disposition='enable_internet_security'
                            )
                        )
                    ),
                    vpn_gateway_scale_unit=dict(
                        type='integer',
                        disposition='vpn_gateway_scale_unit'
                    ),
                    vpn_server_configuration=dict(
                        type='dict',
                        disposition='vpn_server_configuration',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    vpn_client_connection_health=dict(
                        type='dict',
                        updatable=False,
                        disposition='vpn_client_connection_health',
                        options=dict(
                            vpn_client_connections_count=dict(
                                type='integer',
                                disposition='vpn_client_connections_count'
                            ),
                            allocated_ip_addresses=dict(
                                type='list',
                                disposition='allocated_ip_addresses',
                                elements='str'
                            )
                        )
                    ),
                    custom_dns_servers=dict(
                        type='list',
                        disposition='custom_dns_servers',
                        elements='str'
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
        self.vpn_server_configuration_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVpnServerConfiguration, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.vpn_server_configurations.create_or_update(resource_group_name=self.resource_group_name,
                                                                                   vpn_server_configuration_name=self.vpn_server_configuration_name,
                                                                                   vpn_server_configuration_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VpnServerConfiguration instance.')
            self.fail('Error creating the VpnServerConfiguration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vpn_server_configurations.delete(resource_group_name=self.resource_group_name,
                                                                         vpn_server_configuration_name=self.vpn_server_configuration_name)
        except CloudError as e:
            self.log('Error attempting to delete the VpnServerConfiguration instance.')
            self.fail('Error deleting the VpnServerConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vpn_server_configurations.get(resource_group_name=self.resource_group_name,
                                                                      vpn_server_configuration_name=self.vpn_server_configuration_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVpnServerConfiguration()


if __name__ == '__main__':
    main()
