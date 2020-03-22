+++
title = "GridCaseGroup"
published = true
+++


# GridCaseGroup
```python
GridCaseGroup(self, pb2_object=None, channel=None)
```

A statistics case group

**Attributes**:

- `group_id` _int_ - Case Group ID
- `user_description` _str_ - Name
  

## create_statistics_case
```python
GridCaseGroup.create_statistics_case()
```
Create a Statistics case in the Grid Case Group

**Returns**:

  A new Case
  

## statistics_cases
```python
GridCaseGroup.statistics_cases()
```
Get a list of all statistics cases in the Grid Case Group

## views
```python
GridCaseGroup.views()
```
Get a list of views belonging to a grid case group

## view
```python
GridCaseGroup.view(view_id)
```
Get a particular view belonging to a case group by providing view id

**Arguments**:

- `id(int)` - view id
  
- `Returns` - a view object
  
  

## compute_statistics
```python
GridCaseGroup.compute_statistics(case_ids=None)
```
Compute statistics for the given case ids

**Arguments**:

  case_ids(list of integers): list of case ids.
  If this is None all cases in group are included
  
  
