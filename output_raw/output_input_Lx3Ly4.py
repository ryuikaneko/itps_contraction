def Contract_scalar_3x4(\
    t0_5,t1_5,t2_5,t3_5,t4_5,\
    t0_4,t1_4,t2_4,t3_4,t4_4,\
    t0_3,t1_3,t2_3,t3_3,t4_3,\
    t0_2,t1_2,t2_2,t3_2,t4_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,\
    o1_4,o2_4,o3_4,\
    o1_3,o2_3,o3_3,\
    o1_2,o2_2,o3_2,\
    o1_1,o2_1,o3_1\
    ):
    ##############################
    # ./input/input_Lx3Ly4.dat
    ##############################
    # (o2_2*(t2_2*((t1_2.conj()*((t1_2*o1_2)*(t0_2*((t3_1.conj()*((t3_1*o3_1)*(t4_1*(t4_0*t3_0))))*(t2_1*((t2_1.conj()*o2_1)*(t2_0*(t1_1*((o1_1*t1_1.conj())*(t0_1*(t0_0*t1_0)))))))))))*(t2_2.conj()*(t3_2*((o3_2*t3_2.conj())*(t4_2*(t0_3*(t1_3.conj()*((t1_3*o1_3)*(t2_3*((t2_3.conj()*o2_3)*(t3_3*((o3_3*t3_3.conj())*(t4_3*((t1_4*((t1_4.conj()*o1_4)*(t0_4*(t0_5*t1_5))))*(t2_4.conj()*((o2_4*t2_4)*(t2_5*(t3_4.conj()*((o3_4*t3_4)*(t4_4*(t4_5*t3_5)))))))))))))))))))))))
    # cpu_cost= 3.0102e+15  memory= 5e+12
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o2_2, np.tensordot(
            t2_2, np.tensordot(
                np.tensordot(
                    t1_2.conj(), np.tensordot(
                        np.tensordot(
                            t1_2, o1_2, ([4], [0])
                        ), np.tensordot(
                            t0_2, np.tensordot(
                                np.tensordot(
                                    t3_1.conj(), np.tensordot(
                                        np.tensordot(
                                            t3_1, o3_1, ([4], [0])
                                        ), np.tensordot(
                                            t4_1, np.tensordot(
                                                t4_0, t3_0, ([1], [0])
                                            ), ([1], [0])
                                        ), ([2, 3], [1, 4])
                                    ), ([2, 3, 4], [4, 6, 2])
                                ), np.tensordot(
                                    t2_1, np.tensordot(
                                        np.tensordot(
                                            t2_1.conj(), o2_1, ([4], [1])
                                        ), np.tensordot(
                                            t2_0, np.tensordot(
                                                t1_1, np.tensordot(
                                                    np.tensordot(
                                                        o1_1, t1_1.conj(), ([1], [4])
                                                    ), np.tensordot(
                                                        t0_1, np.tensordot(
                                                            t0_0, t1_0, ([0], [1])
                                                        ), ([0], [0])
                                                    ), ([1, 4], [2, 5])
                                                ), ([0, 3, 4], [4, 6, 0])
                                            ), ([1], [5])
                                        ), ([0, 3], [6, 2])
                                    ), ([0, 3, 4], [6, 4, 2])
                                ), ([0, 2, 5], [3, 1, 4])
                            ), ([0], [7])
                        ), ([0, 3], [1, 8])
                    ), ([0, 3, 4], [4, 10, 2])
                ), np.tensordot(
                    t2_2.conj(), np.tensordot(
                        t3_2, np.tensordot(
                            np.tensordot(
                                o3_2, t3_2.conj(), ([1], [4])
                            ), np.tensordot(
                                t4_2, np.tensordot(
                                    t0_3, np.tensordot(
                                        t1_3.conj(), np.tensordot(
                                            np.tensordot(
                                                t1_3, o1_3, ([4], [0])
                                            ), np.tensordot(
                                                t2_3, np.tensordot(
                                                    np.tensordot(
                                                        t2_3.conj(), o2_3, ([4], [1])
                                                    ), np.tensordot(
                                                        t3_3, np.tensordot(
                                                            np.tensordot(
                                                                o3_3, t3_3.conj(), ([1], [4])
                                                            ), np.tensordot(
                                                                t4_3, np.tensordot(
                                                                    np.tensordot(
                                                                        t1_4, np.tensordot(
                                                                            np.tensordot(
                                                                                t1_4.conj(), o1_4, ([4], [1])
                                                                            ), np.tensordot(
                                                                                t0_4, np.tensordot(
                                                                                    t0_5, t1_5, ([1], [0])
                                                                                ), ([1], [0])
                                                                            ), ([0, 1], [2, 5])
                                                                        ), ([0, 1, 4], [4, 6, 2])
                                                                    ), np.tensordot(
                                                                        t2_4.conj(), np.tensordot(
                                                                            np.tensordot(
                                                                                o2_4, t2_4, ([0], [4])
                                                                            ), np.tensordot(
                                                                                t2_5, np.tensordot(
                                                                                    t3_4.conj(), np.tensordot(
                                                                                        np.tensordot(
                                                                                            o3_4, t3_4, ([0], [4])
                                                                                        ), np.tensordot(
                                                                                            t4_4, np.tensordot(
                                                                                                t4_5, t3_5, ([0], [1])
                                                                                            ), ([0], [0])
                                                                                        ), ([2, 3], [4, 1])
                                                                                    ), ([1, 2, 4], [6, 4, 0])
                                                                                ), ([1], [5])
                                                                            ), ([2, 3], [1, 5])
                                                                        ), ([1, 2, 4], [4, 5, 0])
                                                                    ), ([0, 2, 5], [2, 0, 4])
                                                                ), ([0], [7])
                                                            ), ([2, 3], [8, 2])
                                                        ), ([1, 2, 4], [10, 4, 0])
                                                    ), ([1, 2], [8, 2])
                                                ), ([1, 2, 4], [10, 3, 2])
                                            ), ([1, 2], [7, 0])
                                        ), ([1, 2, 4], [9, 4, 2])
                                    ), ([1, 2, 3], [9, 2, 0])
                                ), ([0], [7])
                            ), ([2, 3], [9, 2])
                        ), ([1, 2, 4], [10, 4, 0])
                    ), ([1, 2], [9, 2])
                ), ([0, 1, 2, 4, 5, 6, 7, 9], [8, 0, 9, 7, 5, 4, 6, 1])
            ), ([0, 1, 2, 3], [0, 4, 3, 1])
        ), ([0, 1], [0, 1])
    )
