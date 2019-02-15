import math
import csv
import sys
from operator import itemgetter

x_train =[]
y_train = []
test_data = []
def likelihood(variance,mean,test):
    result = 1 / (math.sqrt(2 * math.pi * variance)) * math.exp((-(float(test) - mean) ** 2) / (2 * variance))
    return result

def data_clean():

    with open("akk.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        data = [data for data in rows]


    for x in range(len(data)):
        ins = []
        for y in range(3):
            ins.append(int(data[x][y]))
        y_train.append(data[x][y+1])
        x_train.append(ins)


    with open("test.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        dota = [dota for dota in rows]

    for x in range(len(dota)):
        ins = []
        for y in range(3):
            ins.append(int(dota[x][y]))

        test_data.append(ins)



def Priors():
    male_count = female_count = 0
    for i in y_train:
        if i == 'M':
            male_count += 1

        if i == 'W':
            female_count += 1


    pb_male = male_count / len(y_train)


    pb_female = female_count / len(y_train)


    tot_count = [male_count,female_count,pb_male,pb_female]
    return tot_count

def Calculate_mean():
    tot_count = Priors()
    mean_female_height = mean_male_height = mean_female_weight = mean_male_weight = mean_female_age = mean_male_age = 0


    for i in range(len(x_train)):
        sum = sum1 = sum2 = 0

        if(y_train[i] == 'M'):
            sum +=  x_train[i][0]

            sum1 += x_train[i][1]
            sum2 += x_train[i][2]
        if(sum != 0 and y_train[i] == 'M'):
            #print("sum", sum)
            mean_male_height += sum / tot_count[0]
            mean_male_weight += sum1 / tot_count[0]
            mean_male_age += sum2 / tot_count[0]


        if (y_train[i] == 'W' ):
            sum += x_train[i][0]
            sum1 += x_train[i][1]
            sum2 += x_train[i][2]

        if (sum != 0 and y_train[i] == 'W'):

            mean_female_height += sum / tot_count[1]
            mean_female_weight += sum1 / tot_count[1]
            mean_female_age += sum2 / tot_count[1]



    male_height_variance = male_weight_variance = male_age_variance = female_height_variance = female_weight_variance = female_age_variance = 0
    for i in range(len(x_train)):
        if (y_train[i] == 'M'):
            male_height_variance +=  pow((x_train[i][0] - mean_male_height),2)
            male_weight_variance += (x_train[i][1] - mean_male_weight) ** 2
            male_age_variance += (x_train[i][2] - mean_male_age) ** 2


        if (y_train[i] == 'W'):
            female_height_variance +=  (x_train[i][0] - mean_female_height) ** 2
            female_weight_variance += (x_train[i][1] - mean_female_weight) ** 2
            female_age_variance += (x_train[i][2] - mean_female_age) ** 2

    male_height_variance = male_height_variance/ tot_count[0]
    male_weight_variance = male_weight_variance / tot_count[0]
    male_age_variance = male_age_variance / tot_count[0]
    male_variance = [male_height_variance,male_weight_variance,male_age_variance]
    print("male variance for height,weight and age ",male_variance)
    female_height_variance = female_height_variance / tot_count[1]
    female_weight_variance = female_weight_variance / tot_count[1]
    female_age_variance = female_age_variance / tot_count[1]
    female_variance = [female_height_variance, female_weight_variance, female_age_variance]
    print("female variance for height,weight and age", female_variance)

    ht_given_male = likelihood(male_height_variance,mean_male_height,test_data[0][0])
    print("ht_given_male",ht_given_male)
    ht_given_female = likelihood(female_height_variance, mean_female_height, test_data[0][0])
    wt_given_male = likelihood(male_weight_variance,mean_male_weight,test_data[0][1])
    print("wt_given_male", wt_given_male)
    wt_given_female = likelihood(female_weight_variance, mean_female_weight, test_data[0][1])
    age_given_male = likelihood(male_age_variance, mean_male_age, test_data[0][2])
    age_given_female = likelihood(female_age_variance, mean_female_age, test_data[0][2])
    print("ht_given_female", ht_given_female)
    print("wt_given_female", wt_given_female)
    print("age_given_female", age_given_female)
    M_given_x = ht_given_male * wt_given_male * age_given_male * tot_count[2]
    print("M_given_x", M_given_x)
    W_given_x = ht_given_female * wt_given_female * age_given_female * tot_count[3]
    print("W_given_x", W_given_x)
    if(M_given_x > W_given_x):
        Final_result = "The result is M"
    else:
        Final_result = "The result is W"

    print(Final_result)
    return Final_result
data_clean()
Priors()
Calculate_mean()
