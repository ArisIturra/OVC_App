from datetime import *
from time import gmtime, strftime
from statistics.models import *

class Report :

	def all(self):
		try:
                        year,month = strftime("%Y-%m", gmtime()).split('-')
                except:
                        pass

                data = {}
                for s in Station.objects.all():
			evs = []
                        for c in Choice.objects.all():
                                if not data.has_key(s.name):
                                        data[s.name] = []
				evs.append( len(Evaluation.objects.filter(
                                                        date__year=year,
                                                        date__month=month,
                                                        choice=c,
                                                        station=s
                                                        )))
			data[s.name].append(evs)
			evs = []
                        for c in Choice.objects.all():
				evs.append( len(Evaluation.objects.filter(
                                                        date__year=year,
                                                        choice=c,
                                                        station=s
                                                        )))
			data[s.name].append(evs)
 
			evs = []
                        for c in Choice.objects.all():
				evs.append( len(Evaluation.objects.filter(
                                                        choice=c,
                                                        station=s
                                                        )))
			data[s.name].append(evs)
		res = {}
		choices = Choice.objects.all() 
		for d in data:
			res[d] = []
			for evs in data[d]:
				t_evs = 0
				counter = 0
				sum = 0
				for e in evs:
					t_evs += e
					sum += e * choices[counter].weight	
					counter += 1
				try:
					sum /= t_evs
				except:
					sum = 0

				res[d].append(sum)		
		return res
	
	def by_month(self,date=None):
		if date==None:
			date = strftime("%Y-%m", gmtime())
		try:
			year,month = date.split('-')
		except:
			pass

		data = {}
		for s in Station.objects.all():
			for c in Choice.objects.all():
				if not data.has_key(s.name):
					data[s.name] = {}
				data[s.name][c.name] = len(Evaluation.objects.filter(
							date__year=year,
							date__month=month,
							choice=c,
							station=s
							)
						)
		res = {}
		for d in data:
			t_evs = 0
			res[d] = 0
			for v in data[d]:
				t_evs += data[d][v]
				res[d] += data[d][v] * Choice.objects.filter(name=v)[0].weight
			try:
				res[d] /= t_evs	
			except:
				res[d] = 0
		return res
					
