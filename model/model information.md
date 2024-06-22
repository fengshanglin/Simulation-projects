# 1.model information

## the whole model of flange
![the whole flange model](image-1.png)
## the cross section of flange
![cross section](image.png)

**the model of flange was designed in the Creo.**
## the meshing information of model

![local model](image-2.png)![whole model](image-3.png)
**the mesh of model was meshed in Hypermesh.**
## the FEM model
![Alt text](image-4.png)

the model of flange using the inp file was imported
## Model material properties were assigned
The flange is set to aluminum, the Young's modulus(E) is 7e4 MPa and the Poisson's ratio(v) is 0.33.

The plug is set to steel, the Young's modulus(E) is 2e5 MPa and the Poisson's ratio(v) is 0.3.

The property of rubber is set as shown in the following figure

![ruber material](image-5.png)

The processing of simulation is divided into 3 steps,

step 1:apply pre-tightening force to the flange,

setp 2:insert the plug into the flange

setp 3:apply lateral to force to the flange

![3 analysis steps](image-6.png)

## build sets
Reference points and sets are built in the module of assembly, as shown in the following figure.

![Alt text](image-7.png)

![Alt text](image-8.png)

![Alt text](image-9.png)


## Interaction
![build connector](image-10.png)

![assign the property of connector](image-11.png)

![assign the property of connector](image-12.png)

![specify local coordinate](image-13.png)

![set of contact surfaces](image-14.png)

![friction](image-15.png)

![specify contact property and pair](image-16.png)

![lateral coupling constraint](image-17.png)

![create rigid constraint](image-18.png)

## load conditions

![plug load](image-19.png)

![flange-displacment](image-20.png)

![plug-displacement](image-24.png)


![pre-force](image-21.png)

![later force](image-22.png)

![Alt text](image-23.png)


![Alt text](image-25.png)
![Alt text](image-26.png)


## post processing

1.Results are displacement 20mm for the plug
![whole_flange_20mm](the_whole_flange_rubber_20mm20246221946321.gif)
![local_flnage_20mm](the_local_flange_rubber_20mm20246221941101.gif)

2.Results are displacement 6mm for the plug
![whole_flange_6mm](the_whole_flange_rubber_6mm20246221852541.gif)
![local_flnage_6mm](the_local_flange_rubber_6mm20246221859301.gif)
