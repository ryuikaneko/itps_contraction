def Contract_scalar_6x1(\
    t0_2,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,t5_1,t6_1,t7_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,t5_0,t6_0,t7_0,\
    o1_1,o2_1,o3_1,o4_1,o5_1,o6_1\
    ):
    ##############################
    # ./input/input_Lx6Ly1.dat
    ##############################
    # (o3_1*(t3_1.conj()*((t3_0*(t2_2*(t2_1*((t2_1.conj()*o2_1)*(t2_0*(t1_0*(t1_1.conj()*((o1_1*t1_1)*(t1_2*(t0_0*(t0_2*t0_1)))))))))))*(t3_1*(t3_2*(t4_0*(t4_1.conj()*((o4_1*t4_1)*(t4_2*(t5_0*(t5_1*((o5_1*t5_1.conj())*(t5_2*(t6_0*(t6_1.conj()*((t6_1*o6_1)*(t6_2*(t7_0*(t7_2*t7_1)))))))))))))))))))
    # cpu_cost= 3.604e+11  memory= 5.041e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o3_1, np.tensordot(
            t3_1.conj(), np.tensordot(
                np.tensordot(
                    t3_0, np.tensordot(
                        t2_2, np.tensordot(
                            t2_1, np.tensordot(
                                np.tensordot(
                                    t2_1.conj(), o2_1, ([4], [1])
                                ), np.tensordot(
                                    t2_0, np.tensordot(
                                        t1_0, np.tensordot(
                                            t1_1.conj(), np.tensordot(
                                                np.tensordot(
                                                    o1_1, t1_1, ([0], [4])
                                                ), np.tensordot(
                                                    t1_2, np.tensordot(
                                                        t0_0, np.tensordot(
                                                            t0_2, t0_1, ([0], [1])
                                                        ), ([1], [1])
                                                    ), ([0], [1])
                                                ), ([1, 2], [4, 1])
                                            ), ([0, 1, 4], [6, 4, 0])
                                        ), ([1, 2, 3], [5, 3, 1])
                                    ), ([1], [0])
                                ), ([0, 3], [3, 2])
                            ), ([0, 3, 4], [5, 4, 2])
                        ), ([0, 2, 3], [5, 0, 2])
                    ), ([1], [3])
                ), np.tensordot(
                    t3_1, np.tensordot(
                        t3_2, np.tensordot(
                            t4_0, np.tensordot(
                                t4_1.conj(), np.tensordot(
                                    np.tensordot(
                                        o4_1, t4_1, ([0], [4])
                                    ), np.tensordot(
                                        t4_2, np.tensordot(
                                            t5_0, np.tensordot(
                                                t5_1, np.tensordot(
                                                    np.tensordot(
                                                        o5_1, t5_1.conj(), ([1], [4])
                                                    ), np.tensordot(
                                                        t5_2, np.tensordot(
                                                            t6_0, np.tensordot(
                                                                t6_1.conj(), np.tensordot(
                                                                    np.tensordot(
                                                                        t6_1, o6_1, ([4], [0])
                                                                    ), np.tensordot(
                                                                        t6_2, np.tensordot(
                                                                            t7_0, np.tensordot(
                                                                                t7_2, t7_1, ([1], [0])
                                                                            ), ([0], [1])
                                                                        ), ([1], [1])
                                                                    ), ([1, 2], [1, 4])
                                                                ), ([1, 2, 4], [4, 6, 2])
                                                            ), ([0, 2, 3], [5, 3, 1])
                                                        ), ([1], [3])
                                                    ), ([2, 3], [2, 4])
                                                ), ([1, 2, 4], [4, 6, 0])
                                            ), ([0, 2, 3], [5, 1, 3])
                                        ), ([1], [3])
                                    ), ([2, 3], [1, 4])
                                ), ([1, 2, 4], [4, 6, 0])
                            ), ([0, 2, 3], [5, 3, 1])
                        ), ([1], [3])
                    ), ([1, 2], [1, 5])
                ), ([0, 1, 3, 4], [5, 1, 3, 0])
            ), ([0, 1, 2, 3], [1, 3, 4, 0])
        ), ([0, 1], [1, 0])
    )
