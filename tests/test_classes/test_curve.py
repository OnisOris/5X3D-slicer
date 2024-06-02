from ThreeDTool import generate_loxodromes, Dspl
import matplotlib as mpl
mpl.use('Qt5Agg')
lox = generate_loxodromes(r=10, layer_height=1)
dspl = Dspl(lox)
dspl.show()
