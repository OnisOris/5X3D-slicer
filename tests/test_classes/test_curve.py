from curve import Curve
from threeDTool import *
from display import Dspl

lox = generate_loxodromes(r=10)

logger.debug(lox[0][0])

dspl = Dspl(lox)
dspl.show()