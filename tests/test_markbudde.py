#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test empty
'''

import nose, sys
import pydna 

def test_empty():
    ''' test mark budde'''
    a = pydna.read('tests/pGREG505.gb')
    assert a.name == "pGREG505"
    assert a.looped().name == "pGREG505"
    #assert a.annotations == "pGREG505"
    assert a.id == "pGREG505"
    assert a.looped().id == "pGREG505"

    """
    >>> a = pydna.read('pGREG505.gb')
    >>> a.name
    'pGREG505'
    >>> a.looped().name
    'pGREG505'
    >>> a.annotations
    {'comment': '\nApEinfo:methylated:1', 'source': '', 'taxonomy': [], 'keywords': [''], 'accessions': ['pGREG505'], 'data_file_division': '   ', 'date': '15-DEC-2012', 'organism': '. .'}
    >>> a.id
    'pGREG505'
    >>> a.looped().id
    'pGREG505'
    >>> 
    """

if __name__ == '__main__':
    nose.runmodule(argv=[sys.argv[0], '--nocapture'])