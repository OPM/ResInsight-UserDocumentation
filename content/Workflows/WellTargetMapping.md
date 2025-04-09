+++
title = "Well Target Mapping"

weight = 90
+++


![](/images/workflows/well-target-mapping.png)

Automatically identify new well target candidates by identifying connected cluster of cells based on user defined threshold values.

[Video Tutorial: Well Target Mapping](https://youtu.be/O-ms2ImgAwM?si=T_F_EdmeLDqE5_CN)

## Configuration

Import a grid model, and from the right-click menu of a grid model select **"New Well Target Mapping"**. A **Well Target Mapping** object is displayed with the following options:

![](/images/workflows/well-target-mapping-properties.png)

Click **Generate** button to compute well target candidates for the grid model. Several results will be computed and available for selection in the **Generated** section for **Cell Results**. The first available view will be used to display the well target clusters.


**Result**

- **Time Step**: the time step of the Eclipse case to produce results for. Default: last time step.
- **Volume**: Oil, Gas, or Hydrocarbon.
- **Result**: Mobile or Total.
- **Volume type**: The vectors used to define the volumes of hydrocarbon. Unavailable options are not shown.
  - Reservoir Volumes (PORV\*SOIL, PORV\*SGAS)
  - Reservoir Volumes (RFIPOIL, RFIPGAS)
  - Surface Volumes (SFIPOIL, SFIPGAS)
  - Surface Volumes (FIPOIL, FIPGAS)



**Minimum Cell Values**

Filter which defines the threshold values to include a candidate cell to a cell cluster.

- **Saturation Oil**: Saturation of oil (fraction). Default: 0.3.
- **Saturation Gas**: Saturation of gas (fraction). Default: 0.3.
- **Pressure**: Minimum pressure. P90 of pressure values.
- **Permeability**: Minimum horizontal permeability (i.e. PERMX).

When **Hydrocarbon Volume** is chosen either **Saturation Oil** or **Saturation Gas** has to be equal to or above the threshold.

## Total Volumes

| Volume      | Equation
|-------------|-----------------------------------------------|
| Oil         | $VOLOIL\_t = PORV * SOIL\_t$                  |
| Gas         | $VOLGAS\_t = PORV * SGAS\_t$                  |
| Hydrocarbon | $VOLHC\_t = PORV * SOIL\_t +  PORV * SGAS\_t$ |

Gas volume is converted to oil equivalents.


## Mobile Volumes: Oil

| Volume Type  | Residual Oil Given By | Equation
|--------------|-----------------------|----------------------------------------------------------------|
| PORV\*SOIL   | Gas Flooding          | $VOLOIL\_t = max( PORV * SOIL\_t - PORV * SOGCR, 0.0)$         |
| PORV\*SOIL   | Water Flooding        | $VOLOIL\_t = max( PORV * SOIL\_t - PORV * SOWCR, 0.0)$         |
| PORV\*SOIL   | User Defined Value    | $VOLOIL\_t = max( PORV * SOIL\_t - PORV * value, 0.0)$         |
| FIPOIL       | Gas Flooding          | $VOLOIL\_t = max( FIPOIL * ( SOIL\_t - SOGCR) / SOIL\_t, 0.0)$ |
| FIPOIL       | Water Flooding        | $VOLOIL\_t = max( FIPOIL * ( SOIL\_t - SOWCR) / SOIL\_t, 0.0)$ |
| FIPOIL       | User Defined Value    | $VOLOIL\_t = max( FIPOIL * ( SOIL\_t - value) / SOIL\_t, 0.0)$ |

## Mobile Volumes: Gas

| Volume Type  | Residual Gas Given By | Equation
|--------------|-----------------------|----------------------------------------------------------------|
| PORV\*SGAS   | Gas Flooding          | $VOLGAS\_t = max( PORV * SGAS\_t - PORV * SGCR, 0.0)$          |
| PORV\*SGAS   | User Defined Value    | $VOLGAS\_t = max( PORV * SGAS\_t - PORV * value, 0.0)$         |
| FIPGAS       | Gas Flooding          | $VOLGAS\_t = max( FIPGAS * ( SGAS\_t - SGCR) / SGAS\_t, 0.0)$  |
| FIPGAS       | User Defined Value    | $VOLGAS\_t = max( FIPGAS * ( SGAS\_t - value) / SGAS\_t, 0.0)$ |

Gas volume is converted to oil equivalents.

## Mobile Volumes: Hydrocarbon

The mobile hydrocarbon volume is sum of the oil and gas volumes.

$VOLHC\_t = VOLOIL\_t + VOLGAS\_t$
