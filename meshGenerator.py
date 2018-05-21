import matplotlib.pyplot as plt;
import numpy as np;
import numpy.linalg as linalg;
import math;

def simpleSquare():
	xs = [0,1,2,2,2,1,0,0,1];
	ys = [0,0,0,1,2,2,2,1,1];
	
	bs = [True, True, True, True, True, True, True, True, False];
	
	triangles = [(0,1,8),(0,7,8),(1,2,8),(2,3,8),(3,4,8),(4,5,8),(5,6,8),(6,7,8)];
	
	return (xs, ys, bs, triangles);

def square(nx, ny):
	xs = [];
	ys = [];
	bs = [];
	
	dx = 1.0/nx;
	dy = 1.0/ny;
	
	indices = {};
	currentindex = 0;
	
	for j in range(0, ny + 1):
		for i in range(0, nx + 1):
			xs += [dx*i];
			ys += [dy*j];
			bs += [(i == 0 or i == nx or j == 0 or j == ny)];
			indices[(i,j)] = currentindex;
			currentindex += 1;
	
	triangles = [];
	
	for j in range(0, ny):
		for i in range(0, nx):
			ind11 = indices[(i,j)];
			ind12 = indices[(i + 1, j)];
			ind13 = indices[(i, j + 1)];
			triangles += [(ind11, ind12, ind13)];
			ind21 = indices[(i + 1, j)];
			ind22 = indices[(i, j + 1)];
			ind23 = indices[(i + 1, j + 1)];
			triangles += [(ind21, ind23, ind22)];
	
	return (xs, ys, bs, triangles);
	
def scale(xs, ys, s):
	nxs = [];
	nys = [];
	for i in range(0, len(xs)):
		nxs += [s*xs[i]];
		nys += [s*ys[i]];
	return(nxs, nys);

def transform(xs, ys, t):
	nxs = [];
	nys = [];
	for i in range(0, len(xs)):
		(nx, ny) = t(xs[i], ys[i]); 
		nxs += [nx];
		nys += [ny];
	return(nxs, nys);