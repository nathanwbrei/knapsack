
import pytest
import solver


def is_correct(data, result):
    capacity, values, weights = solver.process(data)

    taken = [int(x) for x in results.split()[2:]]
    value = sum(v*t for (v,t) in zip(values, taken))

    reported_value = int(results.split()[0])

    actual_value  = sum(v*t for (v,t) in zip(values, taken))
    actual_weight = sum(w*t for (w,t) in zip(weights, taken))

    assert actual_weight<capacity
    assert actual_value == reported_value 

    return actual_value == reported_value



datasets = [{"f":"data/ks_4_0", "r":18}]


def test_given():
    for d in datasets:
        data = solver.getdata(d["f"])
        print "Data"
        print "-"*25
        print data
        result = solver.solveIt(data).split()
        print "Result"
        print "-"*25
        print result

        assert int(result[0]) >= d["r"]


def test_manual():
    data = "4 7\n16 2\n19 3\n23 4\n28 5\n"
    result = solver.solveIt(data)
    assert result == "44 0\n1 0 0 1"

