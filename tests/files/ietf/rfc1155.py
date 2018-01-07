EXPECTED = {'RFC1155-SMI': {'extensibility-implied': False,
                 'imports': {},
                 'object-classes': {},
                 'object-sets': {},
                 'types': {'ApplicationSyntax': {'members': [{'name': 'address',
                                                              'type': 'NetworkAddress'},
                                                             {'name': 'counter',
                                                              'type': 'Counter'},
                                                             {'name': 'gauge',
                                                              'type': 'Gauge'},
                                                             {'name': 'ticks',
                                                              'type': 'TimeTicks'},
                                                             {'name': 'arbitrary',
                                                              'type': 'Opaque'}],
                                                 'type': 'CHOICE'},
                           'Counter': {'restricted-to': [(0, 4294967295)],
                                       'tag': {'class': 'APPLICATION',
                                               'kind': 'IMPLICIT',
                                               'number': 1},
                                       'type': 'INTEGER'},
                           'Gauge': {'restricted-to': [(0, 4294967295)],
                                     'tag': {'class': 'APPLICATION',
                                             'kind': 'IMPLICIT',
                                             'number': 2},
                                     'type': 'INTEGER'},
                           'IpAddress': {'size': [4],
                                         'tag': {'class': 'APPLICATION',
                                                 'kind': 'IMPLICIT',
                                                 'number': 0},
                                         'type': 'OCTET STRING'},
                           'NetworkAddress': {'members': [{'name': 'internet',
                                                           'type': 'IpAddress'}],
                                              'type': 'CHOICE'},
                           'ObjectName': {'type': 'OBJECT IDENTIFIER'},
                           'ObjectSyntax': {'members': [{'name': 'simple',
                                                         'type': 'SimpleSyntax'},
                                                        {'name': 'application-wide',
                                                         'type': 'ApplicationSyntax'}],
                                            'type': 'CHOICE'},
                           'Opaque': {'tag': {'class': 'APPLICATION',
                                              'kind': 'IMPLICIT',
                                              'number': 4},
                                      'type': 'OCTET STRING'},
                           'SimpleSyntax': {'members': [{'name': 'number',
                                                         'type': 'INTEGER'},
                                                        {'name': 'string',
                                                         'type': 'OCTET '
                                                                 'STRING'},
                                                        {'name': 'object',
                                                         'type': 'OBJECT '
                                                                 'IDENTIFIER'},
                                                        {'name': 'empty',
                                                         'type': 'NULL'}],
                                            'type': 'CHOICE'},
                           'TimeTicks': {'restricted-to': [(0, 4294967295)],
                                         'tag': {'class': 'APPLICATION',
                                                 'kind': 'IMPLICIT',
                                                 'number': 3},
                                         'type': 'INTEGER'}},
                 'values': {'directory': {'type': 'OBJECT IDENTIFIER',
                                          'value': ['internet', 1]},
                            'enterprises': {'type': 'OBJECT IDENTIFIER',
                                            'value': ['private', 1]},
                            'experimental': {'type': 'OBJECT IDENTIFIER',
                                             'value': ['internet', 3]},
                            'internet': {'type': 'OBJECT IDENTIFIER',
                                         'value': ['iso',
                                                   ('org', 3),
                                                   ('dod', 6),
                                                   1]},
                            'mgmt': {'type': 'OBJECT IDENTIFIER',
                                     'value': ['internet', 2]},
                            'private': {'type': 'OBJECT IDENTIFIER',
                                        'value': ['internet', 4]}}}}