def projPontoCircunferencia(x, y, c1, c2, r):
 
  point = np.array([x, y])
  center = np.array([c1, c2])

  diff = point - center

  d = np.linalg.norm(diff)

  if d == 0:
      proj = center + np.array([r, 0])
  else:
      proj = center + r * diff / d

  return proj