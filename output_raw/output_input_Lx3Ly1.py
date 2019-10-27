def Contract_scalar_3x1(\
    t0_2,t1_2,t2_2,t3_2,t4_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,\
    o1_1,o2_1,o3_1\
    ):
    ##############################
    # ./input/input_Lx3Ly1.dat
    ##############################
    # (o2_1*(t2_1*((t2_2*(t1_2*(t1_1*((o1_1*t1_1.conj())*(t1_0*(t0_0*(t0_2*t0_1)))))))*(t2_1.conj()*(t2_0*(t3_2*(t3_1*((o3_1*t3_1.conj())*(t3_0*(t4_0*(t4_2*t4_1)))))))))))
    # cpu_cost= 1.804e+11  memory= 5.0206e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o2_1, np.tensordot(
            t2_1, np.tensordot(
                np.tensordot(
                    t2_2, np.tensordot(
                        t1_2, np.tensordot(
                            t1_1, np.tensordot(
                                np.tensordot(
                                    o1_1, t1_1.conj(), ([1], [4])
                                ), np.tensordot(
                                    t1_0, np.tensordot(
                                        t0_0, np.tensordot(
                                            t0_2, t0_1, ([0], [1])
                                        ), ([1], [1])
                                    ), ([1], [0])
                                ), ([1, 4], [5, 2])
                            ), ([0, 3, 4], [6, 4, 0])
                        ), ([0, 2, 3], [5, 0, 2])
                    ), ([0], [0])
                ), np.tensordot(
                    t2_1.conj(), np.tensordot(
                        t2_0, np.tensordot(
                            t3_2, np.tensordot(
                                t3_1, np.tensordot(
                                    np.tensordot(
                                        o3_1, t3_1.conj(), ([1], [4])
                                    ), np.tensordot(
                                        t3_0, np.tensordot(
                                            t4_0, np.tensordot(
                                                t4_2, t4_1, ([1], [0])
                                            ), ([0], [1])
                                        ), ([0], [0])
                                    ), ([3, 4], [5, 2])
                                ), ([2, 3, 4], [6, 4, 0])
                            ), ([1, 2, 3], [5, 1, 3])
                        ), ([0], [3])
                    ), ([2, 3], [5, 2])
                ), ([0, 2, 4, 5], [5, 1, 0, 3])
            ), ([0, 1, 2, 3], [1, 0, 4, 3])
        ), ([0, 1], [0, 1])
    )
