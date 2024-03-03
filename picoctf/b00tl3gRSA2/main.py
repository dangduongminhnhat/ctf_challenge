from attack import hack_RSA
from Crypto.Util.number import long_to_bytes

c = 73847449663356654578789188036594591581461097862078063964007152477111557262044280490576562872211238449026640163135994586117893340479542016096450349396233593454988402165888715602587042900685719336497806397169602769807905386643919863737899515429866408206518522275546444779885332020028220013441135892192337034129
n = 128244086591779323342889828443479203619686762942434307666492851439191407650607571982624986244223669330214386377124224839771732782211267727194376351784138082109700203957357622347690796493795145846093423988072176970865924591688333515560995832024231762845215136256393997407145407988792654809211093374003696592731
e = 107456791905350714284319575799093900965431418896513993182443328866621251502593408423544997400175451692927549529477999951954238582821147687125623433814092152332714857466869368116710137849576085732486687153068256124137233902394852139821999527888539666274045596262371418378998639653959034311399768254251397072673

d = hack_RSA(e, n)
print(long_to_bytes(pow(c, d, n)))