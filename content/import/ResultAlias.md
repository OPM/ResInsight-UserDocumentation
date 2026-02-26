+++
title = "Result Aliases"

weight = 35
+++

**Result Aliases** allow users to assign alternative names to simulation result properties in grid model cases. This is useful when a result has a technical or cryptic name in the simulation file and a more descriptive name is preferred throughout the project.

When an alias is defined, it can be used anywhere a result property is selected — in cell colors, property filters, well log curves, and more — and ResInsight will transparently resolve it to the underlying result.

If the alias name is identical to an existing result name, the alias result takes precedence over the original.

Result aliases are also useful for custom input results used in computations. For example, when exporting **COMPDAT**, specific result names may be required as input to the computation. By defining an alias that maps an existing result to the expected name, the export workflow can find and use the correct data without modifying the underlying simulation results.

## Accessing Result Aliases

Result aliases are configured in the **Property Editor** of a simulation model. Select the simulation model in the **Project Tree** and scroll to the **Result Name Aliases** group in the **Property Editor**. The group is collapsed by default.

## Adding an Alias

Click **Add Result Alias** to add a new entry to the alias table. Each entry has two fields:

| Field | Description |
|-------|-------------|
| **Result Name** | The original result name as it appears in the simulation file. A dropdown lists all available results. |
| **Alias Name** | The user-defined alternative name to use instead. |

Fill in both fields. The alias is active immediately and available in all result selectors within the case.

## Removing Aliases

Click **Reset Result Aliases** to remove all defined aliases for the case. Individual entries can also be deleted by selecting them in the table and pressing **Delete**.

## Persistence

Aliases are saved in the ResInsight project file and are restored when the project is reopened.

## Scripting

Result aliases can be managed via the Python scripting API:

```python
import rips

resinsight = rips.Instance.find()
case = resinsight.project.case(case_id=0)

# Add an alias
case.add_result_alias(result_name="MY_PORO_NAME", alias_name="PORO")

# Clear all aliases
case.clear_result_aliases()
```

See [Python API]({{% relref "pythoninterface" %}}) for details on connecting to ResInsight from Python.
