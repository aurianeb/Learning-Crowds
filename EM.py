#Binary class
def sigma(z):
	return 1/(1+exp(-z))

#Likelihood
def probability(data,w,y,alpha,beta) :
	N = data.shape
	R = y.shape[1] # ou 0 selon le cas
	prod = 1
	for i in range(1,N):
		p = sigma((w.T).dot(x[i]))
		proda = 1
		for j in range(1,R):
			proda = proda*alpha[j]^(y[i][j])*(1-alpha[j])^(1-y[i][j])
		prodb = 1
		for j in range(1,R):
			prodb = prodb*beta[j]^(y[i][j])*(1-beta[j])^(1-y[i][j])
		prod = prod * (proda*p+prodb*(1-p))
	return prod

#Initialisation

def init_mu(y):
	mu = []
	N = y.shape[0]
	R = y.shape[1]
	for i in range(1,N):
		mu.append(np.sum(y[i])/R)
	return mu

#E-step

def a(alpha,y):
	a = []
	N = y.shape[0]
	R = y.shape[1]
	for i in range(1,N):
		proda = 1
		for j in range(1,R):
			proda = proda*alpha[j]^(y[i][j])*(1-alpha[j])^(1-y[i][j])
		a.append(proda)
	return proda

def b(beta,y):
	b = []
	N = y.shape[0]
	R = y.shape[1]
	for i in range(1,N):
		prodb = 1
		for j in range(1,R):
			prodb = prodb*beta[j]^(y[i][j])*(1-beta[j])^(1-y[i][j])
		b.append(prodb)
	return b

def mu(a,b,N):
	mu = []
	for i in range(1,N):
		mu.append(a[i]*p[i]/(a[i]*p[i]+b[i]*(1-p[i])))
	return mu

def E_step(data,alpha,beta):
	CE = 0 #Conditionnal excepectation
	N = data.shape
	a = a(alpha,y)
	b = b(beta,y)
	mu = mu(a,b,N)
	for i in range(1,N):
		CE += mu[i]*ln(p[i])*a[i]+(1-mu[i])*ln(1-p[i])*b[i]
	return CE

#M-step

def alpha(mu,y):
	alpha = []
	N = y.shape[0]
	R = y.shape[1]
	for j in range(1,R):
		tmp1 = 0
		tmp2 = 0
		for i in range(1,N):
			tmp1 += mu[i]*y[i][j]
			tmp2 += mu[i]
		alpha.append(tmp1/tmp2)
	return alpha

def beta(mu,y):
	beta = []
	N = y.shape[0]
	R = y.shape[1]
	for j in range(1,R):
		tmp1 = 0
		tmp2 = 0
		for i in range(1,N):
			tmp1 += (1-mu[i])*(1-y[i][j])
			tmp2 += 1-mu[i]
		beta.append(tmp1/tmp2)
	return beta

