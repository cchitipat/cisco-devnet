# import the ncclient library
from ncclient import manager

# Device Information
HOST = '10.10.20.48'
PORT = 830
USER = 'developer'
PASS = 'C1sco12345'

DEVICE = manager.connect(host=HOST, 
                         port=PORT, 
                         username=USER,
                         password=PASS, 
                         hostkey_verify=False,
                         device_params={'name': 'csr'},
                         allow_agent=False, 
                         look_for_keys=False)

# Get all supported
for DEVICE_Capability in DEVICE.server_capabilities:
    print (DEVICE_Capability)

# Close Session
DEVICE.close_session()