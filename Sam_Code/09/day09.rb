input = File.readlines('input.txt').map { |line| line.chomp.chars.map(&:to_i) }

risk_level_total = 0

input.size.times do |y|
  input[y].size.times do |x|
    point = input[y][x]
    if (y == 0 || input[y - 1][x] > point) && (y == input.size - 1 || input[y + 1][x] > point) &&
      (x == 0 || input[y][x - 1] > point) && (x == input[y].size - 1 || input[y][x + 1] > point)
      risk_level_total += point + 1
    end
  end
end

puts "First part: #{risk_level_total}"
