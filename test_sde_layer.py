import arcpy
import os

# Your SDE connection file
BCGW_SDE = r"connection\bcgw.sde"

# The layer you want to access
layer_name = "WHSE_WILDLIFE_MANAGEMENT.WCP_FISH_SENSITIVE_WS_POLY"

# Construct the full path to the layer
layer_path = os.path.join(BCGW_SDE, layer_name)

print("="*60)
print("TESTING SDE LAYER ACCESS")
print("="*60)
print(f"\nSDE Connection: {BCGW_SDE}")
print(f"Layer Name: {layer_name}")
print(f"Full Path: {layer_path}")
print("\n" + "-"*60)

# CHECK 1: Verify the SDE connection file exists
print("\n1. Checking SDE connection file...")
if os.path.exists(BCGW_SDE):
    print(f"SDE connection file found: {BCGW_SDE}")
else:
    print(f"SDE connection file NOT found: {BCGW_SDE}")
    exit()

# CHECK 2: Verify the layer exists in the database
print("\n2. Checking if layer exists in database...")
if arcpy.Exists(layer_path):
    print(f"Layer exists: {layer_name}")
else:
    print(f" Layer does NOT exist: {layer_name}")
    exit()

# CHECK 3: Get layer properties using Describe
print("\n3. Getting layer properties...")
try:
    desc = arcpy.Describe(layer_path)
    print(f"Layer Type: {desc.dataType}")
    print(f"Shape Type: {desc.shapeType}")
    print(f"Spatial Reference: {desc.spatialReference.name}")
    print(f"Feature Class Type: {desc.featureType}")
except Exception as e:
    print(f"Could not describe layer: {e}")
    exit()

# CHECK 4: Get feature count
print("\n4. Counting features...")
try:
    count = int(arcpy.management.GetCount(layer_path)[0])
    print(f"Feature count: {count:,} features")
except Exception as e:
    print(f"Could not count features: {e}")
    exit()

# CHECK 5: List fields
print("\n5. Listing fields...")
try:
    fields = arcpy.ListFields(layer_path)
    print(f"Found {len(fields)} fields:")
    for field in fields[:10]:  # Show first 10 fields
        print(f"      - {field.name} ({field.type})")
    if len(fields) > 10:
        print(f"      ... and {len(fields) - 10} more fields")
except Exception as e:
    print(f"Could not list fields: {e}")
    exit()

# CHECK 6: Test creating a feature layer (proves it's ready for manipulation)
print("\n6. Testing feature layer creation...")
try:
    temp_layer = "test_layer"
    arcpy.management.MakeFeatureLayer(layer_path, temp_layer)
    print(f"Successfully created feature layer: {temp_layer}")
    
    # Clean up
    arcpy.management.Delete(temp_layer)
    print(f"Cleaned up temporary layer")
except Exception as e:
    print(f"Could not create feature layer: {e}")
    exit()

# CHECK 7: Test selecting features (proves query access works)
print("\n7. Testing feature selection...")
try:
    temp_layer = "test_selection_layer"
    arcpy.management.MakeFeatureLayer(layer_path, temp_layer)
    
    # Get count of selected features (all features)
    selected_count = int(arcpy.management.GetCount(temp_layer)[0])
    print(f"Can query features: {selected_count:,} features accessible")
    
    # Clean up
    arcpy.management.Delete(temp_layer)
except Exception as e:
    print(f"Could not test selection: {e}")
    exit()

print("\n" + "="*60)
print("ALL CHECKS PASSED!")
print("="*60)
print("\nThe layer is accessible and ready for manipulation.")
print("\nYou can use it in your scripts like this:")
print(f'   layer_path = os.path.join(BCGW_SDE, "{layer_name}")')
print('   arcpy.management.MakeFeatureLayer(layer_path, "my_layer")')
print('   arcpy.management.CopyFeatures(layer_path, output_location)')
print("="*60)
