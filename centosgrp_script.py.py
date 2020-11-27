#!/usr/bin/env python3

#import the os module to interact with the system
import os 

# the for loop in the range of 4 to execute the commands four times.
for i in range(4):
    
    # ask the user for the group name and store it in variable called group
    group = input("Enter the name of the group to add:")

    # execute the command groupadd to create the group
    os.system("sudo groupadd %s" %group)

    # execute the command mkdir to create the group folder and the policies and companypolicy inside the group folder.
    os.system("sudo mkdir /home/%s" %group)
    os.system("sudo mkdir /home/%s/policies" %group) 
    os.system("sudo mkdir /home/%s/companypolicy" %group)

    # execute the command mkdir to add each group to skeleton.
    os.system("sudo mkdir /etc/skel/%s" %group)

    # execute the command chgrp to associate each group with it folder.
    os.system("sudo chgrp %s /home/%s" %(group,group))

    #execute the command chmod to change permission for the policies to read only.
    os.system("sudo chmod 440 /home/%s/policies" %group)

    # execute the command chmod to change permission for the companypolicy to public read only.
    os.system("sudo chmod 444 /home/%s/companypolicy" %group)

    # here the group is named temps use the quota to set a limit to their disk usage
    if(group == "temp"):
        os.system("sudo edquota -g %s" %group)
