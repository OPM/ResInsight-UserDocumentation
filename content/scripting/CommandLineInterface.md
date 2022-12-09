+++
title = "Command Line Interface"
published = true
weight = 20
+++

ResInsight supports several command line parameters that can be used to automate some tasks using shell scripts. 

Command line parameters are prefixed using a double dash. This convention is used on all platforms to make it possible to reuse scripts across different platforms. See GNU Standards for [Command Line Interfaces](http://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html#Command_002dLine-Interfaces).

Examples on how command line options are used are given [below]({{< relref "commandlineinterface" >}}#examples)


## Command line options

### General

| Parameter | Description |
|-----------|-------------|
| &#45;&#45;help, &#45;&#45;?           | Displays help text and version info |
| &#45;&#45;project &lt;filename&gt;    | Open project file &lt;filename&gt;. |
| &#45;&#45;last                        | Open last used project. |
| &#45;&#45;size &lt;width&gt; &lt;height&gt;  | Set size of the main application window. |
| &#45;&#45;console                     | Launch as a console application without graphics |
| &#45;&#45;server [&lt;portnumber&gt;] | Launch as a GRPC server. Default port is 50051 |
| &#45;&#45;startdir &lt;folder&gt;     | Set startup directory. |

### Command files

| Parameter | Description |
|-----------|-------------|
| &#45;&#45;commandFile &lt;commandFile&gt; | Execute a command file. See [command file documentation.]({{< relref "commandfile" >}}) |
| &#45;&#45;commandFileProject &lt;filename&gt; | Project to use if performing case looping for command file. Used in conjunction with `commandFileReplaceCases`. |

### Snapshots

| Parameter | Description |
|-----------|-------------|
| &#45;&#45;savesnapshots all&#124;views&#124;plots&#124;          | Save snapshot of all views or plots to project file location sub folder 'snapshots'. Option 'all' will include both views and plots. Application closes after snapshots have been written.|
| &#45;&#45;multiCaseSnapshots &lt;gridListFile&gt; | For each grid file listed in the &lt;gridListFile&gt; file, replace the first case in the project and save snapshot of all views. |

### Case handling

| Parameter | Description |
|-----------|-------------|
| &#45;&#45;case &lt;casename&#124;filename&gt; [&lt;casename&#124;filename&gt;]       | Imports the Eclipse cases specified by case name with or without extension.If &lt;casename&gt;, import the corresponding grid file and summary file. If &lt;filename&gt; has extension .GRRID/.EGRID, import the grid file and corresponding summary file. If &lt;filename&gt; has extension .SMSPEC, import the summary file (does not open the grid file) |
| &#45;&#45;replaceCase [&lt;caseId&gt;] &lt;newGridFile&gt;  | Replace grid in &lt;caseId&gt; or first case with &lt;newGridFile&gt;. Repeat parameter for multiple replace operations.|
| &#45;&#45;replaceSourceCases [&lt;caseGroupId&gt;] &lt;gridListFile&gt; | Replace source cases in &lt;caseGroupId&gt; or first grid case group with the grid files listed in the &lt;gridListFile&gt; file. Repeat parameter for multiple replace operations.|
| &#45;&#45;commandFileReplaceCases [&lt;caseId&gt;] &lt;caseListFile&gt; | Supply list of cases to replace in project, performing command file for each case. Project to replace cases must be set with `commandFileProject`. If caseId is not supplied, first case is replaced. When supplying caseId, multiple cases may be replaced at once, by supplying several caseIds and a file containing a list of grid-files to replace with for each caseId. |



{{% notice note %}}
<b>Reduce project load time using <code>--replaceSourceCases</code></b>
 <br>
ResInsight stores data computed by statistics calculation in a cache file. When a project file is loaded, data from this cache is also imported. For large cases, the cached data can be large. When replacing source cases during batch, this data is never used and can be removed from the cache using the following workaround:
<br>
  - Open the project file used to produce statistics
  <br>
  - Select the statistics object in the project tree
  <br>
  - Click the button <b>Edit (Will DELETE current result)</b>
  <br>
  - Save the project file 
{{% /notice %}}


### Summary plotting
The summary plotting command option follows the following syntax:

```
resinsight --summaryplot [<plotOptions>] <eclipsesummaryvectorfilters> <eclipsedatafiles>

where:
<plotOptions>                 denote summary plot options, see table below
<eclipsesummaryvectorfilters> has the syntax <vectorname>[:<item>[:<subitem>[:i,j,k]]]
<eclipsedatafiles>            lists a set of Eclipse data files with or without extension
```

The summary plotting command option creates one summary plot for each of the the summary vectors matched by  
*\<eclipsesummaryvectorfilters\>* using all listed Eclipse data files in each plot.

Eclipse summary vector filters specify a list of vectors separated by spaces following the syntax noted above. 
Wildcards can be used in the specification. Brief examples are: 

- `WOPT:*`: One total oil production curve for each well.
- `FOPT FWPT`: Two curves with oil and water total production.
- `BPR:15,28,*`: Oil phase pressure for all blocks along k as separate curves. Please note no space in expression.

[Examples]({{< relref "commandlineinterface#summary-plotting-1" >}}) are listed below.

As long as only summary vectors are requested, only the corresponding SMSPEC file will be opened for each case.
However, if a grid property is requested, the corresponding EGRID and restart data will be loaded as well.

Specifying summary plot options is optional, c.f. table below.


| Option     | Description |
|------------|-------------|
| &#45;help  | Shows help text and ignores any other option.
| &#45;h     | Includes history vectors read from summary file if the vectors exist. Only history vectors from the first summary case in the project will be included.
| &#45;nl    | Omits legend in plot.
| &#45;s     | Creates only one plot including all the defined vectors and cases.
| &#45;n     | Scales all curves into the range 0.0-1.0. Useful when using -s.
| &#45;e     | Imports all the cases as an ensemble, and create ensemble curves sets instead of single curves.
| &#45;c  &lt;parametername&gt; | Same as *-e*, but colors the curves by the ensemble parameter <parametername> . 
| &#45;cl &lt;parametername&gt; | Same as *-c*, but uses logarithmic legend.

### Testing

| Parameter | Description |
|-----------|-------------|
| &#45;&#45;regressiontest &lt;folder&gt; | System command |
| &#45;&#45;updateregressiontestbase &lt;folder&gt; | System command |
| &#45;&#45;unittest | Execute integration tests |
| &#45;&#45;ignoreArgs | System command |

See also the [Regression Test System ]({{< relref "regressiontestsystem" >}}) for a more in-depth explanation.


## Examples 

Most examples are also available from the [test section](https://github.com/OPM/ResInsight/tree/master/TestModels/Case_with_10_timesteps).

### Create snapshots of all views for multiple cases
A list of cases is defined in **CaseList.txt**, containing the following

```
Real0/BRUGGE_0000.EGRID
Real10/BRUGGE_0010.EGRID
Real30/BRUGGE_0030.EGRID
Real40/BRUGGE_0040.EGRID
```

The command line used to run this example is shown here:

```
ResInsight --project BatchTest.rsp --multiCaseSnapshots CaseList.txt --size 500 500
```

This will instruct ResInsight to read the project file **BatchTest.rsp**. All cases will be replaced one by one in ResInsight, and snapshots of all views will be written to file. 


### Replace a single case and take snapshots of all views

The command line used to run this example is shown here:

```
ResInsight --project BatchTest.rsp --replaceCase "Real10\BRUGGE_0010.EGRID" --savesnapshots
```

This will instruct ResInsight to read the project file **BatchTest.rsp**. The specified case **Real10\BRUGGE_0010.EGRID** will be imported into the project, and snapshots of all views will be written to file. 


### Replace source cases in a case group and create snapshot
A list of cases is defined in **CaseList2.txt**, containing the following

```
Real0/BRUGGE_0000.EGRID
Real10/BRUGGE_0010.EGRID
```

The command line used to run this example is shown here:

```
ResInsight --project BatchStatistics.rsp --replaceSourceCases CaseList2.txt --savesnapshots
```

This will instruct ResInsight to read the project file **BatchStatistics.rsp**. All cases specified will be imported in the case group specified in the project file. Statistics will be computed, and snapshots for all views will be written to file.

### Replace source cases in multiple case groups and create snapshots
Multiple source case groups can be updated by repeating the replaceSourceCases parameter.

The command line used to run this example is shown here:

```
ResInsight --project BatchStatistics.rsp --replaceSourceCases 0 CaseList2.txt --replaceSourceCases 1 CaseList3.txt --savesnapshots
```
This will instruct ResInsight to read the project file **BatchStatistics.rsp**. Source cases for case group 0 is given in CaseList2.txt, and source cases for case group 1 is given in CaseList3.txt. Statistics will be computed, and snapshots for all views will be written to file.

The possibility to replace multiple cases can also be applied for single case replace (parameter *replaceCase*).


### Summary plotting

The following command line performs a [summary plot]({{< relref "summaryplots" >}}) for *FOPT* based on Eclipse summary file *1_R001_REEK-0.SMSPEC*.

```
ResInsight --summaryplot FOPT 1_R001_REEK-0 
```

Based on file *1_R001_REEK-0.SMSPEC*, the following command line performs a [summary plot]({{< relref "summaryplots" >}}) 
for *FOPT* and any *WOPT*-vector for well *op_2*.
The trailing option *-s* gathers the vectors into a single summary plot.
```
ResInsight --summaryplot -s FOPT WOPT*:op_2 1_R001_REEK-0
```

Adding to previous example, the following command line also plots the 3D grid property `SOIL` for cell (20, 21, 1).
```
ResInsight --summaryplot FOPT WOPT*:op_2 SOIL:20,21,1 1_R001_REEK-0 
```


