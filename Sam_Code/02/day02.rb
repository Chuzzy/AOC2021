input = File.readlines('input.txt').map { |l| l.chomp.split(' ') }

horizontal_pos = input.filter { |command| command[0] == 'forward' }.reduce(0) { |sum, command| sum + command[1].to_i }
depth = input.filter { |command| command[0] != 'forward' }.map { |command| command[0] == 'up' ? -(command[1].to_i) : command[1].to_i }.sum

puts "Part 1: Horizontal pos #{horizontal_pos}, depth #{depth}, product #{horizontal_pos * depth}"

aim = 0
depth = 0
input.each do |command|
  case command[0]
  when 'forward'
    depth += aim * command[1].to_i
  when 'up'
    aim -= command[1].to_i
  else
    aim += command[1].to_i
  end
end

puts "Part 2: Horizontal pos #{horizontal_pos}, depth #{depth}, product #{horizontal_pos * depth}"
