import io
import csv

def read_csv(filename):
	with io.open(filename,encoding='utf-8-sig') as f:
  		reader=csv.reader(f)
		return list(reader)


if __name__=="__main__":
	data=read_csv('./data.csv')
	print(data)
