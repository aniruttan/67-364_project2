from datetime import datetime 
def convert(x):
	months={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
	d,m,y=x.split('-')
	m=months[m]
	date = datetime(year=int(y),month=m,day=int(d))
	return date


print(convert("13-Apr-17"))