from pyqubo import Binary
from dynex import BQM, DynexSampler, DynexConfig


def sample_opposite_layer_pyqubo(v, layer, weights, opposite_layer,
                                 qpu=False, chain_strength=2, num_reads=1):
    # initialize Hamiltonian
    H = 0
    H_vars = []

    # print("opposite_layer:",opposite_layer)

    # initialize all variables (one for each node in the opposite layer)
    for j in range(len(opposite_layer)):
        H_vars.append(Binary("DNX" + str(j)))

    for i, bias in enumerate(layer):
        # filter only chosen nodes in the first layer
        if not v[i]:
            continue

        # add reward to every connection
        for j, opp_bias in enumerate(opposite_layer):
            H += -1 * weights[i][j] * H_vars[j]

    for j, opp_bias in enumerate(opposite_layer):
        H += -1 * opp_bias * H_vars[j]

    model = H.compile()
    # print(model)
    bqm = model.to_bqm()

    if not bqm.variables:
        return [0] * len(opposite_layer)

    config = DynexConfig(compute_backend="cpu")
    dnxmodel = BQM(bqm, config=config)
    dnxsampler = DynexSampler(dnxmodel, logging=False, description="QRBM", config=config)
    sampleset = dnxsampler.sample(num_reads=4096, annealing_time=1000)

    if sampleset is None or len(sampleset) == 0:
        return [0] * len(opposite_layer)

    solution1 = sampleset.first.sample
    solution1_list = [(k[3:], v) for k, v in solution1.items()]
    solution1_list.sort(key=lambda tup: int(tup[0]))
    return [v for (k, v) in solution1_list]


def sample_v(layer, qpu=False, chain_strength=10, num_reads=1):
    H = 0

    for i, bias in enumerate(layer):
        H += -1 * bias * Binary("DNX" + str(i))

    model = H.compile()
    bqm = model.to_bqm()

    if not bqm.variables:
        return [0] * len(layer)

    config = DynexConfig(compute_backend="cpu")
    dnxmodel = BQM(bqm, config=config)
    dnxsampler = DynexSampler(dnxmodel, logging=False, description="QRBM", config=config)
    sampleset = dnxsampler.sample(num_reads=4096, annealing_time=1000)

    if sampleset is None or len(sampleset) == 0:
        return [0] * len(layer)

    solution1 = sampleset.first.sample
    solution1_list = [(k, v) for k, v in solution1.items()]
    solution1_list.sort(key=lambda tup: int(tup[0]))
    return [v for (k, v) in solution1_list]


if __name__ == "__main__":
    v = [0, 1, 0]
    layer = [1, 1, 1]
    weights = [[2, -2], [-4, 4], [2, -2]]
    opp_layer = [2, 1]

    sampleset = sample_opposite_layer_pyqubo(v, layer, weights, opp_layer,
                                             qpu=True)
    sampleset2 = sample_v(layer, qpu=True)
    print(sampleset)
    print(sampleset2)

    # using the best (lowest energy) sample
    solution1 = sampleset.first.sample
    print(solution1)
    solution1_list = [(k, v) for k, v in solution1.items()]
    solution1_list.sort(key=lambda tup: int(tup[0]))  # sorts in place
    solution1_list_final = [v for (k, v) in solution1_list]
