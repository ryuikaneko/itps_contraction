def Contract_scalar_2x4(\
    t0_5,t1_5,t2_5,t3_5,\
    t0_4,t1_4,t2_4,t3_4,\
    t0_3,t1_3,t2_3,t3_3,\
    t0_2,t1_2,t2_2,t3_2,\
    t0_1,t1_1,t2_1,t3_1,\
    t0_0,t1_0,t2_0,t3_0,\
    o1_4,o2_4,\
    o1_3,o2_3,\
    o1_2,o2_2,\
    o1_1,o2_1\
    ):
    ##############################
    # ./input/input_Lx2Ly4.dat
    ##############################
    # (o2_4*(t2_4*((t2_5*(t3_5*t3_4))*(t2_4.conj()*((t1_4*((o1_4*t1_4.conj())*(t0_4*(t0_5*t1_5))))*(t0_3*(t1_3.conj()*((o1_3*t1_3)*(t2_3.conj()*((o2_3*t2_3)*(t3_3*(t0_2*(t1_2.conj()*((o1_2*t1_2)*(t2_2.conj()*((t2_2*o2_2)*(t3_2*((t1_1.conj()*((o1_1*t1_1)*(t1_0*(t0_0*t0_1))))*(t2_1*((o2_1*t2_1.conj())*(t3_1*(t3_0*t2_0))))))))))))))))))))))
    # cpu_cost= 2.22004e+13  memory= 3.02032e+10
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o2_4, np.tensordot(
            t2_4, np.tensordot(
                np.tensordot(
                    t2_5, np.tensordot(
                        t3_5, t3_4, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t2_4.conj(), np.tensordot(
                        np.tensordot(
                            t1_4, np.tensordot(
                                np.tensordot(
                                    o1_4, t1_4.conj(), ([1], [4])
                                ), np.tensordot(
                                    t0_4, np.tensordot(
                                        t0_5, t1_5, ([1], [0])
                                    ), ([1], [0])
                                ), ([1, 2], [2, 5])
                            ), ([0, 1, 4], [4, 6, 0])
                        ), np.tensordot(
                            t0_3, np.tensordot(
                                t1_3.conj(), np.tensordot(
                                    np.tensordot(
                                        o1_3, t1_3, ([0], [4])
                                    ), np.tensordot(
                                        t2_3.conj(), np.tensordot(
                                            np.tensordot(
                                                o2_3, t2_3, ([0], [4])
                                            ), np.tensordot(
                                                t3_3, np.tensordot(
                                                    t0_2, np.tensordot(
                                                        t1_2.conj(), np.tensordot(
                                                            np.tensordot(
                                                                o1_2, t1_2, ([0], [4])
                                                            ), np.tensordot(
                                                                t2_2.conj(), np.tensordot(
                                                                    np.tensordot(
                                                                        t2_2, o2_2, ([4], [0])
                                                                    ), np.tensordot(
                                                                        t3_2, np.tensordot(
                                                                            np.tensordot(
                                                                                t1_1.conj(), np.tensordot(
                                                                                    np.tensordot(
                                                                                        o1_1, t1_1, ([0], [4])
                                                                                    ), np.tensordot(
                                                                                        t1_0, np.tensordot(
                                                                                            t0_0, t0_1, ([1], [0])
                                                                                        ), ([1], [0])
                                                                                    ), ([1, 4], [4, 1])
                                                                                ), ([0, 3, 4], [6, 4, 0])
                                                                            ), np.tensordot(
                                                                                t2_1, np.tensordot(
                                                                                    np.tensordot(
                                                                                        o2_1, t2_1.conj(), ([1], [4])
                                                                                    ), np.tensordot(
                                                                                        t3_1, np.tensordot(
                                                                                            t3_0, t2_0, ([1], [0])
                                                                                        ), ([1], [0])
                                                                                    ), ([3, 4], [2, 5])
                                                                                ), ([2, 3, 4], [4, 6, 0])
                                                                            ), ([1, 3, 4], [2, 0, 5])
                                                                        ), ([1], [5])
                                                                    ), ([2, 3], [1, 6])
                                                                ), ([2, 3, 4], [4, 8, 2])
                                                            ), ([3, 4], [2, 6])
                                                        ), ([2, 3, 4], [3, 7, 0])
                                                    ), ([0, 2, 3], [7, 2, 0])
                                                ), ([1], [5])
                                            ), ([3, 4], [1, 7])
                                        ), ([2, 3, 4], [4, 8, 0])
                                    ), ([3, 4], [2, 7])
                                ), ([2, 3, 4], [3, 8, 0])
                            ), ([0, 2, 3], [7, 2, 0])
                        ), ([1, 3, 4], [2, 1, 0])
                    ), ([0, 3], [1, 3])
                ), ([0, 2, 3, 5], [4, 0, 6, 1])
            ), ([0, 1, 2, 3], [3, 0, 1, 4])
        ), ([0, 1], [0, 1])
    )
