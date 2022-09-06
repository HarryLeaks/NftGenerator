from PIL import Image
from IPython.display import display
import random
import json
import os

cor = ["blue", "classic", "coal", "green", "Orange", "poison", "red"]
cor_weights = [14, 15, 14, 14, 14, 14, 15]

boca = ["1", "2", "3", "4", "5", "6"]
boca_weights = [16, 17, 16, 17, 17, 17]

caudas = ["1", "3", "blue", "Classic", "coal", "fire", "green 2", "green", "orange", "poison 2", "poison", "red"]
caudas_weights = [8, 8, 9, 8, 8, 8, 9, 8, 9, 8, 9, 8]

chapeus = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
chapeus_weights = [11, 11, 11, 11, 12, 11, 11, 11, 11]

nariz = ["1", "2", "3", "5", "6"]
nariz_weights = [20, 20, 20, 20, 20]

olhos = ["blue", "brown 2", "dark red", "Dark", "Desc", "Devil Blue", "Devil red", "Fechado", "Glass", "Green", "happy", "love", "night", "orange", "purple", "scar"]
olhos_weights = [7, 6, 6, 6, 7, 6, 6, 6, 7, 6, 6, 6, 7, 6, 6, 6]

orelhas = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
orelhas_weights = [11, 11, 11, 11, 12, 11, 11, 11, 11]


cor_files = {
	"blue": "blue", 
	"classic": "classic",
	"coal": "coal", 
	"green": "green", 
	"Orange": "Orange", 
	"poison": "poison", 
	"red": "red"
}

boca_files = {
	"1": "1", 
	"2": "2", 
	"3": "3", 
	"4": "4", 
	"5": "5", 
	"6": "6"
}

caudas_files = {
	"1": "1", 
	"3": "3", 
	"blue": "blue", 
	"Classic": "Classic", 
	"coal": "coal", 
	"fire": "fire", 
	"green 2": "green 2", 
	"green": "green", 
	"orange": "orange", 
	"poison 2": "poison 2", 
	"poison": "poison", 
	"red": "red"
}

chapeus_files = {
	"1": "1", 
	"2": "2", 
	"3": "3",
	"4": "4",
	"5": "5", 
	"6": "6", 
	"7": "7", 
	"8": "8", 
	"9": "9"
}

nariz_files = {
	"1": "1",
	"2": "2",
	"3": "3",
	"5": "5",
	"6": "6"
}

olhos_files = {
	"blue": "blue", 
	"brown 2": "brown 2", 
	"dark red": "dark red", 
	"Dark": "Dark", 
	"Desc": "Desc", 
	"Devil Blue": "Devil Blue", 
	"Devil red": "Devil red", 
	"Fechado": "Fechado", 
	"Glass": "Glass", 
	"Green": "Green", 
	"happy": "happy", 
	"love": "love", 
	"night": "night", 
	"orange": "orange", 
	"purple": "purple", 
	"scar": "scar"
}

orelhas_files = {
	"1": "1", 
	"2": "2", 
	"3": "3", 
	"4": "4", 
	"5": "5", 
	"6": "6", 
	"7": "7", 
	"8": "8", 
	"9": "9"
}

TOTAL_IMAGES = 12000

all_images = []

def create_new_image():
	new_image = {}

	new_image["cor"] = random.choices(cor, cor_weights)[0]
	new_image["cauda"] = random.choices(caudas, caudas_weights)[0]
	new_image["boca"] = random.choices(boca, boca_weights)[0]
	new_image["chapeu"] = random.choices(chapeus, chapeus_weights)[0]
	new_image["nariz"] = random.choices(nariz, nariz_weights)[0]
	new_image["olhos"] = random.choices(olhos, olhos_weights)[0]
	new_image["orelhas"] = random.choices(orelhas, orelhas_weights)[0]

	if new_image in all_images:
		return create_new_image()
	else:
		return new_image

for i in range(TOTAL_IMAGES):
	new_trait_image = create_new_image()
	all_images.append(new_trait_image)

def all_images_unique(all_images):
	seen = list()
	return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

i = 0
for item in all_images:
	item["tokenId"] = i
	i = i + 1

print(all_images)

cor_count = {}
for item in cor:
	cor_count[item] = 0

caudas_count = {}
for item in caudas:
	caudas_count[item] = 0

boca_count = {}
for item in boca:
	boca_count[item] = 0

chapeus_count = {}
for item in chapeus:
	chapeus_count[item] = 0

nariz_count = {}
for item in nariz:
	nariz_count[item] = 0

olhos_count = {}
for item in olhos:
	olhos_count[item] = 0

orelhas_count = {}
for item in orelhas:
	orelhas_count[item] = 0

for image in all_images:
	cor_count[image["cor"]] += 1
	caudas_count[image["cauda"]] += 1
	boca_count[image["boca"]] += 1
	chapeus_count[image["chapeu"]] += 1
	nariz_count[image["nariz"]] += 1
	olhos_count[image["olhos"]] += 1
	orelhas_count[image["orelhas"]] += 1

print(cor_count)
print(caudas_count)
print(boca_count)
print(chapeus_count)
print(nariz_count)
print(olhos_count)
print(orelhas_count)

os.mkdir(f'./images')

for item in all_images:
	background = Image.open(f'./ColorBack.png').convert('RGBA')
	im1 = Image.open(f'./Cor/{cor_files[item["cor"]]}.png').convert('RGBA')
	im2 = Image.open(f'./Caudas/{caudas_files[item["cauda"]]}.png').convert('RGBA')
	im3 = Image.open(f'./Boca/{boca_files[item["boca"]]}.png').convert('RGBA')
	im4 = Image.open(f'./Chapeus/{chapeus_files[item["chapeu"]]}.png').convert('RGBA')
	im5 = Image.open(f'./Nariz/{nariz_files[item["nariz"]]}.png').convert('RGBA')
	im6 = Image.open(f'./Olhos/{olhos_files[item["olhos"]]}.png').convert('RGBA')
	im7 = Image.open(f'./Orelhas/{orelhas_files[item["orelhas"]]}.png').convert('RGBA')

	com0 = Image.alpha_composite(background, im1)
	com1 = Image.alpha_composite(com0, im2)
	com2 = Image.alpha_composite(com1, im3)
	com3 = Image.alpha_composite(com2, im4)
	com4 = Image.alpha_composite(com3, im5)
	com5 = Image.alpha_composite(com4, im6)
	com6 = Image.alpha_composite(com5, im7)

	rgb_im = com6.convert('RGB')
	file_name = str(item["tokenId"]) + ".png"
	rgb_im.save("./images/" + file_name)

###Generate Metadata for all traits
os.mkdir(f'./metadata')

METADATA_FILE_NAME = './metadata/all-traits.json';
with open(METADATA_FILE_NAME, 'w') as outfile:
	json.dump(all_images, outfile, indent=4)