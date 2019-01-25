#!/usr/bin/python3.4
# -*-coding:Utf-8 -

class Personne :

	def __init__(self, nom):
		self.nom = nom
		self.prenom = "Pierre"
	def __str__(self):
		return "{} {}".format(self.prenom, self.nom)

class AgentSpe(Personne):
	def __init__(self, nom, matricule):
		Personne.__init__(self, nom)
		self.matricule = matricule
	def __str__(self):
		return "{} {} {}".format(self.prenom, self.nom, self.matricule)

agent = AgentSpe("Fischer", "007")
print(agent.nom)
print(agent)
print(agent.prenom)
print(issubclass(Personne, object))
print(issubclass(AgentSpe, object))
print(isinstance(AgentSpe, object))
print(isinstance(agent, Personne))

