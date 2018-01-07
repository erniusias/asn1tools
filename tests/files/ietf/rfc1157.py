EXPECTED = {'RFC1157-SNMP': {'extensibility-implied': False,
                  'imports': {'RFC1155-SMI': ['ObjectName',
                                              'ObjectSyntax',
                                              'NetworkAddress',
                                              'IpAddress',
                                              'TimeTicks']},
                  'object-classes': {},
                  'object-sets': {},
                  'types': {'GetNextRequest-PDU': {'tag': {'kind': 'IMPLICIT',
                                                           'number': 1},
                                                   'type': 'PDU'},
                            'GetRequest-PDU': {'tag': {'kind': 'IMPLICIT',
                                                       'number': 0},
                                               'type': 'PDU'},
                            'GetResponse-PDU': {'tag': {'kind': 'IMPLICIT',
                                                        'number': 2},
                                                'type': 'PDU'},
                            'Message': {'members': [{'name': 'version',
                                                     'type': 'INTEGER'},
                                                    {'name': 'community',
                                                     'type': 'OCTET STRING'},
                                                    {'name': 'data',
                                                     'type': 'PDUs'}],
                                        'type': 'SEQUENCE'},
                            'PDU': {'members': [{'name': 'request-id',
                                                 'type': 'INTEGER'},
                                                {'name': 'error-status',
                                                 'type': 'INTEGER'},
                                                {'name': 'error-index',
                                                 'type': 'INTEGER'},
                                                {'name': 'variable-bindings',
                                                 'type': 'VarBindList'}],
                                    'type': 'SEQUENCE'},
                            'PDUs': {'members': [{'name': 'get-request',
                                                  'type': 'GetRequest-PDU'},
                                                 {'name': 'get-next-request',
                                                  'type': 'GetNextRequest-PDU'},
                                                 {'name': 'get-response',
                                                  'type': 'GetResponse-PDU'},
                                                 {'name': 'set-request',
                                                  'type': 'SetRequest-PDU'},
                                                 {'name': 'trap',
                                                  'type': 'Trap-PDU'}],
                                     'type': 'CHOICE'},
                            'SetRequest-PDU': {'tag': {'kind': 'IMPLICIT',
                                                       'number': 3},
                                               'type': 'PDU'},
                            'Trap-PDU': {'members': [{'name': 'enterprise',
                                                      'type': 'OBJECT '
                                                              'IDENTIFIER'},
                                                     {'name': 'agent-addr',
                                                      'type': 'NetworkAddress'},
                                                     {'name': 'generic-trap',
                                                      'type': 'INTEGER'},
                                                     {'name': 'specific-trap',
                                                      'type': 'INTEGER'},
                                                     {'name': 'time-stamp',
                                                      'type': 'TimeTicks'},
                                                     {'name': 'variable-bindings',
                                                      'type': 'VarBindList'}],
                                         'tag': {'kind': 'IMPLICIT',
                                                 'number': 4},
                                         'type': 'SEQUENCE'},
                            'VarBind': {'members': [{'name': 'name',
                                                     'type': 'ObjectName'},
                                                    {'name': 'value',
                                                     'type': 'ObjectSyntax'}],
                                        'type': 'SEQUENCE'},
                            'VarBindList': {'element': {'type': 'VarBind'},
                                            'type': 'SEQUENCE OF'}},
                  'values': {}}}