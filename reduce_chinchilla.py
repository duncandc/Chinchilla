#!/usr/bin/env python

import reader_tools
import custom_utilities as cu


def main():
    filepath = cu.get_data_path()+'Chinchilla/halo_catalogues/'
    catalogue = 'hlist_1.00000.list'

    column_info = ([
    (1, 'id', 'int'), 
    (5, 'pid', 'int'), 
    (6, 'upid', 'int'), 
    (10, 'mvir', 'float'), 
    (11, 'rvir', 'float'), 
    (12, 'rs', 'float'), 
    (15, 'scale_of_last_MM', 'float'), 
    (16, 'vmax', 'float'), 
    (17, 'x', 'float'), 
    (18, 'y', 'float'), 
    (19, 'z', 'float'), 
    (20, 'vx', 'float'), 
    (21, 'vy', 'float'), 
    (22, 'vz', 'float'), 
    (56, 'macc', 'float'), 
    (57, 'mpeak', 'float'), 
    (58, 'vacc', 'float'), 
    (59, 'vpeak', 'float'), 
    (60, 'halfmpeak_scale', 'float'), 
    (63, 'mar_tdyn', 'float'), 
    (66, 'mpeak_scale', 'float'), 
    (67, 'acc_scale', 'float'), 
    (68, 'm04_scale', 'float')
    ])

    mp_bolshoi = 1.35e8
    mp_chinchilla = mp_bolshoi/8.
    mpeak_cut = mp_chinchilla*100.
    cuts = [(57, mpeak_cut, None)]

    halos=reader_tools.read_halocat(filepath+catalogue, column_info, input_halo_cuts=cuts)
    print halos

if __name__ == '__main__':
    main()








