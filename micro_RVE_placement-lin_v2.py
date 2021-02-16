# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:47:24 2018

@author: a0132600
"""

# -*- coding: utf-8 -*-
# file
import string
import math
import sys
import os
pi=3.1415926

os.chdir('C:\\Users\\a0132600\\Google Drive\\Zhi Jie\\FE2-2D-v2\\')#directory in which the .inp file is generated
keyword=['*Node','*Element, type=CPS4'];#modify second keyword if CPS4 elements are not used by looking at input file
f1=open('beam-macro.inp','r+')#input file name

FE_2_model_gen='FE2-RVE-placement_v3'#name of python script that will place the RVEs at the Gauss points
model='Model-2'#model name which the generated python script needs to modify
RVE_part_name='Part-1'#RVE part name(microscale) to be same as part name in GUI)
macro_part_name='beam'# macroscale mesh part name
macro_instance_name='beam-1'# macroscale mesh part instance name given in assembly instance
RVE_center=(47.200001,47.200001,0.)#RVE center co-ordinates from the Part-module

Nodes=[];
nodal_connectvity=[];

# Gauss points in the natural coordinates
GPs=([[-3**-0.5,-3**-0.5,0],[3**-0.5,-3**-0.5,0],[3**-0.5,3**-0.5,0],[-3**-0.5,3**-0.5,0]])


inp=[]
#////////////////////////    read in all the lines in the input file
while 1:
	line=f1.readline()
	if not line:
		break
	line=line.strip()
	inp.append(line)
#///////////////////////     search the line2 after line in inp, and assign the variables 
#starting from the start line number after line2
def Search_line(inp,line,line2,array,start):
    array[:]=[]
    b=inp.index(line);
    a=inp[b:].index(line2)
    
    if (inp[a].count("generate")==0):
        #print('if')
        for line_temp in inp[(b+a+start):]:
            if (line_temp=='') or (line_temp.count("*")!=0):
    		    break
            line_temp=(line_temp.replace(',','')).split()
            array.append(line_temp)
    else:
        #print('else')
        for line_temp in inp[(a+1):]:
            if (line_temp=='') or (line_temp.count("*")!=0):
    			break
            line_temp=(line_temp.replace(',','')).split()
            for i in range(int(line_temp[0]),(int(line_temp[1])+1),int(line_temp[2])):   
                array.append(i)
#////
def tsi_eta_shape_fn(tsi,eta):
    N1=float(0.25*(1-tsi)*(1-eta))
    N2=float(0.25*(1+tsi)*(1-eta))
    N3=float(0.25*(1+tsi)*(1+eta))
    N4=float(0.25*(1-tsi)*(1+eta))
    return N1,N2,N3,N4


Search_line(inp,'*Part, name='+macro_part_name,keyword[0],Nodes,1);#node no, x,y,x
Search_line(inp,'*Part, name='+macro_part_name,keyword[1],nodal_connectvity,1);#element no,N1,N2,N3,N4

if (len(nodal_connectvity[0])==5):
    order=1;
else:
    print('number of nodes does not correspond to linear elements')
    
RVE=open('%s.py'%(FE_2_model_gen),'w')

print>>RVE, "from abaqus import *"
print>>RVE, "from abaqusConstants import *"
a='''
#==========import modulus of abaqus
import part
import regionToolset
import displayGroupMdbToolset as dgm
import material
import section
import assembly
import step
import interaction
import load
import mesh
import job
import sketch
import visualization
import xyPlot
import displayGroupMdbToolset as dgm
'''
RVE.write(a)

#=====================   construction of the RVE cell
a='''
import numpy as np
import math
a1 = mdb.models['%s'].rootAssembly
'''%(model)
RVE.write(a)
for i in range(0,len(Nodes)):
    print>>RVE,"a1.Set(name='N%s-RP', nodes=(a1.instances['%s'].nodes[%s:%s],))"%(str(i+1),str(macro_instance_name),str(i),str(i+1))

for i in range(0,len(nodal_connectvity)):
    ele_no=int(nodal_connectvity[i][0]);
    
    n1=int(nodal_connectvity[i][1])
    n2=int(nodal_connectvity[i][2])
    n3=int(nodal_connectvity[i][3])
    n4=int(nodal_connectvity[i][4])
    
    X1=float(Nodes[n1-1][1])
    Y1=float(Nodes[n1-1][2])
        
    X2=float(Nodes[n2-1][1])
    Y2=float(Nodes[n2-1][2])
    

    X3=float(Nodes[n3-1][1])
    Y3=float(Nodes[n3-1][2])

    
    X4=float(Nodes[n4-1][1])
    Y4=float(Nodes[n4-1][2])

    for ii in range(1,(len(GPs)+1)):
        if order==1:
            N1,N2,N3,N4=tsi_eta_shape_fn(GPs[ii-1][0],GPs[ii-1][1]);
            position_x=N1*X1+N2*X2+N3*X3+N4*X4-RVE_center[0]
            position_y=N1*Y1+N2*Y2+N3*Y3+N4*Y4-RVE_center[1]
            position_z=0.0-RVE_center[2] # since this 2D element
                   
        print>>RVE, '#=========When assembling  '+'Super ele-'+str(ele_no)+'-RVE @ GP-'+str(ii)
        a='''a = mdb.models['%s'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
'''%(model)
        RVE.write(a)
        
        print>>RVE, "p = mdb.models['%s'].parts['"%(model)+str(RVE_part_name)+"']"
        
        print>>RVE, "a.Instance(name='Part-1-ele-%s-GP-%s', part=p, dependent=ON)" %(str(ele_no),str(ii))	
        print>>RVE, "p2 = a.instances['Part-1-ele-%s-GP-%s']" %(str(ele_no),str(ii))	
        a='''a = mdb.models['%s'].rootAssembly
a = mdb.models['%s'].rootAssembly
'''%(model,model)
        RVE.write(a)	
        
        angle_x=0.0
        angle_y=0.0
        angle_z=0.0
        print>>RVE,'p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=%s)'   %(str(angle_x))
        print>>RVE,'p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=%s)'   %(str(angle_y))
        print>>RVE,'p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=%s)'   %(str(angle_z))
        print>>RVE, "p2.translate(vector=(%s,%s,%s))"   %(str(position_x),str(position_y),str(position_z))
        print>>RVE, "a = mdb.models['%s'].rootAssembly"%(model)
        print>>RVE, "p2 = a.instances['Part-1-ele-%s-GP-%s']" %(str(ele_no),str(ii))
        print>>RVE,''

       
 
RVE.close()
f1.close()



