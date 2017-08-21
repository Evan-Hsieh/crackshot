# from __future__ import division


class WarheadTypeEnum(object):
    UNDEFINED = 0
    CONE_WARHEAD = 1
    ARC_WARHEAD = 2
    CARMEN_WARHEAD = 3


class SternTypeEnum(object):
    UNDEFINED = 0
    CONE_STERN = 1
    ARC_STERN = 2


class BaseMissile(object):
    def __init__(self):
        self.para_dict = {'type_warhead': WarheadTypeEnum.UNDEFINED,  # missile body
                          'length_warhead': float(0),
                          'diameter_warhead': float(0),
                          'diameter_column': float(0),
                          'length_column': float(0),
                          'type_stern': SternTypeEnum.UNDEFINED,
                          'length_stern': float(0),
                          'diameter_tail': float(0),
                          'diameter_nozzle': float(0),
                          'num_group_wings': 0,  # missile wing
                          'pos_wings': float(0),
                          'num_wings_per_group': float(0),
                          'layout_angle_wings': float(0),
                          'root_chord': float(0),
                          'tip_chord': float(0),
                          'distance_root_chord': float(0),
                          'distance_tip_chord': float(0),
                          'thickness_root_chord': float(0),
                          'thickness_tip_chord': float(0),
                          'angle_front_edge': float(0),
                          'angle_rear_edge': float(0),
                          'height_flight': float(0),  # condition of flight
                          'mach_flight': float(0),
                          'angle_flight': float(0),
                          'barycenter_ref': float(0),  # reference
                          'length_ref': float(0),
                          'area_ref': float(0)}
        # fsw


if __name__ == "__main__":
    pass
