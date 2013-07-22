
using ArgParse
using MathProgBase
using CoinMP



function solve(data)
    capacity, values, weights = data
    println("capacity $capacity")
    println("values $values")
    println("weights $weights")

    f = Float64[3, 2, 3, 1, 2]
    A = [7. 2. 9. 3. 1.]
    types = fill(Integer, 5)
    capacity = 10.
    (z, x, flag) = mixintprog(-f, A, [], [capacity], [], ones(5), types; LogLevel=0)
    println("Solution status: $flag")
    println("Optimal value: $z")
    println("Solution vector: $x") # should be -7

end




function main()
    filename = ARGS[1]

    data = open(filename, "r") do f
        a = split(readline(f))
        numitems = int(a[1])
        capacity = int(a[2])
        values = Integer[]
        weights = Integer[]
        for line = readlines(f)
            a = split(line)
            push!(values, int(a[1]))
            push!(weights, int(a[2]))
        end

        (capacity, values, weights)
    end

    solve(data)
end
main()
