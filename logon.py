from cloudshell.api.cloudshell_api import CloudShellAPISession
import sys

session = CloudShellAPISession("10.0.0.55",
                               "admin",
                               sys.argv[1],
                               "Global")  ##make sure 
