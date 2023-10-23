import Case_pb2 as _Case_pb2
import Definitions_pb2 as _Definitions_pb2
import PdmObject_pb2 as _PdmObject_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlotOutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PNG: _ClassVar[PlotOutputFormat]
    PDF: _ClassVar[PlotOutputFormat]

class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VIEWS: _ClassVar[SnapshotType]
    PLOTS: _ClassVar[SnapshotType]
    ALL: _ClassVar[SnapshotType]

class CompdatExportSplit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNIFIED_FILE: _ClassVar[CompdatExportSplit]
    SPLIT_ON_WELL: _ClassVar[CompdatExportSplit]
    SPLIT_ON_WELL_AND_COMPLETION_TYPE: _ClassVar[CompdatExportSplit]

class CompdatExportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSMISSIBILITIES: _ClassVar[CompdatExportType]
    WPIMULT_AND_DEFAULT_CONNECTION_FACTORS: _ClassVar[CompdatExportType]
    NO_COMPLETIONS: _ClassVar[CompdatExportType]

class CompdatCombinationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INDIVIDUALLY: _ClassVar[CompdatCombinationMode]
    COMBINED: _ClassVar[CompdatCombinationMode]

class ExportFolderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPLETIONS: _ClassVar[ExportFolderType]
    SNAPSHOTS: _ClassVar[ExportFolderType]
    PROPERTIES: _ClassVar[ExportFolderType]
    STATISTICS: _ClassVar[ExportFolderType]
    WELLPATHS: _ClassVar[ExportFolderType]
    CELLS: _ClassVar[ExportFolderType]
    LGRS: _ClassVar[ExportFolderType]

class MultipleFracAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NONE: _ClassVar[MultipleFracAction]
    APPEND_FRACTURES: _ClassVar[MultipleFracAction]
    REPLACE_FRACTURES: _ClassVar[MultipleFracAction]

class LgrSplitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LGR_PER_CELL: _ClassVar[LgrSplitType]
    LGR_PER_COMPLETION: _ClassVar[LgrSplitType]
    LGR_PER_WELL: _ClassVar[LgrSplitType]

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LAS: _ClassVar[ExportFormat]
    ASCII: _ClassVar[ExportFormat]
PNG: PlotOutputFormat
PDF: PlotOutputFormat
VIEWS: SnapshotType
PLOTS: SnapshotType
ALL: SnapshotType
UNIFIED_FILE: CompdatExportSplit
SPLIT_ON_WELL: CompdatExportSplit
SPLIT_ON_WELL_AND_COMPLETION_TYPE: CompdatExportSplit
TRANSMISSIBILITIES: CompdatExportType
WPIMULT_AND_DEFAULT_CONNECTION_FACTORS: CompdatExportType
NO_COMPLETIONS: CompdatExportType
INDIVIDUALLY: CompdatCombinationMode
COMBINED: CompdatCombinationMode
COMPLETIONS: ExportFolderType
SNAPSHOTS: ExportFolderType
PROPERTIES: ExportFolderType
STATISTICS: ExportFolderType
WELLPATHS: ExportFolderType
CELLS: ExportFolderType
LGRS: ExportFolderType
NONE: MultipleFracAction
APPEND_FRACTURES: MultipleFracAction
REPLACE_FRACTURES: MultipleFracAction
LGR_PER_CELL: LgrSplitType
LGR_PER_COMPLETION: LgrSplitType
LGR_PER_WELL: LgrSplitType
LAS: ExportFormat
ASCII: ExportFormat

class FilePathRequest(_message.Message):
    __slots__ = ["path", "gridOnly"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    GRIDONLY_FIELD_NUMBER: _ClassVar[int]
    path: str
    gridOnly: bool
    def __init__(self, path: _Optional[str] = ..., gridOnly: bool = ...) -> None: ...

class ReplaceCaseRequest(_message.Message):
    __slots__ = ["newGridFile", "caseId"]
    NEWGRIDFILE_FIELD_NUMBER: _ClassVar[int]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    newGridFile: str
    caseId: int
    def __init__(self, newGridFile: _Optional[str] = ..., caseId: _Optional[int] = ...) -> None: ...

class ReplaceCaseRequests(_message.Message):
    __slots__ = ["casePairs"]
    CASEPAIRS_FIELD_NUMBER: _ClassVar[int]
    casePairs: _containers.RepeatedCompositeFieldContainer[ReplaceCaseRequest]
    def __init__(self, casePairs: _Optional[_Iterable[_Union[ReplaceCaseRequest, _Mapping]]] = ...) -> None: ...

class ReplaceSourceCasesRequest(_message.Message):
    __slots__ = ["gridListFile", "caseGroupId"]
    GRIDLISTFILE_FIELD_NUMBER: _ClassVar[int]
    CASEGROUPID_FIELD_NUMBER: _ClassVar[int]
    gridListFile: str
    caseGroupId: int
    def __init__(self, gridListFile: _Optional[str] = ..., caseGroupId: _Optional[int] = ...) -> None: ...

class ExportMultiCaseRequest(_message.Message):
    __slots__ = ["gridListFile"]
    GRIDLISTFILE_FIELD_NUMBER: _ClassVar[int]
    gridListFile: str
    def __init__(self, gridListFile: _Optional[str] = ...) -> None: ...

class ExportSnapshotsRequest(_message.Message):
    __slots__ = ["type", "prefix", "caseId", "viewId", "exportFolder", "plotOutputFormat"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    EXPORTFOLDER_FIELD_NUMBER: _ClassVar[int]
    PLOTOUTPUTFORMAT_FIELD_NUMBER: _ClassVar[int]
    type: SnapshotType
    prefix: str
    caseId: int
    viewId: int
    exportFolder: str
    plotOutputFormat: PlotOutputFormat
    def __init__(self, type: _Optional[_Union[SnapshotType, str]] = ..., prefix: _Optional[str] = ..., caseId: _Optional[int] = ..., viewId: _Optional[int] = ..., exportFolder: _Optional[str] = ..., plotOutputFormat: _Optional[_Union[PlotOutputFormat, str]] = ...) -> None: ...

class ExportPropertyRequest(_message.Message):
    __slots__ = ["caseId", "timeStep", "property", "eclipseKeyword", "undefinedValue", "exportFile"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ECLIPSEKEYWORD_FIELD_NUMBER: _ClassVar[int]
    UNDEFINEDVALUE_FIELD_NUMBER: _ClassVar[int]
    EXPORTFILE_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    timeStep: int
    property: str
    eclipseKeyword: str
    undefinedValue: float
    exportFile: str
    def __init__(self, caseId: _Optional[int] = ..., timeStep: _Optional[int] = ..., property: _Optional[str] = ..., eclipseKeyword: _Optional[str] = ..., undefinedValue: _Optional[float] = ..., exportFile: _Optional[str] = ...) -> None: ...

class ExportPropertyInViewsRequest(_message.Message):
    __slots__ = ["caseId", "viewIds", "undefinedValue"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    VIEWIDS_FIELD_NUMBER: _ClassVar[int]
    UNDEFINEDVALUE_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    viewIds: _containers.RepeatedScalarFieldContainer[int]
    undefinedValue: float
    def __init__(self, caseId: _Optional[int] = ..., viewIds: _Optional[_Iterable[int]] = ..., undefinedValue: _Optional[float] = ...) -> None: ...

class ExportWellPathCompRequest(_message.Message):
    __slots__ = ["caseId", "timeStep", "wellPathNames", "fileSplit", "compdatExport", "includePerforations", "includeFishbones", "excludeMainBoreForFishbones", "combinationMode", "customFileName", "exportComments", "exportWelspec"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    FILESPLIT_FIELD_NUMBER: _ClassVar[int]
    COMPDATEXPORT_FIELD_NUMBER: _ClassVar[int]
    INCLUDEPERFORATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEFISHBONES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDEMAINBOREFORFISHBONES_FIELD_NUMBER: _ClassVar[int]
    COMBINATIONMODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMFILENAME_FIELD_NUMBER: _ClassVar[int]
    EXPORTCOMMENTS_FIELD_NUMBER: _ClassVar[int]
    EXPORTWELSPEC_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    timeStep: int
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    fileSplit: CompdatExportSplit
    compdatExport: CompdatExportType
    includePerforations: bool
    includeFishbones: bool
    excludeMainBoreForFishbones: bool
    combinationMode: CompdatCombinationMode
    customFileName: str
    exportComments: bool
    exportWelspec: bool
    def __init__(self, caseId: _Optional[int] = ..., timeStep: _Optional[int] = ..., wellPathNames: _Optional[_Iterable[str]] = ..., fileSplit: _Optional[_Union[CompdatExportSplit, str]] = ..., compdatExport: _Optional[_Union[CompdatExportType, str]] = ..., includePerforations: bool = ..., includeFishbones: bool = ..., excludeMainBoreForFishbones: bool = ..., combinationMode: _Optional[_Union[CompdatCombinationMode, str]] = ..., customFileName: _Optional[str] = ..., exportComments: bool = ..., exportWelspec: bool = ...) -> None: ...

class ExportSimWellPathFracRequest(_message.Message):
    __slots__ = ["caseId", "viewId", "timeStep", "simulationWellNames", "fileSplit", "compdatExport"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    SIMULATIONWELLNAMES_FIELD_NUMBER: _ClassVar[int]
    FILESPLIT_FIELD_NUMBER: _ClassVar[int]
    COMPDATEXPORT_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    viewId: int
    timeStep: int
    simulationWellNames: _containers.RepeatedScalarFieldContainer[str]
    fileSplit: CompdatExportSplit
    compdatExport: CompdatExportType
    def __init__(self, caseId: _Optional[int] = ..., viewId: _Optional[int] = ..., timeStep: _Optional[int] = ..., simulationWellNames: _Optional[_Iterable[str]] = ..., fileSplit: _Optional[_Union[CompdatExportSplit, str]] = ..., compdatExport: _Optional[_Union[CompdatExportType, str]] = ...) -> None: ...

class ExportMswRequest(_message.Message):
    __slots__ = ["caseId", "wellPath"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    WELLPATH_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    wellPath: str
    def __init__(self, caseId: _Optional[int] = ..., wellPath: _Optional[str] = ...) -> None: ...

class ExportWellPathRequest(_message.Message):
    __slots__ = ["wellPathNames", "mdStepSize"]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    MDSTEPSIZE_FIELD_NUMBER: _ClassVar[int]
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    mdStepSize: float
    def __init__(self, wellPathNames: _Optional[_Iterable[str]] = ..., mdStepSize: _Optional[float] = ...) -> None: ...

class ExportVisibleCellsRequest(_message.Message):
    __slots__ = ["caseId", "viewId", "exportKeyword", "visibleActiveCellsValue", "hiddenActiveCellsValue", "inactiveCellsValue"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    EXPORTKEYWORD_FIELD_NUMBER: _ClassVar[int]
    VISIBLEACTIVECELLSVALUE_FIELD_NUMBER: _ClassVar[int]
    HIDDENACTIVECELLSVALUE_FIELD_NUMBER: _ClassVar[int]
    INACTIVECELLSVALUE_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    viewId: int
    exportKeyword: str
    visibleActiveCellsValue: int
    hiddenActiveCellsValue: int
    inactiveCellsValue: int
    def __init__(self, caseId: _Optional[int] = ..., viewId: _Optional[int] = ..., exportKeyword: _Optional[str] = ..., visibleActiveCellsValue: _Optional[int] = ..., hiddenActiveCellsValue: _Optional[int] = ..., inactiveCellsValue: _Optional[int] = ...) -> None: ...

class SetExportFolderRequest(_message.Message):
    __slots__ = ["type", "path", "createFolder"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CREATEFOLDER_FIELD_NUMBER: _ClassVar[int]
    type: ExportFolderType
    path: str
    createFolder: bool
    def __init__(self, type: _Optional[_Union[ExportFolderType, str]] = ..., path: _Optional[str] = ..., createFolder: bool = ...) -> None: ...

class RunOctaveScriptRequest(_message.Message):
    __slots__ = ["path", "caseIds"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CASEIDS_FIELD_NUMBER: _ClassVar[int]
    path: str
    caseIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, path: _Optional[str] = ..., caseIds: _Optional[_Iterable[int]] = ...) -> None: ...

class SetWindowSizeParams(_message.Message):
    __slots__ = ["height", "width"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class ComputeCaseGroupStatRequest(_message.Message):
    __slots__ = ["caseIds", "caseGroupId"]
    CASEIDS_FIELD_NUMBER: _ClassVar[int]
    CASEGROUPID_FIELD_NUMBER: _ClassVar[int]
    caseIds: _containers.RepeatedScalarFieldContainer[int]
    caseGroupId: int
    def __init__(self, caseIds: _Optional[_Iterable[int]] = ..., caseGroupId: _Optional[int] = ...) -> None: ...

class SetTimeStepParams(_message.Message):
    __slots__ = ["caseId", "viewId", "timeStep"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    viewId: int
    timeStep: int
    def __init__(self, caseId: _Optional[int] = ..., viewId: _Optional[int] = ..., timeStep: _Optional[int] = ...) -> None: ...

class ScaleFractureTemplateRequest(_message.Message):
    __slots__ = ["id", "halfLength", "height"]
    ID_FIELD_NUMBER: _ClassVar[int]
    HALFLENGTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    halfLength: float
    height: float
    def __init__(self, id: _Optional[int] = ..., halfLength: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class SetFracContainmentRequest(_message.Message):
    __slots__ = ["id", "topLayer", "baseLayer"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOPLAYER_FIELD_NUMBER: _ClassVar[int]
    BASELAYER_FIELD_NUMBER: _ClassVar[int]
    id: int
    topLayer: int
    baseLayer: int
    def __init__(self, id: _Optional[int] = ..., topLayer: _Optional[int] = ..., baseLayer: _Optional[int] = ...) -> None: ...

class CreateMultipleFracRequest(_message.Message):
    __slots__ = ["caseId", "templateId", "wellPathNames", "minDistFromWellTd", "maxFracturesPerWell", "topLayer", "baseLayer", "spacing", "action"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    MINDISTFROMWELLTD_FIELD_NUMBER: _ClassVar[int]
    MAXFRACTURESPERWELL_FIELD_NUMBER: _ClassVar[int]
    TOPLAYER_FIELD_NUMBER: _ClassVar[int]
    BASELAYER_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    templateId: int
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    minDistFromWellTd: float
    maxFracturesPerWell: int
    topLayer: int
    baseLayer: int
    spacing: int
    action: MultipleFracAction
    def __init__(self, caseId: _Optional[int] = ..., templateId: _Optional[int] = ..., wellPathNames: _Optional[_Iterable[str]] = ..., minDistFromWellTd: _Optional[float] = ..., maxFracturesPerWell: _Optional[int] = ..., topLayer: _Optional[int] = ..., baseLayer: _Optional[int] = ..., spacing: _Optional[int] = ..., action: _Optional[_Union[MultipleFracAction, str]] = ...) -> None: ...

class CreateLgrForCompRequest(_message.Message):
    __slots__ = ["caseId", "timeStep", "wellPathNames", "refinementI", "refinementJ", "refinementK", "splitType"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    REFINEMENTI_FIELD_NUMBER: _ClassVar[int]
    REFINEMENTJ_FIELD_NUMBER: _ClassVar[int]
    REFINEMENTK_FIELD_NUMBER: _ClassVar[int]
    SPLITTYPE_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    timeStep: int
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    refinementI: int
    refinementJ: int
    refinementK: int
    splitType: LgrSplitType
    def __init__(self, caseId: _Optional[int] = ..., timeStep: _Optional[int] = ..., wellPathNames: _Optional[_Iterable[str]] = ..., refinementI: _Optional[int] = ..., refinementJ: _Optional[int] = ..., refinementK: _Optional[int] = ..., splitType: _Optional[_Union[LgrSplitType, str]] = ...) -> None: ...

class CreateSatPressPlotRequest(_message.Message):
    __slots__ = ["caseIds"]
    CASEIDS_FIELD_NUMBER: _ClassVar[int]
    caseIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, caseIds: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateGridCaseGroupRequest(_message.Message):
    __slots__ = ["casePaths"]
    CASEPATHS_FIELD_NUMBER: _ClassVar[int]
    casePaths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, casePaths: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateStatisticsCaseRequest(_message.Message):
    __slots__ = ["caseGroupId"]
    CASEGROUPID_FIELD_NUMBER: _ClassVar[int]
    caseGroupId: int
    def __init__(self, caseGroupId: _Optional[int] = ...) -> None: ...

class ExportFlowInfoRequest(_message.Message):
    __slots__ = ["caseId", "timeSteps", "injectors", "producers", "fileName", "minimumCommunication", "aquiferCellThreshold"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    TIMESTEPS_FIELD_NUMBER: _ClassVar[int]
    INJECTORS_FIELD_NUMBER: _ClassVar[int]
    PRODUCERS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MINIMUMCOMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    AQUIFERCELLTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    timeSteps: _containers.RepeatedScalarFieldContainer[int]
    injectors: _containers.RepeatedScalarFieldContainer[str]
    producers: _containers.RepeatedScalarFieldContainer[str]
    fileName: str
    minimumCommunication: float
    aquiferCellThreshold: float
    def __init__(self, caseId: _Optional[int] = ..., timeSteps: _Optional[_Iterable[int]] = ..., injectors: _Optional[_Iterable[str]] = ..., producers: _Optional[_Iterable[str]] = ..., fileName: _Optional[str] = ..., minimumCommunication: _Optional[float] = ..., aquiferCellThreshold: _Optional[float] = ...) -> None: ...

class CreateViewRequest(_message.Message):
    __slots__ = ["caseId"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    def __init__(self, caseId: _Optional[int] = ...) -> None: ...

class CloneViewRequest(_message.Message):
    __slots__ = ["viewId"]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    viewId: int
    def __init__(self, viewId: _Optional[int] = ...) -> None: ...

class CreateWbsPlotRequest(_message.Message):
    __slots__ = ["caseId", "wellPath", "timeStep", "wbsParameters"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    WELLPATH_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    WBSPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    wellPath: str
    timeStep: int
    wbsParameters: _PdmObject_pb2.PdmObject
    def __init__(self, caseId: _Optional[int] = ..., wellPath: _Optional[str] = ..., timeStep: _Optional[int] = ..., wbsParameters: _Optional[_Union[_PdmObject_pb2.PdmObject, _Mapping]] = ...) -> None: ...

class ImportWellPathsRequest(_message.Message):
    __slots__ = ["wellPathFolder", "wellPathFiles"]
    WELLPATHFOLDER_FIELD_NUMBER: _ClassVar[int]
    WELLPATHFILES_FIELD_NUMBER: _ClassVar[int]
    wellPathFolder: str
    wellPathFiles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wellPathFolder: _Optional[str] = ..., wellPathFiles: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportWellLogFilesRequest(_message.Message):
    __slots__ = ["wellLogFolder", "wellLogFiles"]
    WELLLOGFOLDER_FIELD_NUMBER: _ClassVar[int]
    WELLLOGFILES_FIELD_NUMBER: _ClassVar[int]
    wellLogFolder: str
    wellLogFiles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wellLogFolder: _Optional[str] = ..., wellLogFiles: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportFormationNamesRequest(_message.Message):
    __slots__ = ["formationFiles", "applyToCaseId"]
    FORMATIONFILES_FIELD_NUMBER: _ClassVar[int]
    APPLYTOCASEID_FIELD_NUMBER: _ClassVar[int]
    formationFiles: _containers.RepeatedScalarFieldContainer[str]
    applyToCaseId: int
    def __init__(self, formationFiles: _Optional[_Iterable[str]] = ..., applyToCaseId: _Optional[int] = ...) -> None: ...

class ExportWellLogPlotDataRequest(_message.Message):
    __slots__ = ["exportFormat", "viewId", "exportFolder", "filePrefix", "exportTvdRkb", "capitalizeFileNames", "resampleInterval", "convertCurveUnits"]
    EXPORTFORMAT_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    EXPORTFOLDER_FIELD_NUMBER: _ClassVar[int]
    FILEPREFIX_FIELD_NUMBER: _ClassVar[int]
    EXPORTTVDRKB_FIELD_NUMBER: _ClassVar[int]
    CAPITALIZEFILENAMES_FIELD_NUMBER: _ClassVar[int]
    RESAMPLEINTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONVERTCURVEUNITS_FIELD_NUMBER: _ClassVar[int]
    exportFormat: ExportFormat
    viewId: int
    exportFolder: str
    filePrefix: str
    exportTvdRkb: bool
    capitalizeFileNames: bool
    resampleInterval: float
    convertCurveUnits: bool
    def __init__(self, exportFormat: _Optional[_Union[ExportFormat, str]] = ..., viewId: _Optional[int] = ..., exportFolder: _Optional[str] = ..., filePrefix: _Optional[str] = ..., exportTvdRkb: bool = ..., capitalizeFileNames: bool = ..., resampleInterval: _Optional[float] = ..., convertCurveUnits: bool = ...) -> None: ...

class ExportContourMapToTextRequest(_message.Message):
    __slots__ = ["exportFileName", "exportLocalCoordinates", "undefinedValueLabel", "excludeUndefinedValues", "viewId"]
    EXPORTFILENAME_FIELD_NUMBER: _ClassVar[int]
    EXPORTLOCALCOORDINATES_FIELD_NUMBER: _ClassVar[int]
    UNDEFINEDVALUELABEL_FIELD_NUMBER: _ClassVar[int]
    EXCLUDEUNDEFINEDVALUES_FIELD_NUMBER: _ClassVar[int]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    exportFileName: str
    exportLocalCoordinates: bool
    undefinedValueLabel: str
    excludeUndefinedValues: bool
    viewId: int
    def __init__(self, exportFileName: _Optional[str] = ..., exportLocalCoordinates: bool = ..., undefinedValueLabel: _Optional[str] = ..., excludeUndefinedValues: bool = ..., viewId: _Optional[int] = ...) -> None: ...

class SaveProjectRequest(_message.Message):
    __slots__ = ["filePath"]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    filePath: str
    def __init__(self, filePath: _Optional[str] = ...) -> None: ...

class CommandParams(_message.Message):
    __slots__ = ["openProject", "closeProject", "setStartDir", "loadCase", "replaceCase", "replaceSourceCases", "exportMultiCaseSnapshots", "exportSnapshots", "exportProperty", "exportPropertyInViews", "exportWellPathCompletions", "exportSimWellFractureCompletions", "exportMsw", "exportWellPaths", "exportVisibleCells", "setExportFolder", "runOctaveScript", "setMainWindowSize", "computeCaseGroupStatistics", "setTimeStep", "scaleFractureTemplate", "setFractureContainment", "createMultipleFractures", "createLgrForCompletions", "createSaturationPressurePlots", "replaceMultipleCases", "createGridCaseGroup", "createStatisticsCase", "exportFlowCharacteristics", "createView", "cloneView", "createWellBoreStabilityPlot", "importWellPaths", "importWellLogFiles", "importFormationNames", "exportWellLogPlotData", "setPlotWindowSize", "exportContourMapToText", "saveProject"]
    OPENPROJECT_FIELD_NUMBER: _ClassVar[int]
    CLOSEPROJECT_FIELD_NUMBER: _ClassVar[int]
    SETSTARTDIR_FIELD_NUMBER: _ClassVar[int]
    LOADCASE_FIELD_NUMBER: _ClassVar[int]
    REPLACECASE_FIELD_NUMBER: _ClassVar[int]
    REPLACESOURCECASES_FIELD_NUMBER: _ClassVar[int]
    EXPORTMULTICASESNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    EXPORTSNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    EXPORTPROPERTY_FIELD_NUMBER: _ClassVar[int]
    EXPORTPROPERTYINVIEWS_FIELD_NUMBER: _ClassVar[int]
    EXPORTWELLPATHCOMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    EXPORTSIMWELLFRACTURECOMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    EXPORTMSW_FIELD_NUMBER: _ClassVar[int]
    EXPORTWELLPATHS_FIELD_NUMBER: _ClassVar[int]
    EXPORTVISIBLECELLS_FIELD_NUMBER: _ClassVar[int]
    SETEXPORTFOLDER_FIELD_NUMBER: _ClassVar[int]
    RUNOCTAVESCRIPT_FIELD_NUMBER: _ClassVar[int]
    SETMAINWINDOWSIZE_FIELD_NUMBER: _ClassVar[int]
    COMPUTECASEGROUPSTATISTICS_FIELD_NUMBER: _ClassVar[int]
    SETTIMESTEP_FIELD_NUMBER: _ClassVar[int]
    SCALEFRACTURETEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SETFRACTURECONTAINMENT_FIELD_NUMBER: _ClassVar[int]
    CREATEMULTIPLEFRACTURES_FIELD_NUMBER: _ClassVar[int]
    CREATELGRFORCOMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    CREATESATURATIONPRESSUREPLOTS_FIELD_NUMBER: _ClassVar[int]
    REPLACEMULTIPLECASES_FIELD_NUMBER: _ClassVar[int]
    CREATEGRIDCASEGROUP_FIELD_NUMBER: _ClassVar[int]
    CREATESTATISTICSCASE_FIELD_NUMBER: _ClassVar[int]
    EXPORTFLOWCHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    CREATEVIEW_FIELD_NUMBER: _ClassVar[int]
    CLONEVIEW_FIELD_NUMBER: _ClassVar[int]
    CREATEWELLBORESTABILITYPLOT_FIELD_NUMBER: _ClassVar[int]
    IMPORTWELLPATHS_FIELD_NUMBER: _ClassVar[int]
    IMPORTWELLLOGFILES_FIELD_NUMBER: _ClassVar[int]
    IMPORTFORMATIONNAMES_FIELD_NUMBER: _ClassVar[int]
    EXPORTWELLLOGPLOTDATA_FIELD_NUMBER: _ClassVar[int]
    SETPLOTWINDOWSIZE_FIELD_NUMBER: _ClassVar[int]
    EXPORTCONTOURMAPTOTEXT_FIELD_NUMBER: _ClassVar[int]
    SAVEPROJECT_FIELD_NUMBER: _ClassVar[int]
    openProject: FilePathRequest
    closeProject: _Definitions_pb2.Empty
    setStartDir: FilePathRequest
    loadCase: FilePathRequest
    replaceCase: ReplaceCaseRequest
    replaceSourceCases: ReplaceSourceCasesRequest
    exportMultiCaseSnapshots: ExportMultiCaseRequest
    exportSnapshots: ExportSnapshotsRequest
    exportProperty: ExportPropertyRequest
    exportPropertyInViews: ExportPropertyInViewsRequest
    exportWellPathCompletions: ExportWellPathCompRequest
    exportSimWellFractureCompletions: ExportSimWellPathFracRequest
    exportMsw: ExportMswRequest
    exportWellPaths: ExportWellPathRequest
    exportVisibleCells: ExportVisibleCellsRequest
    setExportFolder: SetExportFolderRequest
    runOctaveScript: RunOctaveScriptRequest
    setMainWindowSize: SetWindowSizeParams
    computeCaseGroupStatistics: ComputeCaseGroupStatRequest
    setTimeStep: SetTimeStepParams
    scaleFractureTemplate: ScaleFractureTemplateRequest
    setFractureContainment: SetFracContainmentRequest
    createMultipleFractures: CreateMultipleFracRequest
    createLgrForCompletions: CreateLgrForCompRequest
    createSaturationPressurePlots: CreateSatPressPlotRequest
    replaceMultipleCases: ReplaceCaseRequests
    createGridCaseGroup: CreateGridCaseGroupRequest
    createStatisticsCase: CreateStatisticsCaseRequest
    exportFlowCharacteristics: ExportFlowInfoRequest
    createView: CreateViewRequest
    cloneView: CloneViewRequest
    createWellBoreStabilityPlot: CreateWbsPlotRequest
    importWellPaths: ImportWellPathsRequest
    importWellLogFiles: ImportWellLogFilesRequest
    importFormationNames: ImportFormationNamesRequest
    exportWellLogPlotData: ExportWellLogPlotDataRequest
    setPlotWindowSize: SetWindowSizeParams
    exportContourMapToText: ExportContourMapToTextRequest
    saveProject: SaveProjectRequest
    def __init__(self, openProject: _Optional[_Union[FilePathRequest, _Mapping]] = ..., closeProject: _Optional[_Union[_Definitions_pb2.Empty, _Mapping]] = ..., setStartDir: _Optional[_Union[FilePathRequest, _Mapping]] = ..., loadCase: _Optional[_Union[FilePathRequest, _Mapping]] = ..., replaceCase: _Optional[_Union[ReplaceCaseRequest, _Mapping]] = ..., replaceSourceCases: _Optional[_Union[ReplaceSourceCasesRequest, _Mapping]] = ..., exportMultiCaseSnapshots: _Optional[_Union[ExportMultiCaseRequest, _Mapping]] = ..., exportSnapshots: _Optional[_Union[ExportSnapshotsRequest, _Mapping]] = ..., exportProperty: _Optional[_Union[ExportPropertyRequest, _Mapping]] = ..., exportPropertyInViews: _Optional[_Union[ExportPropertyInViewsRequest, _Mapping]] = ..., exportWellPathCompletions: _Optional[_Union[ExportWellPathCompRequest, _Mapping]] = ..., exportSimWellFractureCompletions: _Optional[_Union[ExportSimWellPathFracRequest, _Mapping]] = ..., exportMsw: _Optional[_Union[ExportMswRequest, _Mapping]] = ..., exportWellPaths: _Optional[_Union[ExportWellPathRequest, _Mapping]] = ..., exportVisibleCells: _Optional[_Union[ExportVisibleCellsRequest, _Mapping]] = ..., setExportFolder: _Optional[_Union[SetExportFolderRequest, _Mapping]] = ..., runOctaveScript: _Optional[_Union[RunOctaveScriptRequest, _Mapping]] = ..., setMainWindowSize: _Optional[_Union[SetWindowSizeParams, _Mapping]] = ..., computeCaseGroupStatistics: _Optional[_Union[ComputeCaseGroupStatRequest, _Mapping]] = ..., setTimeStep: _Optional[_Union[SetTimeStepParams, _Mapping]] = ..., scaleFractureTemplate: _Optional[_Union[ScaleFractureTemplateRequest, _Mapping]] = ..., setFractureContainment: _Optional[_Union[SetFracContainmentRequest, _Mapping]] = ..., createMultipleFractures: _Optional[_Union[CreateMultipleFracRequest, _Mapping]] = ..., createLgrForCompletions: _Optional[_Union[CreateLgrForCompRequest, _Mapping]] = ..., createSaturationPressurePlots: _Optional[_Union[CreateSatPressPlotRequest, _Mapping]] = ..., replaceMultipleCases: _Optional[_Union[ReplaceCaseRequests, _Mapping]] = ..., createGridCaseGroup: _Optional[_Union[CreateGridCaseGroupRequest, _Mapping]] = ..., createStatisticsCase: _Optional[_Union[CreateStatisticsCaseRequest, _Mapping]] = ..., exportFlowCharacteristics: _Optional[_Union[ExportFlowInfoRequest, _Mapping]] = ..., createView: _Optional[_Union[CreateViewRequest, _Mapping]] = ..., cloneView: _Optional[_Union[CloneViewRequest, _Mapping]] = ..., createWellBoreStabilityPlot: _Optional[_Union[CreateWbsPlotRequest, _Mapping]] = ..., importWellPaths: _Optional[_Union[ImportWellPathsRequest, _Mapping]] = ..., importWellLogFiles: _Optional[_Union[ImportWellLogFilesRequest, _Mapping]] = ..., importFormationNames: _Optional[_Union[ImportFormationNamesRequest, _Mapping]] = ..., exportWellLogPlotData: _Optional[_Union[ExportWellLogPlotDataRequest, _Mapping]] = ..., setPlotWindowSize: _Optional[_Union[SetWindowSizeParams, _Mapping]] = ..., exportContourMapToText: _Optional[_Union[ExportContourMapToTextRequest, _Mapping]] = ..., saveProject: _Optional[_Union[SaveProjectRequest, _Mapping]] = ...) -> None: ...

class GridCaseGroupResult(_message.Message):
    __slots__ = ["groupId", "groupName"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    groupId: int
    groupName: str
    def __init__(self, groupId: _Optional[int] = ..., groupName: _Optional[str] = ...) -> None: ...

class CreateStatisticsCaseResult(_message.Message):
    __slots__ = ["caseId"]
    CASEID_FIELD_NUMBER: _ClassVar[int]
    caseId: int
    def __init__(self, caseId: _Optional[int] = ...) -> None: ...

class CreateViewResult(_message.Message):
    __slots__ = ["viewId"]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    viewId: int
    def __init__(self, viewId: _Optional[int] = ...) -> None: ...

class CreateWbsPlotResult(_message.Message):
    __slots__ = ["viewId"]
    VIEWID_FIELD_NUMBER: _ClassVar[int]
    viewId: int
    def __init__(self, viewId: _Optional[int] = ...) -> None: ...

class ImportWellPathsResult(_message.Message):
    __slots__ = ["wellPathNames"]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wellPathNames: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportWellLogFilesResult(_message.Message):
    __slots__ = ["wellPathNames"]
    WELLPATHNAMES_FIELD_NUMBER: _ClassVar[int]
    wellPathNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wellPathNames: _Optional[_Iterable[str]] = ...) -> None: ...

class ExportWellLogPlotDataResult(_message.Message):
    __slots__ = ["exportedFiles"]
    EXPORTEDFILES_FIELD_NUMBER: _ClassVar[int]
    exportedFiles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, exportedFiles: _Optional[_Iterable[str]] = ...) -> None: ...

class CommandReply(_message.Message):
    __slots__ = ["emptyResult", "loadCaseResult", "createGridCaseGroupResult", "createStatisticsCaseResult", "createViewResult", "createWbsPlotResult", "importWellPathsResult", "importWellLogFilesResult", "exportWellLogPlotDataResult"]
    EMPTYRESULT_FIELD_NUMBER: _ClassVar[int]
    LOADCASERESULT_FIELD_NUMBER: _ClassVar[int]
    CREATEGRIDCASEGROUPRESULT_FIELD_NUMBER: _ClassVar[int]
    CREATESTATISTICSCASERESULT_FIELD_NUMBER: _ClassVar[int]
    CREATEVIEWRESULT_FIELD_NUMBER: _ClassVar[int]
    CREATEWBSPLOTRESULT_FIELD_NUMBER: _ClassVar[int]
    IMPORTWELLPATHSRESULT_FIELD_NUMBER: _ClassVar[int]
    IMPORTWELLLOGFILESRESULT_FIELD_NUMBER: _ClassVar[int]
    EXPORTWELLLOGPLOTDATARESULT_FIELD_NUMBER: _ClassVar[int]
    emptyResult: _Definitions_pb2.Empty
    loadCaseResult: _Case_pb2.CaseRequest
    createGridCaseGroupResult: GridCaseGroupResult
    createStatisticsCaseResult: CreateStatisticsCaseResult
    createViewResult: CreateViewResult
    createWbsPlotResult: CreateWbsPlotResult
    importWellPathsResult: ImportWellPathsResult
    importWellLogFilesResult: ImportWellLogFilesResult
    exportWellLogPlotDataResult: ExportWellLogPlotDataResult
    def __init__(self, emptyResult: _Optional[_Union[_Definitions_pb2.Empty, _Mapping]] = ..., loadCaseResult: _Optional[_Union[_Case_pb2.CaseRequest, _Mapping]] = ..., createGridCaseGroupResult: _Optional[_Union[GridCaseGroupResult, _Mapping]] = ..., createStatisticsCaseResult: _Optional[_Union[CreateStatisticsCaseResult, _Mapping]] = ..., createViewResult: _Optional[_Union[CreateViewResult, _Mapping]] = ..., createWbsPlotResult: _Optional[_Union[CreateWbsPlotResult, _Mapping]] = ..., importWellPathsResult: _Optional[_Union[ImportWellPathsResult, _Mapping]] = ..., importWellLogFilesResult: _Optional[_Union[ImportWellLogFilesResult, _Mapping]] = ..., exportWellLogPlotDataResult: _Optional[_Union[ExportWellLogPlotDataResult, _Mapping]] = ...) -> None: ...
