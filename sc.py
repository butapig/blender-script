import bpy

obj = bpy.context.active_object

dic = {}
list =[]

if obj.type == 'MESH':
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
    i=0
    for vt in obj.data.vertices:
        x = str(vt.co)
        if dic.get(x,0) == 1:
            list.append(i)
        dic[x] = 1
        i+=1
        
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
for j in list:
    obj.data.vertices[j].select = True   
bpy.ops.object.mode_set(mode = 'EDIT')