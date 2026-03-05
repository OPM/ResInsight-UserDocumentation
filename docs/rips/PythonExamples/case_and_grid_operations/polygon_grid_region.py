####################################################################################
# This example demonstrates how to:
# 1. Define N polygons based on a list of coordinates
# 2. Create grid cell filters based on each of these polygons
# 3. Create a Generated result that assigns a unique integer value to all cells
#    in each region
####################################################################################

import rips


def point_in_polygon_2d(px, py, polygon_xy):
    """Check if point (px, py) is inside a 2D polygon using the ray casting algorithm.

    Arguments:
        px (float): X coordinate of the point
        py (float): Y coordinate of the point
        polygon_xy (list): List of [x, y] pairs defining the polygon vertices

    Returns:
        bool: True if the point is inside the polygon, False otherwise
    """
    n = len(polygon_xy)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon_xy[i][0], polygon_xy[i][1]
        xj, yj = polygon_xy[j][0], polygon_xy[j][1]
        if ((yi > py) != (yj > py)) and (
            px < (xj - xi) * (py - yi) / (yj - yi) + xi
        ):
            inside = not inside
        j = i
    return inside


resinsight = rips.Instance.find()
if resinsight is None:
    print("No ResInsight instance found")
    exit()

cases = resinsight.project.cases()
if not cases:
    print("No cases found in the project")
    exit()

case = cases[0]
print(f"Using case: {case.name}")

# Get reservoir bounding box to define example polygons relative to the model
bbox = case.reservoir_boundingbox()
depth = bbox.max_z - ((bbox.max_z - bbox.min_z) / 2.0)

mid_x = (bbox.min_x + bbox.max_x) / 2.0
mid_y = (bbox.min_y + bbox.max_y) / 2.0

# Step 1: Define N polygons as lists of [x, y, depth] coordinates.
# Each polygon is a list of at least 3 points. The example below divides
# the reservoir bounding box into four quadrant regions.
polygon_definitions = [
    # Polygon 1: Lower-left quadrant
    [
        [bbox.min_x, bbox.min_y, depth],
        [mid_x, bbox.min_y, depth],
        [mid_x, mid_y, depth],
        [bbox.min_x, mid_y, depth],
    ],
    # Polygon 2: Lower-right quadrant
    [
        [mid_x, bbox.min_y, depth],
        [bbox.max_x, bbox.min_y, depth],
        [bbox.max_x, mid_y, depth],
        [mid_x, mid_y, depth],
    ],
    # Polygon 3: Upper-left quadrant
    [
        [bbox.min_x, mid_y, depth],
        [mid_x, mid_y, depth],
        [mid_x, bbox.max_y, depth],
        [bbox.min_x, bbox.max_y, depth],
    ],
    # Polygon 4: Upper-right quadrant
    [
        [mid_x, mid_y, depth],
        [bbox.max_x, mid_y, depth],
        [bbox.max_x, bbox.max_y, depth],
        [mid_x, bbox.max_y, depth],
    ],
]

# Create polygon objects in ResInsight for visualization
polygon_collection = resinsight.project.descendants(rips.PolygonCollection)[0]
polygons = []
for i, coords in enumerate(polygon_definitions):
    p = polygon_collection.create_polygon(
        name=f"Region {i + 1}", coordinates=coords
    )
    polygons.append(p)
    print(f"Created polygon: {p.name}")

# Step 2: Create grid cell filters based on each polygon.
# For each active cell, determine which polygon region it belongs to
# by checking whether the cell center falls inside the polygon (2D XY check).
print("Computing cell-to-region assignments...")
cell_centers = case.active_cell_centers()

# Initialize all cells with value 0 (no region assigned)
region_values = [0.0] * len(cell_centers)

for cell_idx, cell_center in enumerate(cell_centers):
    for polygon_idx, coords in enumerate(polygon_definitions):
        polygon_xy = [[c[0], c[1]] for c in coords]
        if point_in_polygon_2d(cell_center.x, cell_center.y, polygon_xy):
            # Assign 1-based region index so each region has a unique integer value
            region_values[cell_idx] = float(polygon_idx + 1)
            break  # Assign cell to the first matching polygon

# Step 3: Create a Generated result that stores the unique integer region value
# for every active cell. Cells not covered by any polygon receive value 0.
property_name = "POLYGON_REGION"
case.set_active_cell_property(region_values, "GENERATED", property_name, 0)

print(f"Generated property '{property_name}' created successfully")
for i in range(len(polygon_definitions)):
    count = sum(1 for v in region_values if v == float(i + 1))
    print(f"  Region {i + 1} (polygon '{polygons[i].name}'): {count} cells")

unassigned = sum(1 for v in region_values if v == 0.0)
print(f"  Unassigned (no polygon): {unassigned} cells")

# Apply the generated result in the view to visualize the regions
view = case.views()[0] if case.views() else case.create_view()
view.apply_cell_result(result_type="GENERATED", result_variable=property_name)
print(f"Applied '{property_name}' cell result to view")
