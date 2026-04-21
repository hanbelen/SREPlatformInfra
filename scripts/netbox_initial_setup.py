import pynetbox
import os

# Connect to local NetBox
nb = pynetbox.api(
    url=os.environ.get('NETBOX_URL', 'http://localhost:8000'),
    token=os.environ.get('NETBOX_TOKEN', '0123456789abcdef0123456789abcdef01234567')
)

def bootstrap_netbox():
    print("🚀 Starting NetBox SRE Platform Bootstrap...")

    # 1. Standard Roles (3-character convention)
    roles = [
        {'name': 'Access', 'slug': 'acc', 'color': '9e9e9e'},
        {'name': 'Distribution', 'slug': 'dis', 'color': '4caf50'},
        {'name': 'Core', 'slug': 'cor', 'color': 'f44336'},
        {'name': 'Transit', 'slug': 'tra', 'color': '2196f3'},
    ]
    for role in roles:
        if not nb.dcim.device_roles.get(slug=role['slug']):
            print(f"  Creating Role: {role['name']} ({role['slug']})")
            nb.dcim.device_roles.create(**role)

    # 2. Manufacturers
    manufacturers = [
        {'name': 'Cisco', 'slug': 'cisco'},
        {'name': 'Nokia', 'slug': 'nokia'},
    ]
    for man in manufacturers:
        if not nb.dcim.manufacturers.get(slug=man['slug']):
            print(f"  Creating Manufacturer: {man['name']}")
            nb.dcim.manufacturers.create(**man)

    # 3. Device Types (Placeholders for our Lab)
    device_types = [
        {'manufacturer': {'slug': 'cisco'}, 'model': 'Generic Cisco', 'slug': 'generic-cisco'},
        {'manufacturer': {'slug': 'nokia'}, 'model': 'SR Linux', 'slug': 'sr-linux'},
    ]
    for dt in device_types:
        man_obj = nb.dcim.manufacturers.get(slug=dt['manufacturer']['slug'])
        if not nb.dcim.device_types.get(slug=dt['slug']):
            print(f"  Creating Device Type: {dt['model']}")
            nb.dcim.device_types.create(
                manufacturer=man_obj.id,
                model=dt['model'],
                slug=dt['slug']
            )

    print("✅ Bootstrap Complete. Platform is ready for Site Sync.")

if __name__ == "__main__":
    try:
        bootstrap_netbox()
    except Exception as e:
        print(f"❌ Error bootstrapping NetBox: {e}")
        print("Note: Ensure NetBox is running and the API token is valid.")
