f= File.open("input.txt")
data = f.readlines.map(&:chomp)
f.close

data.each do |x|
  data.each do |y|
    data.each do |z|
      if x.to_i != y.to_i and y.to_i != z.to_i and (x.to_i + y.to_i + z.to_i) == 2020
        puts (x.to_i * y.to_i * z.to_i)
        exit
      end
    end
  end
end


