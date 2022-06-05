import bpy
import math

ctx = bpy.context

# Setting the armature to be the active object
object = bpy.data.objects['Armature']
ctx.view_layer.objects.active = object

# If object is loaded correctly, set the mode to POSE; needed for animation
if ctx.object is not None:
    print(ctx.object.name)
    print(ctx.object.mode)
    bpy.ops.object.mode_set(mode='POSE', toggle=False)
    print(ctx.object.mode + " " + ctx.mode)

pbone = object.pose.bones['Head']

# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'

# selecting the axis (bone local) and the angle of the rotation
axis = 'Z'
angle = 3

#pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
#bpy.ops.object.mode_set(mode='OBJECT')
#pbone.keyframe_insert(data_path="rotation_euler", frame=0)
for i in range(0, 61):
    if(i % 15 == 0):
        angle *= -1
    
    pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
    bpy.ops.object.mode_set(mode='OBJECT')
    pbone.keyframe_insert(data_path="rotation_euler", frame=i)
    bpy.ops.object.mode_set(mode='POSE')