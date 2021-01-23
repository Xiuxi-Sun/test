#!/usr/bin/python
#
# Copyright (c) 2020 Microsoft
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_recordset
version_added: 1.3.1
short_description: Manage Azure RecordSet instance.
description:
    - 'Create, update and delete instance of Azure RecordSet.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    zone_name:
        description:
            - The name of the DNS zone (without a terminating dot).
        required: true
        type: str
    relative_record_set_name:
        description:
            - 'The name of the record set, relative to the name of the zone.'
        required: true
        type: str
    record_type:
        description:
            - The type of DNS record in this record set.
            - >-
                The type of DNS record in this record set. Record sets of type SOA can
                be updated but not created (they are created when the DNS zone is
                created).
            - >-
                The type of DNS record in this record set. Record sets of type SOA
                cannot be deleted (they are deleted when the DNS zone is deleted).
        required: true
        type: str
        choices:
            - A
            - AAAA
            - CAA
            - CNAME
            - MX
            - NS
            - PTR
            - SOA
            - SRV
            - TXT
    if_match:
        description:
            - >-
                The etag of the record set. Omit this value to always overwrite the
                current record set. Specify the last-seen etag value to prevent
                accidentally overwriting concurrent changes.
            - >-
                The etag of the record set. Omit this value to always overwrite the
                current record set. Specify the last-seen etag value to prevent
                accidentally overwriting any concurrent changes.
            - >-
                The etag of the record set. Omit this value to always delete the current
                record set. Specify the last-seen etag value to prevent accidentally
                deleting any concurrent changes.
        type: str
    etag:
        description:
            - The etag of the record set.
        type: str
    metadata:
        description:
            - The metadata attached to the record set.
        type: dict
    ttl:
        description:
            - The TTL (time-to-live) of the records in the record set.
        type: int
    target_resource:
        description:
            - >-
                A reference to an azure resource from where the dns resource value is
                taken.
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id.
                type: str
    a_records:
        description:
            - The list of A records in the record set.
        type: list
        suboptions:
            ipv4_address:
                description:
                    - The IPv4 address of this A record.
                type: str
    aaaa_records:
        description:
            - The list of AAAA records in the record set.
        type: list
        suboptions:
            ipv6_address:
                description:
                    - The IPv6 address of this AAAA record.
                type: str
    mx_records:
        description:
            - The list of MX records in the record set.
        type: list
        suboptions:
            preference:
                description:
                    - The preference value for this MX record.
                type: int
            exchange:
                description:
                    - The domain name of the mail host for this MX record.
                type: str
    ns_records:
        description:
            - The list of NS records in the record set.
        type: list
        suboptions:
            nsdname:
                description:
                    - The name server name for this NS record.
                type: str
    ptr_records:
        description:
            - The list of PTR records in the record set.
        type: list
        suboptions:
            ptrdname:
                description:
                    - The PTR target domain name for this PTR record.
                type: str
    srv_records:
        description:
            - The list of SRV records in the record set.
        type: list
        suboptions:
            priority:
                description:
                    - The priority value for this SRV record.
                type: int
            weight:
                description:
                    - The weight value for this SRV record.
                type: int
            port:
                description:
                    - The port value for this SRV record.
                type: int
            target:
                description:
                    - The target domain name for this SRV record.
                type: str
    txt_records:
        description:
            - The list of TXT records in the record set.
        type: list
        suboptions:
            value:
                description:
                    - The text value of this TXT record.
                type: list
    cname_record:
        description:
            - The CNAME record in the  record set.
        type: dict
        suboptions:
            cname:
                description:
                    - The canonical name for this CNAME record.
                type: str
    soa_record:
        description:
            - The SOA record in the record set.
        type: dict
        suboptions:
            host:
                description:
                    - >-
                        The domain name of the authoritative name server for this SOA
                        record.
                type: str
            email:
                description:
                    - The email contact for this SOA record.
                type: str
            serial_number:
                description:
                    - The serial number for this SOA record.
                type: int
            refresh_time:
                description:
                    - The refresh value for this SOA record.
                type: int
            retry_time:
                description:
                    - The retry time for this SOA record.
                type: int
            expire_time:
                description:
                    - The expire time for this SOA record.
                type: int
            minimum_ttl:
                description:
                    - >-
                        The minimum value for this SOA record. By convention this is used to
                        determine the negative caching duration.
                type: int
    caa_records:
        description:
            - The list of CAA records in the record set.
        type: list
        suboptions:
            flags:
                description:
                    - The flags for this CAA record as an integer between 0 and 255.
                type: int
            tag:
                description:
                    - The tag for this CAA record.
                type: str
            value:
                description:
                    - The value for this CAA record.
                type: str
    if_none_match:
        description:
            - >-
                Set to '*' to allow a new record set to be created, but to prevent
                updating an existing record set. Other values will be ignored.
        type: str
    state:
        description:
            - Assert the state of the RecordSet.
            - >-
                Use C(present) to create or update an RecordSet and C(absent) to delete
                it.
        default: present
        choices:
            - absent
            - present
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - Microsoft

'''

EXAMPLES = '''
    - name: Patch A recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch AAAA recordset
      azure_rm_recordset: 
        record_type: AAAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch CAA recordset
      azure_rm_recordset: 
        record_type: CAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch CNAME recordset
      azure_rm_recordset: 
        record_type: CNAME
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch MX recordset
      azure_rm_recordset: 
        record_type: MX
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch NS recordset
      azure_rm_recordset: 
        record_type: NS
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch PTR recordset
      azure_rm_recordset: 
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: rg1
        zone_name: 0.0.127.in-addr.arpa
        properties:
          metadata:
            key2: value2

    - name: Patch SOA recordset
      azure_rm_recordset: 
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch SRV recordset
      azure_rm_recordset: 
        record_type: SRV
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Patch TXT recordset
      azure_rm_recordset: 
        record_type: TXT
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          metadata:
            key2: value2

    - name: Create A recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          arecords:
            - ipv4address: 127.0.0.1
          ttl: 3600
          metadata:
            key1: value1

    - name: Create A recordset with alias target resource
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          ttl: 3600
          metadata:
            key1: value1
          target_resource:
            id: >-
              /subscriptions/726f8cd6-6459-4db4-8e6d-2cd2716904e2/resourceGroups/test/providers/Microsoft.Network/trafficManagerProfiles/testpp2

    - name: Create AAAA recordset
      azure_rm_recordset: 
        record_type: AAAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          aaaarecords:
            - ipv6address: '::1'
          ttl: 3600
          metadata:
            key1: value1

    - name: Create CAA recordset
      azure_rm_recordset: 
        record_type: CAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          ttl: 3600
          caa_records:
            - flags: 0
              tag: issue
              value: ca.contoso.com
          metadata:
            key1: value1

    - name: Create CNAME recordset
      azure_rm_recordset: 
        record_type: CNAME
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          cnamerecord:
            cname: contoso.com
          ttl: 3600
          metadata:
            key1: value1

    - name: Create MX recordset
      azure_rm_recordset: 
        record_type: MX
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          mxrecords:
            - exchange: mail.contoso.com
              preference: 0
          ttl: 3600
          metadata:
            key1: value1

    - name: Create NS recordset
      azure_rm_recordset: 
        record_type: NS
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          nsrecords:
            - nsdname: ns1.contoso.com
          ttl: 3600
          metadata:
            key1: value1

    - name: Create PTR recordset
      azure_rm_recordset: 
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: rg1
        zone_name: 0.0.127.in-addr.arpa
        properties:
          ptrrecords:
            - ptrdname: localhost
          ttl: 3600
          metadata:
            key1: value1

    - name: Create SOA recordset
      azure_rm_recordset: 
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: rg1
        zone_name: zone1
        properties:
          soarecord:
            email: hostmaster.contoso.com
            expire_time: 2419200
            host: ns1.contoso.com
            minimum_ttl: 300
            refresh_time: 3600
            retry_time: 300
            serial_number: 1
          ttl: 3600
          metadata:
            key1: value1

    - name: Create SRV recordset
      azure_rm_recordset: 
        record_type: SRV
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          srvrecords:
            - port: 80
              priority: 0
              target: contoso.com
              weight: 10
          ttl: 3600
          metadata:
            key1: value1

    - name: Create TXT recordset
      azure_rm_recordset: 
        record_type: TXT
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1
        properties:
          ttl: 3600
          txtrecords:
            - value:
                - string1
                - string2
          metadata:
            key1: value1

    - name: Delete A recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete AAAA recordset
      azure_rm_recordset: 
        record_type: AAAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete CAA recordset
      azure_rm_recordset: 
        record_type: CAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete CNAME recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete MX recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete NS recordset
      azure_rm_recordset: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete PTR recordset
      azure_rm_recordset: 
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: rg1
        zone_name: 0.0.127.in-addr.arpa

    - name: Delete SRV recordset
      azure_rm_recordset: 
        record_type: SRV
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Delete TXT recordset
      azure_rm_recordset: 
        record_type: TXT
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

'''

RETURN = '''
id:
    description:
        - The ID of the record set.
    type: str
    sample: null
name:
    description:
        - The name of the record set.
    type: str
    sample: null
type:
    description:
        - The type of the record set.
    type: str
    sample: null
etag:
    description:
        - The etag of the record set.
    type: str
    sample: null
metadata:
    description:
        - The metadata attached to the record set.
    type: dict
    sample: null
ttl:
    description:
        - The TTL (time-to-live) of the records in the record set.
    type: int
    sample: null
fqdn:
    description:
        - Fully qualified domain name of the record set.
    type: str
    sample: null
provisioning_state:
    description:
        - provisioning State of the record set.
    type: str
    sample: null
target_resource:
    description:
        - >-
            A reference to an azure resource from where the dns resource value is
            taken.
    type: dict
    sample: null
    contains:
        id:
            description:
                - Resource Id.
            type: str
            sample: null
a_records:
    description:
        - The list of A records in the record set.
    type: list
    sample: null
    contains:
        ipv4_address:
            description:
                - The IPv4 address of this A record.
            type: str
            sample: null
aaaa_records:
    description:
        - The list of AAAA records in the record set.
    type: list
    sample: null
    contains:
        ipv6_address:
            description:
                - The IPv6 address of this AAAA record.
            type: str
            sample: null
mx_records:
    description:
        - The list of MX records in the record set.
    type: list
    sample: null
    contains:
        preference:
            description:
                - The preference value for this MX record.
            type: int
            sample: null
        exchange:
            description:
                - The domain name of the mail host for this MX record.
            type: str
            sample: null
ns_records:
    description:
        - The list of NS records in the record set.
    type: list
    sample: null
    contains:
        nsdname:
            description:
                - The name server name for this NS record.
            type: str
            sample: null
ptr_records:
    description:
        - The list of PTR records in the record set.
    type: list
    sample: null
    contains:
        ptrdname:
            description:
                - The PTR target domain name for this PTR record.
            type: str
            sample: null
srv_records:
    description:
        - The list of SRV records in the record set.
    type: list
    sample: null
    contains:
        priority:
            description:
                - The priority value for this SRV record.
            type: int
            sample: null
        weight:
            description:
                - The weight value for this SRV record.
            type: int
            sample: null
        port:
            description:
                - The port value for this SRV record.
            type: int
            sample: null
        target:
            description:
                - The target domain name for this SRV record.
            type: str
            sample: null
txt_records:
    description:
        - The list of TXT records in the record set.
    type: list
    sample: null
    contains:
        value:
            description:
                - The text value of this TXT record.
            type: list
            sample: null
cname_record:
    description:
        - The CNAME record in the  record set.
    type: dict
    sample: null
    contains:
        cname:
            description:
                - The canonical name for this CNAME record.
            type: str
            sample: null
soa_record:
    description:
        - The SOA record in the record set.
    type: dict
    sample: null
    contains:
        host:
            description:
                - The domain name of the authoritative name server for this SOA record.
            type: str
            sample: null
        email:
            description:
                - The email contact for this SOA record.
            type: str
            sample: null
        serial_number:
            description:
                - The serial number for this SOA record.
            type: int
            sample: null
        refresh_time:
            description:
                - The refresh value for this SOA record.
            type: int
            sample: null
        retry_time:
            description:
                - The retry time for this SOA record.
            type: int
            sample: null
        expire_time:
            description:
                - The expire time for this SOA record.
            type: int
            sample: null
        minimum_ttl:
            description:
                - >-
                    The minimum value for this SOA record. By convention this is used to
                    determine the negative caching duration.
            type: int
            sample: null
caa_records:
    description:
        - The list of CAA records in the record set.
    type: list
    sample: null
    contains:
        flags:
            description:
                - The flags for this CAA record as an integer between 0 and 255.
            type: int
            sample: null
        tag:
            description:
                - The tag for this CAA record.
            type: str
            sample: null
        value:
            description:
                - The value for this CAA record.
            type: str
            sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dns import DnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRecordSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            zone_name=dict(
                type='str',
                required=True
            ),
            relative_record_set_name=dict(
                type='str',
                required=True
            ),
            record_type=dict(
                type='str',
                choices=['A',
                         'AAAA',
                         'CAA',
                         'CNAME',
                         'MX',
                         'NS',
                         'PTR',
                         'SOA',
                         'SRV',
                         'TXT'],
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            metadata=dict(
                type='dict',
                disposition='/metadata'
            ),
            ttl=dict(
                type='int',
                disposition='/ttl'
            ),
            target_resource=dict(
                type='dict',
                disposition='/target_resource',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            a_records=dict(
                type='list',
                disposition='/a_records',
                elements='dict',
                options=dict(
                    ipv4_address=dict(
                        type='str',
                        disposition='ipv4_address'
                    )
                )
            ),
            aaaa_records=dict(
                type='list',
                disposition='/aaaa_records',
                elements='dict',
                options=dict(
                    ipv6_address=dict(
                        type='str',
                        disposition='ipv6_address'
                    )
                )
            ),
            mx_records=dict(
                type='list',
                disposition='/mx_records',
                elements='dict',
                options=dict(
                    preference=dict(
                        type='int',
                        disposition='preference'
                    ),
                    exchange=dict(
                        type='str',
                        disposition='exchange'
                    )
                )
            ),
            ns_records=dict(
                type='list',
                disposition='/ns_records',
                elements='dict',
                options=dict(
                    nsdname=dict(
                        type='str',
                        disposition='nsdname'
                    )
                )
            ),
            ptr_records=dict(
                type='list',
                disposition='/ptr_records',
                elements='dict',
                options=dict(
                    ptrdname=dict(
                        type='str',
                        disposition='ptrdname'
                    )
                )
            ),
            srv_records=dict(
                type='list',
                disposition='/srv_records',
                elements='dict',
                options=dict(
                    priority=dict(
                        type='int',
                        disposition='priority'
                    ),
                    weight=dict(
                        type='int',
                        disposition='weight'
                    ),
                    port=dict(
                        type='int',
                        disposition='port'
                    ),
                    target=dict(
                        type='str',
                        disposition='target'
                    )
                )
            ),
            txt_records=dict(
                type='list',
                disposition='/txt_records',
                elements='dict',
                options=dict(
                    value=dict(
                        type='list',
                        disposition='value',
                        elements='str'
                    )
                )
            ),
            cname_record=dict(
                type='dict',
                disposition='/cname_record',
                options=dict(
                    cname=dict(
                        type='str',
                        disposition='cname'
                    )
                )
            ),
            soa_record=dict(
                type='dict',
                disposition='/soa_record',
                options=dict(
                    host=dict(
                        type='str',
                        disposition='host'
                    ),
                    email=dict(
                        type='str',
                        disposition='email'
                    ),
                    serial_number=dict(
                        type='int',
                        disposition='serial_number'
                    ),
                    refresh_time=dict(
                        type='int',
                        disposition='refresh_time'
                    ),
                    retry_time=dict(
                        type='int',
                        disposition='retry_time'
                    ),
                    expire_time=dict(
                        type='int',
                        disposition='expire_time'
                    ),
                    minimum_ttl=dict(
                        type='int',
                        disposition='minimum_ttl'
                    )
                )
            ),
            caa_records=dict(
                type='list',
                disposition='/caa_records',
                elements='dict',
                options=dict(
                    flags=dict(
                        type='int',
                        disposition='flags'
                    ),
                    tag=dict(
                        type='str',
                        disposition='tag'
                    ),
                    value=dict(
                        type='str',
                        disposition='value'
                    )
                )
            ),
            if_none_match=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.zone_name = None
        self.relative_record_set_name = None
        self.record_type = None
        self.if_match = None
        self.if_none_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRecordSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-05-01')

        if 'location' not in self.body:
            resource_group = self.get_resource_group(self.resource_group)
            self.body['location'] = resource_group.location

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
            self.results['state'] = response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.record_sets.create_or_update(resource_group_name=self.resource_group,
                                                                     zone_name=self.zone_name,
                                                                     relative_record_set_name=self.relative_record_set_name,
                                                                     record_type=self.record_type,
                                                                     if_match=self.if_match,
                                                                     if_none_match=self.if_none_match,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RecordSet instance.')
            self.fail('Error creating the RecordSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.record_sets.delete(resource_group_name=self.resource_group,
                                                           zone_name=self.zone_name,
                                                           relative_record_set_name=self.relative_record_set_name,
                                                           record_type=self.record_type,
                                                           if_match=self.if_match)
        except CloudError as e:
            self.log('Error attempting to delete the RecordSet instance.')
            self.fail('Error deleting the RecordSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.record_sets.get(resource_group_name=self.resource_group,
                                                        zone_name=self.zone_name,
                                                        relative_record_set_name=self.relative_record_set_name,
                                                        record_type=self.record_type)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRecordSet()


if __name__ == '__main__':
    main()
