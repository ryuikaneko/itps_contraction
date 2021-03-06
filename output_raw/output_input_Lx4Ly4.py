def Contract_scalar_4x4(\
    t0_5,t1_5,t2_5,t3_5,t4_5,t5_5,\
    t0_4,t1_4,t2_4,t3_4,t4_4,t5_4,\
    t0_3,t1_3,t2_3,t3_3,t4_3,t5_3,\
    t0_2,t1_2,t2_2,t3_2,t4_2,t5_2,\
    t0_1,t1_1,t2_1,t3_1,t4_1,t5_1,\
    t0_0,t1_0,t2_0,t3_0,t4_0,t5_0,\
    o1_4,o2_4,o3_4,o4_4,\
    o1_3,o2_3,o3_3,o4_3,\
    o1_2,o2_2,o3_2,o4_2,\
    o1_1,o2_1,o3_1,o4_1\
    ):
    ##############################
    # ./input/input_Lx4Ly4.dat
    ##############################
    # (o1_1*(t1_1*((t1_0*(t0_0*t0_1))*(t1_1.conj()*(t2_0*(t2_1*((t2_1.conj()*o2_1)*((t3_1*((t3_1.conj()*o3_1)*(t3_0*(t4_1*((t4_1.conj()*o4_1)*(t4_0*(t5_0*t5_1)))))))*(t0_2*(t1_2*((t1_2.conj()*o1_2)*(t2_2*((t2_2.conj()*o2_2)*(t3_2*((t3_2.conj()*o3_2)*(t4_2*((t4_2.conj()*o4_2)*(t5_2*(t0_3*(t1_3*((t1_3.conj()*o1_3)*(t2_3*((t2_3.conj()*o2_3)*(t3_3*((t3_3.conj()*o3_3)*(t4_3*((t4_3.conj()*o4_3)*(t5_3*((t2_4*((t2_4.conj()*o2_4)*(t2_5*(t1_4*((t1_4.conj()*o1_4)*(t0_4*(t0_5*t1_5)))))))*(t3_4*((t3_4.conj()*o3_4)*(t3_5*(t4_4*((t4_4.conj()*o4_4)*(t4_5*(t5_5*t5_4))))))))))))))))))))))))))))))))))))
    # cpu_cost= 3.8002e+17  memory= 3.0001e+14
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_1, np.tensordot(
            t1_1, np.tensordot(
                np.tensordot(
                    t1_0, np.tensordot(
                        t0_0, t0_1, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t1_1.conj(), np.tensordot(
                        t2_0, np.tensordot(
                            t2_1, np.tensordot(
                                np.tensordot(
                                    t2_1.conj(), o2_1, ([4], [1])
                                ), np.tensordot(
                                    np.tensordot(
                                        t3_1, np.tensordot(
                                            np.tensordot(
                                                t3_1.conj(), o3_1, ([4], [1])
                                            ), np.tensordot(
                                                t3_0, np.tensordot(
                                                    t4_1, np.tensordot(
                                                        np.tensordot(
                                                            t4_1.conj(), o4_1, ([4], [1])
                                                        ), np.tensordot(
                                                            t4_0, np.tensordot(
                                                                t5_0, t5_1, ([0], [1])
                                                            ), ([0], [0])
                                                        ), ([2, 3], [5, 2])
                                                    ), ([2, 3, 4], [6, 4, 2])
                                                ), ([0], [4])
                                            ), ([2, 3], [5, 2])
                                        ), ([2, 3, 4], [5, 4, 2])
                                    ), np.tensordot(
                                        t0_2, np.tensordot(
                                            t1_2, np.tensordot(
                                                np.tensordot(
                                                    t1_2.conj(), o1_2, ([4], [1])
                                                ), np.tensordot(
                                                    t2_2, np.tensordot(
                                                        np.tensordot(
                                                            t2_2.conj(), o2_2, ([4], [1])
                                                        ), np.tensordot(
                                                            t3_2, np.tensordot(
                                                                np.tensordot(
                                                                    t3_2.conj(), o3_2, ([4], [1])
                                                                ), np.tensordot(
                                                                    t4_2, np.tensordot(
                                                                        np.tensordot(
                                                                            t4_2.conj(), o4_2, ([4], [1])
                                                                        ), np.tensordot(
                                                                            t5_2, np.tensordot(
                                                                                t0_3, np.tensordot(
                                                                                    t1_3, np.tensordot(
                                                                                        np.tensordot(
                                                                                            t1_3.conj(), o1_3, ([4], [1])
                                                                                        ), np.tensordot(
                                                                                            t2_3, np.tensordot(
                                                                                                np.tensordot(
                                                                                                    t2_3.conj(), o2_3, ([4], [1])
                                                                                                ), np.tensordot(
                                                                                                    t3_3, np.tensordot(
                                                                                                        np.tensordot(
                                                                                                            t3_3.conj(), o3_3, ([4], [1])
                                                                                                        ), np.tensordot(
                                                                                                            t4_3, np.tensordot(
                                                                                                                np.tensordot(
                                                                                                                    t4_3.conj(), o4_3, ([4], [1])
                                                                                                                ), np.tensordot(
                                                                                                                    t5_3, np.tensordot(
                                                                                                                        np.tensordot(
                                                                                                                            t2_4, np.tensordot(
                                                                                                                                np.tensordot(
                                                                                                                                    t2_4.conj(), o2_4, ([4], [1])
                                                                                                                                ), np.tensordot(
                                                                                                                                    t2_5, np.tensordot(
                                                                                                                                        t1_4, np.tensordot(
                                                                                                                                            np.tensordot(
                                                                                                                                                t1_4.conj(), o1_4, ([4], [1])
                                                                                                                                            ), np.tensordot(
                                                                                                                                                t0_4, np.tensordot(
                                                                                                                                                    t0_5, t1_5, ([1], [0])
                                                                                                                                                ), ([1], [0])
                                                                                                                                            ), ([0, 1], [2, 5])
                                                                                                                                        ), ([0, 1, 4], [4, 6, 2])
                                                                                                                                    ), ([0], [5])
                                                                                                                                ), ([0, 1], [5, 2])
                                                                                                                            ), ([0, 1, 4], [5, 4, 2])
                                                                                                                        ), np.tensordot(
                                                                                                                            t3_4, np.tensordot(
                                                                                                                                np.tensordot(
                                                                                                                                    t3_4.conj(), o3_4, ([4], [1])
                                                                                                                                ), np.tensordot(
                                                                                                                                    t3_5, np.tensordot(
                                                                                                                                        t4_4, np.tensordot(
                                                                                                                                            np.tensordot(
                                                                                                                                                t4_4.conj(), o4_4, ([4], [1])
                                                                                                                                            ), np.tensordot(
                                                                                                                                                t4_5, np.tensordot(
                                                                                                                                                    t5_5, t5_4, ([1], [0])
                                                                                                                                                ), ([1], [0])
                                                                                                                                            ), ([1, 2], [2, 5])
                                                                                                                                        ), ([1, 2, 4], [4, 6, 2])
                                                                                                                                    ), ([1], [4])
                                                                                                                                ), ([1, 2], [2, 5])
                                                                                                                            ), ([1, 2, 4], [4, 5, 2])
                                                                                                                        ), ([0, 2, 4], [0, 2, 4])
                                                                                                                    ), ([0], [9])
                                                                                                                ), ([1, 2], [11, 2])
                                                                                                            ), ([1, 2, 4], [12, 4, 2])
                                                                                                        ), ([1, 2], [11, 2])
                                                                                                    ), ([1, 2, 4], [12, 3, 2])
                                                                                                ), ([1, 2], [8, 2])
                                                                                            ), ([1, 2, 4], [9, 3, 2])
                                                                                        ), ([1, 2], [10, 2])
                                                                                    ), ([1, 2, 4], [11, 3, 2])
                                                                                ), ([1, 2, 3], [11, 0, 2])
                                                                            ), ([0], [9])
                                                                        ), ([1, 2], [11, 2])
                                                                    ), ([1, 2, 4], [12, 4, 2])
                                                                ), ([1, 2], [11, 2])
                                                            ), ([1, 2, 4], [12, 3, 2])
                                                        ), ([1, 2], [11, 2])
                                                    ), ([1, 2, 4], [12, 3, 2])
                                                ), ([1, 2], [11, 2])
                                            ), ([1, 2, 4], [12, 3, 2])
                                        ), ([1, 2, 3], [11, 0, 2])
                                    ), ([1, 3, 5, 6, 7], [5, 6, 7, 8, 9])
                                ), ([1, 2], [7, 1])
                            ), ([1, 2, 4], [8, 3, 2])
                        ), ([0, 2, 3], [4, 1, 3])
                    ), ([1, 2], [5, 2])
                ), ([0, 2, 3, 5], [3, 1, 5, 0])
            ), ([0, 1, 2, 3], [1, 4, 3, 0])
        ), ([0, 1], [0, 1])
    )
