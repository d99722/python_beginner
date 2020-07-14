arr = [1, 3, 56, 7, 345, 61, 1234]
arr.delete_if() do |item|
  item > 7
end
puts arr
