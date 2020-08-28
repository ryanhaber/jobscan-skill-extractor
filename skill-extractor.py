from bs4 import BeautifulSoup

skillInputFile = open("sampleskills.html", "r")
skillOutputFile = open("skillslist.txt", "w")

htmlList = BeautifulSoup(skillInputFile, "lxml")

skillsNeeded = htmlList.find_all("button", attrs={"data-cvcount": "0"})

for skill in skillsNeeded:
	outputSkill = skill.string.strip() + "\n"
	skillOutputFile.write(outputSkill)

skillOutputFile.close()