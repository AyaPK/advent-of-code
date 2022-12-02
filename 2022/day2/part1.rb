def read_file(path)
  file = File.new(path, 'r')
  if file
    data = file.read.to_s
  else
    puts 'Not able to access the file'
  end
end

d = read_file('day1/input.txt').split("\n\n")
elves = d.map { |elf| elf = elf.split("\n").map(&:to_i)
 elf.sum }
elves = elves.sort

puts elves.max
puts elves.slice(elves.length-3,elves.length+1).sum
