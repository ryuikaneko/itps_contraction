def Contract_scalar_1x2(\
    t0_3,t1_3,t2_3,\
    t0_2,t1_2,t2_2,\
    t0_1,t1_1,t2_1,\
    t0_0,t1_0,t2_0,\
    o1_2,\
    o1_1\
    ):
    ##############################
    # ./input/input_Lx1Ly2.dat
    ##############################
    # (o1_1*(t1_1.conj()*((t0_1*(t0_0*t1_0))*(t1_1*((t2_0*t2_1)*(t2_2*(t1_2.conj()*((o1_2*t1_2)*(t0_2*(t0_3*(t2_3*t1_3)))))))))))
    # cpu_cost= 1.204e+11  memory= 4.0209e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_1, np.tensordot(
            t1_1.conj(), np.tensordot(
                np.tensordot(
                    t0_1, np.tensordot(
                        t0_0, t1_0, ([0], [1])
                    ), ([0], [0])
                ), np.tensordot(
                    t1_1, np.tensordot(
                        np.tensordot(
                            t2_0, t2_1, ([0], [1])
                        ), np.tensordot(
                            t2_2, np.tensordot(
                                t1_2.conj(), np.tensordot(
                                    np.tensordot(
                                        o1_2, t1_2, ([0], [4])
                                    ), np.tensordot(
                                        t0_2, np.tensordot(
                                            t0_3, np.tensordot(
                                                t2_3, t1_3, ([0], [1])
                                            ), ([1], [1])
                                        ), ([1], [0])
                                    ), ([1, 2], [1, 4])
                                ), ([0, 1, 4], [4, 6, 0])
                            ), ([0, 2, 3], [5, 2, 0])
                        ), ([1], [0])
                    ), ([1, 2], [4, 1])
                ), ([0, 1, 3, 4], [6, 0, 3, 1])
            ), ([0, 1, 2, 3], [0, 4, 3, 1])
        ), ([0, 1], [1, 0])
    )
