def Contract_scalar_3x3(\
    t0_4,t1_4,t2_4,t3_4,t4_4,\
    t0_3,t1_3,t2_3,t3_3,t4_3,\
    t0_2,t1_2,t2_2,t3_2,t4_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,\
    o1_3,o2_3,o3_3,\
    o1_2,o2_2,o3_2,\
    o1_1,o2_1,o3_1\
    ):
    ##############################
    # ./input/input_Lx3Ly3.dat
    ##############################
    # (o3_1*(t3_1.conj()*((t4_1*(t4_0*t3_0))*(t3_1*(t2_0*(t2_1*((t2_1.conj()*o2_1)*((t1_1.conj()*((o1_1*t1_1)*(t0_1*(t0_0*t1_0))))*(t0_2*(t1_2*((t1_2.conj()*o1_2)*(t2_2*((t2_2.conj()*o2_2)*(t3_2*((o3_2*t3_2.conj())*(t4_2*((t1_3*((o1_3*t1_3.conj())*(t0_3*(t0_4*t1_4))))*(t2_3.conj()*((t2_3*o2_3)*(t2_4*(t3_3*((t3_3.conj()*o3_3)*(t3_4*(t4_4*t4_3))))))))))))))))))))))))
    # cpu_cost= 1.6102e+15  memory= 3.0002e+12
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o3_1, np.tensordot(
            t3_1.conj(), np.tensordot(
                np.tensordot(
                    t4_1, np.tensordot(
                        t4_0, t3_0, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t3_1, np.tensordot(
                        t2_0, np.tensordot(
                            t2_1, np.tensordot(
                                np.tensordot(
                                    t2_1.conj(), o2_1, ([4], [1])
                                ), np.tensordot(
                                    np.tensordot(
                                        t1_1.conj(), np.tensordot(
                                            np.tensordot(
                                                o1_1, t1_1, ([0], [4])
                                            ), np.tensordot(
                                                t0_1, np.tensordot(
                                                    t0_0, t1_0, ([0], [1])
                                                ), ([0], [0])
                                            ), ([1, 4], [1, 4])
                                        ), ([0, 3, 4], [4, 6, 0])
                                    ), np.tensordot(
                                        t0_2, np.tensordot(
                                            t1_2, np.tensordot(
                                                np.tensordot(
                                                    t1_2.conj(), o1_2, ([4], [1])
                                                ), np.tensordot(
                                                    t2_2, np.tensordot(
                                                        np.tensordot(
                                                            t2_2.conj(), o2_2, ([4], [1])
                                                        ), np.tensordot(
                                                            t3_2, np.tensordot(
                                                                np.tensordot(
                                                                    o3_2, t3_2.conj(), ([1], [4])
                                                                ), np.tensordot(
                                                                    t4_2, np.tensordot(
                                                                        np.tensordot(
                                                                            t1_3, np.tensordot(
                                                                                np.tensordot(
                                                                                    o1_3, t1_3.conj(), ([1], [4])
                                                                                ), np.tensordot(
                                                                                    t0_3, np.tensordot(
                                                                                        t0_4, t1_4, ([1], [0])
                                                                                    ), ([1], [0])
                                                                                ), ([1, 2], [2, 5])
                                                                            ), ([0, 1, 4], [4, 6, 0])
                                                                        ), np.tensordot(
                                                                            t2_3.conj(), np.tensordot(
                                                                                np.tensordot(
                                                                                    t2_3, o2_3, ([4], [0])
                                                                                ), np.tensordot(
                                                                                    t2_4, np.tensordot(
                                                                                        t3_3, np.tensordot(
                                                                                            np.tensordot(
                                                                                                t3_3.conj(), o3_3, ([4], [1])
                                                                                            ), np.tensordot(
                                                                                                t3_4, np.tensordot(
                                                                                                    t4_4, t4_3, ([1], [0])
                                                                                                ), ([1], [0])
                                                                                            ), ([1, 2], [2, 5])
                                                                                        ), ([1, 2, 4], [4, 6, 2])
                                                                                    ), ([1], [4])
                                                                                ), ([1, 2], [1, 3])
                                                                            ), ([1, 2, 4], [4, 6, 2])
                                                                        ), ([0, 2, 5], [2, 0, 4])
                                                                    ), ([0], [7])
                                                                ), ([2, 3], [9, 2])
                                                            ), ([1, 2, 4], [10, 4, 0])
                                                        ), ([1, 2], [8, 2])
                                                    ), ([1, 2, 4], [10, 3, 2])
                                                ), ([1, 2], [8, 2])
                                            ), ([1, 2, 4], [9, 3, 2])
                                        ), ([1, 2, 3], [9, 0, 2])
                                    ), ([0, 2, 4], [2, 1, 0])
                                ), ([0, 1], [0, 4])
                            ), ([0, 1, 4], [3, 5, 2])
                        ), ([1, 2, 3], [4, 1, 3])
                    ), ([0, 1], [1, 3])
                ), ([0, 1, 3, 4], [6, 0, 3, 1])
            ), ([0, 1, 2, 3], [3, 4, 0, 1])
        ), ([0, 1], [1, 0])
    )
