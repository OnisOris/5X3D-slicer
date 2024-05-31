from ThreeDTool.threeDTool import *
from ThreeDTool.display import Dspl
import matplotlib as mpl
mpl.use('Qt5Agg')
lox = generate_loxodromes(r=10)
logger.debug(lox[0][0])
dspl = Dspl(lox)
dspl.show()
