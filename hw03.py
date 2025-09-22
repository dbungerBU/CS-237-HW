# INPUT:
# Eight integer numbers, 0 <= X1, Y1, X2, T2, X3, Y3, X4, Y4 <= 10, such that:
# (X1, Y1) is the bottom-left coordinate of the first rectangle;
# (X2, Y2) is the top-right coordinate of the  first rectangle;
# (X3, Y3) is the bottom-left coordinate of the second rectangle;
# (X4, Y4) is the top-right coordinate of the second rectangle;

# OUTPUT
# The probability of hitting the intersection area if a dart is thrown randomly within the 10x10 region.
# Your answer should be expressed as float number within the interval [0.0,1.0]
def answer(x1,y1,x2,y2,x3,y3,x4,y4):
    if not((x1<=x3<=x2 or x3<=x1<=x4) and (y1<=y3<=y2 or y3<=y1<=y4)):
        return 0.0
    xsorted = sorted([x1,x2,x3,x4])
    ysorted = sorted([y1,y2,y3,y4])
    w = xsorted[2]-xsorted[1]
    h = ysorted[2]-ysorted[1]
    probability = (w*h)/100
    return probability

