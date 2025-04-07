from Server import Server
from Cluster import Cluster

def main():

    servers = [
        "hp1", "hp2", "hp3", "hp4", "hp5", "hp6", "hp7", "hp8", "hp9", "hp10",
        "hp11", "hp12", "hp13", "hp14", "hp15", "hp16", "hp17", "hp18", "hp19", "hp20",
        "hp21", "hp22", "hp23", "hp24", "hp25", "hp26", "hp27", "hp28", "hp29", "hp30",
        "hp31", "hp32", "hp33", "srv-23-01", "srv-23-02", "srv-23-03", "srv-23-04", "srv-23-05",
        "srv-23-06", "srv-23-07", "srv-23-08", "srv-23-09", "srv-23-10", "srv-24-01", "srv-24-02",
        "srv-24-03", "srv-24-04", "srv-24-05", "srv-24-06", "srv-24-07", "srv-24-08", "srv-24-09",
        "srv-24-10", "srv-26-01", "srv-26-02", "srv-26-03", "srv-26-04", "srv-26-05", "srv-26-06",
        "srv-26-07", "srv-26-08", "srv-26-09", "srv-26-10", "srv-34-01", "srv-34-02", "srv-34-03",
        "srv-34-04", "srv-34-05", "srv-34-06", "srv-34-07", "srv-34-08", "srv-34-09", "srv-34-10",
        "srv-35-01", "srv-35-02", "srv-35-03", "srv-35-04", "srv-35-05", "srv-35-06", "srv-35-07",
        "srv-35-08", "srv-35-09", "srv-35-10", "srv-36-01", "srv-36-02", "srv-36-03", "srv-36-04",
        "srv-36-05", "srv-36-06", "srv-36-07", "srv-36-08", "srv-36-09", "wekabox1", "wekabox2",
        "wekabox3", "wekabox4", "wekabox5", "wekabox6", "wekabox7", "wekabox8", "wekabox9", "wekabox10",
        "wekabox11", "wekabox12", "wekabox13", "wekabox14", "wekabox15", "wekabox16", "wekabox17",
        "wekabox18", "wekabox20"
    ]

    servers_objects = [Server(name) for name in servers]
    for server in servers_objects:
        server.check_ping()
        if server.ping_status:
            server.check_ssh()
            if server.ssh_status:
                server.check_if_weka_installed()
                server.check_if_server_is_a_backend()
                server.get_cluster_guid()
                server.check_if_the_cluster_has_io()
                server.check_if_has_wekafs_mount()

        # Print the results
        print('\n')
        print(f"Server: {server.name}")
        print(f"Ping Status: {server.ping_status}")
        if server.ping_status:
            print(f"SSH Status: {server.ssh_status}")
            if server.ssh_status:
                print(f"Weka Installed: {server.weka_installed}")
                print(f"Is Backend: {server.is_backend}")
                print(f"Cluster GUID: {server.cluster_guid}")
                print(f"Has I/O: {server.has_io}")
                print(f"Has WekaFS Mount: {server.has_wekafs_mount}")

if __name__ == "__main__":
    main()