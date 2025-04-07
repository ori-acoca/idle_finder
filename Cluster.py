class Cluster:
    def __init__(self, guid):
        self.guid = guid
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def check_cluster_status(self):
        for server in self.servers:
            server.check_if_the_cluster_has_io()
            if not server.has_io:
                print(f"Flag: Server {server.name} in cluster {self.guid} has no I/O activity in the last 5 hours")