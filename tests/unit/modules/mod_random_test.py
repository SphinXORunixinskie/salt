# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Rupesh Tare <rupesht@saltstack.com>`
'''

# Import Salt Testing Libs
from salttesting import TestCase, skipIf
from salttesting.mock import (
    patch,
    NO_MOCK,
    NO_MOCK_REASON
)

# Import Salt Libs
from salt.modules import mod_random
import salt.utils.pycrypto
from salt.exceptions import SaltInvocationError

# Globals
mod_random.__grains__ = {}
mod_random.__salt__ = {}
mod_random.__context__ = {}
mod_random.__opts__ = {}


@skipIf(NO_MOCK, NO_MOCK_REASON)
class ModrandomTestCase(TestCase):
    '''
    Test cases for salt.modules.mod_random
    '''
    def test_hash(self):
        '''
        Test for Encodes a value with the specified encoder.
        '''
        self.assertEqual(mod_random.hash('value')[0:4], 'ec2c')

        self.assertRaises(SaltInvocationError,
                          mod_random.hash, 'value', 'algorithm')

    def test_str_encode(self):
        '''
        Test for The value to be encoded.
        '''
        self.assertRaises(SaltInvocationError,
                          mod_random.str_encode, 'None', 'abc')

        self.assertRaises(SaltInvocationError,
                          mod_random.str_encode, None)

        self.assertEqual(mod_random.str_encode('A'), 'QQ==\n')

    def test_get_str(self):
        '''
        Test for Returns a random string of the specified length.
        '''
        with patch.object(salt.utils.pycrypto,
                          'secure_password', return_value='A'):
            self.assertEqual(mod_random.get_str(), 'A')

    def test_shadow_hash(self):
        '''
        Test for Generates a salted hash suitable for /etc/shadow.
        '''
        with patch.object(salt.utils.pycrypto,
                          'gen_hash', return_value='A'):
            self.assertEqual(mod_random.shadow_hash(), 'A')


if __name__ == '__main__':
    from integration import run_tests
    run_tests(ModrandomTestCase, needs_daemon=False)
