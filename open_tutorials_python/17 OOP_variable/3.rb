class Cal
  def initialize(v1, v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
  def setV2(v)
    if v.is_a?(Integer)
      @v2 = v
    end
  end
  def getV2()
    return @v2
  end
end

c1 = Cal.new(10,10)
p c1.add()
p c1.subtract()

c1.setV1(20)
p c1.add()
p c1.getV1()

c1.setV2('30')
p c1.add()
p c1. getV2()

c1.setV2(30)
p c1.add()
p c1.getV2()
