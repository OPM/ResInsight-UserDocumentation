+++
title = "Well Target Mapping"

weight = 90
+++


### Introduction ###

Automatically find suitable well targets.




## Configuration ##

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

Filter which defines which cells that can be included in a well target.

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
