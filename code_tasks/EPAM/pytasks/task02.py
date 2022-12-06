#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'

# Task02-01
# Create *very* simple http server which can execute shell (not all, due to HTTP URL restrictions) command
# on host and returns stdout as plain text: `http:/<IP>:<PORT>/shell;<CMD>`
# - Use only standard python library.
# - At the same time can be executed a few commands.
# - Pay attention on HTTP headers and encoding (respects cyrillic alphabet).
# - Make sure there are no errors in developers console (firefox).

# Addition info:
# GIL - Global Interpreter Lock
# BaseHTTPServer uses classes from SocketServer to create base classes for making HTTP servers.
# HTTPServer can be used directly, but the BaseHTTPRequestHandler is intended to be extended to handle each
# protocol method (GET, POST, etc.).
# HTTPServer is a simple subclass of SocketServer.TCPServer, and does not use multiple threads or processes
# to handle requests. To add threading or forking, create a new class using the appropriate mix-in from SocketServer.

import urllib2
import subprocess
from urlparse import urlparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from time import strftime

# Input for main
port = 7777
hostname = 'localhost'

class Handler(BaseHTTPRequestHandler, object):

    def __init__(self, *args, **kwargs):
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
        Handler.Get_handler_full2()

    #Input for class
    encode = 'UTF-8' # encoding
    urlshell = u'/shell' # path in URL
    handles = [] # empty list of handles

    # Respond to a GET request
    def do_GET(self):
        req = urlparse(urllib2.unquote(self.path).decode('UTF-8'))
        # reg - parse URLs into components
        # http://127.0.0.1:7777/shell;ls
        # ParseResult(scheme='', netloc='', path=u'/shell', params=u'ls', query='', fragment='')

        if req.path == self.urlshell: # if shell; in URL
            stdout = self.Run_url(req.params) # get stdout from run shell command
            self.Response(200, req.params, stdout) # OK + stdout (content)

        elif req.path in Handler.handles: # if /date in URL
            id = Handler.handles.index(req.path) # id +1 (element) of list will be function
            self.Response(200,'',str(Handler.handles[id+1]()))  # () used in order to convert object to value

        elif req.path == '/': # if root dir in URL
            self.Response(200) # OK

        elif (req.path != self.urlshell) and (req.path != '/') and (req.path not in Handler.handles): # if no in above
            self.Response(404) # Not Found

    # Response (return status and provide header)
    def Response(self, id, command=None, content=None):
        self.send_response(id)
        self.send_header('Content-type', 'text/html; charset=%s' % (self.encode))
        self.end_headers()
        self.wfile.write('<html><head><title>HTTP server (URL to SHELL)</title></head>')
        self.wfile.write('<body><p><b>Client:</b> %s\n</p>' % str(self.client_address))
        self.wfile.write('<body><p><b>User-agent:</b> %s\n</p>' % str(self.headers['user-agent']))
        self.wfile.write('<body><p><b>Path:</b> %s\n</p>' % self.path)
        self.wfile.write('<body><p><b> HTTP code:</b> %s\n</p>' % id)
        if command != '' and content is not None: # for shell;
            self.wfile.write('<body><p><b>The shell command has been executed via URL in HTTP server:</b><p>')
            self.wfile.write('<body><p><b>Command:</b><p> %s via http://%s:%d/shell;%s' % (command,hostname,port,command))
            self.wfile.write('<body><p><b>Result:</b><p> %s' % (content.encode(self.encode)))
        if command == '' and content is not None: # for /data
            self.wfile.write('<body><p><b>The shell command has been executed via URL in HTTP server:</b><p>')
            self.wfile.write('<body><p><b>Result:</b><p> %s' % (content.encode(self.encode)))
        self.wfile.write("</body></html>")

    # Run command from URL used subprocess and stdout execution result
    def Run_url(self, command):
        cmd = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, stderr = cmd.communicate()
        return output.decode()

    # Class-based plug-in model for handing requests (task05-01)
    @classmethod
    # @staticmethod
    def Get_handler_full2(self):
    # def Get_handler_full2():
        for h in Handler.__subclasses__():
            if '__url__' in dir(h) and 'Get_handler2' in dir(h):
                Handler.handles = [h.__url__,h.Get_handler2]

# Handle requests in a separate thread
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer): pass

# Run HTTPServer (Multithreaded web server)
def Server():
    server = ThreadedHTTPServer((hostname, port), Handler)
    print 'HTTPServer %s:%d has started in %s' % (hostname, port, str(strftime('%Y-%m-%d %H:%M:%S')))
    print 'Use <Ctrl-C> to stop'
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.shutdown()
    server.server_close()
    print 'HTTPServer %s:%d has closed in %s' % (hostname, port, str(strftime('%Y-%m-%d %H:%M:%S')))

# Run HTTPClient (make the requests in parallel the threaded HTTPServer)
def Client():
    pass

# Decorator-based plug-in model for handing requests (task05-02)
def Get_handler(url):
    def Get_handler_full(function):
        Handler.handles = [url, function] # list items to match in URL [/date, function_date]
        return function
    return Get_handler_full

# Server()
# Client()
if __name__ == '__main__':
    Server(), Client()