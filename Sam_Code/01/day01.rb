input = File.readlines('input.txt').map{ |n| n.chomp.to_i }

print "First part: "
p input.each_cons(2).count{ |pair| pair[1] > pair[0] }

print "Second part: "
p input.each_cons(3).each_cons(2).count{ |pair| pair[1].sum > pair[0].sum }