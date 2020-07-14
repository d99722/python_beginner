# -*-coding:utf-8-*-

#공급가 10000 (n)
#소비자지불 11000 (1.1n)
#VAT 1000 (0.1n)
#expense 3000 (0.3n)
#income 7000 (0.7n)
# A : income * 0.5
# B : income * 0.3
# C : income * 0.2

class Cal:
    sum_gg=0
    sum_buyer=0
    sum_VAT=0
    sum_exp=0
    sum_inc=0
    sum_incA=0
    sum_incB=0
    sum_incC=0
    def __init__(self,v1):
        self.v1=v1
    def _gg(self):
        Cal.result_gg = self.v1
        Cal.sum_gg = Cal.result_gg + Cal.sum_gg
        return Cal.result_gg
    def _buyer(self):
        Cal.result_buyer = self.v1*1.1
        Cal.sum_buyer = Cal.sum_buyer + Cal.result_buyer
        return Cal.result_buyer
    def _VAT(self):
        Cal.result_VAT = self.v1*0.1
        Cal.sum_VAT = Cal.sum_VAT + Cal.result_VAT
        return Cal.result_VAT
    def _exp(self):
        Cal.result_exp = self.v1*0.3
        Cal.sum_exp = Cal.sum_exp + Cal.result_exp
        return Cal.result_exp
    def _inc(self):
        Cal.result_inc=self.v1*0.7
        Cal.sum_inc = Cal.sum_inc + Cal.result_inc
        return Cal.result_inc
    def _incA(self):
        Cal.result_incA=Cal.result_inc*0.5
        Cal.sum_incA=Cal.sum_incA+Cal.result_incA
        return Cal.result_incA
    def _incB(self):
        Cal.result_incB=Cal.result_inc*0.3
        Cal.sum_incB=Cal.sum_incB+Cal.result_incB
        return Cal.result_incB
    def _incC(self):
        Cal.result_incC=Cal.result_inc*0.2
        Cal.sum_incC=Cal.sum_incC+Cal.result_incC
        return Cal.result_incC
    @classmethod
    def _total(cls):
        print('\n총 공 급 가 : %d원'% (Cal.sum_gg))
        print('총 소비자 구매가 : %d원'% (Cal.sum_buyer))
        print('총 부가 가치세 : %d원'% (Cal.sum_VAT))
        print('총 비용 : %d원'% (Cal.sum_exp))
        print('총 총이익 : %d원'% (Cal.sum_inc))
        print('총 분배/A : %d원'% (Cal.sum_incA))
        print('총 분배/B : %d원'% (Cal.sum_incB))
        print('총 분배/C : %d원\n'% (Cal.sum_incC))


exit_c='1'
while exit_c=='1':
    v1 = input("\n공급가를 입력하세요 (원)\n")
    v1 = int(v1)

    p=Cal(v1)

    print('\n공 급 가 : %d원'% (p._gg()))
    print('소비자 구매가 : %d원'% (p._buyer()))
    print('부가 가치세 : %d원'% (p._VAT()))
    print('비용 : %d원'% (p._exp()))
    print('총이익 : %d원'% (p._inc()))
    print('분배/A : %d원'% (p._incA()))
    print('분배/B : %d원'% (p._incB()))
    print('분배/C : %d원\n'% (p._incC()))

    exit_c = input('계속 하시겠습니까?\nresult = 0, yes = 1, no = *\n')
    if exit_c == '0':
        Cal._total()
        exit_c = input('계속 하시겠습니까?\nyes = 1, no = *\n')
