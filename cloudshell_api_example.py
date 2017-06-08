from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys

server_ip = sys.argv[1] ##'172.31.22.239' ## This is the internal IP of our CloudShell in AWS
reservation_id = sys.argv[2]
DEPLOYED_APP_MODEL = 'Generic Deployed App'

session = CloudShellAPISession(server_ip,
                               sys.argv[3],
                               sys.argv[4],
                               sys.argv[5])  ##make sure 
										  ##to pass these credentials from jenkins and don't store them in GitHub!!

print session.GetUserDetails('admin').Name
