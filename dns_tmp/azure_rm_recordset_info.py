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
module: azure_rm_recordset_info
version_added: 1.3.1
short_description: Get RecordSet info.
description:
    - Get info of RecordSet.
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
        type: str
    record_type:
        description:
            - The type of DNS record in this record set.
            - The type of record sets to enumerate.
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
    top:
        description:
            - >-
                The maximum number of record sets to return. If not specified, returns
                up to 100 record sets.
        type: int
    recordsetnamesuffix:
        description:
            - >-
                The suffix label of the record set name that has to be used to filter
                the record set enumerations. If this parameter is specified, Enumeration
                will return only records that end with .:code:`<recordSetNameSuffix>`
        type: str
    record_set_name_suffix:
        description:
            - >-
                The suffix label of the record set name that has to be used to filter
                the record set enumerations. If this parameter is specified, Enumeration
                will return only records that end with .:code:`<recordSetNameSuffix>`
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - Microsoft

'''

EXAMPLES = '''
    - name: Get A recordset
      azure_rm_recordset_info: 
        record_type: A
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get AAAA recordset
      azure_rm_recordset_info: 
        record_type: AAAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get CAA recordset
      azure_rm_recordset_info: 
        record_type: CAA
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get CNAME recordset
      azure_rm_recordset_info: 
        record_type: CNAME
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get MX recordset
      azure_rm_recordset_info: 
        record_type: MX
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get NS recordset
      azure_rm_recordset_info: 
        record_type: NS
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get PTR recordset
      azure_rm_recordset_info: 
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: rg1
        zone_name: 0.0.127.in-addr.arpa

    - name: Get SOA recordset
      azure_rm_recordset_info: 
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: rg1
        zone_name: zone1

    - name: Get SRV recordset
      azure_rm_recordset_info: 
        record_type: SRV
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: Get TXT recordset
      azure_rm_recordset_info: 
        record_type: TXT
        relative_record_set_name: record1
        resource_group_name: rg1
        zone_name: zone1

    - name: List A recordsets
      azure_rm_recordset_info: 
        record_type: A
        resource_group_name: rg1
        zone_name: zone1

    - name: List AAAA recordsets
      azure_rm_recordset_info: 
        record_type: AAAA
        resource_group_name: rg1
        zone_name: zone1

    - name: List CAA recordsets
      azure_rm_recordset_info: 
        record_type: CAA
        resource_group_name: rg1
        zone_name: zone1

    - name: List CNAME recordsets
      azure_rm_recordset_info: 
        record_type: CNAME
        resource_group_name: rg1
        zone_name: zone1

    - name: List MX recordsets
      azure_rm_recordset_info: 
        record_type: MX
        resource_group_name: rg1
        zone_name: zone1

    - name: List NS recordsets
      azure_rm_recordset_info: 
        record_type: NS
        resource_group_name: rg1
        zone_name: zone1

    - name: List PTR recordsets
      azure_rm_recordset_info: 
        record_type: PTR
        resource_group_name: rg1
        zone_name: 0.0.127.in-addr.arpa

    - name: List SOA recordsets
      azure_rm_recordset_info: 
        record_type: SOA
        resource_group_name: rg1
        zone_name: zone1

    - name: List SRV recordsets
      azure_rm_recordset_info: 
        record_type: SRV
        resource_group_name: rg1
        zone_name: zone1

    - name: List TXT recordsets
      azure_rm_recordset_info: 
        record_type: TXT
        resource_group_name: rg1
        zone_name: zone1

    - name: List recordsets by zone
      azure_rm_recordset_info: 
        resource_group_name: rg1
        zone_name: zone1

'''

RETURN = '''
record_sets:
    description: >-
        A list of dict results where the key is the name of the RecordSet and the
        values are the facts for that RecordSet.
    returned: always
    type: complex
    contains:
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
                        - >-
                            The domain name of the authoritative name server for this SOA
                            record.
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
                            The minimum value for this SOA record. By convention this is used
                            to determine the negative caching duration.
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
        value:
            description:
                - Information about the record sets in the response.
            type: list
            sample: null
            contains:
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
                target_resource:
                    description:
                        - >-
                            A reference to an azure resource from where the dns resource value
                            is taken.
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
                                - >-
                                    The domain name of the authoritative name server for this SOA
                                    record.
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
                                    The minimum value for this SOA record. By convention this is
                                    used to determine the negative caching duration.
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
        next_link:
            description:
                - The continuation token for the next page of results.
            type: str
            sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dns import DnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecordSetInfo(AzureRMModuleBase):
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
                type='str'
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
                         'TXT']
            ),
            top=dict(
                type='int'
            ),
            recordsetnamesuffix=dict(
                type='str'
            ),
            record_set_name_suffix=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.zone_name = None
        self.relative_record_set_name = None
        self.record_type = None
        self.top = None
        self.recordsetnamesuffix = None
        self.record_set_name_suffix = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRecordSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-05-01')

        if (self.resource_group is not None and
            self.zone_name is not None and
            self.relative_record_set_name is not None and
            self.record_type is not None):
            self.results['record_sets'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.zone_name is not None and
              self.record_type is not None):
            self.results['record_sets'] = self.format_item(self.list_by_type())
        elif (self.resource_group is not None and
              self.zone_name is not None):
            self.results['record_sets'] = self.format_item(self.list_by_dns_zone())
        elif (self.resource_group is not None and
              self.zone_name is not None):
            self.results['record_sets'] = self.format_item(self.list_all_by_dns_zone())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.get(resource_group_name=self.resource_group,
                                                        zone_name=self.zone_name,
                                                        relative_record_set_name=self.relative_record_set_name,
                                                        record_type=self.record_type)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_type(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.list_by_type(resource_group_name=self.resource_group,
                                                                 zone_name=self.zone_name,
                                                                 record_type=self.record_type,
                                                                 top=self.top,
                                                                 recordsetnamesuffix=self.recordsetnamesuffix)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_dns_zone(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.list_by_dns_zone(resource_group_name=self.resource_group,
                                                                     zone_name=self.zone_name,
                                                                     top=self.top,
                                                                     recordsetnamesuffix=self.recordsetnamesuffix)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all_by_dns_zone(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.list_all_by_dns_zone(resource_group_name=self.resource_group,
                                                                         zone_name=self.zone_name,
                                                                         top=self.top,
                                                                         record_set_name_suffix=self.record_set_name_suffix)
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
    AzureRMRecordSetInfo()


if __name__ == '__main__':
    main()
