def remdup(l):
  L=[]
  for ips in l:
    if ips not in L:
      L.append(ips)
  return(L)


def sumsquare(l):
  odd_sum=0
  even_sum=0
  for ats in l:
    if ats%2!=0:
      odd_sum+=ats*ats
    else:
      even_sum+=ats*ats
  return([odd_sum,even_sum])


def transpose(m):
  ans=list()
  for ind in range(len(m[0])):
    a=[]
    for j in range(len(m)):
      a.append(m[j][ind])
    ans.append(a)
  return(ans)