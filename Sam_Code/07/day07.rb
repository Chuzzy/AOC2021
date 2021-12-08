input = File.read('input.txt').split(',').map(&:to_i)

lo, hi = input.min, input.max
best_target, best_fuel = 0, 1/0.0

(lo..hi).each do |target|
  fuel_used = 0
  input.each do |crab_position|
    fuel_used += (crab_position - target).abs
  end
  if fuel_used < best_fuel
    best_target = target
    best_fuel = fuel_used
  end
end

puts "First part: best target is #{best_target} using #{best_fuel} fuel"

best_fuel = 1/0.0

(lo..hi).each do |target|
  fuel_used = 0
  input.each do |crab_position|
    delta = (crab_position - target).abs
    fuel_used += (delta ** 2 + delta) / 2
  end
  if fuel_used < best_fuel
    best_target = target
    best_fuel = fuel_used
  end
end

puts "Second part: best target is #{best_target} using #{best_fuel} fuel"
