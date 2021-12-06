fishies = File.read('input.txt').split(',').map(&:to_i)

80.times do |day|
  puts "Day #{day}, #{fishies.size} fish"
  fishies.size.times do |i|
    if fishies[i] == 0 then
      fishies.push(8)
      fishies[i] = 6
    else
      fishies[i] -= 1
    end 
  end
end

puts "First part: after 80 days the number of lanternfish is #{fishies.size}"

(256 - 80).times do |day|
  puts "Day #{80 + day}, #{fishies.size} fish"
  fishies.size.times do |i|
    if fishies[i] == 0 then
      fishies.push(8)
      fishies[i] = 6
    else
      fishies[i] -= 1
    end 
  end
end

puts "Second part: after 256 days the number of lanternfish is #{fishies.size}"
