# Open CMD session as Admin
    # Run: pip install requests
        # install and upgrade as prompted

# Register application in tenant's Entra ID admin center
# to generate authentication credential and secret

"""
Rename Devices in Intune
"""

import requests
import json

# Replace these values with your own
tenant_id = '[REDACTED]'
client_id = '[REDACTED]' 
client_secret = '[REDACTED]'
device_id = '[REDACTED]'
new_device_name = 'NewName'

# Get OAuth token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}

token_response = requests.post(token_url, data=token_data)
token = token_response.json().get('access_token')

# Rename device using Microsoft Graph API
rename_url = f'https://graph.microsoft.com/v1.0/devices/{device_id}'
rename_data = {
    'displayName': new_device_name
}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

rename_response = requests.patch(rename_url, headers=headers, data=json.dumps(rename_data))

if rename_response.status_code == 200:
    print(f"Device {device_id} successfully renamed to {new_device_name}")
else:
    print(f"Failed to rename device. Status code: {rename_response.status_code}, Response: {rename_response.text}")
