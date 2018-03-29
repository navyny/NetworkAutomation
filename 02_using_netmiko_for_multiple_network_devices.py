import netmiko

#using Docstring '''
#A Docstring is a string of text ecapulated in 3 single quotes (or)  3 double quotes
#Using strip() to strip white spaces on either side...and splitlines() to create a list
 

devices = """
10.200.130.5
10.200.130.6
10.200.130.7
10.200.140.5
""".strip().splitlines()

device_type = 'cisco_ios'
username = 'vallabh'
password = '*******'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

#for device in devices:
#	connection =netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
#	print(connection.send_command('show clock'))
#	connection.disconnect()


#If there was an error in authenticating to second network device in list...the script would stop.
#In order to avoid this (catch the exception...and continue to nect devices in loop)

for device in devices:
    try:
        print('~' * 79)
        print('Connecting to device:', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
                                            username=username, password=password)
        print(connection.send_command('show clock'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
