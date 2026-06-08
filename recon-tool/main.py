import socket 
from pyparsing import line
import requests

ports = [21, 22, 80, 443, 8080, 3306, 5432]

target = input("Enter IP address or domain: ")
print(f"Scan target: {target}")   


def check_cves(banner):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {"keywordSearch": banner, "resultsPerPage": 3}
    response = requests.get(url, params=params)
    data = response.json()
    cves = data.get("vulnerabilities", [])
    results = []
    if cves:
        for cve in cves:
            cve_id = cve["cve"]["id"]
            description = cve["cve"]["descriptions"][0]["value"]
            results.append(f"  CVE: {cve_id} - {description[:100]}")
    return results


with open("results.txt", "w") as f:
    f.write(f"Scan target: {target}\n")
    for port in ports:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    if "OpenSSH" in banner:
                        keyword = "OpenSSH 8.9"
                    elif "FTP" in banner:
                        keyword = "GNU FTP"
                    else:
                        keyword = banner
                    cve_results = check_cves(keyword)
                    for line in cve_results:
                          print(line)
                          f.write(line + "\n")
                    print(f"Banner: {banner}")
                    f.write(f"Banner: {banner}\n")
                    print("-" * 20)
                    f.write("-" * 20 + "\n")

            except:
                pass
            print(f"Port {port} is open")
            f.write(f"Port {port} is open\n")
            print("-" * 20)
            f.write("-" * 20 + "\n")
        else:
            print(f"Port {port} is closed")
            f.write(f"Port {port} is closed\n")
            print("-" * 20)
            f.write("-" * 20 + "\n")

        sock.close()