def Contract_scalar_1x4(\
    t0_5,t1_5,t2_5,\
    t0_4,t1_4,t2_4,\
    t0_3,t1_3,t2_3,\
    t0_2,t1_2,t2_2,\
    t0_1,t1_1,t2_1,\
    t0_0,t1_0,t2_0,\
    o1_4,\
    o1_3,\
    o1_2,\
    o1_1\
    ):
    ##############################
    # ./input/input_Lx1Ly4.dat
    ##############################
    # (o1_1*(t1_1.conj()*((t1_0*(t2_0*t2_1))*(t1_1*((t0_0*t0_1)*(t0_2*(t1_2.conj()*((o1_2*t1_2)*(t2_2*(t2_3*(t1_3*((o1_3*t1_3.conj())*(t0_3*(t0_4*(t1_4.conj()*((t1_4*o1_4)*(t2_4*(t0_5*(t1_5*t2_5)))))))))))))))))))
    # cpu_cost= 2.404e+11  memory= 4.0617e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_1, np.tensordot(
            t1_1.conj(), np.tensordot(
                np.tensordot(
                    t1_0, np.tensordot(
                        t2_0, t2_1, ([0], [1])
                    ), ([0], [0])
                ), np.tensordot(
                    t1_1, np.tensordot(
                        np.tensordot(
                            t0_0, t0_1, ([1], [0])
                        ), np.tensordot(
                            t0_2, np.tensordot(
                                t1_2.conj(), np.tensordot(
                                    np.tensordot(
                                        o1_2, t1_2, ([0], [4])
                                    ), np.tensordot(
                                        t2_2, np.tensordot(
                                            t2_3, np.tensordot(
                                                t1_3, np.tensordot(
                                                    np.tensordot(
                                                        o1_3, t1_3.conj(), ([1], [4])
                                                    ), np.tensordot(
                                                        t0_3, np.tensordot(
                                                            t0_4, np.tensordot(
                                                                t1_4.conj(), np.tensordot(
                                                                    np.tensordot(
                                                                        t1_4, o1_4, ([4], [0])
                                                                    ), np.tensordot(
                                                                        t2_4, np.tensordot(
                                                                            t0_5, np.tensordot(
                                                                                t1_5, t2_5, ([1], [0])
                                                                            ), ([1], [0])
                                                                        ), ([0], [3])
                                                                    ), ([1, 2], [4, 1])
                                                                ), ([1, 2, 4], [6, 4, 2])
                                                            ), ([1, 2, 3], [5, 2, 0])
                                                        ), ([1], [0])
                                                    ), ([1, 2], [2, 3])
                                                ), ([0, 1, 4], [4, 5, 0])
                                            ), ([0, 2, 3], [5, 0, 2])
                                        ), ([0], [0])
                                    ), ([2, 3], [3, 1])
                                ), ([1, 2, 4], [5, 4, 0])
                            ), ([1, 2, 3], [5, 2, 0])
                        ), ([1], [0])
                    ), ([0, 1], [1, 4])
                ), ([0, 1, 3, 4], [3, 1, 6, 0])
            ), ([0, 1, 2, 3], [3, 4, 1, 0])
        ), ([0, 1], [1, 0])
    )
