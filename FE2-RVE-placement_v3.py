from abaqus import *
from abaqusConstants import *

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

import numpy as np
import math
a1 = mdb.models['Model-2'].rootAssembly
a1.Set(name='N1-RP', nodes=(a1.instances['beam-1'].nodes[0:1],))
a1.Set(name='N2-RP', nodes=(a1.instances['beam-1'].nodes[1:2],))
a1.Set(name='N3-RP', nodes=(a1.instances['beam-1'].nodes[2:3],))
a1.Set(name='N4-RP', nodes=(a1.instances['beam-1'].nodes[3:4],))
a1.Set(name='N5-RP', nodes=(a1.instances['beam-1'].nodes[4:5],))
a1.Set(name='N6-RP', nodes=(a1.instances['beam-1'].nodes[5:6],))
a1.Set(name='N7-RP', nodes=(a1.instances['beam-1'].nodes[6:7],))
a1.Set(name='N8-RP', nodes=(a1.instances['beam-1'].nodes[7:8],))
a1.Set(name='N9-RP', nodes=(a1.instances['beam-1'].nodes[8:9],))
a1.Set(name='N10-RP', nodes=(a1.instances['beam-1'].nodes[9:10],))
a1.Set(name='N11-RP', nodes=(a1.instances['beam-1'].nodes[10:11],))
a1.Set(name='N12-RP', nodes=(a1.instances['beam-1'].nodes[11:12],))
a1.Set(name='N13-RP', nodes=(a1.instances['beam-1'].nodes[12:13],))
a1.Set(name='N14-RP', nodes=(a1.instances['beam-1'].nodes[13:14],))
a1.Set(name='N15-RP', nodes=(a1.instances['beam-1'].nodes[14:15],))
a1.Set(name='N16-RP', nodes=(a1.instances['beam-1'].nodes[15:16],))
a1.Set(name='N17-RP', nodes=(a1.instances['beam-1'].nodes[16:17],))
a1.Set(name='N18-RP', nodes=(a1.instances['beam-1'].nodes[17:18],))
a1.Set(name='N19-RP', nodes=(a1.instances['beam-1'].nodes[18:19],))
a1.Set(name='N20-RP', nodes=(a1.instances['beam-1'].nodes[19:20],))
a1.Set(name='N21-RP', nodes=(a1.instances['beam-1'].nodes[20:21],))
a1.Set(name='N22-RP', nodes=(a1.instances['beam-1'].nodes[21:22],))
a1.Set(name='N23-RP', nodes=(a1.instances['beam-1'].nodes[22:23],))
a1.Set(name='N24-RP', nodes=(a1.instances['beam-1'].nodes[23:24],))
a1.Set(name='N25-RP', nodes=(a1.instances['beam-1'].nodes[24:25],))
a1.Set(name='N26-RP', nodes=(a1.instances['beam-1'].nodes[25:26],))
a1.Set(name='N27-RP', nodes=(a1.instances['beam-1'].nodes[26:27],))
a1.Set(name='N28-RP', nodes=(a1.instances['beam-1'].nodes[27:28],))
a1.Set(name='N29-RP', nodes=(a1.instances['beam-1'].nodes[28:29],))
a1.Set(name='N30-RP', nodes=(a1.instances['beam-1'].nodes[29:30],))
a1.Set(name='N31-RP', nodes=(a1.instances['beam-1'].nodes[30:31],))
a1.Set(name='N32-RP', nodes=(a1.instances['beam-1'].nodes[31:32],))
a1.Set(name='N33-RP', nodes=(a1.instances['beam-1'].nodes[32:33],))
a1.Set(name='N34-RP', nodes=(a1.instances['beam-1'].nodes[33:34],))
a1.Set(name='N35-RP', nodes=(a1.instances['beam-1'].nodes[34:35],))
a1.Set(name='N36-RP', nodes=(a1.instances['beam-1'].nodes[35:36],))
a1.Set(name='N37-RP', nodes=(a1.instances['beam-1'].nodes[36:37],))
a1.Set(name='N38-RP', nodes=(a1.instances['beam-1'].nodes[37:38],))
a1.Set(name='N39-RP', nodes=(a1.instances['beam-1'].nodes[38:39],))
a1.Set(name='N40-RP', nodes=(a1.instances['beam-1'].nodes[39:40],))
a1.Set(name='N41-RP', nodes=(a1.instances['beam-1'].nodes[40:41],))
a1.Set(name='N42-RP', nodes=(a1.instances['beam-1'].nodes[41:42],))
a1.Set(name='N43-RP', nodes=(a1.instances['beam-1'].nodes[42:43],))
a1.Set(name='N44-RP', nodes=(a1.instances['beam-1'].nodes[43:44],))
a1.Set(name='N45-RP', nodes=(a1.instances['beam-1'].nodes[44:45],))
a1.Set(name='N46-RP', nodes=(a1.instances['beam-1'].nodes[45:46],))
a1.Set(name='N47-RP', nodes=(a1.instances['beam-1'].nodes[46:47],))
a1.Set(name='N48-RP', nodes=(a1.instances['beam-1'].nodes[47:48],))
a1.Set(name='N49-RP', nodes=(a1.instances['beam-1'].nodes[48:49],))
a1.Set(name='N50-RP', nodes=(a1.instances['beam-1'].nodes[49:50],))
a1.Set(name='N51-RP', nodes=(a1.instances['beam-1'].nodes[50:51],))
a1.Set(name='N52-RP', nodes=(a1.instances['beam-1'].nodes[51:52],))
a1.Set(name='N53-RP', nodes=(a1.instances['beam-1'].nodes[52:53],))
a1.Set(name='N54-RP', nodes=(a1.instances['beam-1'].nodes[53:54],))
a1.Set(name='N55-RP', nodes=(a1.instances['beam-1'].nodes[54:55],))
a1.Set(name='N56-RP', nodes=(a1.instances['beam-1'].nodes[55:56],))
a1.Set(name='N57-RP', nodes=(a1.instances['beam-1'].nodes[56:57],))
a1.Set(name='N58-RP', nodes=(a1.instances['beam-1'].nodes[57:58],))
a1.Set(name='N59-RP', nodes=(a1.instances['beam-1'].nodes[58:59],))
a1.Set(name='N60-RP', nodes=(a1.instances['beam-1'].nodes[59:60],))
a1.Set(name='N61-RP', nodes=(a1.instances['beam-1'].nodes[60:61],))
a1.Set(name='N62-RP', nodes=(a1.instances['beam-1'].nodes[61:62],))
a1.Set(name='N63-RP', nodes=(a1.instances['beam-1'].nodes[62:63],))
#=========When assembling  Super ele-1-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-1-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-1-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-92.3122193298,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-1-GP-1']

#=========When assembling  Super ele-1-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-1-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-1-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-59.2877834702,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-1-GP-2']

#=========When assembling  Super ele-1-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-1-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-1-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-59.2877834702,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-1-GP-3']

#=========When assembling  Super ele-1-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-1-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-1-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-92.3122193298,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-1-GP-4']

#=========When assembling  Super ele-2-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-2-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-2-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-35.1122185298,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-2-GP-1']

#=========When assembling  Super ele-2-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-2-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-2-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-2.08778267024,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-2-GP-2']

#=========When assembling  Super ele-2-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-2-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-2-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-2.08778267024,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-2-GP-3']

#=========When assembling  Super ele-2-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-2-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-2-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-35.1122185298,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-2-GP-4']

#=========When assembling  Super ele-3-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-3-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-3-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(22.0877823548,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-3-GP-1']

#=========When assembling  Super ele-3-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-3-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-3-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(55.1122184452,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-3-GP-2']

#=========When assembling  Super ele-3-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-3-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-3-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(55.1122184452,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-3-GP-3']

#=========When assembling  Super ele-3-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-3-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-3-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(22.0877823548,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-3-GP-4']

#=========When assembling  Super ele-4-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-4-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-4-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(79.2877841465,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-4-GP-1']

#=========When assembling  Super ele-4-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-4-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-4-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(112.312221854,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-4-GP-2']

#=========When assembling  Super ele-4-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-4-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-4-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(112.312221854,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-4-GP-3']

#=========When assembling  Super ele-4-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-4-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-4-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(79.2877841465,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-4-GP-4']

#=========When assembling  Super ele-5-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-5-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-5-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(136.487786667,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-5-GP-1']

#=========When assembling  Super ele-5-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-5-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-5-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(169.512220333,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-5-GP-2']

#=========When assembling  Super ele-5-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-5-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-5-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(169.512220333,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-5-GP-3']

#=========When assembling  Super ele-5-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-5-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-5-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(136.487786667,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-5-GP-4']

#=========When assembling  Super ele-6-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-6-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-6-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(193.687783667,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-6-GP-1']

#=========When assembling  Super ele-6-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-6-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-6-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(226.712217333,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-6-GP-2']

#=========When assembling  Super ele-6-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-6-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-6-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(226.712217333,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-6-GP-3']

#=========When assembling  Super ele-6-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-6-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-6-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(193.687783667,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-6-GP-4']

#=========When assembling  Super ele-7-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-7-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-7-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(250.887783837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-7-GP-1']

#=========When assembling  Super ele-7-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-7-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-7-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(283.912226163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-7-GP-2']

#=========When assembling  Super ele-7-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-7-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-7-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(283.912226163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-7-GP-3']

#=========When assembling  Super ele-7-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-7-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-7-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(250.887783837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-7-GP-4']

#=========When assembling  Super ele-8-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-8-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-8-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(308.087789497,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-8-GP-1']

#=========When assembling  Super ele-8-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-8-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-8-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(341.112214503,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-8-GP-2']

#=========When assembling  Super ele-8-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-8-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-8-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(341.112214503,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-8-GP-3']

#=========When assembling  Super ele-8-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-8-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-8-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(308.087789497,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-8-GP-4']

#=========When assembling  Super ele-9-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-9-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-9-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(365.287777837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-9-GP-1']

#=========When assembling  Super ele-9-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-9-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-9-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(398.312220163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-9-GP-2']

#=========When assembling  Super ele-9-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-9-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-9-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(398.312220163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-9-GP-3']

#=========When assembling  Super ele-9-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-9-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-9-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(365.287777837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-9-GP-4']

#=========When assembling  Super ele-10-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-10-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-10-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(422.487783497,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-10-GP-1']

#=========When assembling  Super ele-10-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-10-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-10-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(455.512208503,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-10-GP-2']

#=========When assembling  Super ele-10-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-10-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-10-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(455.512208503,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-10-GP-3']

#=========When assembling  Super ele-10-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-10-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-10-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(422.487783497,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-10-GP-4']

#=========When assembling  Super ele-11-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-11-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-11-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(479.687771837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-11-GP-1']

#=========When assembling  Super ele-11-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-11-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-11-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(512.712214163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-11-GP-2']

#=========When assembling  Super ele-11-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-11-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-11-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(512.712214163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-11-GP-3']

#=========When assembling  Super ele-11-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-11-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-11-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(479.687771837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-11-GP-4']

#=========When assembling  Super ele-12-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-12-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-12-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(536.887783837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-12-GP-1']

#=========When assembling  Super ele-12-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-12-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-12-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(569.912226163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-12-GP-2']

#=========When assembling  Super ele-12-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-12-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-12-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(569.912226163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-12-GP-3']

#=========When assembling  Super ele-12-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-12-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-12-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(536.887783837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-12-GP-4']

#=========When assembling  Super ele-13-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-13-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-13-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(594.087795837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-13-GP-1']

#=========When assembling  Super ele-13-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-13-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-13-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(627.112238163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-13-GP-2']

#=========When assembling  Super ele-13-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-13-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-13-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(627.112238163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-13-GP-3']

#=========When assembling  Super ele-13-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-13-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-13-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(594.087795837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-13-GP-4']

#=========When assembling  Super ele-14-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-14-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-14-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(651.287795158,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-14-GP-1']

#=========When assembling  Super ele-14-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-14-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-14-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(684.312202842,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-14-GP-2']

#=========When assembling  Super ele-14-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-14-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-14-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(684.312202842,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-14-GP-3']

#=========When assembling  Super ele-14-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-14-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-14-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(651.287795158,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-14-GP-4']

#=========When assembling  Super ele-15-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-15-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-15-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(708.487759837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-15-GP-1']

#=========When assembling  Super ele-15-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-15-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-15-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(741.512202163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-15-GP-2']

#=========When assembling  Super ele-15-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-15-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-15-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(741.512202163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-15-GP-3']

#=========When assembling  Super ele-15-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-15-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-15-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(708.487759837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-15-GP-4']

#=========When assembling  Super ele-16-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-16-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-16-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(765.687771837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-16-GP-1']

#=========When assembling  Super ele-16-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-16-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-16-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(798.712214163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-16-GP-2']

#=========When assembling  Super ele-16-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-16-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-16-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(798.712214163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-16-GP-3']

#=========When assembling  Super ele-16-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-16-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-16-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(765.687771837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-16-GP-4']

#=========When assembling  Super ele-17-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-17-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-17-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(822.887783837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-17-GP-1']

#=========When assembling  Super ele-17-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-17-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-17-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(855.912226163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-17-GP-2']

#=========When assembling  Super ele-17-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-17-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-17-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(855.912226163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-17-GP-3']

#=========When assembling  Super ele-17-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-17-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-17-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(822.887783837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-17-GP-4']

#=========When assembling  Super ele-18-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-18-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-18-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(880.087795837,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-18-GP-1']

#=========When assembling  Super ele-18-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-18-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-18-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(913.112238163,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-18-GP-2']

#=========When assembling  Super ele-18-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-18-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-18-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(913.112238163,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-18-GP-3']

#=========When assembling  Super ele-18-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-18-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-18-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(880.087795837,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-18-GP-4']

#=========When assembling  Super ele-19-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-19-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-19-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(937.287796003,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-19-GP-1']

#=========When assembling  Super ele-19-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-19-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-19-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(970.312205997,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-19-GP-2']

#=========When assembling  Super ele-19-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-19-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-19-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(970.312205997,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-19-GP-3']

#=========When assembling  Super ele-19-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-19-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-19-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(937.287796003,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-19-GP-4']

#=========When assembling  Super ele-20-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-20-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-20-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(994.487776094,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-20-GP-1']

#=========When assembling  Super ele-20-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-20-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-20-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(1027.51225191,-92.3122193298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-20-GP-2']

#=========When assembling  Super ele-20-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-20-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-20-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(1027.51225191,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-20-GP-3']

#=========When assembling  Super ele-20-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-20-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-20-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(994.487776094,-59.2877834702,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-20-GP-4']

#=========When assembling  Super ele-21-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-21-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-21-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-92.3122193298,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-21-GP-1']

#=========When assembling  Super ele-21-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-21-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-21-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-59.2877834702,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-21-GP-2']

#=========When assembling  Super ele-21-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-21-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-21-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-59.2877834702,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-21-GP-3']

#=========When assembling  Super ele-21-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-21-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-21-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-92.3122193298,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-21-GP-4']

#=========When assembling  Super ele-22-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-22-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-22-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-35.1122185298,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-22-GP-1']

#=========When assembling  Super ele-22-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-22-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-22-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-2.08778267024,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-22-GP-2']

#=========When assembling  Super ele-22-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-22-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-22-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-2.08778267024,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-22-GP-3']

#=========When assembling  Super ele-22-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-22-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-22-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(-35.1122185298,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-22-GP-4']

#=========When assembling  Super ele-23-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-23-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-23-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(22.0877823548,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-23-GP-1']

#=========When assembling  Super ele-23-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-23-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-23-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(55.1122184452,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-23-GP-2']

#=========When assembling  Super ele-23-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-23-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-23-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(55.1122184452,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-23-GP-3']

#=========When assembling  Super ele-23-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-23-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-23-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(22.0877823548,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-23-GP-4']

#=========When assembling  Super ele-24-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-24-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-24-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(79.2877841465,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-24-GP-1']

#=========When assembling  Super ele-24-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-24-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-24-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(112.312221854,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-24-GP-2']

#=========When assembling  Super ele-24-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-24-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-24-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(112.312221854,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-24-GP-3']

#=========When assembling  Super ele-24-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-24-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-24-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(79.2877841465,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-24-GP-4']

#=========When assembling  Super ele-25-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-25-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-25-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(136.487786667,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-25-GP-1']

#=========When assembling  Super ele-25-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-25-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-25-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(169.512220333,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-25-GP-2']

#=========When assembling  Super ele-25-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-25-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-25-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(169.512220333,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-25-GP-3']

#=========When assembling  Super ele-25-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-25-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-25-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(136.487786667,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-25-GP-4']

#=========When assembling  Super ele-26-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-26-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-26-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(193.687783667,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-26-GP-1']

#=========When assembling  Super ele-26-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-26-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-26-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(226.712217333,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-26-GP-2']

#=========When assembling  Super ele-26-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-26-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-26-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(226.712217333,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-26-GP-3']

#=========When assembling  Super ele-26-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-26-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-26-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(193.687783667,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-26-GP-4']

#=========When assembling  Super ele-27-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-27-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-27-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(250.887783837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-27-GP-1']

#=========When assembling  Super ele-27-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-27-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-27-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(283.912226163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-27-GP-2']

#=========When assembling  Super ele-27-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-27-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-27-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(283.912226163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-27-GP-3']

#=========When assembling  Super ele-27-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-27-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-27-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(250.887783837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-27-GP-4']

#=========When assembling  Super ele-28-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-28-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-28-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(308.087789497,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-28-GP-1']

#=========When assembling  Super ele-28-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-28-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-28-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(341.112214503,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-28-GP-2']

#=========When assembling  Super ele-28-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-28-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-28-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(341.112214503,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-28-GP-3']

#=========When assembling  Super ele-28-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-28-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-28-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(308.087789497,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-28-GP-4']

#=========When assembling  Super ele-29-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-29-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-29-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(365.287777837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-29-GP-1']

#=========When assembling  Super ele-29-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-29-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-29-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(398.312220163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-29-GP-2']

#=========When assembling  Super ele-29-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-29-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-29-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(398.312220163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-29-GP-3']

#=========When assembling  Super ele-29-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-29-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-29-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(365.287777837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-29-GP-4']

#=========When assembling  Super ele-30-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-30-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-30-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(422.487783497,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-30-GP-1']

#=========When assembling  Super ele-30-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-30-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-30-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(455.512208503,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-30-GP-2']

#=========When assembling  Super ele-30-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-30-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-30-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(455.512208503,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-30-GP-3']

#=========When assembling  Super ele-30-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-30-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-30-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(422.487783497,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-30-GP-4']

#=========When assembling  Super ele-31-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-31-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-31-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(479.687771837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-31-GP-1']

#=========When assembling  Super ele-31-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-31-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-31-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(512.712214163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-31-GP-2']

#=========When assembling  Super ele-31-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-31-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-31-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(512.712214163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-31-GP-3']

#=========When assembling  Super ele-31-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-31-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-31-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(479.687771837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-31-GP-4']

#=========When assembling  Super ele-32-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-32-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-32-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(536.887783837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-32-GP-1']

#=========When assembling  Super ele-32-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-32-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-32-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(569.912226163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-32-GP-2']

#=========When assembling  Super ele-32-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-32-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-32-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(569.912226163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-32-GP-3']

#=========When assembling  Super ele-32-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-32-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-32-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(536.887783837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-32-GP-4']

#=========When assembling  Super ele-33-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-33-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-33-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(594.087795837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-33-GP-1']

#=========When assembling  Super ele-33-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-33-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-33-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(627.112238163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-33-GP-2']

#=========When assembling  Super ele-33-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-33-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-33-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(627.112238163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-33-GP-3']

#=========When assembling  Super ele-33-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-33-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-33-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(594.087795837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-33-GP-4']

#=========When assembling  Super ele-34-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-34-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-34-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(651.287795158,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-34-GP-1']

#=========When assembling  Super ele-34-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-34-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-34-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(684.312202842,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-34-GP-2']

#=========When assembling  Super ele-34-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-34-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-34-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(684.312202842,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-34-GP-3']

#=========When assembling  Super ele-34-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-34-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-34-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(651.287795158,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-34-GP-4']

#=========When assembling  Super ele-35-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-35-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-35-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(708.487759837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-35-GP-1']

#=========When assembling  Super ele-35-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-35-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-35-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(741.512202163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-35-GP-2']

#=========When assembling  Super ele-35-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-35-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-35-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(741.512202163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-35-GP-3']

#=========When assembling  Super ele-35-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-35-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-35-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(708.487759837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-35-GP-4']

#=========When assembling  Super ele-36-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-36-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-36-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(765.687771837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-36-GP-1']

#=========When assembling  Super ele-36-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-36-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-36-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(798.712214163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-36-GP-2']

#=========When assembling  Super ele-36-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-36-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-36-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(798.712214163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-36-GP-3']

#=========When assembling  Super ele-36-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-36-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-36-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(765.687771837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-36-GP-4']

#=========When assembling  Super ele-37-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-37-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-37-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(822.887783837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-37-GP-1']

#=========When assembling  Super ele-37-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-37-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-37-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(855.912226163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-37-GP-2']

#=========When assembling  Super ele-37-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-37-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-37-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(855.912226163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-37-GP-3']

#=========When assembling  Super ele-37-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-37-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-37-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(822.887783837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-37-GP-4']

#=========When assembling  Super ele-38-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-38-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-38-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(880.087795837,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-38-GP-1']

#=========When assembling  Super ele-38-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-38-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-38-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(913.112238163,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-38-GP-2']

#=========When assembling  Super ele-38-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-38-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-38-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(913.112238163,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-38-GP-3']

#=========When assembling  Super ele-38-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-38-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-38-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(880.087795837,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-38-GP-4']

#=========When assembling  Super ele-39-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-39-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-39-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(937.287796003,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-39-GP-1']

#=========When assembling  Super ele-39-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-39-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-39-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(970.312205997,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-39-GP-2']

#=========When assembling  Super ele-39-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-39-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-39-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(970.312205997,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-39-GP-3']

#=========When assembling  Super ele-39-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-39-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-39-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(937.287796003,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-39-GP-4']

#=========When assembling  Super ele-40-RVE @ GP-1
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-40-GP-1', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-40-GP-1']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(994.487776094,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-40-GP-1']

#=========When assembling  Super ele-40-RVE @ GP-2
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-40-GP-2', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-40-GP-2']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(1027.51225191,-35.1122185298,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-40-GP-2']

#=========When assembling  Super ele-40-RVE @ GP-3
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-40-GP-3', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-40-GP-3']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(1027.51225191,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-40-GP-3']

#=========When assembling  Super ele-40-RVE @ GP-4
a = mdb.models['Model-2'].rootAssembly
#a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-2'].parts['Part-1']
a.Instance(name='Part-1-ele-40-GP-4', part=p, dependent=ON)
p2 = a.instances['Part-1-ele-40-GP-4']
a = mdb.models['Model-2'].rootAssembly
a = mdb.models['Model-2'].rootAssembly
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(1.0,0.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,1.0,0.0),angle=0.0)
p2.rotateAboutAxis(axisPoint=(0.0,0.0,0.0),axisDirection=(0.0,0.0,1.0),angle=0.0)
p2.translate(vector=(994.487776094,-2.08778267024,0.0))
a = mdb.models['Model-2'].rootAssembly
p2 = a.instances['Part-1-ele-40-GP-4']

