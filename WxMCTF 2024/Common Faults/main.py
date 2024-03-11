from gmpy2 import gcd
from Crypto.Util.number import long_to_bytes, inverse
n = 19290563578327453949336521542006226917305579089238611319340418865328530239156980001148287094794597245123342342649855430461737481257157770687174830619431639754196595918514001386358652631605986698185365603862366462464354475435147445345755769464304858043419123264809730783029021355227182841798894442177927483078138507520231852246431337982584453172947670828725583176749755687698515274495507626279949858815116849415334900660204540013242983358025753756615290790683594556065352249470422727993888306130121329010803896204476837596104298196365868904948872583257714213914727558162469953472832667212915079478881070361647287015227
e = 65537
c = 18651644693683054500673994100601459545925853716962588421795414933698538684984482916159946002793177633717078905622925228071773514366713805302237236714442930364546559314843428959267114429105532705487024783842788301859773264126504840457220646595816221419555235469896275131927965495584860587878045966243673199696688948322690985185539666907621802019743685283044241203593017376586867315108177287787350717174687351233595394833663147023752431508036796976955242838752921981607946587816363632082619157176008888168613496313967922129619654124493807707014504868657108592724853408470318017578423378680540301597591896080826893418241

file = open("CTF_Challenge/WxMCTF 2024/Common Faults/past_keys", "r")

arr = []
data = file.readline()
while data:
    if len(data) > 1:
        arr.append(int(data))
    data = file.readline()

for i in arr:
    p = gcd(n, i)
    if p > 1:
        q = n // p
        assert n == p * q
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
        print(long_to_bytes(pow(c, d, n)))
        break
