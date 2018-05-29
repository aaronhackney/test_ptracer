import ssl
import base64
import random
import urllib
import urllib2
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser


class ASDM(object):

    def __init__(self):
        self.asdm_endpoint = None
        self.headers = None
        self.b64_credentials = None
        self.ctx = None
        self.response = None
        self.action = None
        self.data = None
        return

    def set_credentials(self, username, password):
        self.b64_credentials = base64.b64encode(username + ':' + password)

    def set_headers(self):
        self.headers = {
            'Content-Type': 'text/xml',
            'Authorization': 'Basic ' + self.b64_credentials
        }

    def set_ssl_insecure(self):
        # !!! DO NOT IGNORE CERTIFICATE VALIDITY IN PRODUCTION !!!
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False         # Ignore SSL hostname validity on handshake
        self.ctx.verify_mode = ssl.CERT_NONE    # Ignore SSL certificate validity (self signed)

    def set_asdm_endpoint(self, asa_ip, asdm_port):
        self.asdm_endpoint = 'https://' + asa_ip + ':' + str(asdm_port) + '/admin/config'

    def asdm_call(self):
        req = urllib2.Request(self.asdm_endpoint, self.data, headers=self.headers)
        response = urllib2.urlopen(req, context=self.ctx)
        if response.code == 200:
            self.response = urllib.unquote_plus(response.read())
            self._parse_asdm_ptracer()

    def _parse_asdm_ptracer(self):
        h = HTMLParser()
        self.response = h.unescape(self.response)               # Convert lt; to < and gt; to > and other HTML encodings

        soup = BeautifulSoup(self.response, "html.parser")      # Parse the HTML tags
        test = soup.find_all('result')                          # Find all of the <result> </result> tags
        for t in test:
            if t.find('action'):                                # Look for the final <action></action> tags
                self.action = t.find('action').text

    def set_ptrace_data(self, source_ip, dest_ip, dest_port):
        # Create a packet tracer with the given parameters and a random source port
        self.data = ('<?xml version="1.0" encoding="ISO-8859-1"?><config-data config-action="merge" '
                     'errors="continue"><cli id="0">packet-tracer input outside tcp ' + source_ip + ' ' +
                     str(random.randint(1024, 65535)) + ' ' + dest_ip + ' ' + str(dest_port) +
                     ' xml</cli></config-data>')
        return
