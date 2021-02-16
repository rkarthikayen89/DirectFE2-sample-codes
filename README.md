# DirectFE2-sample-codes
These files can help set up a Direct FE2 model in 2D in ABAQUS

Description of files in the folder

(1)micro_RVE_placement-lin_v2.py: 
This script is used to generate another python script which places RVEs at the macroscale Gauss points
(needed to execute section A in readme word document)
sample input is file(2)
sample ouput is file(3)

(2)beam-macro.inp 
A sample input file with only the macroscale mesh details that can be given as input to (1).

(3)FE2-RVE-placement_v3.py: 
A sample generated python script which is the output after executing file(1) with file(2) given as input. 
This script when executed on ABAQUS CAE GUI will place the RVEs at the macroscale Gauss points. 

(4)input_file_PBCs-2D_v5.py:
Python script that applies RVE boundary conditions as MPCs by modifying input file
(needed to execute section B in readme word document) 
sample input is file(5)
sample output is file(6)

(5)beam-macro-RVEs-model-2.inp
This is sample file that can be used as input to file(4).
This is a sample ABAQUS input file that is generated after executing (3) in ABAQUS GUI with macroscale mesh and the RVEs placed at the 
macroscale gauss points with all the macroscale boundary conditions except the microscale boundary conditions which will be applied when
this file is given as input to file(4).

(6)beam-macro-RVEs-model-2-with-MPCs.inp
This is a sample input file that is the ouput after running file (4) in ABAQUS cae nogui command prompt or Python2.7 command line with file(5) as input.
this file can be run from the ABAQUS command line with the command "ABAQUS job='beam-macro-RVEs-model-2-with-MPCs" in the ABAQUS command prompt

(7)Direct-FE2-python-scripts-read-meV3.docx
This is a word document that describes usage of files(1) and (4) to set up Direct FE2 models.

(8)README.md
This file which describes the files in the folder.
