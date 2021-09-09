import subprocess
import json

container_status_stdout = subprocess.check_output(["docker", "inspect", "demo-system_service2_1"])
container_status = json.loads(container_status_stdout)

service2_container_pid = container_status[0]["State"]["Pid"]

# This needs Linux
subprocess.check_output(["sudo", "nsenter", "-t", str(service2_container_pid), "-n", "tc", "qdisc", "del", "dev", "eth0", "root"])