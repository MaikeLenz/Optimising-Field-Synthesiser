function quad(x)
    y = x^2 + 1000
    return y
end

function Booth(x,y)
    z = (x+2y-7)^2 + (2x+y-5)^2
    return z
end


function two(x)
    #return 10
    return x["key"]
end

function dictionary(d)
    return "apres"
end


#x = range(-10, 10, length=101)
#println(x)
#y = range(-10, 10, length=101)
#println(y)
#p = surface(x,y, Booth)

#display(p)
#readline()