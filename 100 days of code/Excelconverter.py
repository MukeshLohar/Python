import csv,os

clients = []
client_server = {}
servers_client = []
def extract_client(inputfilename):
    """ This function will extract client and return back text file/s for individual patch group for a client"""
    global client_server
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    filepath =(os.path.join(desktop,"SCM_Patching_Grouping"))
    if os.path.exists(filepath) :
        pass
    else:
        os.makedirs(filepath)
    with open(inputfilename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for lines in csv_reader:
            client = lines[1]
            
            if client not in clients:
                clients.append(client)
        for client in clients:
            client_server[client] = []

        csv_file.seek(0)
        for rows in csv_reader:
            extracted_server = rows[0]
            extracted_client = rows[1]

            if extracted_client in client_server:

                client_server[extracted_client].append(extracted_server)


    client_server = dict(sorted(client_server.items()))
    print("\n\n")
    for key, values in client_server.items():
        
        clientfilename = (os.path.join(desktop,"SCM_Patching_Grouping",(f"{str(key)} ({len(values)}).txt")))
        
        with open(clientfilename, 'w+') as newfile:
            for n in values:
                newfile.write(f'{n} \n')
                
        print(f"{key} has these {len(values)} \n")


extract_client("C:\\Temp\\temp.csv") #provide your inputfile in quotes


