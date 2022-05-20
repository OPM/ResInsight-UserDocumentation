+++
title = "Grid Property Calculator"
published = true
weight = 105
+++

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorMain.png)

ResInsight offers a built-in property calculator for grid parameters. 
The **Grid Property Calculator** enables arithmetic expressions to be parsed and calculated for visualization purposes.

## Invoking the Grid Property Calculator
Invoke the the **Grid Property Calculator** by right-clicking 
{{< image-in-text src="images/3d-main-window/CellResult.png" >}} **Cell Result** in **Project Tree**. 

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorInvoke.png)


## Example using Grid Property Calculator
As shown, the **Grid Property Calculator** is invoked by right-clicking 
{{< image-in-text src="images/3d-main-window/CellResult.png" >}} **Cell Result** in **Project Tree**.
As seen below, the **Grid Property Calculator** is per default prefilled with the simple summation 
*Calculation_1 := x + y*. 
Though you may add additional variables and arithmetic operators, the simple summation suffices for examplifying its use.

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorDefault.png)

The next step is to define the variables *x* and *y*. 
An easy way to define each variable is to drag and drop properties from **Data Sources**. See screenshot below for drag and drop of *SOIL* from **Data Sources** to the row of variable *x* in **Grid Property Calculator** (emphasized in red). 
Continue with drag and drop of *SGAS* to define *y*.

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorDragDrop.png)

Finally, press **Calculate** to perform the actual calculation. 

The calculated result is accessable via **Property Editor** as **Type** ***Generated*** **Result Property**.

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorGeneratedProperty.png)


## Reference Procedure for Grid Property Calculator

1. Invoke the the **Grid Property Calculator** by right-clicking 
{{< image-in-text src="images/3d-main-window/CellResult.png" >}} **Cell Result** in **Project Tree**.
1. Define the expression for calculation by the involved variables and arithmetic operators
   - Type the required variables and aritmetic operators into the *Expression* field
   - Press button **Parse Expression** to verify the expression and referrals to actual variables
1. Define each actual variable referred by the expression, e.g. by drag and drop from **Data Sources**
1. Press **Calculate** to perform the actual calculation
1. Access the calculated result in **Property Editor** as **Type** ***Generated*** **Result Property**

![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorSolo.png)


