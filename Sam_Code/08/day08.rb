input = File.readlines('input.txt').map { |line| line.chomp.split(' | ').map(&:split) }

print 'First part: '
puts input.map(&:last).flatten.count { |output| [2, 4, 3, 7].include? output.size }

print 'Second part: '

class String
  def includes_all_from? substr
    substr.chars.all? { |c| self.chars.include? c }
  end
end

class Array

  def decode
    patterns, output = *self
    patterns.map! { |pattern| pattern.chars.sort.join }
    output.map! { |out| out.chars.sort.join }

    mappings = []

    # Find which two wires make up the '1' pattern
    mappings[1] = patterns.detect { |pattern| pattern.size == 2 }

    # Find which three wires make up the '7' pattern
    mappings[7] = patterns.detect { |pattern| pattern.size == 3 }

    # and which four make up the '4'
    mappings[4] = patterns.detect { |pattern| pattern.size == 4 }

    # and which seven make up the '8'
    mappings[8] = patterns.detect { |pattern| pattern.size == 7 }

    patterns.delete_if { |pattern| mappings.include? pattern }

    # Find the '9' by looking for the 6-wire long pattern which has wire signals in both the '4' and '7' pattern
    mappings[9] = patterns.detect { |pattern| pattern.size == 6 && pattern.includes_all_from?(mappings[4]) && pattern.includes_all_from?(mappings[7]) }
    patterns.delete mappings[9]

    # Find the '0' by looking for the 6-wire long pattern which hasn't been identified and has wire signals in the '7' pattern
    mappings[0] = patterns.detect { |pattern| pattern.size == 6 && pattern.includes_all_from?(mappings[7]) }
    patterns.delete mappings[0]

    # The remaining 6-wire long pattern is the '6' pattern
    mappings[6] = patterns.detect { |pattern| pattern.size == 6 }
    patterns.delete mappings[6]

    # Find the '3' by looking for the pattern that has wire signals in the '1' pattern
    mappings[3] = patterns.detect { |pattern| pattern.includes_all_from? mappings[1] }
    patterns.delete mappings[3]

    # Find the '5' by looking for the pattern that has wire signals in '4', excluding those found in '1'
    four_excluding_one = (mappings[4].chars - mappings[1].chars).join
    mappings[5] = patterns.detect { |pattern| pattern.includes_all_from? four_excluding_one }
    patterns.delete mappings[5]

    # The last remaining pattern is the '2'
    mappings[2] = patterns.first

    output.map { |digit| mappings.find_index digit }.join.to_i
  end
end

puts input.map(&:decode).sum
