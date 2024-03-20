import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3,8,1,10])
ypoints = np.array([2,7,4,3])

plt.plot(xpoints,ypoints,marker='o')
plt.show()

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline