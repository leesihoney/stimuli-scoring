import psycopg2 as pg2
import os
from pathlib import Path

import random
# Establish a connection by specifying the database and user
# This is the psycopg2 analog to
#   %  psql -d postgres -U isdb

con = pg2.connect(database='score', user='isdb')  

con.autocommit = True

# SQL statements are executed via a cursor object
cur = con.cursor()

# reading by file by file
def readFile(filename):
	fo = open(filename, "r+")
	personName = filename[fo.name.find("/")+1:fo.name.find("_old.txt")]
	print("Getting %s's scoring comparison data...." % (personName,))
	result = fo.read()
	resultArray = result.splitlines()
	resultFile = open("%s_old_score_comparison.txt" % (personName),"w")
	resultFile.write("%s Score Result \n\n" % (personName))
	# debug test
	totalCount = 0
	matchCount = 0
	generated_list = []
	for dataLine in resultArray:
		if dataLine != ",,,,,,,,,,,,,,,,,":
			line= dataLine.split(",")
			# looking at the line
			donationType = int(line[0])
			sizeA=calcOrgSize(int(line[1]),donationType, personName)
			accessA=calcFoodAccess(int(line[2]),donationType,personName)
			incomeA=calcIncomeLevel(int(line[3]),donationType, personName)
			povertyA=calcPovertyLevel(int(line[4]),donationType, personName)
			last_donationA=calcLastDonation(int(line[5]),donationType, personName)
			total_donationA=calcTotalDonation(int(line[6]),donationType, personName)
			distanceA=calcTravelTime(int(line[7]),donationType, personName)

			sizeB=calcOrgSize(int(line[8]),donationType, personName)
			accessB = calcFoodAccess(int(line[9]),donationType, personName)
			incomeB = calcIncomeLevel(int(line[10]),donationType, personName)
			povertyB = calcPovertyLevel(int(line[11]),donationType, personName)
			last_donationB= calcLastDonation(int(line[12]),donationType, personName)
			total_donationB= calcTotalDonation(int(line[13]),donationType, personName)
			distanceB = calcTravelTime(int(line[14]),donationType,personName)

			if None in [sizeA, accessA, incomeA, povertyA, last_donationA, total_donationA, distanceA,
						sizeB, accessB, incomeB, povertyB, last_donationB, total_donationB, distanceB]:
				
				continue
			else:
				sumA = sizeA + accessA + incomeA + povertyA + last_donationA + total_donationA + distanceA
				sumB = sizeB + accessB + incomeB + povertyB + last_donationB + total_donationB + distanceB

				question_num = int(line[15])
				choice = line[16]

				algoChoice = getAlgoChoice(sumA, sumB)

				resultFile.write("%d. \n" %(question_num))
				resultFile.write("Recipient A: \n")
				resultFile.write("Organization Size(%d) + Food Access(%d) + Income Level(%d) + Poverty Rate(%d) + Last Donation Received(%d) + Total Donation Received(%d) + Travel Time(%d) = %d \n" % (sizeA, accessA, incomeA, povertyA, last_donationA, total_donationA, distanceA, sumA))
				resultFile.write("Recipient B: \n")
				resultFile.write("Organization Size(%d) + Food Access(%d) + Income Level(%d) + Poverty Rate(%d) + Last Donation Received(%d) + Total Donation Received(%d) + Travel Time(%d) = %d \n" % (sizeB, accessB, incomeB, povertyB, last_donationB, total_donationB, distanceB, sumB))

				resultFile.write("\nAlgorithm's Choice: %s" % (algoChoice))
				resultFile.write("\nOriginal Choice: %s" % choice)
				resultFile.write("\nMatch? %s\n\n" % str(algoChoice==choice))

				if algoChoice == choice:
					matchCount+=1
				totalCount+=1 

	resultFile.write("%d/%d testings have shown matched\n" % (matchCount,totalCount))

	if totalCount != 0:
		percentage = (matchCount/totalCount) * 100
		resultFile.write("Total Percentage of Match: %0.1f \n" % (percentage,))
		resultFile.write("\nFuture predictions \n")

		# 10 random generated values with scores indicated
		while(len(generated_list)<10):
			pos_foodType = random.randint(0,1)
			pos_sizeA = random.randint(0,4)
			pos_accessA = random.randint(0,2)
			pos_incomeA = random.randint(0,5)
			pos_povertyA = random.randint(0,6)
			pos_last_donationA = random.randint(0,13)
			pos_total_donationA = random.randint(0,90)
			pos_distanceA = random.randint(0,3)

			pos_sizeB = random.randint(0,4)
			pos_accessB = random.randint(0,2)
			pos_incomeB = random.randint(0,5)
			pos_povertyB = random.randint(0,6)
			pos_last_donationB = random.randint(0,13)
			pos_total_donationB = random.randint(0,90)
			pos_distanceB = random.randint(0,3)

			# generation combos 

			if pos_last_donationA == 13:
				pos_total_donationA = 0
			elif pos_last_donationB == 12:
				pos_total_donationA = random.randint(1,5)

			if pos_last_donationB == 13:
				pos_total_donationB = 0
			elif pos_last_donationB == 12:
				pos_total_donationB = random.randint(1,5)

			if pos_incomeA == 0:
				pos_povertyA = random.randint(0,4) + 2
			elif pos_incomeA == 1 or pos_incomeA == 2:
				pos_povertyA = random.randint(0,4)
			else:
				pos_povertyA = random.randint(0,2)

			if pos_incomeB == 0:
				pos_povertyB = random.randint(0,4) + 2
			elif pos_incomeB == 1 or pos_incomeB == 2:
				pos_povertyB = random.randint(0,4)
			else:
				pos_povertyB = random.randint(0,2)



			score_pos_sizeA = calcOrgSize(pos_sizeA, pos_foodType, personName)
			score_pos_accessA = calcFoodAccess(pos_accessA, pos_foodType, personName)
			score_pos_incomeA = calcIncomeLevel(pos_incomeA, pos_foodType, personName)
			score_pos_povertyA = calcPovertyLevel(pos_povertyA, pos_foodType, personName)
			score_pos_last_donationA = calcLastDonation(pos_last_donationA, pos_foodType, personName)
			score_pos_total_donationA = calcTotalDonation(pos_total_donationA, pos_foodType, personName)
			score_pos_distanceA = calcTravelTime(pos_distanceA, pos_foodType, personName)

			score_pos_sizeB = calcOrgSize(pos_sizeB, pos_foodType, personName)
			score_pos_accessB = calcFoodAccess(pos_accessB, pos_foodType, personName)
			score_pos_incomeB = calcIncomeLevel(pos_incomeB, pos_foodType, personName)
			score_pos_povertyB = calcPovertyLevel(pos_povertyB, pos_foodType, personName)
			score_pos_last_donationB = calcLastDonation(pos_last_donationB, pos_foodType, personName)
			score_pos_total_donationB = calcTotalDonation(pos_total_donationB, pos_foodType, personName)
			score_pos_distanceB = calcTravelTime(pos_distanceB, pos_foodType, personName)

			if None in [
			score_pos_sizeA, score_pos_accessA, score_pos_incomeA, score_pos_povertyA, score_pos_last_donationA, 
			score_pos_total_donationA, score_pos_distanceA,
			score_pos_sizeB, score_pos_accessB, score_pos_incomeB, score_pos_povertyB, score_pos_last_donationB, 
			score_pos_total_donationB, score_pos_distanceB
			]:
				continue
			else:
				generated_list.append([
			score_pos_sizeA, score_pos_accessA, score_pos_incomeA, score_pos_povertyA, score_pos_last_donationA, 
			score_pos_total_donationA, score_pos_distanceA,
			score_pos_sizeB, score_pos_accessB, score_pos_incomeB, score_pos_povertyB, score_pos_last_donationB, 
			score_pos_total_donationB, score_pos_distanceB
			])


				pos_scoreA = score_pos_sizeA + score_pos_accessA + score_pos_incomeA + score_pos_povertyA + score_pos_last_donationA + score_pos_total_donationA + score_pos_distanceA
				pos_scoreB = score_pos_sizeB + score_pos_accessB + score_pos_incomeB + score_pos_povertyB + score_pos_last_donationB + score_pos_total_donationB + score_pos_distanceB 
				resultFile.write("%d. Donation Type: %d\n" % (len(generated_list), pos_foodType))
				resultFile.write("Organization Size of Recipient A: %d \n" % pos_sizeA)	
				resultFile.write("Food Access Level of Recipient A: %d \n"	% pos_accessA)
				resultFile.write("Income Level of Recipient A: %d \n"	% pos_incomeA)
				resultFile.write("Poverty Rate of Recipient A: %d \n" % pos_povertyA)
				resultFile.write("Last Donation Received of Recipient A: %d \n" % pos_last_donationA)
				resultFile.write("Total Donation Received of Recipient A: %d \n" % pos_total_donationA) 
				resultFile.write("Travel Time of Recipient A: %d \n" % pos_distanceA)


				resultFile.write("\nScore for Recipient A: Organization Size(%d) + Food Access(%d) + Income Level(%d) + Poverty Rate(%d) + Last Donation Received(%d) + Total Donation Received(%d) + Travel Time(%d) = %d \n\n" % (score_pos_sizeA, score_pos_accessA, score_pos_incomeA, score_pos_povertyA, score_pos_last_donationA, score_pos_total_donationA, score_pos_distanceA, pos_scoreA))

				resultFile.write("Organization Size of Recipient B: %d \n" % pos_sizeB)	
				resultFile.write("Food Access Level of Recipient B: %d \n"	% pos_accessB)
				resultFile.write("Income Level of Recipient B: %d \n"	% pos_incomeB)
				resultFile.write("Poverty Rate of Recipient B: %d \n" % pos_povertyB)
				resultFile.write("Last Donation Received of Recipient B: %d \n" % pos_last_donationB)
				resultFile.write("Total Donation Received of Recipient B: %d \n" % pos_total_donationB) 
				resultFile.write("Travel Time of Recipient B: %d \n" % pos_distanceB)


				resultFile.write("\nScore for Recipient B: Organization Size(%d) + Food Access(%d) + Income Level(%d) + Poverty Rate(%d) + Last Donation Received(%d) + Total Donation Received(%d) + Travel Time(%d) = %d \n\n" % (score_pos_sizeB, score_pos_accessB, score_pos_incomeB, score_pos_povertyB, score_pos_last_donationB, score_pos_total_donationB, score_pos_distanceB, pos_scoreB))

				resultFile.write("\nChoice: %s\n\n" % getAlgoChoice(pos_scoreA, pos_scoreB))

	resultFile.close()

def executeQuery(query, columnTuple):
	cur.execute(query, columnTuple)
	ans = cur.fetchall()
	if len(ans) == 1:
		return ans[0][0]
	else:
		return None

def calcOrgSize(org, donation, person):
	if org == 0:
		query = '''SELECT fifty 
				 	 FROM organization_size
					WHERE person = (%s) and food_type = (%s)'''

	elif org == 1:
		query = '''SELECT hundred
				 	 FROM organization_size
					WHERE person = (%s) and food_type = (%s)'''

	elif org == 2:
		query = '''SELECT fiveHundred 
					 FROM organization_size
					WHERE person = (%s) and food_type = (%s)'''

	elif org == 3:
		query = '''SELECT thousand 
					 FROM organization_size
					WHERE person = (%s) and food_type = (%s)'''

	elif org == 4:
		query = '''SELECT larger
					 FROM organization_size
					WHERE person = (%s) and food_type = (%s)'''

	return executeQuery(query, (person, donation))

def calcFoodAccess(foodAccess, donation, person):
	if foodAccess == 0:
		query = '''SELECT normal
					 FROM food_access
					WHERE person = (%s) and food_type = (%s)'''

	elif foodAccess == 1:
		query = '''SELECT low
					 FROM food_access
					WHERE person = (%s) and food_type = (%s)'''

	elif foodAccess == 2:
		query = '''SELECT extremely_low
					 FROM food_access
					WHERE person = (%s) and food_type = (%s)'''
	return executeQuery(query, (person, donation))


def calcIncomeLevel(incomeLevel, donation, person):
	if incomeLevel == 0:
		query = '''SELECT zeroK
					 FROM income
					WHERE person = (%s) and food_type = (%s)'''

	elif incomeLevel == 1:
		query = '''SELECT twentyK
					 FROM income
					WHERE person = (%s) and food_type = (%s)'''	

	elif incomeLevel == 2:
		query = '''SELECT fourtyK
					 FROM income
					WHERE person = (%s) and food_type = (%s)'''

	elif incomeLevel == 3:
		query = '''SELECT sixtyK 
					 FROM income
					WHERE person = (%s) and food_type = (%s)'''

	elif incomeLevel == 4:
		query = '''SELECT eightyK
				 	FROM income
					WHERE person = (%s) and food_type = (%s)'''

	elif incomeLevel == 5:
		query = '''SELECT hundredK
					 FROM income
					WHERE person = (%s) and food_type = (%s)'''

	return executeQuery(query, (person, donation))


def calcPovertyLevel(poverty, donation, person):
	if poverty == 0:
		query = '''SELECT zero
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''

	elif poverty == 1:
		query = '''SELECT twenty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''
	elif poverty == 2:
		query = '''SELECT thirty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''

	elif poverty == 3:
		query = '''SELECT forty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''

	elif poverty == 4:
		query = '''SELECT forty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''

	elif poverty == 5:
		query = '''SELECT fifty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''
	elif poverty == 6:
		query = '''SELECT sixty
					 FROM poverty
					WHERE person = (%s) and food_type = (%s)'''
	elif poverty == 7:
		return None
	return executeQuery(query, (person, donation))


def calcLastDonation(lastD, donation, person):
	if lastD == 0:
		return 0
	if lastD == 1:
		query = '''SELECT one
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 2:
		query = '''SELECT two 
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 3:
		query = '''SELECT three
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 4:
		query = '''SELECT four
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 5:
		query = '''SELECT five
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 6:
		query = '''SELECT six 
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 7:
		query = '''SELECT seven
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 8:
		query = '''SELECT eight
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 9:
		query = '''SELECT nine
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 10:
		query = '''SELECT ten 
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 11:
		query = '''SELECT eleven 
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 12:
		query = '''SELECT twelve
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	elif lastD == 13:
		query = '''SELECT never
					 FROM lastDonation
					WHERE person = (%s) and food_type = (%s)'''

	return executeQuery(query, (person, donation))



def calcTotalDonation(totalD, donation, person):
	if totalD == 0:
		query = '''SELECT zero
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [1,2]:
		query = '''SELECT one 
					 FROM totalDonation
					WHERE person = (%s)'''	

	elif totalD in [3,4,5]:
		query = '''SELECT two
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [6,7,8,9]:
		query = '''SELECT three
					 FROM totalDonation
					WHERE person = (%s)'''
	elif totalD in [10,11,12,13,14]:
		query = '''SELECT four 
					 FROM totalDonation
					WHERE person = (%s)'''


	elif totalD in [15,16,17,18,19,20]:
		query = '''SELECT five
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [21,22,23,24,25,26,27]:
		query = '''SELECT six
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [28,29,30,31,32,33,34,35]:
		query = '''SELECT seven
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [36,37,38,39,40,41,42,43,44]:
		query = '''SELECT eight
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [45,46,47,48,49,50,51,52,53,54]:
		query = '''SELECT nine
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [55,56,57,58,59,60,61,62,63,64,65]:
		column = "ten"
		query = '''SELECT ten 
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [66,67,68,69,70,71,72,73,74,75,76,77]:
		column = "eleven"
		query = '''SELECT eleven 
					 FROM totalDonation
					WHERE person = (%s)'''

	elif totalD in [78,79,80,81,82,83,84,85,86,87,88,89,90]:
		query = '''SELECT twelve
					 FROM totalDonation
					WHERE person = (%s)'''

	return executeQuery(query, (person,))


def calcTravelTime(travel, donation, person):
	if travel == 0:
		query = '''SELECT fifteen
					 FROM distance
					WHERE person = (%s) and food_type = (%s)'''

	elif travel == 1:
		query = '''SELECT thirty
					 FROM distance
					WHERE person = (%s) and food_type = (%s)'''

	elif travel == 2:
		query = '''SELECT fourtyFive
					 FROM distance
					WHERE person = (%s) and food_type = (%s)'''

	elif travel == 3:
		query = '''SELECT sixty
					 FROM distance
					WHERE person = (%s) and food_type = (%s)'''

	return executeQuery(query, (person, donation))


def getAlgoChoice(sumA, sumB):
	if sumA > sumB:
		return 'A'
	elif sumB > sumA:
		return 'B'
	else:
		return 'Tied'

def test():
	query = '''SELECT fifty
				 FROM organization_size
				WHERE person = (%s)'''
	cur.execute(query,('D4',))
	rows = cur.fetchall()
	for row in rows:
		print(row)

def main():
	status = True
	while(status):
		fileName = input("Enter File Name (press '#' if you want to end the program): ")
		if fileName == '#':
			print("Exiting the program...")
			status = False
		else:
			try:
				readFile("textFiles/%s" % (fileName,))
				print("Successful!")
			except(FileNotFoundError):
				print("%s does not exist in the 'stimuliCalculator' directory" % fileName)

if __name__ == "__main__":
	main()









