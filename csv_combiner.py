import csv
fileName = "_books_youngadult.csv"
f = open(fileName,"w")
headers = "genre,title,author,image_link,num_of_pages,publish_date,audible_link,barns_and_nobel_link,google_link,amazon_link,rating,num_of_ratings\n"
f.write(headers)
current_list = []
with open('books_youngadult1.csv','r') as csv1_file:
    csv_reader1 = csv.reader(csv1_file)
    for line in csv_reader1:
        temp1 = str(line[0])
        temp2 = line[1]
        temp3 = line[2]
        temp4 = line[3]
        temp5 = line[4]
        temp6 = line[5]
        temp7 = line[6]
        temp8 = line[7]
        temp9 = line[8]
        temp10 = line[9]
        if temp1 == "  youngadult" or temp1 == "  ratingyoungadult":
            temp1 = "youngadult"
        temp3.replace("   ","")
        if temp9 == "https://www.goodreads.comjavascript:void(0)":
            temp9 = "N/A"
        out_string = (temp1 + "," + temp2 + "," + temp3 + "," + temp4 + "," + temp5 + "," + temp6 + "," + temp7 + "," + temp8 + "," + temp9 + "," + temp10 + "\n")
        f.write(out_string)
        current_list.append([temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10])
with open('books_youngadult2.csv','r') as csv2_file:
    csv_reader2 = csv.reader(csv2_file)
    for line in csv_reader2:
        temp1 = str(line[0])
        temp2 = line[1]
        temp3 = line[2]
        temp4 = line[3]
        temp5 = line[4]
        temp6 = line[5]
        temp7 = line[6]
        temp8 = line[7]
        temp9 = line[8]
        temp10 = line[9]
        if temp1 == "  youngadult" or temp1 == "  ratingyoungadult":
            temp1 = "youngadult"
        temp3.replace("   ", "")
        if temp9 == "https://www.goodreads.comjavascript:void(0)":
            temp9 = "N/A"
        out_string = (temp1 + "," + temp2 + "," + temp3 + "," + temp4 + "," + temp5 + "," + temp6 + "," + temp7 + "," + temp8 + "," + temp9 + "," + temp10 + "\n")
        f.write(out_string)
        current_list.append([temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10])

with open('books_youngadult3.csv','r') as csv_file3:
    csv_reader3 = csv.reader(csv_file3)
    for line in csv_reader3:
        temp1 = str(line[0])
        temp2 = line[1]
        temp3 = line[2]
        temp4 = line[3]
        temp5 = line[4]
        temp6 = line[5]
        temp7 = line[6]
        temp8 = line[7]
        temp9 = line[8]
        temp10 = line[9]
        if temp1 == "  youngadult" or temp1 == "  ratingyoungadult":
            temp1 = "youngadult"
        temp3.replace("   ", "")
        if temp9 == "https://www.goodreads.comjavascript:void(0)":
            temp9 = "N/A"
        out_string = (temp1 + "," + temp2 + "," + temp3 + "," + temp4 + "," + temp5 + "," + temp6 + "," + temp7 + "," + temp8 + "," + temp9 + "," + temp10 + "\n")
        f.write(out_string)
        current_list.append([temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10])

f.close()