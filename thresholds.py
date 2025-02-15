


# Get thresholds for beginner mode
def get_thresholds():

    _ANGLE_HIP_KNEE_VERT = {
                            'STAND' : (0,  10),
                            'TRANS'  : (15, 75),
                            'PASS'   : 80
                        }    

        
    thresholds = {
                    'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

                    'KNEE_THRESH'  : [15, 75, 80],

                    'OFFSET_THRESH'    : 70.0,
                    # 'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }
                
    return thresholds
