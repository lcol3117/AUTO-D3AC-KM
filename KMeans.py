import random as rnd, functools as ft, math as math
def getClusterCenters(data, n, dims):
  ccs = [ list(map(lambda _ : rnd.random(), range(dims))) for i in range(n) ]
  lastccs = [ list(map(lambda _ : rnd.random(), range(dims))) for i in range(n) ]
  while ccs != lastccs:
    lastccs = ccs[:]
    print("Got cluster centers now of {}. ".format(ccs.__repr__()))
    cclusters = seperateByDistance(data, ccs)
    print("Got cclusters now of {}. ".format(cclusters.__repr__()))
    for i in range(len(cclusters)):
      ccs[i] = avgPt(cclusters[i])
  return ccs
def avg(data):
  dsum = ft.reduce(
    lambda a,x : a + x,
    data,
    0
  )
  return dsum / len(data)
def avgPt(ptl):
  return list(map(lambda x : avg(x), zip(*ptl)))
def l2dist(p1, p2):
  dsum = ft.reduce(
    lambda a,x : a + ((x[0] - x[1]) ** 2),
    zip(p1, p2),
    0
  )
  return math.sqrt(dsum)
def seperateByDistance(data, ccs):
  print("Data: {}. ".format(data.__repr__()))
  print("CCs: {}. ".format(ccs.__repr__()))
  res = list(map(lambda _ : [], range(len(ccs))))
  for i in data:
    ccdists = list(map(lambda x : l2dist(x, i), ccs))
    mindistcc_i = ccdists.index(min(ccdists))
    res[mindistcc_i].append(i)
  print("Result: {}. ".format(res.__repr__()))
  return res