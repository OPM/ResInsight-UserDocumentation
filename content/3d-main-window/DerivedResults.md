+++
title = "Derived Results"
published = true
weight = 160
hidden = false
+++

ResInsight computes several derived results. In this section we will explain what they are, and briefly how they are calculated.

## Derived Results for Eclipse Cases

ResInsight calculates several derived cell properties that is made available as **Static** or **Dynamic** cell properties.
The derived results listed at the bottom of the **Static** result properties, are shown below.

![]({{< relref "" >}}images/appendix/DerivedStaticResults.png)

### Transmissibility Normalized by Area
The transmissibility for cells and Non-Neighbor Connections (NNCs) are dependent on both cell properties and geometry. ResInsight normalizes TRANX, TRANY and TRANZ with the overlapping flow area for both neighbor cells and NNC-cells. The results are named **riTRANXbyArea**, **riTRANYbyArea** and **riTRANZbyArea** respectively.

The normalized transmissibilities make it easier to compare and check the flow capacity visually. This can be useful when history matching pressure differences across a fault. 

### Overall Transmissibility Multiplier
Transmissibility can be set or adjusted with multiple keywords in an Eclipse data deck. To visualize the adjustments made, ResInsight calculates a multiplicator for the overall change. First unadjusted transmissibilities for all neighbor cells and NNCs are evaluated based on geometry and permeabilities, similar to the NEWTRAN algorithm in Eclipse. For x- and y-directions, the NTG parameter is also included. The results are named **riTRANX**, **riTRANY** and **riTRANZ** respectively.

The TRANX, TRANY and TRANZ used in the simulation are divided by the ResInsight calculated transmissibilities and the resulting multiplicators are named **riMULTX**, **riMULTY** and **riMULTZ** respectively. The derived properties are listed under **Static** properties. The riMULT-properties are useful for quality checking consistence in user input for fault seal along a fault plane. 

### Directional Combined Results

Cell properties with names ending in I, J, K, X, Y, or Z, and an optional "+" or "-" are combined into derived results post-fixed with IJK, or XYZ depending on their origin. (Eg. the static cell properties MULTX, MULTY, MULTZ, and their negatives are combined into the result MULTXYZ, while the dynamic cell properties FLRGASI, FLRGASJ, FLRGASK are combined to FLRGASIJK). 

These combined cell properties visualize the property as a color in all directions combined when selected in 
as a **Cell Result** and **Separate Fault Result**. 

The face of a cell is then colored based on the value associated with that particular face. The Positive I-face of the cell gets the cell X/I-value, while the J-face gets the Y/J-value etc. The negative faces, however, get the value from the neighbor cell on that side. The negative I-face gets the X-value of the IJK-neighbor in negative I direction, and so on for the J- and K-faces.

The directional combined parameters available are:

- Static Properties
  - **TRANXYZ** (inluding NNCs)
  - **MULTXYZ**
  - **riTRANXYZ** (inluding NNCs)
  - **riMULTXYZ** (inluding NNCs)
  - **riTRANXYZbyArea** (inluding NNCs)
- Dynamic Properties
  - **FLRWATIJK** (inluding NNCs)
  - **FLROILIJK** (inluding NNCs)
  - **FLRGASIJK** (inluding NNCs)
- Generated
  - Octave generated results with same name but ending with I,J and K will also be combined into a _`<name>IJK`_ cell property.

### Completion Type

![]({{< relref "" >}}images/appendix/CompletionTypes.png)

The dynamic cell property named **Completion Type** is calculated from the intersections between [Completions]({{< relref "completions" >}}) and the grid cells. All grid cells intersected by a completion will be assigned a color based on the type of completion that intersects the cell.

If a cell is completed with multiple completions, the following priority is used : **Fracture**, **Fishbones**, and **Perforation Interval**.

### Identification of Questionable NNCs
In the process of normalizing transmissibility by the overlapping flow area, the NNCs in the model without any shared surface between two cells are identified. These NNCs are listed in the **Faults/NNCs With No Common Area** folder. These NNCs are questionable since flow normally is associated with a flow area.

![]({{< relref "" >}}images/appendix/ResInsight_NNCsWithNoCommonArea.png)
 
### Water Flooded PV

Water Flooded PV, also called _Number of flooded porevolumes_ shows the amount of flow from a selected set of simulation tracers into a particular cell, compared to the cells mobile pore volume. A value of 1.0 will tell that the tracers accumulated flow into the cell has reached a volume equal to the mobile pore volume in the cell.   

## Derived Geomechanical results

ResInsight calculates several of the presented geomechanical results based on the native results present in the odb-files. 

### Relative Results (Time Lapse Results) 

ResInsight can calculate and display relative results, sometimes also referred to as Time Lapse results.
When enabled, every result variable is calculated as :

$$Value'(t) = Value(t) - Value(BaseTime)$$

Enable the **Enable Relative Result**  option in the **Relative Result Options** group, and select the appropriate **Base Time Step**. 

![]({{< relref "" >}}images/appendix/DerivedRelativeResults.png)

Each variable is then post-fixed with "_D*TimeStepIndex*" to distinguish them from the native variables.

Note: Relative Results calculated based on Gamma values are calculated slightly differently:

Gamma_D*n* = ST_D*n* / POR_D*n*

### Derived Result Fields

The calculated result fields are:

* Nodal
  * COMPACTION (Magnitude of compression)
* Element Nodal and Integration Points
  * ST (Total Stress)
     * All tensor components
     * Principals, with directions ($S\_iinc, S\_iazi$)
     * STM (Mean total stress)
     * Q (Deviatoric stress)
  * Gamma (Stress path)
  * SE (Effective Stress)
     * All tensor components
     * Principals, with directions
     * SEM (Mean effective stress)
     * SFI
     * FOS
     * DSM
  * E (Strain) 
     * All tensor components
     * EV (Volumetric strain)
     * ED (Deviatoric strain)
* Element Nodal On Face
  * Plane 
    * Pinc (Face inclination angle)
    * Pazi (Face azimuth angle)
  * Transformed Total and Effective Stress
    * SN (Stress component normal to face)
    * TP (Total in-plane shear)
    * TPinc (Direction of TP)
    * TPH ( Horizontal in-plane shear component )
    * TPQV ( Quasi vertical in-plane shear component )
    * FAULTMOB 
    * PCRIT
    
### Definitions of Derived Results

In this text the label Sa and Ea will be used to denote the unchanged stress and strain tensor respectively from the odb file.

Components with one subscript denotes the principal values 1, 2, and 3 which refers to the maximum, middle, and minimum principals respectively. 

Components with two subscripts however, refers to the global directions 1, 2, and 3 which corresponds to  X, Y, and Z and thus also easting, northing, and depth.

- Inclination is measured from the downwards direction
- Azimuth is measured from the Northing (Y) Axis in Clockwise direction looking down.

### Case Constants

Two constants can be assigned to a Geomechanical case:

- Cohesion
- Friction angle

In the following they are denoted s0 and fa respectively. Some of the derived results use these constants, that can be changed in the property panel of the Case.

![]({{< relref "" >}}images/appendix/GeoMechCasePropertyPanel.png)

### COMPACTION

Compaction is the difference in vertical displacement (U3) between a grid node and a specified reference K layer.
The reference K layer is specified in the property editor.

For each node <i>n</i> in the grid, a node <i>nref</i> in the reference K layer is found by vertical intersection from the node <i>n</i>.

$ If (Depth\_n <= Depth\_{nref}) $

$ \space \space COMPACTION\_n = -(U3\_n - U3\_{nref})$

$ else $

$\space \space COMPACTION\_n = -(U3\_{nref} - U3\_n )$

### ST - Total Stress

$ST\_{ii} = -Sa\_{ii} + \alpha * POR (i= 1,2,3)$

$\alpha$ is the Biot porelastic coefficient which defines the compressibility of sand grains: $\alpha = 1.0$ for incompressible grains,
and $\alpha < 1.0$ for compressible grains. $\alpha$ is not used for the initial (Geostatic) time step. The default value is 1.0, but values
per element can be imported as an [element property table]({{< relref "ElementPropertyTable.md" >}}). $Sa\_{ii}$ is the stress calculated by Abaqus.
We use a value of $POR=0.0$ where it is not defined.

$ST\_{ij} = -Sa\_{ij} (i,j = 1,2,3 \text{ and i $\ne$ j})$

$Sa\_{ij}$ is the stress calculated by Abaqus.

$ST\_i = \text{Principal value i of ST}$

### STM - Total Mean Stress

$STM = \frac{ST\_{11} + ST\_{22} + ST\_{33}}{3} $

### Q - Deviatoric Stress

$Q = \sqrt {\frac{3}{2} * ((ST\_1 - STM)^2 + (ST\_2 - STM)^2 + (ST\_3 - STM)^2 }$

### Gamma - Stress Path

$Gamma\_{ii} = \frac{ST\_{ii}} {POR} (i= 1,2,3) $

$Gamma\_{i} = \frac{ST\_{i}} {POR}  $

In these calculations we set Gamma to *undefined* if abs(POR) > 0.01 MPa. 

### SE - Effective Stress

$SE\_{ii} = ST\_{ii} - \alpha * POR - (1.0 - \alpha) * POR\_0  \text{ (Where POR is defined)} $

where $\alpha$ is the Biot porelastic coefficient (see $ST\_{ii}$ definition above for details), $POR$ is the pore pressure at the given time step, and $POR\_0$ is the
initial pore pressure (Geostatic step).

$SE\_{ij} = -Sa\_{ij} (i,j = 1,2,3 \text{ and i $\ne$ j})$

where $Sa\_{ij}$ is the stress calculated by Abaqus.

$SE\_i = \text{Principal value i of SE} $

### SEM - Effective Mean Stress

$SEM = \frac{SE\_{11} + SE\_{22} + SE\_{33}} {3}  $


### STA/SEA - Stress Anisotropy

$STA\_{ij} = 2 \frac{ST\_{i} - ST\_{j}}{ ST\_{i} + ST\_{j}} (i,j = 1,2,3 \text{ and i $\lt$ j})$

The same expressions are available for effective stresses as $SEA\_{12}$, $SEA\_{13}$ and $SEA\_{23}$.

### SFI

$$SFI = \frac{\frac{S0}{tan(fa)} + 0.5 * (SE\_1 + SE\_3) * sin(fa)} {0.5*(SE\_1-SE\_3)}  $$

### DSM 

$DSM = \frac{tan(\rho)} {tan(fa)} $

where 

$$ \rho = 2 * (arctan (\sqrt \frac{ SE\_1 + a} {SE\_3 + a}) \space – \frac {\pi} {4}) $$
$$ a = \frac {s0} {tan(fa)} $$

### FOS

$FOS = \frac{1}{DSM}$

### E - Strain

$E\_{ij} = -Ea\_{ij}$

### EV - Volumetric Strain

EV = E11 + E22 + E33 

### ED - Deviatoric Strain

$ED = 2*\frac {E1-E3} {3}  $

### Element Nodal On Face

For each face displayed, (might be an element face or an intersection/intersection box face), 
a coordinate system is established such that:

- Ez is normal to the face, named N - Normal
- Ex is horizontal and in the plane of the face, named H - Horizontal 
- Ey is in the plane pointing upwards, named QV - Quasi Vertical

The stress tensors in that particular face are then transformed to that coordinate system.  The following quantities are derived from the transformed tensor named TS in the following:

### SN - Stress component Normal to face

$SN = TS\_{33}$

### TPH - Horizontal in-plane shear component

$TPH = TS\_{31} = TS\_{ZX} $

### TNQV - Horizontal in-plane shear component

$TPQV = TS\_{32} = TS\_{ZY}$

### TP - Total in-plane shear

$TP = \sqrt {(TPH^2 + TPQV^2)} $

### TPinc - Direction of TP

Angle of the total in-plane shear relative to the Quasi Vertical direction 

$TPinc = acos (\frac {TPQV} {TP}) $

### Pinc and Pazi - Face Inclination and Azimuth

These are the directional angles of the face-normal itself. 


### Pore Compressibility

#### Pore Compressibility

Pore compressibility between a reference state and the current stress state is defined as:

$ C\_{p} = -\frac{ \alpha \Delta\epsilon\_{vol}}{ \Delta P\_p \phi_0} + \frac{1}{K\_s} ( \frac{ \alpha } { \phi_0 } - 1) $

Where:

- $ \alpha $ is the Biot coefficient (see $ST\_{ii}$ definition above for details),
- $ \Delta\epsilon\_{vol} $ is volumetric strain change (EV in ResInsight) between curret state and reference state,
- $ \phi_0 $ is porosity on the Geostatic step,
- $ \Delta P\_p $ is change in pore pressure between current state and reference state,
- $ K\_s $ bulk modulus for the solid material (grain).

The bulk modulus for solid material is defined as:

$ K\_s = \frac{ K\_{fr} }{ 1 - \alpha}, K\_{fr} = \frac{ E }{ 3(1-2\nu)} $

Where:

- $ E $ is the elastic modulus (Young's modulus) from element property table [MODULUS]({{< relref "ElementPropertyTable.md" >}}).
- $ \nu $ is Poisson's ratio imported from element property table [RATIO]({{< relref "ElementPropertyTable.md" >}}).


#### Vertical Compressibility

$ C\_{v} = - \frac{ \Delta\epsilon\_{\nu}}{ \alpha \Delta P\_p } $

$ \Delta\epsilon\_\nu $ is the vertical strain change between current state and reference state (E33 in ResInsight).


#### Vertical Compressibility Ratio

$ C\_{vr} = \frac{ C\_v E(1-\nu) } { (1+\nu) ( 1 - 2\nu) } $

Vertical Compression Ratio is the ratio between the real vertical compression and the compression in a uniaxial strain case.
All parameters are described above.
