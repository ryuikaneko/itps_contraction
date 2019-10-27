def Contract_scalar_1x3(\
    t0_4,t1_4,t2_4,\
    t0_3,t1_3,t2_3,\
    t0_2,t1_2,t2_2,\
    t0_1,t1_1,t2_1,\
    t0_0,t1_0,t2_0,\
    o1_3,\
    o1_2,\
    o1_1\
    ):
    ##############################
    # ./input/input_Lx1Ly3.dat
    ##############################
    # (o1_2*(t1_2*((t2_2*(t2_1*(t1_1*((o1_1*t1_1.conj())*(t0_1*(t0_0*(t2_0*t1_0)))))))*(t1_2.conj()*(t0_2*(t0_3*(t1_3*((o1_3*t1_3.conj())*(t2_3*(t0_4*(t2_4*t1_4)))))))))))
    # cpu_cost= 1.804e+11  memory= 5.0206e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_2, np.tensordot(
            t1_2, np.tensordot(
                np.tensordot(
                    t2_2, np.tensordot(
                        t2_1, np.tensordot(
                            t1_1, np.tensordot(
                                np.tensordot(
                                    o1_1, t1_1.conj(), ([1], [4])
                                ), np.tensordot(
                                    t0_1, np.tensordot(
                                        t0_0, np.tensordot(
                                            t2_0, t1_0, ([1], [0])
                                        ), ([0], [1])
                                    ), ([0], [0])
                                ), ([1, 4], [2, 5])
                            ), ([0, 3, 4], [4, 6, 0])
                        ), ([1, 2, 3], [5, 1, 3])
                    ), ([1], [0])
                ), np.tensordot(
                    t1_2.conj(), np.tensordot(
                        t0_2, np.tensordot(
                            t0_3, np.tensordot(
                                t1_3, np.tensordot(
                                    np.tensordot(
                                        o1_3, t1_3.conj(), ([1], [4])
                                    ), np.tensordot(
                                        t2_3, np.tensordot(
                                            t0_4, np.tensordot(
                                                t2_4, t1_4, ([0], [1])
                                            ), ([1], [1])
                                        ), ([0], [1])
                                    ), ([2, 3], [5, 2])
                                ), ([1, 2, 4], [6, 4, 0])
                            ), ([1, 2, 3], [5, 0, 2])
                        ), ([1], [0])
                    ), ([0, 1], [2, 4])
                ), ([0, 2, 4, 5], [6, 0, 1, 3])
            ), ([0, 1, 2, 3], [3, 4, 0, 1])
        ), ([0, 1], [0, 1])
    )
