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
        # The parameter of missile body
        self.type_warhead = WarheadTypeEnum.UNDEFINED  # Warhead type, symbol: Tn
        self.length_warhead = float(0)  # symbol: Ln
        self.diameter_warhead = float(0)  # symbol: Dn
        self.diameter_column = float(0)  # symbol: Dc
        self.length_column = float(0)  # symbol: Lc
        self.type_stern = SternTypeEnum.UNDEFINED  # symbol: Tt
        self.length_stern = float(0)  # symbol: Lt
        self.diameter_tail = float(0)  # symbol: Dt
        self.diameter_nozzle = float(0)  # symbol: Dbt

        # The parameter of missile wing
        self.num_group_wings = 0   # symbol: Ngw
        self.pos_wings = float(0)  # symbol: Pw
        self.num_wings_per_group = float(0)  # symbol: Nwpg
        self.layout_angle_wings = float(0)  # symbol: Law
        self.root_chord = float(0)  # symbol: b0
        self.tip_chord = float(0)  # symbol: b1
        self.distance_root_chord = float(0)  # symbol: h0
        self.distance_tip_chord = float(0)  # symbol: h1
        self.thickness_root_chord = float(0)  # symbol: c0
        self.thickness_tip_chord = float(0)  # symbol: c1
        self.angle_front_edge = float(0)  # symbol: x0
        self.angle_rear_edge = float(0)  # symbol: x1

        # The condition of flight
        self.height_flight = float(0)  # symbol: Hf
        self.mach_flight = float(0)  # symbol: Mf
        self.angle_flight = float(0)  # symbol: Af
        # type_pomian

        # The reference
        self.barycenter_ref = float(0)  # symbol: Br
        self.length_ref = float(0)  # symbol: Lr
        self.area_ref = float(0)  # symbol: Ar
        # fs




