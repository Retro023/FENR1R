import subprocess
import json


def get_disks():

    try:
        result = subprocess.run(
            [
                "lsblk",
                "-J",
                "-o",
                "NAME,PATH,FSTYPE,SIZE,MOUNTPOINTS,TYPE,UUID,LABEL",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        data = json.loads(result.stdout)

    except (subprocess.CalledProcessError, json.JSONDecodeError, FileNotFoundError):
        return "Unable to retrieve disk information.\n"

    output = []

    def walk(devices, indent=0):
        for dev in devices:
            prefix = "  " * indent

            output.append(f"\n{prefix}Device: {dev.get('name', 'Unknown')}")
            output.append(f"{prefix}Path: {dev.get('path', 'Unknown')}")
            output.append(f"{prefix}Type: {dev.get('type', 'Unknown')}")
            output.append(f"{prefix}Size: {dev.get('size', 'Unknown')}")
            output.append(f"{prefix}Filesystem: {dev.get('fstype', 'Unknown')}")
            output.append(f"{prefix}UUID: {dev.get('uuid', 'Unknown')}")
            output.append(f"{prefix}Label: {dev.get('label', 'None')}")

            mounts = dev.get("mountpoints")
            if mounts:
                output.append(f"{prefix}Mountpoints: {mounts}")

            if dev.get("children"):
                walk(dev["children"], indent + 1)

    walk(data["blockdevices"])

    return "\n".join(output)


def get_Luks():

    try:
        result = subprocess.run(
            [
                "lsblk",
                "-J",
                "-o",
                "NAME,PATH,FSTYPE,SIZE,MOUNTPOINTS,TYPE",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        data = json.loads(result.stdout)

    except (subprocess.CalledProcessError, json.JSONDecodeError, FileNotFoundError):
        return "Unable to retrieve LUKS information.\n"

    output = []

    def walk(devices):
        for dev in devices:
            if dev.get("fstype") == "crypto_LUKS":
                output.append("Found LUKS device:")
                output.append(f"  Name: {dev.get('name', 'Unknown')}")
                output.append(f"  Path: {dev.get('path', 'Unknown')}")
                output.append(f"  Size: {dev.get('size', 'Unknown')}")
                output.append("")

            if dev.get("children"):
                walk(dev["children"])

    walk(data["blockdevices"])

    if not output:
        return "No LUKS devices found.\n"

    return "\n".join(output)
