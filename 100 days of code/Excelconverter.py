import csv

clients = []
client_server = {}
servers_client = []

with open("new 3.txt", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for lines in csv_reader:
        client = lines[1]
        server_patch_group = lines[0]
        if client not in clients:
            clients.append(client)
    for client in clients:
        client_server[client] = []


for c_clients in clients:
    print(f'this is {c_clients}')
    with open("new 3.txt", "r") as csv_ffile :
        for lines in csv_ffile :
            extracted_server = lines[0]
            extracted_client = lines[1]
            
            if c_clients == extracted_client :
                client_server[extracted_client].append(extracted_server)
                print(extracted_server , extracted_client)

print(client_server)
