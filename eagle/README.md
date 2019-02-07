<h1 id="fab-header"> "Marionette" ("DK") PCB Manufacturing ("fab") Information </h1>
<h1 id="assembly-header"> APDM "Marionette" ("DK") PCB Assembly ("PCBA") Information </h1>

# Overview

### CURRENT PCB NAME AND VERSION: "DK-2.2"
### CURRENT PCBA NAME AND VERSION: "DK-2.2"


Ver   | Date       | Notes
------|------------|------------------------------------------------------------
2.0   | 2015-12-01 | Marionette V2.0 
2.1   | 2016.05.26 | Marionette V2.1 
2.2   | 2019.02.01 | Marionette V2.2 


## Description

The Marionette PCBA is 150 x 95 mm four layer PCB with a mix of through-hole
and SMT components on the top side.  


<h1 class="pdf" id="fab-pdf:fab" task="pdf:fab"/>

<h1 class="pdf" id="assembly-pdf:assembly" task="pdf:assembly"/>


<h1 id="assembly-images"> 
</h1>

![](images/marionette-side.jpg)
![](images/marionette-angle.jpg)

Images of the Marionette v2.2


<h1 id="fab-info"> 
Printed Circuit Board (PCB) Fabrication information 
</h1>

- 4 layers, 1.59 mm (0.0625 inches) thick PCB 
- PCB bounding box size is 150 mm x 95 mm (5.9 x 3.74 inches)
- Minimum Trace / Space design rules
   - Outer layers: 0.15 mm (6.0 mil)
   - Inner layers: 0.2000 mm (7.8 mil)
- Outer dimension router tolerance: +/- 0.127 mm (0.005 in)
- Hole placement tolerance: .075 mm (+/-0.003 inch)
- Inner tab routed slot tolerance: +/- 0.127 mm (5 mil)
- Plated/Un-plated holes
  - There are 7 un-plated holes
  - There are 1304 plated through holes
  - PTH minimum diameter: 0.254 mm (10 mil)
  - PTH minimum annulus: 0.127 mm (5 mil) radius
- Plated slots
  - There 0 interior plated slots
- There are 3 fiducials
   - 3 on the top layer
- Panel tabs
   - Board does not yet have marked tabs. 
   - (Ignore for now) Do NOT place tabs anywhere else.
- Controlled impedance
   - While this board is no controlled impedance, the stackup is critical
     for performance of high speed signals (USB 2.0 high speed @ 480 Mbps)
- If not otherwise specified, build to IPC 6012 Class 2 or better.

## Materials

- Board thickness is 1.59 mm (0.063 inch) +/- 2 mil)
- Isola 370HR or equivalent
   - Laminate material MUST be Isola 370HR or equivalent (including an equivalent Dk).
   - Must have a flammability rating of at least V-0 (according to UL 94).
   - Must have a Dielectric Constant of ~ 4.5 at 1 MHz.
- Board Surface treatment should be ENIG, althogh immersion Silver is acceptable.
- White silkscreen on top and bottom surface
- Taiyo PSR-4000 or equivalent green soldermask on top and bottom

## Stack up

- Top and bottom prepreg thickness **MUST** be 0.111mm (4.4 mil) because of microstrips.

| Layer         | Thickness           | Notes                                        |
|---------------|---------------------|----------------------------------------------|
| Top Copper    | 0.043 mm /  1.7 mil |  Layer 1 foil, 1 oz Cu after plating         |
| prepreg       | 0.111 mm /  4.4 mil |  Prepreg Isola 370HR - 2x "1080"             |
| Layer 2       | 0.036 mm /  1.4 mil |  Layer 2 foil, 1 oz Cu                       |
| Core          | 1.207 mm / 47.5 mil |  Core Isola 370HR                            |
| Layer 3       | 0.036 mm /  1.4 mil |  Layer 3 foil, 1 oz Cu                       |
| prepreg       | 0.111 mm /  4.4 mil |  Prepreg Isola 370HR - 2x "1080"             |
| Bottom Copper | 0.043 mm /  1.7 mil |  Layer 4 foil, 1 oz copper after plating     |
| **Total Stackup** | **1.588 mm / 62.5 mil** |                                              |

## Array / Panel Information

- Coordinate with Contract Manufacturer (CM) for optimal size of this panel
- If no feedback from CM, then:
   - Panelize single board into apropriate sized array. Example: 5 x 3 array.
   - Use only "TAB" locations for attachment tabs
   - Use a ~ 6 mm (0.25 in) frame around the entire outside panel.


<div style="page-break-before: always;"></div>
## Fabrication Files

### PCB Artwork

| Filename              | Notes                                         |
| --------------------- | --------------------------------------------- |
| marionette.outline.gbx      | RS274X file for the dimension (outline) layer |
| marionette.milling.gbx      | RS274X file for internal milling              |
| marionette.xln              | Excellon drill file                           |
| marionette.topsilk.gbx      | RS274X file for the top silkscreen            |
| marionette.topmask.gbx      | RS274X file for the top soldermask            |
| marionette.toplayer.gbx     | RS274X file for the top copper layer          |
| marionette.layer2.gbx       | RS274X file for the layer 2 copper            |
| marionette.layer3.gbx       | RS274X file for the layer 3 copper            |
| marionette.bottomlayer.gbx  | RS274X file for the bottom copper layer       |
| marionette.bottommask.gbx   | RS274X file for the bottom soldermask         |
| marionette.bottomsilk.gbx   | RS274X file for the bottom silkscreen         |

### Documentation

| Filename            | Notes                                   |
| ------------------- | --------------------------------------- |
| marionette.doc.gbx        | RS274X file for documentation           |
| marionette.ipc            | IPC-D-356 netlist and board layout file |


### Stencils

| Filename                 | Notes                                |
| ------------------------ | ------------------------------------ |
| marionette.toppaste.gbx        | RS274X file for solder paste stencil |


<h1 id="assembly-info">
<div style="page-break-before: always;"></div>
Printed Circuit Board Assembly (PCBA) Information
</h1>

## Assembly info

- Assemble to IPC Class 2 or better
- Assemble with leaded solder 
- Aqueous flux and wash.
- There are 9 placements of 4 different components that require through hole soldering:
   - 6x Hirose ZX80-B-5SA microUSB vertical connectors (J5101 - J5106)
   - 1x CUI PJ-047AH 5.5mm x 2.1mm barrel power connector (J5001)
   - 1x Hirose ZX62D-B-5P8 USB micro connector (CF5101)
   - 1x FCI 73725-0110BLF USB Type-A vertical RA connector (J5107
- The J22 ZX62D-B-5P8 made by Hirose.  This is a hybrid through hole and SMT part.
**Beware solder ingress from J22 shield pins into the USB chamber.**
If there is solder ingress into the connector, please use a micro B USB
female connector to press into the J22 and clear the excess solder.



<div style="page-break-before: always;"></div>

## Assembly Files

### Mounting location files

| Filename             | Description                                 |
| -------------------- | ------------------------------------------- |
| marionette.mnt    | Pick and place locations for components     |

### Standard netlist/layout files

Not ready yet

| Filename             | Description                             |
| -------------------- | --------------------------------------- |
| marionette.ipc         | IPC-D-356 netlist and board layout file |

### Stencils

| Filename                       | Notes                                |
| ------------------------------ | ------------------------------------ |
|     marionette.toppaste.gbx          | RS274X file for solder paste stencil |


### Bill of materials

There is the option of populating the 26 MHz clock with a TCXO or an XTAL
with associated filter networks.  The ATTRIBUTE: 'NO_MNT' indicates whether the
component should be populated.  

| Filename                    | Description                        |
| --------------------------- | ---------------------------------- |
| bom/marionette_bom.xls           | BOM with TCXO/XTAL population variants |

