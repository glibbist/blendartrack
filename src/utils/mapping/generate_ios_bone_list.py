import bpy
import math
from mathutils import Vector

class sub_buddy:
    def __init__(self):
        self.jaw_master_influence = "user.get_user().jaw_master_influence"
        self.jaw_sides_influence = "user.get_user().jaw_sides_influence"
        self.chin_master_influence = "user.get_user().chin_master_influence"
        self.chin_sides_influence = "user.get_user().chin_sides_influence"
        self.lips_influence = "user.get_user().lips_influence"
        self.nose_influence = "user.get_user().nose_influence"
        self.brow_sides_influence = "user.get_user().brow_sides_influence"
        self.brow_master_influence = "user.get_user().brow_master_influence"
        self.lid_influence = "user.get_user().lid_influence"
    
class m_user:
    def __init__(self):
        pass
    
    def get_user(self):
        sub_bud = sub_buddy()
        return sub_bud

        
user = m_user()

constrained_bones = {
        # JAW
        "jaw": ["jaw", "FaceEmpty_152", 23,                     user.get_user().jaw_master_influence],
        "jaw.L.001": ["jaw.L.001", "FaceEmpty_435", 3,          user.get_user().jaw_sides_influence],
        "jaw.R.001": ["jaw.R.001", "FaceEmpty_215", 3,          user.get_user().jaw_sides_influence],

        # CHIN
        "chin": ["chin", "FaceEmpty_152", 3,                    user.get_user().chin_master_influence],
        "chin.R": ["chin.R", "FaceEmpty_32", 3,                 user.get_user().chin_sides_influence],
        "chin.L": ["chin.L", "FaceEmpty_262", 3,                user.get_user().chin_sides_influence],

        # LIPS
        "lips.R": ["lips.R", "FaceEmpty_61", 3,                 user.get_user().lips_influence],
        "lips.L": ["lips.L", "FaceEmpty_291", 3,                user.get_user().lips_influence],
        "lips.T": ["lips.T", "FaceEmpty_0", 3,                  user.get_user().lips_influence],

        # NOSE
        "nose.L": ["nose.L", "FaceEmpty_437", 3,                user.get_user().nose_influence],
        "nose.L.001": ["nose.L.001", "FaceEmpty_358", 3,        user.get_user().nose_influence],
        "nose.R": ["nose.R", "FaceEmpty_217", 3,                user.get_user().nose_influence],
        "nose.R.001": ["nose.R.001", "FaceEmpty_129", 3,        user.get_user().nose_influence],

        # BROW
        "brow.T.R": ["brow.T.R", "FaceEmpty_143", 3,            user.get_user().brow_sides_influence],
        "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70", 3,     user.get_user().brow_sides_influence],
        "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107", 3,    user.get_user().brow_master_influence],
        "brow.B.R": ["brow.B.R", "FaceEmpty_247", 3,            user.get_user().brow_master_influence],
        "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30", 3,     user.get_user().brow_master_influence],
        "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27", 3,     user.get_user().brow_master_influence],
        "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56", 3,     user.get_user().brow_master_influence],

        "brow.T.L": ["brow.T.L", "FaceEmpty_372", 3,            user.get_user().brow_sides_influence],
        "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300", 3,    user.get_user().brow_sides_influence],
        "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336", 3,    user.get_user().brow_master_influence],
        "brow.B.L": ["brow.B.L", "FaceEmpty_467", 3,            user.get_user().brow_master_influence],
        "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260", 3,    user.get_user().brow_master_influence],
        "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257", 3,    user.get_user().brow_master_influence],
        "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286", 3,    user.get_user().brow_master_influence],

        # EYES
        "lid.T.R": ["lid.T.R", "FaceEmpty_33", 3,               user.get_user().lid_influence],
        "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161", 3,      user.get_user().lid_influence],
        "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159", 3,      user.get_user().lid_influence],
        "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157", 3,      user.get_user().lid_influence],
        "lid.B.R": ["lid.B.R", "FaceEmpty_133", 3,              user.get_user().lid_influence],
        "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154", 3,      user.get_user().lid_influence],
        "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145", 3,      user.get_user().lid_influence],
        "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163", 3,      user.get_user().lid_influence],

        "lid.B.L": ["lid.B.L", "FaceEmpty_362", 3,              user.get_user().lid_influence],
        "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381", 3,      user.get_user().lid_influence],
        "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374", 3,      user.get_user().lid_influence],
        "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390", 3,      user.get_user().lid_influence],
        "lid.T.L": ["lid.T.L", "FaceEmpty_263", 3,              user.get_user().lid_influence],
        "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388", 3,      user.get_user().lid_influence],
        "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386", 3,      user.get_user().lid_influence],
        "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384", 3,      user.get_user().lid_influence]
}


head_ref = {
    "chin": ["chin", "FaceEmpty_152"],
    "chin.001": ["chin.001", "FaceEmpty_199"],
    "nose": ["nose", "FaceEmpty_168"],
    "nose.001": ["nose.001", "FaceEmpty_5"],
    "nose.002": ["nose.002", "FaceEmpty_4"],
    "nose.003": ["nose.003", "FaceEmpty_19"],
    "nose.004": ["nose.004", "FaceEmpty_94"],

    "temple.L": ["temple.L", "FaceEmpty_251"],
    "jaw.L": ["jaw.L", "FaceEmpty_447"],
    "jaw.L.001": ["jaw.L.001", "FaceEmpty_435"],

    "chin.L": ["chin.L", "FaceEmpty_262"],

    "nose.L": ["nose.L", "FaceEmpty_437"],
    "nose.L.001": ["nose.L.001", "FaceEmpty_358"],

    "cheek.T.L": ["cheek.T.L", "FaceEmpty_372"],
    "cheek.T.L.001": ["cheek.T.L.001", "FaceEmpty_425"],
    "cheek.B.L": ["cheek.B.L", "FaceEmpty_291"],
    "cheek.B.L.001": ["cheek.B.L.001", "FaceEmpty_411"],

    "brow.T.L": ["brow.T.L", "FaceEmpty_372"],
    "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300"],
    "brow.T.L.002": ["brow.T.L.002", "FaceEmpty_334"],
    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336"],

    "forehead.L": ["forehead.L", "FaceEmpty_338"],
    "forehead.L.001": ["forehead.L.001", "FaceEmpty_297"],
    "forehead.L.002": ["forehead.L.002", "FaceEmpty_332"],

    "lip.T.L": ["lip.T.L", "FaceEmpty_0"],
    "lip.T.L.001": ["lip.T.L.001", "FaceEmpty_269"],
    "lip.B.L": ["lip.B.L", "FaceEmpty_17"],
    "lip.B.L.001": ["lip.B.L.001", "FaceEmpty_405"],

    "brow.B.L": ["brow.B.L", "FaceEmpty_467"],
    "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260"],
    "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257"],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286"],

    "lid.B.L": ["lid.B.L", "FaceEmpty_362"],
    "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381"],
    "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374"],
    "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390"],
    "lid.T.L": ["lid.T.L", "FaceEmpty_263"],
    "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388"],
    "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386"],
    "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384"],

    "nose.R": ["nose.R", "FaceEmpty_217"],
    "nose.R.001": ["nose.R.001", "FaceEmpty_129"],
    "cheek.T.R": ["cheek.T.R", "FaceEmpty_143"],
    "cheek.T.R.001": ["cheek.T.R.001", "FaceEmpty_205"],

    "temple.R": ["temple.R", "FaceEmpty_21"],
    "jaw.R": ["jaw.R", "FaceEmpty_227"],
    "jaw.R.001": ["jaw.R.001", "FaceEmpty_215"],

    "chin.R": ["chin.R", "FaceEmpty_32"],
    "cheek.B.R": ["cheek.B.R", "FaceEmpty_61"],
    "cheek.B.R.001": ["cheek.B.R.001", "FaceEmpty_187"],

    "brow.T.R": ["brow.T.R", "FaceEmpty_143"],
    "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70"],
    "brow.T.R.002": ["brow.T.R.002", "FaceEmpty_105"],
    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107"],

    "forehead.R": ["forehead.R", "FaceEmpty_109"],
    "forehead.R.001": ["forehead.R.001", "FaceEmpty_67"],
    "forehead.R.002": ["forehead.R.002", "FaceEmpty_103"],

    "lip.T.R": ["lip.T.R", "FaceEmpty_0"],
    "lip.T.R.001": ["lip.T.R.001", "FaceEmpty_39"],
    "lip.B.R": ["lip.B.R", "FaceEmpty_17"],
    "lip.B.R.001": ["lip.B.R.001", "FaceEmpty_181"],

    "lid.T.R": ["lid.T.R", "FaceEmpty_33"],
    "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161"],
    "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159"],
    "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157"],
    "lid.B.R": ["lid.B.R", "FaceEmpty_133"],
    "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154"],
    "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145"],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163"],

    "brow.B.R": ["brow.B.R", "FaceEmpty_247"],
    "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30"],
    "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27"],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56"],
}

tail_ref = {
    "nose.L.001": ["nose.L.001", "FaceEmpty_4"],
    "nose.R.001": ["nose.R.001", "FaceEmpty_4"],
    "chin.001": ["chin.001", "FaceEmpty_18"],
    "lip.T.L.001": ["lip.T.L.001", "FaceEmpty_291"],
    "lip.B.L.001": ["lip.B.L.001", "FaceEmpty_291"],
    "lip.T.R.001": ["lip.T.R.001", "FaceEmpty_61"],
    "lip.B.R.001": ["lip.B.R.001", "FaceEmpty_61"],
    "forehead.R": ["forehead.R", "FaceEmpty_107"],
    "forehead.R.001": ["forehead.R.001", "FaceEmpty_105"],
    "forehead.R.002": ["forehead.R.002", "FaceEmpty_70"],

    "forehead.L": ["forehead.L", "FaceEmpty_336"],
    "forehead.L.001": ["forehead.L.001", "FaceEmpty_334"],
    "forehead.L.002": ["forehead.L.002", "FaceEmpty_300"],

    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_168"],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_414"],
    "lid.B.L.003": ["brow.T.L.003", "FaceEmpty_263"],

    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_168"],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_190"],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_33"],
}

def get_armature(name='Armature.001'):
    objs = bpy.context.selected_objects
    arm = None
    
    try:
        if objs[0].type == "ARMATURE":
            arm = objs[0]
        else:
            arm = bpy.data.objects[name]
            
    except IndexError:
        arm = bpy.data.objects[name]
        
        
    return arm, arm.data.bones


def get_face_empties(col='FaceEmpties'):
    empties = bpy.data.collections[col].objects
    return empties
 
def round_value(n, r):
    return n - math.fmod(n, r)

def get_s_vector(xyz_vec, name, round):
    s_vec = Vector((
        round_value(xyz_vec[0], round),
        round_value(xyz_vec[1], round),
        round_value(xyz_vec[2], round),
    ))
    return s_vec

def print_equal_element(empties, bones):
    equal_datas = []
    for e in empties:
        for b in bones:
            if e[0] == b[0]:
                # print(e[1], b[1], b[0])
                equal_datas.append([e[1], b[1], b[0]])
    return equal_datas

def main():
    arm, bones = get_armature()
    empties = get_face_empties()


    abs_r = 0.0005

    empty_data = []
    head_data = []
    tail_data = []

    for e in empties:
        vec = get_s_vector(e.location, e.name, abs_r)
        empty_data.append([vec, e.name])

    for b in bones:
        vec = get_s_vector(b.head_local, b.name, abs_r)
        head_data.append([vec, b.name])
        vec = get_s_vector(b.tail_local, b.name, abs_r)
        tail_data.append([vec, b.name])



    print("\n\nMATCHING HEAD BONE POS DICT")
    updated_head_data = print_equal_element(empty_data, head_data)
    for key, value in head_ref.items():
        matches = False
        m_data = None
        ref = None
        for data in updated_head_data:
            if data[1] == key:
                matches = True
                ref = data[0]
                m_data = data
        print(f"'{key}': ['{value[0]}', '{ref}'],")


    print("\n\nMATCHING TAIL BONE POSE DICT")
    updated_tail_data = print_equal_element(empty_data, tail_data)    
    for key, value in tail_ref.items():
        matches = False
        ref = None
        for data in updated_tail_data:
            if data[1] == key:
                ref = data[0]
                matches = True
        print(f"'{key}': ['{value[0]}', '{ref}'],")
    
    print("\n\nMATCHING CONSTRAINT BONES DICT")
    for key, value in constrained_bones.items():
        matches = False
        ref = None
        for data in updated_head_data:
            if data[1] == key:
                ref = data[0]
                matches = True
        print(f"'{key}': ['{value[0]}', '{ref}', {value[2]}, {value[3]}], ----------------------- {matches}")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    