def Contract_scalar_2x2(\
    t0_3,t1_3,t2_3,t3_3,\
    t0_2,t1_2,t2_2,t3_2,\
    t0_1,t1_1,t2_1,t3_1,\
    t0_0,t1_0,t2_0,t3_0,\
    o1_2,o2_2,\
    o1_1,o2_1\
    ):
    ##############################
    # ./input/input_Lx2Ly2.dat
    ##############################
    # (o1_2*(t1_2.conj()*((t0_2*(t0_3*t1_3))*(t1_2*((t2_2.conj()*((o2_2*t2_2)*(t2_3*(t3_3*t3_2))))*((t1_1*((t1_1.conj()*o1_1)*(t1_0*(t0_0*t0_1))))*(t2_1.conj()*((o2_1*t2_1)*(t2_0*(t3_0*t3_1))))))))))
    # cpu_cost= 2.2004e+12  memory= 6.0008e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_2, np.tensordot(
            t1_2.conj(), np.tensordot(
                np.tensordot(
                    t0_2, np.tensordot(
                        t0_3, t1_3, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t1_2, np.tensordot(
                        np.tensordot(
                            t2_2.conj(), np.tensordot(
                                np.tensordot(
                                    o2_2, t2_2, ([0], [4])
                                ), np.tensordot(
                                    t2_3, np.tensordot(
                                        t3_3, t3_2, ([1], [0])
                                    ), ([1], [0])
                                ), ([2, 3], [1, 4])
                            ), ([1, 2, 4], [4, 6, 0])
                        ), np.tensordot(
                            np.tensordot(
                                t1_1, np.tensordot(
                                    np.tensordot(
                                        t1_1.conj(), o1_1, ([4], [1])
                                    ), np.tensordot(
                                        t1_0, np.tensordot(
                                            t0_0, t0_1, ([1], [0])
                                        ), ([1], [0])
                                    ), ([0, 3], [5, 2])
                                ), ([0, 3, 4], [6, 4, 2])
                            ), np.tensordot(
                                t2_1.conj(), np.tensordot(
                                    np.tensordot(
                                        o2_1, t2_1, ([0], [4])
                                    ), np.tensordot(
                                        t2_0, np.tensordot(
                                            t3_0, t3_1, ([0], [1])
                                        ), ([0], [0])
                                    ), ([3, 4], [4, 1])
                                ), ([2, 3, 4], [6, 4, 0])
                            ), ([1, 3, 4], [2, 0, 4])
                        ), ([1, 3, 5], [3, 4, 5])
                    ), ([2, 3], [1, 3])
                ), ([0, 1, 3, 4], [6, 0, 4, 1])
            ), ([0, 1, 2, 3], [0, 1, 3, 4])
        ), ([0, 1], [1, 0])
    )
