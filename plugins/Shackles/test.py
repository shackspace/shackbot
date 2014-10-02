###
# Copyright (c) 2014, rash
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from supybot.test import *
from mock import Mock, patch
import urllib2

class ShacklesTestCase(PluginTestCase):
    plugins = ('Shackles',)

    @patch('urllib2.urlopen')
    def testOnline(self, urlopenMock):
        readlineMock = Mock()
        expectedResponse = 'mock server response'
        readlineMock.readline.return_value = expectedResponse
        urlopenMock.return_value = readlineMock
        self.assertResponse('online', expectedResponse)

    @patch('urllib2.urlopen')
    def testURLError(self, urlopenMock):
        expectedResponse = 'Sorry, I cannot reach the magical proxybridge into the shack.'
        urlopenMock.side_effect = urllib2.URLError('')
        self.assertResponse('online', expectedResponse)

    @patch('urllib2.urlopen')
    def testHTTPError(self, urlopenMock):
        expectedResponse = 'Sorry, I cannot reach the magical proxybridge into the shack. (Code 500)'
        urlopenMock.side_effect = urllib2.HTTPError('http://mock.mock/mock', 500, 'Internal Server Error', None, None)
        self.assertResponse('online', expectedResponse)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
