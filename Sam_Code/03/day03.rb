input = File.readlines('input.txt').map { |l| l.chomp }

totals = [0] * input[0].size

input.each do |binary|
  binary.each_char.with_index { |bit, i| totals[i] += 1 if bit == '1' }
end

gamma = totals.map { |count| count > input.size / 2 ? 1 : 0}.join.to_i(2)
epislon = totals.map { |count| count < input.size / 2 ? 1 : 0 }.join.to_i(2)

puts "First part: gamma is #{gamma}, epislon is #{epislon}, power consumption is #{gamma * epislon}"

candidates = input.clone
input.size.times do |i|
  ones_count = candidates.count { |binary| binary[i] == '1' }
  preferred_bit = ones_count >= candidates.size / 2.0 ? '1' : '0'
  candidates.delete_if { |binary| binary[i] != preferred_bit }
  break if candidates.size == 1
end
oxygen = candidates.first.to_i(2)

candidates = input.clone
input.size.times do |i|
  ones_count = candidates.count { |binary| binary[i] == '1' }
  preferred_bit = ones_count >= candidates.size / 2.0 ? '0' : '1'
  candidates.delete_if { |binary| binary[i] != preferred_bit }
  break if candidates.size == 1
end
co2 = candidates.first.to_i(2)

puts "Second part: oxygen is #{oxygen}, co2 is #{co2}, life support rating is #{oxygen * co2}"
