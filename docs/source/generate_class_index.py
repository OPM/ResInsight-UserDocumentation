#!/usr/bin/env python3
"""Generate a category-grouped class index for the rips package.

This replaces a single flat ``.. automodapi:: rips`` class list (~140
classes in one alphabetical table) with one short landing page plus a
small ``autosummary`` page per functional group.

Run from the ``docs/source`` directory::

    python generate_class_index.py

Output:

* ``GeneratedClasses.rst`` - landing page: intro text plus a ``toctree``
  that links to one page per category. The ``toctree`` makes every
  category show up in the Read the Docs sidebar.
* ``api_categories/<slug>.rst`` - one page per category, each holding a
  single ``autosummary`` table.

Any rips class that is not listed in ``CATEGORIES`` below is collected
into an "Other Classes" group, so the build never silently drops a class
when new classes are added upstream. When that happens, move the class
name into the appropriate category in this file.
"""

import argparse
import inspect
import os
import re
import sys

# Ordered list of (group title, [class names]). The order here is the
# order the groups appear in the generated documentation.
CATEGORIES = [
    ("Application and Project", [
        "Instance", "Project", "CommandRouter",
    ]),
    ("Cases and Case Collections", [
        "Case", "Reservoir", "EclipseCase", "GeoMechCase", "EmCase",
        "RoffCase", "CornerPointCase", "GridCaseGroup",
        "EclipseCaseEnsemble", "ReservoirGridEnsemble",
    ]),
    ("Grids", [
        "Grid", "TriangleGeometry",
    ]),
    ("Summary Data", [
        "SummaryCase", "FileSummaryCase", "GridSummaryCase",
        "SummaryCaseSumo", "SummaryCaseSubCollection",
    ]),
    ("Views and Contour Maps", [
        "View", "EclipseView", "GeoMechView", "EclipseContourMap",
        "GeoMechContourMap", "GeoMechPart", "GeoMechPartCollection",
    ]),
    ("Cell Results and Color Legends", [
        "EclipseResult", "CellColors", "ColorLegend",
        "ColorLegendCollection", "ColorLegendItem",
    ]),
    ("Cell Filters and Intersections", [
        "CellFilter", "CellFilterCollection", "CombinedFilter",
        "CurveIntersection", "IntersectionCollection",
    ]),
    ("Annotations and Polygons", [
        "TextAnnotation", "Polygon", "PolygonCollection",
        "RimPolygonAppearance",
    ]),
    ("Wells and Well Paths", [
        "WellPath", "FileWellPath", "ModeledWellPath", "OsduWellPath",
        "PointBasedWellPath", "WellPathGeometry", "WellPathTarget",
        "WellPathCollection", "WellPathTimeIn", "SimulationWell",
    ]),
    ("Well Events", [
        "WellEvent", "KeywordEvent", "WellEventControl",
        "WellEventKeyword", "WellEventPerf", "WellEventState",
        "WellEventTimeline", "WellEventTubing", "WellEventType",
        "WellEventValve",
    ]),
    ("Well Logs", [
        "WellLog", "ImportedWellLog", "OsduWellLog", "WellLogLasFile",
        "WellLogFileInterface", "WellLogExtractionCurve",
        "EnsembleWellLogs",
    ]),
    ("Well Log Plots", [
        "WellLogPlot", "WellLogPlotTrack", "WellLogPlotCurve",
        "WellLogPlotCollection", "DepthTrackPlot",
        "WellBoreStabilityPlot",
    ]),
    ("Perforations and Fishbones", [
        "Perforation", "PerforationCollection",
        "NonDarcyPerforationParameters", "Fishbones",
        "FishbonesCollection", "DiameterRoughnessInterval",
        "CustomSegmentInterval", "MswSettings",
        "CompletionTemplateCollection", "WellPathCompletions",
        "WellPathCompletionSettings",
    ]),
    ("Valves", [
        "ValveTemplate", "ValveTemplateCollection", "ValveCollection",
        "WellPathValve", "WellPathAicdParameters",
        "WellPathSicdParameters",
    ]),
    ("Fractures", [
        "Fracture", "WellPathFracture", "FractureTemplate",
        "FractureTemplateCollection", "StimPlanFractureTemplate",
        "ThermalFractureTemplate", "MeshFractureTemplate",
    ]),
    ("Fracture Models", [
        "StimPlanModel", "StimPlanModelCollection",
        "StimPlanModelTemplate", "StimPlanModelTemplateCollection",
        "StimPlanModelPlot", "StimPlanModelPlotCollection",
        "ElasticProperties", "ElasticPropertyScaling",
        "ElasticPropertyScalingCollection", "FaciesProperties",
        "FaciesInitialPressureConfig", "NonNetLayers",
        "PressureTable", "PressureTableItem",
    ]),
    ("Well Bore Stability", [
        "WbsParameters", "MudWeightWindowParameters",
    ]),
    ("Surfaces", [
        "Surface", "SurfaceInterface", "SurfaceCollection",
        "DepthSurface", "GridCaseSurface", "RegularSurface",
        "RegularFileSurface", "FractureSurface", "EnsembleSurface",
        "EnsembleStatisticsSurface",
    ]),
    ("Plots and Curves", [
        "Plot", "PlotWindow", "PlotCurve", "SummaryPlot",
        "SummaryPlotCollection", "HistogramPlot",
    ]),
    ("Data Containers and Statistics", [
        "DataContainerFloat", "DataContainerString",
        "DataContainerTime", "ResampleData",
        "RimStatisticalCalculation",
    ]),
    ("Base Classes", [
        "PdmObjectBase", "NamedObject", "CheckableNamedObject",
        "ViewWindow",
    ]),
]

OTHER_TITLE = "Other Classes"

# Sub-directory (relative to this script) that holds the per-category
# pages. It is referenced from the landing page ``toctree``.
CATEGORY_DIRNAME = "api_categories"

# Generated stub pages for each class. The path is relative to the
# category pages, which live one level down in CATEGORY_DIRNAME, so the
# stubs all land in a single ``source/api`` directory. conf.py removes
# that directory after every build.
STUB_TOCTREE = "../api"

# Intro text kept at the top of the landing page. The ``.. _AllClasses:``
# label is referenced from rips.rst, so it must remain.
INTRO = """.. This file is auto-generated by generate_class_index.py - do not edit manually.

.. _AllClasses:

Project Tree Classes
====================
ResInsight provides access to a number of other objects in the Project Tree. These all inherit the
:ref:`PdmObjectBaseLabel` class.

You can look for objects of a specific type by using the **descendants** method of **rips.project** ::

   import rips
   # Connect to ResInsight instance
   resinsight = rips.Instance.find()
   # Example code
   print("ResInsight version: " + resinsight.version_string())
   # Get a list of all Eclipse views in the project
   views = resinsight.project.descendants(rips.EclipseView)

The classes are grouped by topic. Select a topic below to see its
classes; each class links to its full API reference. Members shared by
every class are documented once on :ref:`PdmObjectBaseLabel`.
"""

CATEGORY_HEADER = (
    ".. This file is auto-generated by generate_class_index.py - do not edit manually.\n"
)


def slugify(title):
    """Return a file-name-safe slug for a category title."""
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower())
    return slug.strip("_")


def discover_classes():
    """Return the sorted list of public class names exported by rips."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.dirname(script_dir)
    if docs_dir not in sys.path:
        sys.path.insert(0, docs_dir)

    import rips  # noqa: E402

    return sorted(
        name
        for name in rips.__all__
        if inspect.isclass(getattr(rips, name))
    )


def build_groups(actual_classes):
    """Map the discovered classes onto the configured categories.

    Returns a list of (title, [class names]) and the set of class names
    that were configured but no longer exist in the rips package.
    """
    actual = set(actual_classes)
    assigned = set()
    groups = []
    missing = []

    for title, names in CATEGORIES:
        present = []
        for name in names:
            if name in actual:
                present.append(name)
                assigned.add(name)
            else:
                missing.append(name)
        if present:
            groups.append((title, sorted(present)))

    leftover = sorted(actual - assigned)
    if leftover:
        groups.append((OTHER_TITLE, leftover))

    return groups, leftover, sorted(missing)


def render_category_page(title, class_names):
    """Render one category page: a heading plus an autosummary table."""
    lines = [
        CATEGORY_HEADER.rstrip(),
        "",
        title,
        "=" * len(title),
        "",
        ".. autosummary::",
        f"   :toctree: {STUB_TOCTREE}",
        "   :nosignatures:",
        "",
    ]
    for name in class_names:
        lines.append(f"   rips.{name}")
    lines.append("")
    return "\n".join(lines)


def render_landing(groups):
    """Render the landing page: intro text plus a toctree of categories."""
    parts = [INTRO, "", ".. toctree::", "   :maxdepth: 1", ""]
    for title, _ in groups:
        parts.append(f"   {CATEGORY_DIRNAME}/{slugify(title)}")
    parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def write_category_pages(groups, category_dir):
    """Write one page per group and remove stale pages from a prior run."""
    os.makedirs(category_dir, exist_ok=True)

    written = set()
    for title, class_names in groups:
        slug = slugify(title)
        written.add(slug + ".rst")
        path = os.path.join(category_dir, slug + ".rst")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(render_category_page(title, class_names))

    removed = []
    for existing in os.listdir(category_dir):
        if existing.endswith(".rst") and existing not in written:
            os.remove(os.path.join(category_dir, existing))
            removed.append(existing)
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parser.add_argument(
        "--output",
        default=os.path.join(script_dir, "GeneratedClasses.rst"),
        help="Landing page RST file (default: GeneratedClasses.rst next to this script).",
    )
    parser.add_argument(
        "--category-dir",
        default=os.path.join(script_dir, CATEGORY_DIRNAME),
        help=f"Directory for the per-category pages (default: {CATEGORY_DIRNAME}/).",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Generating grouped class index")
    print("=" * 60)

    actual_classes = discover_classes()
    print(f"Discovered {len(actual_classes)} classes in the rips package")

    groups, leftover, missing = build_groups(actual_classes)

    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(render_landing(groups))

    removed = write_category_pages(groups, args.category_dir)

    print(f"Wrote landing page {args.output}")
    print(f"Wrote {len(groups)} category pages to {args.category_dir}")
    for title, class_names in groups:
        print(f"  - {title}: {len(class_names)}")
    for stale in removed:
        print(f"  removed stale page: {stale}")

    if leftover:
        print()
        print("WARNING: the following classes are not assigned to a category")
        print("         and were placed in '%s'." % OTHER_TITLE)
        print("         Add them to CATEGORIES in generate_class_index.py:")
        for name in leftover:
            print(f"           {name}")

    if missing:
        print()
        print("NOTE: these configured classes no longer exist in rips and")
        print("      were skipped. Remove them from CATEGORIES when convenient:")
        for name in missing:
            print(f"        {name}")

    print()
    print("=" * 60)
    print("Class index generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
