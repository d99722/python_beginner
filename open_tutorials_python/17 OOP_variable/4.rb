class C
  attr_accessor:value
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
end

c1 = C.new(10)
# p c1.value
p c1.value
c1.value = 20
p c1.value
