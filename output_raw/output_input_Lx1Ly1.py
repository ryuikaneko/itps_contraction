def Contract_scalar_1x1(\
    t0_2,t1_2,t2_2,\
    t0_1,t1_1,t2_1,\
    t0_0,t1_0,t2_0,\
    o1_1\
    ):
    ##############################
    # ./input/input_Lx1Ly1.dat
    ##############################
    # (o1_1*(t1_1.conj()*((t2_1*(t2_0*t1_0))*(t1_1*((t0_0*t0_1)*(t0_2*(t2_2*t1_2)))))))
    # cpu_cost= 6.04e+10  memory= 4.0004e+08
    # final_bond_order ()
    ##############################
    return np.tensordot(
        o1_1, np.tensordot(
            t1_1.conj(), np.tensordot(
                np.tensordot(
                    t2_1, np.tensordot(
                        t2_0, t1_0, ([1], [0])
                    ), ([1], [0])
                ), np.tensordot(
                    t1_1, np.tensordot(
                        np.tensordot(
                            t0_0, t0_1, ([1], [0])
                        ), np.tensordot(
                            t0_2, np.tensordot(
                                t2_2, t1_2, ([0], [1])
                            ), ([1], [1])
                        ), ([1], [0])
                    ), ([0, 1], [1, 4])
                ), ([0, 1, 3, 4], [5, 0, 3, 1])
            ), ([0, 1, 2, 3], [3, 4, 0, 1])
        ), ([0, 1], [1, 0])
    )
