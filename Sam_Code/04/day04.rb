input = File.readlines('input.txt').map(&:chomp).reject(&:empty?)

numbers_to_call = input[0].split(',').map(&:to_i).reverse
$called_numbers = []

bingo_cards = []
for i in 1..(input.size / 5) do
  bingo_card = []
  ((5*i-4)..(5*i)).each do |j|
    bingo_card.push(*(input[j].split(' ').map(&:to_i)))
  end
  bingo_cards << bingo_card
end

WINNING_LINES = (0..4).collect { |i| [((i * 5)..(i * 5 + 4)).to_a, (0..4).collect { |x| i + 5 * x} ] }.flatten(1)

class Array
  def winner?
    WINNING_LINES.any? do |line|
      line.all? { |i| $called_numbers.include? self[i] }
    end
  end

  def unmarked_numbers
    self.reject { |number| $called_numbers.include? number }
  end
end

until winning_card = bingo_cards.find(&:winner?)
  $called_numbers << numbers_to_call.pop
end

puts "First part: The winning card is #{winning_card}"
puts "The unmarked numbers are #{winning_card.unmarked_numbers}"
puts "The last called number was #{$called_numbers.last}"
puts "The score is #{winning_card.unmarked_numbers.sum * $called_numbers.last}"

numbers_to_call = input[0].split(',').map(&:to_i).reverse
$called_numbers = []

while bingo_cards.size > 1
  $called_numbers << numbers_to_call.pop
  bingo_cards.reject!(&:winner?)
end

last_card = bingo_cards.first
until last_card.winner?
  $called_numbers << numbers_to_call.pop
end

puts "Second part: The winning card is #{last_card}"
puts "The unmarked numbers are #{last_card.unmarked_numbers}"
puts "The last called number was #{$called_numbers.last}"
puts "The score is #{last_card.unmarked_numbers.sum * $called_numbers.last}"
