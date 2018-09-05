import nmap

ns = nmap.PortScanner()

print(ns.nmap_version())

# ns.scan('192.168.1.1/24', '22-445', '-v --version-all')

ns.scan('192.168.1.1', '22-445', '-v --version-all')

# print(ns.scaninfo())

# print(ns.csv())

print(f'scanstats:\n{ns.scanstats()}')

# print(f'all_hosts:\n{ns.all_hosts()}')

# print(ns['192.168.1.1'].state())

# print(ns['192.168.1.1'].all_protocols())

# print(ns['192.168.1.1']['tcp'].keys())

print(ns['192.168.1.1'].has_tcp(80))
