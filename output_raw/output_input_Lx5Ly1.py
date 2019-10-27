def Contract_scalar_5x1(\
    t0_2,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,t5_1,t6_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,t5_0,t6_0,\
    o1_1,o2_1,o3_1,o4_1,o5_1\
    ):
    ##############################
    # ./input/input_Lx5Ly1.dat
    ##############################
    # (o2_1*(t2_1.conj()*((t2_2*(t1_0*(t1_1.conj()*((o1_1*t1_1)*(t1_2*(t0_0*(t0_1*t0_2)))))))*(t2_1*(t2_0*(t3_2*(t3_1.conj()*((t3_1*o3_1)*(t3_0*(t4_0*(t4_1.conj()*((o4_1*t4_1)*(t4_2*(t5_0*(t5_1.conj()*((o5_1*t5_1)*(t5_2*(t6_0*(t6_2*t6_1)))))))))))))))))))
    # cpu_cost= 3.004e+11  memory= 5.0206e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o2_1, np.tensordot(
            t2_1.conj(), np.tensordot(
                np.tensordot(
                    t2_2, np.tensordot(
                        t1_0, np.tensordot(
                            t1_1.conj(), np.tensordot(
                                np.tensordot(
                                    o1_1, t1_1, ([0], [4])
                                ), np.tensordot(
                                    t1_2, np.tensordot(
                                        t0_0, np.tensordot(
                                            t0_1, t0_2, ([1], [0])
                                        ), ([1], [0])
                                    ), ([0], [3])
                                ), ([1, 2], [4, 1])
                            ), ([0, 1, 4], [6, 4, 0])
                        ), ([1, 2, 3], [5, 3, 1])
                    ), ([0], [3])
                ), np.tensordot(
                    t2_1, np.tensordot(
                        t2_0, np.tensordot(
                            t3_2, np.tensordot(
                                t3_1.conj(), np.tensordot(
                                    np.tensordot(
                                        t3_1, o3_1, ([4], [0])
                                    ), np.tensordot(
                                        t3_0, np.tensordot(
                                            t4_0, np.tensordot(
                                                t4_1.conj(), np.tensordot(
                                                    np.tensordot(
                                                        o4_1, t4_1, ([0], [4])
                                                    ), np.tensordot(
                                                        t4_2, np.tensordot(
                                                            t5_0, np.tensordot(
                                                                t5_1.conj(), np.tensordot(
                                                                    np.tensordot(
                                                                        o5_1, t5_1, ([0], [4])
                                                                    ), np.tensordot(
                                                                        t5_2, np.tensordot(
                                                                            t6_0, np.tensordot(
                                                                                t6_2, t6_1, ([1], [0])
                                                                            ), ([0], [1])
                                                                        ), ([1], [1])
                                                                    ), ([2, 3], [1, 4])
                                                                ), ([1, 2, 4], [4, 6, 0])
                                                            ), ([0, 2, 3], [5, 3, 1])
                                                        ), ([1], [3])
                                                    ), ([2, 3], [1, 5])
                                                ), ([1, 2, 4], [4, 6, 0])
                                            ), ([0, 2, 3], [5, 3, 1])
                                        ), ([0], [0])
                                    ), ([2, 3], [4, 1])
                                ), ([2, 3, 4], [5, 4, 2])
                            ), ([1, 2, 3], [5, 3, 1])
                        ), ([0], [3])
                    ), ([2, 3], [5, 1])
                ), ([0, 1, 3, 5], [5, 1, 3, 0])
            ), ([0, 1, 2, 3], [1, 0, 4, 3])
        ), ([0, 1], [1, 0])
    )
