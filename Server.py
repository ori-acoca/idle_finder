import subprocess

class Server:
    def __init__(self, name):
        self._name = name
        self._ping_status = None
        self._ssh_status = None
        self._weka_installed = None
        self._is_backend = None
        self._cluster_guid = None
        self._has_io = None
        self._has_wekafs_mount = None

    @property
    def name(self):
        return self._name

    @property
    def ping_status(self):
        return self._ping_status

    @property
    def ssh_status(self):
        return self._ssh_status

    @property
    def weka_installed(self):
        return self._weka_installed

    @property
    def is_backend(self):
        return self._is_backend

    @property
    def cluster_guid(self):
        return self._cluster_guid

    @property
    def has_io(self):
        return self._has_io

    @property
    def has_wekafs_mount(self):
        return self._has_wekafs_mount

    def check_ping(self):
        command = ["ping", "-c", "1", self.name]
        result = subprocess.run(command, capture_output=True, text=True)
        self._ping_status = result.returncode == 0

    def check_ssh(self):
        command = ["ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name, "echo 'SSH is available'"]
        result = subprocess.run(command, capture_output=True, text=True)
        self._ssh_status = result.returncode == 0

    def check_if_weka_installed(self):
        command = [
            "ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name,
            "weka -v | grep -q 'Weka' && echo 'TRUE' || echo 'FALSE'"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        self._weka_installed = result.stdout.strip() == "TRUE"

    def check_if_server_is_a_backend(self):
        command = [
            "ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name,
            "weka local ps | grep -Eq 'compute|drive' && echo 'TRUE' || echo 'FALSE'"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        self._is_backend = result.stdout.strip() == "TRUE"

    def get_cluster_guid(self):
        command = [
            "ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name,
            "weka local status -v | grep 'Cluster Membership' | uniq | awk '{print $4}' | tr -d '()'"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if "MODE" in result.stdout:
            self._cluster_guid = "STEM MODE"
        elif "(" and ")" and "-" in result.stdout:
            self._cluster_guid = result.stdout.strip()
        else:
            self._cluster_guid = "unknown"

    def check_if_the_cluster_has_io(self):
        command = [
            "ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name,
            "weka stats --category ops --stat WRITE_BYTES,READ_BYTES --start-time -72h | "
            "awk '{print \$5}' | grep -v VALUE | sort | uniq | grep -vw '0' > /dev/null && echo TRUE || echo FALSE"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        self._has_io = result.stdout.strip() == "TRUE"

    def check_if_has_wekafs_mount(self):
        command = [
            "ssh", "-i", "~/.ssh/weka_dev_ssh_key", self.name,
            "mount | grep -q 'weka' && echo 'TRUE' || echo 'FALSE'"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        self._has_wekafs_mount = result.stdout.strip() == "TRUE"