from Crypto.Util.number import isPrime, inverse, long_to_bytes

N = 894011376132861406416081994144221048298348543110763436400156707035479762291337096368301340210777912166253392435275663746074998964323198306974285233167719096055553347615918699581765041856450618725024365550285245909593290693757548300976025136185960841538482656726074757217987326418213368306947431668797511869941369363510575799319146232381645606378509284692783439527001482275434870365007864755014763434476875230779298152747668036103797086099448952638933614839186234115539057353208089196503236476069765055958643599622359809306429773621018079928117609961649006558217734057147235098517323614637509521563090769478823258676357262436290835475545437211168106617010859479612214627871047960151415095910992231687737019157788664429412462674876326653667300420128914036327499885103193423178025962079282185227746880809451234195481664650147610375976243181422075319601793906090392759832052648670731266344219250793991957964535801285606036631861341696305110038590888086491568683507575846576623827059055577036404611548224528600604898405714747157240730264673180051312634408192644777331633111950232485559076080686217541095754245034143596485147084607615402187454830802772582891800608645679493263524678084504132604846410243911260803002065871918398725293311473
e = 49999
c = 127990258916322713210704002931365496210647826869578493680557063836772515914303363145985391647430839311330158084206710072455465957218072448099969815961814463831667357474852426061475210363277306704257877402661232669936031043625938011115290529377505573367883714424182150449678726041360949463375982144652910707759221795772350872426009873120527309342093683340576731241704191541296890578962805029558926492259701366885936092059693759354255247540815813052543086204934376066884066060405947003334121725632674642690548675916126384013014552545338699198239765357561083183401525044638243204528501965028598782513999767237563252331767079569128151380305983732341553403814650118788711703476805307790685184506737890913441497269132749881622937761764492015610811577966553776703680435092016590690563200951474073620866158140866931856293211794418637441400021472249887178225738960768608549559781531479910409684884180658879621882231073123533851227894797415625533435081416099549459198508358607887551022339960981663266529984544362524495679204397590064106335341279871204905873532415276380340515150499389237587052633736125460704219829657692767592459700685070039056607335118481257774532132073976558433243315868939654221066341581052013795470559435542389710686098062

phi = N - 1
d = inverse(e, phi)
pt = pow(c, d, N)
print(long_to_bytes(pt))
