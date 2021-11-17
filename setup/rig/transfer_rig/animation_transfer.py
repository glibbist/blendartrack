from utils.blend import reference, armature, viewport, scene
from setup.rig.diver_rig.add_bone_constraints import get_constraint_dict
import bpy
import importlib

importlib.reload(scene)


# TODO: apply action directly to target rig.
def transfer():
    # referencing
    # target_rig = reference.get_selected_object()
    driver_rig = armature.get_armature("driver_rig")

    # get driver bones
    viewport.set_pose_mode()
    driver_bones = []
    for bone in driver_rig.pose.bones:
        try:
            constrained_bone = get_constraint_dict[bone.name][0]
            driver_bones.append(bone)
        except KeyError:
            pass

    # select driver bones
    bpy.ops.pose.select_all(action='DESELECT') # todo: util.blend
    for b in driver_bones:
        b.bone.select = True

    # create new action
    animation_data = driver_rig.animation_data
    animation_data.use_nla = False

    # baking
    bpy.ops.nla.bake(
        frame_start=scene.get_frame_start(),
        frame_end=scene.get_frame_end(),
        only_selected=True,
        visual_keying=True,
        use_current_action=True,
        bake_types={'POSE'}
    )

    viewport.set_object_mode()

    # todo: select action on target rig
    # transfer active action
    # action = driver_rig.animation_data.action
    # target_rig.animation_data.action = animation_data.action