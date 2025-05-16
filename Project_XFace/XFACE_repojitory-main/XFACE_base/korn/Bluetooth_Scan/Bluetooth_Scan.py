import subprocess

def get_bluetooth_status():
    try:
        print("Running hciconfig...")
        status_output = subprocess.check_output(['hciconfig'], stderr=subprocess.STDOUT)
        print("Bluetooth Status:")
        print(status_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error checking Bluetooth status:", e.output.decode('utf-8'))

def scan_bluetooth_devices():
    try:
        print("Running hcitool scan...")
        scan_output = subprocess.check_output(['sudo', 'hcitool', 'scan'], stderr=subprocess.STDOUT)
        print("Scanned Bluetooth Devices:")
        print(scan_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error scanning Bluetooth devices:", e.output.decode('utf-8'))

if __name__ == "__main__":
    print("Getting Bluetooth status...")
    get_bluetooth_status()
    print("Scanning for Bluetooth devices...")
    scan_bluetooth_devices()
