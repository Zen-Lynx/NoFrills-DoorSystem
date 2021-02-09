#################################################################
#  PLEASE DO NOT USE THIS FILE FOR PRODUCTION ENV! INSECURE!    #
#  THIS APPLICATION HAS BEEN CREATED FOR TESTING USE AT NO      #
#  FRILLS SHEDIAC NB. HARDWARE IS PROPRIETARY ON THE NoName     #
#  BOARD IN TESTING CURRENTLY. DO NOT USE THIS CODE IN          #
#  PRODUCTION! THANK YOU!                                       #
#################################################################



import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('/nofrills')

# Create server listening the port 4933 according to policys 
server_object = HTTPServer(server_address=('', 4933), RequestHandlerClass=CGIHTTPRequestHandler)

# Start the web server
server_object.serve_forever()
