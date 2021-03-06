def Contract_scalar_2x1(\
    t0_2,t1_2,t2_2,t3_2,\
    t0_1,t1_1,t2_1,t3_1,\
    t0_0,t1_0,t2_0,t3_0,\
    o1_1,o2_1\
    ):
    ##############################
    # ./input/input_Lx2Ly1.dat
    ##############################
    # (o1_1*(t1_1.conj()*((t0_1*(t0_2*t1_2))*(t1_1*((t0_0*t1_0)*(t2_0*(t2_1.conj()*((o2_1*t2_1)*(t2_2*(t3_0*(t3_1*t3_2)))))))))))
    # cpu_cost= 1.204e+11  memory= 4.0209e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_1, np.tensordot(
            t1_1.conj(), np.tensordot(
                np.tensordot(
                    t0_1, np.tensordot(
                        t0_2, t1_2, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t1_1, np.tensordot(
                        np.tensordot(
                            t0_0, t1_0, ([0], [1])
                        ), np.tensordot(
                            t2_0, np.tensordot(
                                t2_1.conj(), np.tensordot(
                                    np.tensordot(
                                        o2_1, t2_1, ([0], [4])
                                    ), np.tensordot(
                                        t2_2, np.tensordot(
                                            t3_0, np.tensordot(
                                                t3_1, t3_2, ([0], [1])
                                            ), ([0], [0])
                                        ), ([1], [3])
                                    ), ([2, 3], [1, 4])
                                ), ([1, 2, 4], [4, 6, 0])
                            ), ([0, 2, 3], [5, 3, 1])
                        ), ([1], [0])
                    ), ([2, 3], [4, 1])
                ), ([0, 1, 3, 4], [3, 0, 6, 1])
            ), ([0, 1, 2, 3], [0, 1, 4, 3])
        ), ([0, 1], [1, 0])
    )
