input = File.readlines('input.txt').map { |l| l.chomp.split(' -> ')}.map { |coords| coords.map { |coord| coord.split(',').map(&:to_i) } } 

grid = Array.new(1000) { Array.new(1000) { 0 } }

class Array
  def diagonal?
    self[0][0] != self[1][0] && self[0][1] != self[1][1]
  end

  def vertical?
    self[0][0] == self[1][0]
  end

  def decreasing?
    self[0][0] > self[1][0] || self[0][1] > self[1][1]
  end
  
  def diagonal_downwards?
    self[0][1] < self[1][1]
  end

  def diagonal_rightwards?
    self[0][0] < self[1][0]
  end
end

def print_grid grid
  grid.each do |row|
    row.each do |cell|
      print cell > 0 ? cell : '.'
    end
    print "\n"
  end
end

input.reject(&:diagonal?).map{ |line| line.decreasing? ? line.reverse : line }.each do |line|
  if line.vertical?
    x = line[0][0]
    y_range = (line[0][1])..(line[1][1])

    y_range.each { |y| grid[y][x] += 1 }
  else
    x_range = (line[0][0])..(line[1][0])
    y = line[0][1]

    x_range.each { |x| grid[y][x] += 1 }
  end
end

puts "First part: there are #{grid.map { |row| row.count { |cell| cell >= 2 } }.sum} points where at least two vents overlap" 

input.select(&:diagonal?).each do |line|
  x_range = (line[0][0])..(line[1][0])
  y_range = (line[0][1])..(line[1][1])
  x_step = line.diagonal_rightwards? ? 1 : -1
  y_step = line.diagonal_downwards? ? 1 : -1

  coords = x_range.step(x_step).to_a.zip(y_range.step(y_step).to_a)

  coords.each { |coord| grid[coord[1]][coord[0]] += 1 }
end

puts "Second part: including diagonals, there are #{grid.map { |row| row.count { |cell| cell >= 2 } }.sum} points where at least two vents overlap" 
