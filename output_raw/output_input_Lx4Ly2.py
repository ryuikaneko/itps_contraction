def Contract_scalar_4x2(\
    t0_3,t1_3,t2_3,t3_3,t4_3,t5_3,\
    t0_2,t1_2,t2_2,t3_2,t4_2,t5_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,t5_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,t5_0,\
    o1_2,o2_2,o3_2,o4_2,\
    o1_1,o2_1,o3_1,o4_1\
    ):
    ##############################
    # ./input/input_Lx4Ly2.dat
    ##############################
    # (o4_2*(t4_2*((t4_3*(t5_3*t5_2))*(t4_2.conj()*((t4_1.conj()*((t4_1*o4_1)*(t4_0*(t5_0*t5_1))))*(t3_3*(t3_2*((o3_2*t3_2.conj())*(t3_1.conj()*((o3_1*t3_1)*(t3_0*(t2_0*(t2_1*((o2_1*t2_1.conj())*(t2_2.conj()*((o2_2*t2_2)*(t2_3*((t1_1.conj()*((o1_1*t1_1)*(t0_1*(t0_0*t1_0))))*(t1_2.conj()*((o1_2*t1_2)*(t0_2*(t0_3*t1_3))))))))))))))))))))))
    # cpu_cost= 2.22004e+13  memory= 3.02032e+10
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o4_2, np.tensordot(
            t4_2, np.tensordot(
                np.tensordot(
                    t4_3, np.tensordot(
                        t5_3, t5_2, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t4_2.conj(), np.tensordot(
                        np.tensordot(
                            t4_1.conj(), np.tensordot(
                                np.tensordot(
                                    t4_1, o4_1, ([4], [0])
                                ), np.tensordot(
                                    t4_0, np.tensordot(
                                        t5_0, t5_1, ([0], [1])
                                    ), ([0], [0])
                                ), ([2, 3], [4, 1])
                            ), ([2, 3, 4], [6, 4, 2])
                        ), np.tensordot(
                            t3_3, np.tensordot(
                                t3_2, np.tensordot(
                                    np.tensordot(
                                        o3_2, t3_2.conj(), ([1], [4])
                                    ), np.tensordot(
                                        t3_1.conj(), np.tensordot(
                                            np.tensordot(
                                                o3_1, t3_1, ([0], [4])
                                            ), np.tensordot(
                                                t3_0, np.tensordot(
                                                    t2_0, np.tensordot(
                                                        t2_1, np.tensordot(
                                                            np.tensordot(
                                                                o2_1, t2_1.conj(), ([1], [4])
                                                            ), np.tensordot(
                                                                t2_2.conj(), np.tensordot(
                                                                    np.tensordot(
                                                                        o2_2, t2_2, ([0], [4])
                                                                    ), np.tensordot(
                                                                        t2_3, np.tensordot(
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
                                                                                t1_2.conj(), np.tensordot(
                                                                                    np.tensordot(
                                                                                        o1_2, t1_2, ([0], [4])
                                                                                    ), np.tensordot(
                                                                                        t0_2, np.tensordot(
                                                                                            t0_3, t1_3, ([1], [0])
                                                                                        ), ([1], [0])
                                                                                    ), ([1, 2], [1, 4])
                                                                                ), ([0, 1, 4], [4, 6, 0])
                                                                            ), ([0, 2, 4], [1, 3, 4])
                                                                        ), ([0], [5])
                                                                    ), ([1, 2], [7, 1])
                                                                ), ([0, 1, 4], [8, 4, 0])
                                                            ), ([1, 2], [5, 1])
                                                        ), ([0, 1, 4], [7, 5, 0])
                                                    ), ([1, 2, 3], [7, 1, 3])
                                                ), ([1], [0])
                                            ), ([1, 4], [3, 1])
                                        ), ([0, 3, 4], [5, 4, 0])
                                    ), ([1, 4], [5, 0])
                                ), ([0, 3, 4], [7, 4, 0])
                            ), ([0, 2, 3], [7, 0, 2])
                        ), ([0, 2, 4], [3, 4, 5])
                    ), ([0, 3], [5, 0])
                ), ([0, 2, 3, 5], [5, 0, 4, 1])
            ), ([0, 1, 2, 3], [4, 0, 1, 3])
        ), ([0, 1], [0, 1])
    )
