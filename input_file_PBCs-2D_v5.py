# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:48:49 2018

@author: a0132600
"""
# for rectangualar macroscale elements, modify vertex_shape_fn and 
# also account for different volume scaling of RVE(microscale) for irregular elements as per eqn  

import string
import math
import sys
import os
import numpy as np
pi=3.1415926

os.chdir('C:\\Users\\a0132600\\Google Drive\\Zhi Jie\\FE2-2D-v2\\')#directory where input files are
f1=open('beam-macro-RVEs-model-2.inp','r+')#FE2-input file name

RVE_part_name='Part-1'# Part-name of RVE
macro_part_name='beam'# Part-name of macro-scale mesh
mod_inp='beam-macro-RVEs-FE2-run-model-2'# name of input file with all completed constraints
accuracy=7# no. of significant figures(digits) the shape functions are calculated upto

keyword=['*Node','*Element, type=CPS4','*Element, type=CPS4'];

# sets and eqns files are used for storing data needed to modify the inp file. 
# these are deleted after applying MPCs.
sets_data='sets'# name of .dat file in which nodal sets of Edge nodes of RVE will be defined
eqns_data='eqns'# name of .dat file in which the MPCs will be saved

Nodes=[];# list of RVE nodes(microscale)
# nodal_connectvity=[];# nodal connectivity of RVE(microscale)
SE_Nodes=[];# list of macroscale part nodes
SE_nodal_connectvity=[];
n_GP=5# (no of gauss point RVEs + 1)


Vertexes=['*Nset, nset=Vertex11','*Nset, nset=Vertex12','*Nset, nset=Vertex13','*Nset, nset=Vertex14',
          '*Nset, nset=M11','*Nset, nset=M12','*Nset, nset=M13','*Nset, nset=M14']


Faces=['*Nset, nset=Face11','*Nset, nset=Face12','*Nset, nset=Face13','*Nset, nset=Face14']


inp=[]

#////////////////////////    read in all the lines in the input file
while 1:
	line=f1.readline()
	if not line:
		break
	line=line.strip()
	inp.append(line)
    

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
                
def Search(inp,line,array):
    array[:]=[]
    a=inp.index(line);
    
    if (inp[a].count("generate")==0):
        for line_temp in inp[(a+1):]:
            if (line_temp=='') or (line_temp.count("*")!=0):
    		    break
            line_temp=(line_temp.replace(',','')).split()
            array.append(line_temp)
    else:
        for line_temp in inp[(a+1):]:
            if (line_temp=='') or (line_temp.count("*")!=0):
    			break
            line_temp=(line_temp.replace(',','')).split()
            for i in range(int(line_temp[0]),(int(line_temp[1])+1),int(line_temp[2])):   
                array.append(i)
        
def int_Search(inp,line,array):
	array[:]=[]
	a=inp.index(line)
	
	for line_temp in inp[(a+1):]:
		if (line_temp=='') or (line_temp.count("*")!=0):
			break
        print(line_temp)
        line_temp=(line_temp.replace(',','')).split()
        print(line_temp)
        line_int=[]
        for i in line_temp:
            line_int.append(int(i))
        array.append(line_int)
        
def array_append(sets):
    array=[];
    for i in sets:
        for j in i:
            array.append(int(j))
    sets=[]
    return array

def nodes_append(sets):
    nc=[];
    
    for i in sets:
        array=[];
        for j in range(len(i)):
            if j==0:
                array.append(int(i[j]))
            else:
                array.append(float(i[j]))
        nc.append(array)
    sets=[]
    return nc

def float_append(sets):
    array=[];
    for i in sets:
        for j in i:
            array.append(float(j))
    sets=[]
    return array

def nodal_connect_append(sets):
    nc=[];
    
    for i in sets:
        array=[];
        for j in range(1,len(i)):
            if j==0:
                array.append(str(i[j]))
            else:
                array.append(int(i[j]))
        nc.append(array)
    sets=[]
    return nc
    
# Search_line(inp,'*Part, name='+RVE_part_name,keyword[1],nodal_connectvity,1)
# nodal_connectvity=nodal_connect_append(nodal_connectvity)

Search_line(inp,'*Part, name='+RVE_part_name,keyword[0],Nodes,1);#node no, x,y,x
Nodes=nodes_append(Nodes)

Search_line(inp,'*Part, name='+macro_part_name,keyword[0],SE_Nodes,1);
Search_line(inp,'*Part, name='+macro_part_name,keyword[2],SE_nodal_connectvity,1);


SE_nodal_connectvity=nodal_connect_append(SE_nodal_connectvity)
SE_Nodes=nodes_append(SE_Nodes)

    
if (len(SE_nodal_connectvity[0])==4):
    order=1;
else:
    print('number of nodes does not correspond to linear elements')

Vertex1=[];
Vertex2=[];
Vertex3=[];
Vertex4=[];

Search(inp,Vertexes[0],Vertex1)
Search(inp,Vertexes[1],Vertex2)
Search(inp,Vertexes[2],Vertex3)
Search(inp,Vertexes[3],Vertex4)

Vertex1=array_append(Vertex1);
Vertex2=array_append(Vertex2);
Vertex3=array_append(Vertex3);
Vertex4=array_append(Vertex4);


M11=[];
M12=[];
M13=[];
M14=[];


Search(inp,Vertexes[4],M11)
Search(inp,Vertexes[5],M12)
Search(inp,Vertexes[6],M13)
Search(inp,Vertexes[7],M14)


M11=array_append(M11);
M12=array_append(M12);
M13=array_append(M13);
M14=array_append(M14);


Face1=[];
Face2=[];
Face3=[];
Face4=[];


Search(inp,Faces[0],Face1)
Search(inp,Faces[1],Face2)
Search(inp,Faces[2],Face3)
Search(inp,Faces[3],Face4)


Face1=array_append(Face1);
Face2=array_append(Face2);
Face3=array_append(Face3);
Face4=array_append(Face4);

# removes the first and last element out of face
def TakeVertexOut(face):
    face.pop(0)
    face.pop(-1)
    return face

# returns an ordered list of nodes in face as per the input coordinate 
def SortListOfNodes(face,coordinate):
    newlist = []
    oldlist = []
    for ii in face:#ii is the node label in face
        oldlist.append(Nodes[ii-1][coordinate+1])
    
    orderedlist = sorted(oldlist)
    for ii in range(len(oldlist)):
        vecindex = oldlist.index(orderedlist[ii])
        #newlist.append(oldlist[vecindex])
        newlist.append(face[vecindex])#node_labels
    return newlist



# gives the shape functions for a nodal point P with respect to macroscale element with nodal coordinates (X1,Y1),(X2,Y2),(X3,Y3) and (X4,Y4)
def vertex_shape_fn(P,X1,X2,X3,X4,Y1,Y2,Y3,Y4,n):               
# co-efficients of interpolation equations only for quadrilateral elements
#Dx=Ax*e+Bx*n+Cx*e*n ; Dy=Ay*e+By*n+Cy*e*n
#constant terms
    X=P[0][0]
    Y=P[1][0]
    
    Dx=float(4*X-(X1+X2+X3+X4))
    Dy=float(4*Y-(Y1+Y2+Y3+Y4))
            
    Ax=float(-X1+X2+X3-X4)
    Ay=float(-Y1+Y2+Y3-Y4)
            
    Bx=float(-X1-X2+X3+X4)
    By=float(-Y1-Y2+Y3+Y4)
            
    Cx=float(X1-X2+X3-X4)
    Cy=float(Y1-Y2+Y3-Y4)
            
    tsi=float(Dx/Ax);
    eta=float(Dy/By);
   
    N1=float(0.25*(1-tsi)*(1-eta))
    N2=float(0.25*(1+tsi)*(1-eta))
    N3=float(0.25*(1+tsi)*(1+eta))
    N4=float(0.25*(1-tsi)*(1+eta))
    return round(N1,n),round(N2,n),round(N3,n),round(N4,n)



def coord_transform(origin,ply_theta,M11):
    M1=np.array([[Nodes[M11[0]-1][1]],[Nodes[M11[0]-1][2]]])
    M1=np.array([[origin[0]+M1[0][0]],[origin[1]+M1[1][0]]])
    return M1




ParingFaces13=[];
ParingFaces13.append(TakeVertexOut(SortListOfNodes(Face1,1)))
ParingFaces13.append(TakeVertexOut(SortListOfNodes(Face3,1)))
ParingFaces24=[];
ParingFaces24.append(TakeVertexOut(SortListOfNodes(Face2,0)))
ParingFaces24.append(TakeVertexOut(SortListOfNodes(Face4,0)))


Sets=open('%s.dat'%(str(sets_data)),'w') 
Eqns=open('%s.dat'%(str(eqns_data)),'w') 

 
for i in range(0,len(SE_nodal_connectvity)):
    nodes=SE_nodal_connectvity[i]
    ele=i+1;#element number
    

    X1=SE_Nodes[(nodes[0])-1][1]
    X2=SE_Nodes[(nodes[1])-1][1]
    X3=SE_Nodes[(nodes[2])-1][1]
    X4=SE_Nodes[(nodes[3])-1][1]
        
    Y1=SE_Nodes[(nodes[0])-1][2]
    Y2=SE_Nodes[(nodes[1])-1][2]
    Y3=SE_Nodes[(nodes[2])-1][2]
    Y4=SE_Nodes[(nodes[3])-1][2]
    

    
    
    for j in range(1,n_GP):# loop to go around the gauss point RVEs
        #Faces = a.sets['Part-1-1-lin-'+str(ele)+'-1.Faces']
        #Partname='' c stands for current
        RVE_name='*Instance, name=Part-1-ele-'+str(ele)+'-GP-'+str(j)+', part='+RVE_part_name
        instance_name='Part-1-ele-'+str(ele)+'-GP-'+str(j)
        #*Instance, name=Part-1-ele-1-GP-2, part=Part-1
        origin=[];
        Search(inp,RVE_name,origin)
        origin=float_append(origin);
        ply_theta=0
               
        cFace1 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Face11-nodes'
        cFace2 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Face12-nodes'
        cFace3 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Face13-nodes'
        cFace4 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Face14-nodes'
        
        
        cVertex1 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Vertex11'
        cVertex2 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Vertex12'
        cVertex3 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Vertex13'
        cVertex4 = 'Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Vertex14'
        

        cM1='Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.M11' 
        M1=coord_transform(origin,ply_theta,M11)
        
        
        cM2='Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.M12'
        M2=coord_transform(origin,ply_theta,M12)#-RVE_size_z/2]])
        
        
        cM3='Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.M13'
        M3=coord_transform(origin,ply_theta,M13)#-RVE_size_z/2]])
        
        
        cM4='Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.M14'
        M4=coord_transform(origin,ply_theta,M14)#-RVE_size_z/2]])
        
        
        
        V3=coord_transform(origin,ply_theta,Vertex3)      
                
        if order==1:
            N1M1,N2M1,N3M1,N4M1=vertex_shape_fn(M1,X1,X2,X3,X4,Y1,Y2,Y3,Y4,accuracy)
            N1M2,N2M2,N3M2,N4M2=vertex_shape_fn(M2,X1,X2,X3,X4,Y1,Y2,Y3,Y4,accuracy)
            N1M3,N2M3,N3M3,N4M3=vertex_shape_fn(M3,X1,X2,X3,X4,Y1,Y2,Y3,Y4,accuracy)
            N1M4,N2M4,N3M4,N4M4=vertex_shape_fn(M4,X1,X2,X3,X4,Y1,Y2,Y3,Y4,accuracy)
            N1v3,N2v3,N3v3,N4v3=vertex_shape_fn(V3,X1,X2,X3,X4,Y1,Y2,Y3,Y4,accuracy)
    
        
##        
        # Writting Constrain equations 
        # For the Vertices
        #V3
        for dof in range(1,3):
            print>>Eqns, "** Constraint: %s" %(('Ele-'+str(ele)+'-Constraint_V3'+'-RVE'+str(j)+'-'+str(dof)),)
            print>>Eqns, "*Equation"
            print>>Eqns, "%s"%(str(order*4+1))
            print>>Eqns,"%s, %s, 1.0"%(str(cVertex3), str(dof))
            #print>>Eqns,"%s, %s, 1"%('Part-1-ele-'+str(ele)+'-GP-'+str(j)+'.Vertex15', str(dof))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-N1v3))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-N2v3))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-N3v3))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-N4v3))
            
        

        # Master V1 (Contained in 1 and 3)
        for dof in range(1,3):
            print>>Eqns, "** Constraint: %s" %(('ConstraintV1-V3-'+str(dof)+'-Ele-'+str(ele)+'-RVE'+str(j)))
            print>>Eqns, "*Equation"
            print>>Eqns, "%s"%(str(order*4+2))
            print>>Eqns,"%s, %s, 1."%(str(cVertex1), str(dof))
            print>>Eqns,"%s, %s, -1."%(str(cVertex3), str(dof))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-(N1M1-N1M3)-(N1M2-N1M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-(N2M1-N2M3)-(N2M2-N2M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-(N3M1-N3M3)-(N3M2-N3M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-(N4M1-N4M3)-(N4M2-N4M4)))
           
        
       
    # Master V2 (Contained in 4 and 3)
        for dof in range(1,3):
            print>>Eqns, "** Constraint: %s" %(('ConstraintV4-V3-'+str(dof)+'-Ele-'+str(ele)+'-RVE'+str(j)))
            print>>Eqns, "*Equation"
            print>>Eqns, "%s"%(str(order*4+2))
            print>>Eqns,"%s, %s, 1."%(str(cVertex4), str(dof))
            print>>Eqns,"%s, %s, -1."%(str(cVertex3), str(dof))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-(N1M1-N1M3)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-(N2M1-N2M3)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-(N3M1-N3M3)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-(N4M1-N4M3)))
           
        
    # Master V3 (Contained in 2 and 3)
        for dof in range(1,3):
            print>>Eqns, "** Constraint: %s" %(('ConstraintV2-V3-'+str(dof)+'-Ele-'+str(ele)+'-RVE'+str(j)))
            print>>Eqns, "*Equation"
            print>>Eqns, "%s"%(str(order*4+2))
            print>>Eqns,"%s, %s, 1."%(str(cVertex2), str(dof))
            print>>Eqns,"%s, %s, -1."%(str(cVertex3), str(dof))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-(N1M2-N1M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-(N2M2-N2M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-(N3M2-N3M4)))
            print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-(N4M2-N4M4)))
           
                 

    
        #for the faces		
        for ii in range(len(ParingFaces13[0])):
            
            print>>Sets,"*Nset, nset=%s, instance=%s"%(('Ele'+str(ele)+'-RVE'+str(j)+'-Face13-mas_node-'+str(ParingFaces13[0][ii])+'-'+str(ii)),str(instance_name))
            print>>Sets,"%s"%(str(ParingFaces13[0][ii]))
            print>>Sets,"*Nset, nset=%s, instance=%s"%(('Ele'+str(ele)+'-RVE'+str(j)+'-Face13-sla_node-'+str(ParingFaces13[1][ii])+'-'+str(ii)),str(instance_name))
            print>>Sets,"%s"%(str(ParingFaces13[1][ii]))

            
            for dof in range(1,3):
                print>>Eqns, "** Constraint: %s" %(('SEle-'+str(ele)+'gRVE'+str(j)+'-Constraint_Face13_nodes-'+str(dof)+'-'+str(ii)))
                print>>Eqns, "*Equation"
                print>>Eqns, "%s"%(str(order*4+2))
                print>>Eqns,"%s, %s, 1."%(str('Ele'+str(ele)+'-RVE'+str(j)+'-Face13-mas_node-'+str(ParingFaces13[0][ii])+'-'+str(ii)), str(dof))
                print>>Eqns,"%s, %s, -1."%(str('Ele'+str(ele)+'-RVE'+str(j)+'-Face13-sla_node-'+str(ParingFaces13[1][ii])+'-'+str(ii)), str(dof))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-(N1M1-N1M3)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-(N2M1-N2M3)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-(N3M1-N3M3)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-(N4M1-N4M3)))
                
                  

        for ii in range(len(ParingFaces24[0])):
            
            print>>Sets,"*Nset, nset=%s, instance=%s"%(('Ele'+str(ele)+'-RVE'+str(j)+'-Face24-mas_node-'+str(ParingFaces24[0][ii])+'-'+str(ii)),str(instance_name))
            print>>Sets,"%s"%(str(ParingFaces24[0][ii]))
            print>>Sets,"*Nset, nset=%s, instance=%s"%(('Ele'+str(ele)+'-RVE'+str(j)+'-Face24-sla_node-'+str(ParingFaces24[1][ii])+'-'+str(ii)),str(instance_name))
            print>>Sets,"%s"%(str(ParingFaces24[1][ii]))

            
            for dof in range(1,3):
                print>>Eqns, "** Constraint: %s" %(('SEle-'+str(ele)+'gRVE'+str(j)+'-Constraint_Face24_nodes-'+str(dof)+'-'+str(ii)))
                print>>Eqns, "*Equation"
                print>>Eqns, "%s"%(str(order*4+2))
                print>>Eqns,"%s, %s, 1."%(str('Ele'+str(ele)+'-RVE'+str(j)+'-Face24-mas_node-'+str(ParingFaces24[0][ii])+'-'+str(ii)), str(dof))
                print>>Eqns,"%s, %s, -1."%(str('Ele'+str(ele)+'-RVE'+str(j)+'-Face24-sla_node-'+str(ParingFaces24[1][ii])+'-'+str(ii)), str(dof))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[0])+'-RP', str(dof),str(-(N1M2-N1M4)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[1])+'-RP', str(dof),str(-(N2M2-N2M4)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[2])+'-RP', str(dof),str(-(N3M2-N3M4)))
                print>>Eqns,"%s, %s, %s"%('N'+str(nodes[3])+'-RP', str(dof),str(-(N4M2-N4M4)))
              
                  
Sets.close()
Eqns.close()

Sets=open('%s.dat'%(str(sets_data)),'r') 
Eqns=open('%s.dat'%(str(eqns_data)),'r') 

sets_lines=[];
eqns_lines=[];

mod_inp_file=open('%s.inp'%(str(mod_inp)),'w') 
    
while 1:
	line=Sets.readline()
	if not line:
		break
	line=line.strip()
	sets_lines.append(line)
    
while 1:
	line=Eqns.readline()
	if not line:
		break
	line=line.strip()
	eqns_lines.append(line)
    
end_asmbly=int(inp.index('*End Assembly'))
for i in range(0,end_asmbly):
    print>>mod_inp_file,"%s"%(inp[i])

for i in range(0,len(sets_lines)):
    print>>mod_inp_file,"%s"%(sets_lines[i])

for i in range(0,len(eqns_lines)):
    print>>mod_inp_file,"%s"%(eqns_lines[i])
    
for i in range(end_asmbly,len(inp)):
    print>>mod_inp_file,"%s"%(inp[i]);
    
mod_inp_file.close()
Sets.close()
Eqns.close()
f1.close()
os.remove('%s.dat'%(str(sets_data)))    
os.remove('%s.dat'%(str(eqns_data)))    
    
    
                  
          