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
module: azure_rm_vpngateway
version_added: '2.9'
short_description: Manage Azure VpnGateway instance.
description:
  - 'Create, update and delete instance of Azure VpnGateway.'
options:
  resource_group_name:
    description:
      - The resource group name of the VpnGateway.
    required: true
    type: str
  gateway_name:
    description:
      - The name of the gateway.
    required: true
    type: str
  virtual_hub:
    description:
      - The VirtualHub to which the gateway belongs.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  connections:
    description:
      - List of all vpn connections to the gateway.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      remote_vpn_site:
        description:
          - Id of the connected vpn site.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      routing_weight:
        description:
          - Routing weight for vpn connection.
        type: integer
      dpd_timeout_seconds:
        description:
          - DPD timeout in seconds for vpn connection.
        type: integer
      vpn_connection_protocol_type:
        description:
          - Connection protocol used for this connection.
        type: str
        choices:
          - IKEv2
          - IKEv1
      connection_bandwidth:
        description:
          - Expected bandwidth in MBPS.
        type: integer
      shared_key:
        description:
          - SharedKey for the vpn connection.
        type: str
      enable_bgp:
        description:
          - EnableBgp flag.
        type: bool
      use_policy_based_traffic_selectors:
        description:
          - Enable policy-based traffic selectors.
        type: bool
      ipsec_policies:
        description:
          - The IPSec Policies to be considered by this connection.
        type: list
        suboptions:
          sa_life_time_seconds:
            description:
              - >-
                The IPSec Security Association (also called Quick Mode or Phase
                2 SA) lifetime in seconds for a site to site VPN tunnel.
            required: true
            type: integer
          sa_data_size_kilobytes:
            description:
              - >-
                The IPSec Security Association (also called Quick Mode or Phase
                2 SA) payload size in KB for a site to site VPN tunnel.
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
      enable_rate_limiting:
        description:
          - EnableBgp flag.
        type: bool
      enable_internet_security:
        description:
          - Enable internet security.
        type: bool
      use_local_azure_ip_address:
        description:
          - Use local azure ip to initiate connection.
        type: bool
      vpn_link_connections:
        description:
          - List of all vpn site link connections to the gateway.
        type: list
        suboptions:
          name:
            description:
              - >-
                The name of the resource that is unique within a resource group.
                This name can be used to access the resource.
            type: str
          vpn_site_link:
            description:
              - Id of the connected vpn site link.
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          routing_weight:
            description:
              - Routing weight for vpn connection.
            type: integer
          vpn_connection_protocol_type:
            description:
              - Connection protocol used for this connection.
            type: str
            choices:
              - IKEv2
              - IKEv1
          connection_bandwidth:
            description:
              - Expected bandwidth in MBPS.
            type: integer
          shared_key:
            description:
              - SharedKey for the vpn connection.
            type: str
          enable_bgp:
            description:
              - EnableBgp flag.
            type: bool
          use_policy_based_traffic_selectors:
            description:
              - Enable policy-based traffic selectors.
            type: bool
          ipsec_policies:
            description:
              - The IPSec Policies to be considered by this connection.
            type: list
            suboptions:
              sa_life_time_seconds:
                description:
                  - >-
                    The IPSec Security Association (also called Quick Mode or
                    Phase 2 SA) lifetime in seconds for a site to site VPN
                    tunnel.
                required: true
                type: integer
              sa_data_size_kilobytes:
                description:
                  - >-
                    The IPSec Security Association (also called Quick Mode or
                    Phase 2 SA) payload size in KB for a site to site VPN
                    tunnel.
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
          enable_rate_limiting:
            description:
              - EnableBgp flag.
            type: bool
          use_local_azure_ip_address:
            description:
              - Use local azure ip to initiate connection.
            type: bool
      routing_configuration:
        description:
          - >-
            The Routing Configuration indicating the associated and propagated
            route tables on this connection.
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
  bgp_settings:
    description:
      - Local network gateway's BGP speaker settings.
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
  vpn_gateway_scale_unit:
    description:
      - The scale unit for this vpn gateway.
    type: integer
  ip_configurations:
    description:
      - List of all IPs configured on the gateway.
    type: list
    suboptions:
      id:
        description:
          - The identifier of the IP configuration for a VPN Gateway.
        type: str
      public_ip_address:
        description:
          - The public IP address of this IP configuration.
        type: str
      private_ip_address:
        description:
          - The private IP address of this IP configuration.
        type: str
  is_routing_preference_internet:
    description:
      - >-
        Enable Routing Preference property for the Public IP Interface of the
        VpnGateway.
    type: bool
  state:
    description:
      - Assert the state of the VpnGateway.
      - >-
        Use C(present) to create or update an VpnGateway and C(absent) to delete
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
    - name: VpnGatewayPut
      azure_rm_vpngateway: 
        gateway_name: gateway1
        resource_group_name: rg1
        

    - name: VpnGatewayDelete
      azure_rm_vpngateway: 
        gateway_name: gateway1
        resource_group_name: rg1
        

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
connections:
  description:
    - List of all vpn connections to the gateway.
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
    remote_vpn_site:
      description:
        - Id of the connected vpn site.
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
    routing_weight:
      description:
        - Routing weight for vpn connection.
      returned: always
      type: integer
      sample: null
    dpd_timeout_seconds:
      description:
        - DPD timeout in seconds for vpn connection.
      returned: always
      type: integer
      sample: null
    vpn_connection_protocol_type:
      description:
        - Connection protocol used for this connection.
      returned: always
      type: str
      sample: null
    connection_bandwidth:
      description:
        - Expected bandwidth in MBPS.
      returned: always
      type: integer
      sample: null
    shared_key:
      description:
        - SharedKey for the vpn connection.
      returned: always
      type: str
      sample: null
    enable_bgp:
      description:
        - EnableBgp flag.
      returned: always
      type: bool
      sample: null
    use_policy_based_traffic_selectors:
      description:
        - Enable policy-based traffic selectors.
      returned: always
      type: bool
      sample: null
    ipsec_policies:
      description:
        - The IPSec Policies to be considered by this connection.
      returned: always
      type: list
      sample: null
      contains:
        sa_life_time_seconds:
          description:
            - >-
              The IPSec Security Association (also called Quick Mode or Phase 2
              SA) lifetime in seconds for a site to site VPN tunnel.
          returned: always
          type: integer
          sample: null
        sa_data_size_kilobytes:
          description:
            - >-
              The IPSec Security Association (also called Quick Mode or Phase 2
              SA) payload size in KB for a site to site VPN tunnel.
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
    enable_rate_limiting:
      description:
        - EnableBgp flag.
      returned: always
      type: bool
      sample: null
    enable_internet_security:
      description:
        - Enable internet security.
      returned: always
      type: bool
      sample: null
    use_local_azure_ip_address:
      description:
        - Use local azure ip to initiate connection.
      returned: always
      type: bool
      sample: null
    vpn_link_connections:
      description:
        - List of all vpn site link connections to the gateway.
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
        vpn_site_link:
          description:
            - Id of the connected vpn site link.
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
        routing_weight:
          description:
            - Routing weight for vpn connection.
          returned: always
          type: integer
          sample: null
        vpn_connection_protocol_type:
          description:
            - Connection protocol used for this connection.
          returned: always
          type: str
          sample: null
        connection_bandwidth:
          description:
            - Expected bandwidth in MBPS.
          returned: always
          type: integer
          sample: null
        shared_key:
          description:
            - SharedKey for the vpn connection.
          returned: always
          type: str
          sample: null
        enable_bgp:
          description:
            - EnableBgp flag.
          returned: always
          type: bool
          sample: null
        use_policy_based_traffic_selectors:
          description:
            - Enable policy-based traffic selectors.
          returned: always
          type: bool
          sample: null
        ipsec_policies:
          description:
            - The IPSec Policies to be considered by this connection.
          returned: always
          type: list
          sample: null
          contains:
            sa_life_time_seconds:
              description:
                - >-
                  The IPSec Security Association (also called Quick Mode or
                  Phase 2 SA) lifetime in seconds for a site to site VPN tunnel.
              returned: always
              type: integer
              sample: null
            sa_data_size_kilobytes:
              description:
                - >-
                  The IPSec Security Association (also called Quick Mode or
                  Phase 2 SA) payload size in KB for a site to site VPN tunnel.
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
        enable_rate_limiting:
          description:
            - EnableBgp flag.
          returned: always
          type: bool
          sample: null
        use_local_azure_ip_address:
          description:
            - Use local azure ip to initiate connection.
          returned: always
          type: bool
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
              List of routes that control routing from VirtualHub into a virtual
              network connection.
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
bgp_settings:
  description:
    - Local network gateway's BGP speaker settings.
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
    - The provisioning state of the VPN gateway resource.
  returned: always
  type: str
  sample: null
vpn_gateway_scale_unit:
  description:
    - The scale unit for this vpn gateway.
  returned: always
  type: integer
  sample: null
ip_configurations:
  description:
    - List of all IPs configured on the gateway.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - The identifier of the IP configuration for a VPN Gateway.
      returned: always
      type: str
      sample: null
    public_ip_address:
      description:
        - The public IP address of this IP configuration.
      returned: always
      type: str
      sample: null
    private_ip_address:
      description:
        - The private IP address of this IP configuration.
      returned: always
      type: str
      sample: null
is_routing_preference_internet:
  description:
    - >-
      Enable Routing Preference property for the Public IP Interface of the
      VpnGateway.
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


class AzureRMVpnGateway(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            gateway_name=dict(
                type='str',
                required=True
            ),
            virtual_hub=dict(
                type='dict',
                disposition='/virtual_hub',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            connections=dict(
                type='list',
                disposition='/connections',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    remote_vpn_site=dict(
                        type='dict',
                        disposition='remote_vpn_site',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    routing_weight=dict(
                        type='integer',
                        disposition='routing_weight'
                    ),
                    dpd_timeout_seconds=dict(
                        type='integer',
                        disposition='dpd_timeout_seconds'
                    ),
                    vpn_connection_protocol_type=dict(
                        type='str',
                        disposition='vpn_connection_protocol_type',
                        choices=['IKEv2',
                                 'IKEv1']
                    ),
                    connection_bandwidth=dict(
                        type='integer',
                        disposition='connection_bandwidth'
                    ),
                    shared_key=dict(
                        type='str',
                        disposition='shared_key'
                    ),
                    enable_bgp=dict(
                        type='bool',
                        disposition='enable_bgp'
                    ),
                    use_policy_based_traffic_selectors=dict(
                        type='bool',
                        disposition='use_policy_based_traffic_selectors'
                    ),
                    ipsec_policies=dict(
                        type='list',
                        disposition='ipsec_policies',
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
                    enable_rate_limiting=dict(
                        type='bool',
                        disposition='enable_rate_limiting'
                    ),
                    enable_internet_security=dict(
                        type='bool',
                        disposition='enable_internet_security'
                    ),
                    use_local_azure_ip_address=dict(
                        type='bool',
                        disposition='use_local_azure_ip_address'
                    ),
                    vpn_link_connections=dict(
                        type='list',
                        disposition='vpn_link_connections',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vpn_site_link=dict(
                                type='dict',
                                disposition='vpn_site_link',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            routing_weight=dict(
                                type='integer',
                                disposition='routing_weight'
                            ),
                            vpn_connection_protocol_type=dict(
                                type='str',
                                disposition='vpn_connection_protocol_type',
                                choices=['IKEv2',
                                         'IKEv1']
                            ),
                            connection_bandwidth=dict(
                                type='integer',
                                disposition='connection_bandwidth'
                            ),
                            shared_key=dict(
                                type='str',
                                disposition='shared_key'
                            ),
                            enable_bgp=dict(
                                type='bool',
                                disposition='enable_bgp'
                            ),
                            use_policy_based_traffic_selectors=dict(
                                type='bool',
                                disposition='use_policy_based_traffic_selectors'
                            ),
                            ipsec_policies=dict(
                                type='list',
                                disposition='ipsec_policies',
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
                            enable_rate_limiting=dict(
                                type='bool',
                                disposition='enable_rate_limiting'
                            ),
                            use_local_azure_ip_address=dict(
                                type='bool',
                                disposition='use_local_azure_ip_address'
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
                    )
                )
            ),
            bgp_settings=dict(
                type='dict',
                disposition='/bgp_settings',
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
            vpn_gateway_scale_unit=dict(
                type='integer',
                disposition='/vpn_gateway_scale_unit'
            ),
            ip_configurations=dict(
                type='list',
                updatable=False,
                disposition='/ip_configurations',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    ),
                    public_ip_address=dict(
                        type='str',
                        disposition='public_ip_address'
                    ),
                    private_ip_address=dict(
                        type='str',
                        disposition='private_ip_address'
                    )
                )
            ),
            is_routing_preference_internet=dict(
                type='bool',
                disposition='/is_routing_preference_internet'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.gateway_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVpnGateway, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-07-01')

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
            response = self.mgmt_client.vpn_gateways.create_or_update(resource_group_name=self.resource_group_name,
                                                                      gateway_name=self.gateway_name,
                                                                      vpn_gateway_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VpnGateway instance.')
            self.fail('Error creating the VpnGateway instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.vpn_gateways.delete(resource_group_name=self.resource_group_name,
                                                            gateway_name=self.gateway_name)
        except CloudError as e:
            self.log('Error attempting to delete the VpnGateway instance.')
            self.fail('Error deleting the VpnGateway instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.vpn_gateways.get(resource_group_name=self.resource_group_name,
                                                         gateway_name=self.gateway_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVpnGateway()


if __name__ == '__main__':
    main()
