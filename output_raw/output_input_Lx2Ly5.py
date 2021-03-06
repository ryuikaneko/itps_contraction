def Contract_scalar_2x5(\
    t0_6,t1_6,t2_6,t3_6,\
    t0_5,t1_5,t2_5,t3_5,\
    t0_4,t1_4,t2_4,t3_4,\
    t0_3,t1_3,t2_3,t3_3,\
    t0_2,t1_2,t2_2,t3_2,\
    t0_1,t1_1,t2_1,t3_1,\
    t0_0,t1_0,t2_0,t3_0,\
    o1_5,o2_5,\
    o1_4,o2_4,\
    o1_3,o2_3,\
    o1_2,o2_2,\
    o1_1,o2_1\
    ):
    ##############################
    # ./input/input_Lx2Ly5.dat
    ##############################
    # (o1_2*(t1_2*((t0_2*((t1_1*((t1_1.conj()*o1_1)*(t1_0*(t0_0*t0_1))))*(t2_1*((o2_1*t2_1.conj())*(t2_0*(t3_0*t3_1))))))*(t1_2.conj()*(t2_2.conj()*((o2_2*t2_2)*(t3_2*(t0_3*(t1_3.conj()*((t1_3*o1_3)*(t2_3*((t2_3.conj()*o2_3)*(t3_3*(t0_4*(t1_4*((t1_4.conj()*o1_4)*(t2_4*((t2_4.conj()*o2_4)*(t3_4*((t2_5*((o2_5*t2_5.conj())*(t2_6*(t3_6*t3_5))))*(t1_5.conj()*((o1_5*t1_5)*(t0_5*(t0_6*t1_6))))))))))))))))))))))))
    # cpu_cost= 3.22004e+13  memory= 4.00042e+10
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_2, np.tensordot(
            t1_2, np.tensordot(
                np.tensordot(
                    t0_2, np.tensordot(
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
                            t2_1, np.tensordot(
                                np.tensordot(
                                    o2_1, t2_1.conj(), ([1], [4])
                                ), np.tensordot(
                                    t2_0, np.tensordot(
                                        t3_0, t3_1, ([0], [1])
                                    ), ([0], [0])
                                ), ([3, 4], [5, 2])
                            ), ([2, 3, 4], [6, 4, 0])
                        ), ([1, 3, 4], [0, 2, 4])
                    ), ([0], [2])
                ), np.tensordot(
                    t1_2.conj(), np.tensordot(
                        t2_2.conj(), np.tensordot(
                            np.tensordot(
                                o2_2, t2_2, ([0], [4])
                            ), np.tensordot(
                                t3_2, np.tensordot(
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
                                                            t0_4, np.tensordot(
                                                                t1_4, np.tensordot(
                                                                    np.tensordot(
                                                                        t1_4.conj(), o1_4, ([4], [1])
                                                                    ), np.tensordot(
                                                                        t2_4, np.tensordot(
                                                                            np.tensordot(
                                                                                t2_4.conj(), o2_4, ([4], [1])
                                                                            ), np.tensordot(
                                                                                t3_4, np.tensordot(
                                                                                    np.tensordot(
                                                                                        t2_5, np.tensordot(
                                                                                            np.tensordot(
                                                                                                o2_5, t2_5.conj(), ([1], [4])
                                                                                            ), np.tensordot(
                                                                                                t2_6, np.tensordot(
                                                                                                    t3_6, t3_5, ([1], [0])
                                                                                                ), ([1], [0])
                                                                                            ), ([2, 3], [2, 5])
                                                                                        ), ([1, 2, 4], [4, 6, 0])
                                                                                    ), np.tensordot(
                                                                                        t1_5.conj(), np.tensordot(
                                                                                            np.tensordot(
                                                                                                o1_5, t1_5, ([0], [4])
                                                                                            ), np.tensordot(
                                                                                                t0_5, np.tensordot(
                                                                                                    t0_6, t1_6, ([1], [0])
                                                                                                ), ([1], [0])
                                                                                            ), ([1, 2], [1, 4])
                                                                                        ), ([0, 1, 4], [4, 6, 0])
                                                                                    ), ([0, 2, 4], [2, 0, 5])
                                                                                ), ([0], [2])
                                                                            ), ([1, 2], [4, 2])
                                                                        ), ([1, 2, 4], [5, 4, 2])
                                                                    ), ([1, 2], [5, 2])
                                                                ), ([1, 2, 4], [7, 3, 2])
                                                            ), ([1, 2, 3], [7, 0, 2])
                                                        ), ([0], [5])
                                                    ), ([1, 2], [7, 2])
                                                ), ([1, 2, 4], [8, 4, 2])
                                            ), ([1, 2], [6, 0])
                                        ), ([1, 2, 4], [8, 4, 2])
                                    ), ([1, 2, 3], [7, 2, 0])
                                ), ([0], [5])
                            ), ([2, 3], [6, 1])
                        ), ([1, 2, 4], [8, 4, 0])
                    ), ([1, 2], [6, 0])
                ), ([0, 2, 4, 5, 6, 7], [7, 0, 1, 5, 3, 6])
            ), ([0, 1, 2, 3], [0, 4, 3, 1])
        ), ([0, 1], [0, 1])
    )
