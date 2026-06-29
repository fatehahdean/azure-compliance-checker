from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
import subprocess
import json

# Get subscription ID
result = subprocess.run(['az', 'account', 'show'], capture_output=True, text=True)
account = json.loads(result.stdout)
subscription_id = account['id']

print(f"Connected to subscription: {account['name']}")
print("-" * 50)

# Authenticate
credential = AzureCliCredential()

# Check resource groups and tagging
resource_client = ResourceManagementClient(credential, subscription_id)
print("\nRESOURCE GROUP TAGGING COMPLIANCE:")
for rg in resource_client.resource_groups.list():
    tags = rg.tags or {}
    status = "OK" if tags else "WARNING - No tags"
    print(f"  {rg.name}: {status}")

# Check VMs
compute_client = ComputeManagementClient(credential, subscription_id)
print("\nVIRTUAL MACHINE STATUS:")
vms = list(compute_client.virtual_machines.list_all())
if not vms:
    print("  No VMs found in subscription")
else:
    for vm in vms:
        print(f"  {vm.name} - Location: {vm.location}")

print("\nAudit complete.")
