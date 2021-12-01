# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

# then press play in Coppelia Sim, then run code to import sim and connect 
# Spyder to CoppeliaSim 


import sim
import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

# Getting Handles for Joints
errorCode, Joint1=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint1', sim.simx_opmode_blocking)
errorCode, Joint2=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint2', sim.simx_opmode_blocking)
errorCode, Joint3=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint3', sim.simx_opmode_blocking)
errorCode, Joint4=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint4', sim.simx_opmode_blocking)
errorCode, Joint5=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint5', sim.simx_opmode_blocking)
errorCode, Joint6=sim.simxGetObjectHandle(clientID, 'NiryoOneJoint6', sim.simx_opmode_blocking)

# Getting Handle for Dummy Objects
errorCode, EndEffector=sim.simxGetObjectHandle(clientID, 'EndEffector', sim.simx_opmode_blocking)
errorCode, Dummy1=sim.simxGetObjectHandle(clientID, 'Dummy1', sim.simx_opmode_blocking)
errorCode, Dummy2=sim.simxGetObjectHandle(clientID, 'Dummy2', sim.simx_opmode_blocking)
errorCode, Dummy3=sim.simxGetObjectHandle(clientID, 'Dummy3', sim.simx_opmode_blocking)
errorCode, Dummy4=sim.simxGetObjectHandle(clientID, 'Dummy4', sim.simx_opmode_blocking)
errorCode, Dummy5=sim.simxGetObjectHandle(clientID, 'Dummy5', sim.simx_opmode_blocking)

# Initial Position of all joints

returncode, position2_0 = sim.simxGetObjectPosition(clientID, Joint2, Joint2, sim.simx_opmode_blocking)
returncode, position3_0 = sim.simxGetObjectPosition(clientID, Joint3, Joint2, sim.simx_opmode_blocking)
returncode, position4_0 = sim.simxGetObjectPosition(clientID, Joint4, Joint3, sim.simx_opmode_blocking)
returncode, position5_0 = sim.simxGetObjectPosition(clientID, Joint5, Joint4, sim.simx_opmode_blocking)
returncode, position6_0 = sim.simxGetObjectPosition(clientID, EndEffector, Dummy5, sim.simx_opmode_blocking)


# Getting Handles for Links
# errorCode, Link1=sim.simxGetObjectHandle(clientID, 'redundantRob_link1', sim.simx_opmode_blocking)
# errorCode, Link2=sim.simxGetObjectHandle(clientID, 'redundantRob_link2', sim.simx_opmode_blocking)
# errorCode, Link3=sim.simxGetObjectHandle(clientID, 'redundantRob_link3', sim.simx_opmode_blocking)
# errorCode, Link4=sim.simxGetObjectHandle(clientID, 'redundantRob_link4', sim.simx_opmode_blocking)
# errorCode, Link5=sim.simxGetObjectHandle(clientID, 'redundantRob_link5', sim.simx_opmode_blocking)
# errorCode, Link6=sim.simxGetObjectHandle(clientID, 'redundantRob_link6', sim.simx_opmode_blocking)
# errorCode, Link7=sim.simxGetObjectHandle(clientID, 'redundantRob_link7', sim.simx_opmode_blocking)

# Giving joints an initial velocity
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint1,0.00,sim.simx_opmode_streaming ) #Base joint does not move in this simulation
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint2,0.04,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint3,0.04,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint4,0.05,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint5,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint6,0.0,sim.simx_opmode_streaming )


time.sleep(0.5)

returncode, orientation = sim.simxGetObjectOrientation(clientID, EndEffector, -1, sim.simx_opmode_blocking)
returncode, position = sim.simxGetObjectPosition(clientID, EndEffector, -1, sim.simx_opmode_blocking)
errorcode1, linearV, angularV=sim.simxGetObjectVelocity(clientID, EndEffector, sim.simx_opmode_blocking)

time.sleep(0.1)

errorcode= sim.simxSetJointTargetVelocity(clientID, Joint1,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint2,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint3,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint4,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint5,0.0,sim.simx_opmode_streaming )
errorcode= sim.simxSetJointTargetVelocity(clientID, Joint6,0.0,sim.simx_opmode_streaming )


#(clientID, Joint1, 5, sim.simx_opmode_streaming)