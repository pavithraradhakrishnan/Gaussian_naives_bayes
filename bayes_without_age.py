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

# for omega

def data_clean():

    with open("akk_without_age.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        data = [data for data in rows]


    for x in range(len(data)):
        ins = []
        for y in range(2):
            ins.append(int(data[x][y]))
        y_train.append(data[x][y+1])
        x_train.append(ins)
    #print("x_train is")
    #print(x_train)
    #print("y_train is")
    #print(y_train)

    with open("test.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        dota = [dota for dota in rows]
        #print("test is",dota)
    for x in range(len(dota)):
        ins = []
        for y in range(2):
            ins.append(int(dota[x][y]))

        test_data.append(ins)
        #print("test data is ",test_data)


def Priors():
    male_count = 0
    female_count = 0
    for i in y_train:
        if i == 'M':
            male_count += 1

        if i == 'W':
            female_count += 1
            #print("count = ",female_count)

    pb_male = male_count / len(y_train)

    #print(pb_male)
    pb_female = female_count / len(y_train)
    #print(pb_female)

    tot_count = [male_count,female_count,pb_male,pb_female]
    return tot_count

def Calculate_mean():
    print("x train is",x_train)
    print("y_train is",y_train)
    tot_count = Priors()
    mean_female_height = 0
    mean_male_height = 0
    mean_female_weight = 0
    mean_male_weight = 0



    for i in range(len(x_train)):
        sum = 0
        sum1 = 0
        sum2 = 0

        if(y_train[i] == 'M'):
            sum +=  x_train[i][0]

            sum1 += x_train[i][1]

        if(sum != 0 and y_train[i] == 'M'):
            #print("sum", sum)
            mean_male_height += sum / tot_count[0]
            mean_male_weight += sum1 / tot_count[0]



        if (y_train[i] == 'W' ):
            sum += x_train[i][0]
            sum1 += x_train[i][1]


        if (sum != 0 and y_train[i] == 'W'):
            #print("summ", sum)
            #print("female_count",female_count)
            mean_female_height += sum / tot_count[1]
            mean_female_weight += sum1 / tot_count[1]


    #print(mean_male_height)
    #print(mean_female_height)
    #print(mean_male_weight)
    #print(mean_female_weight)
    #print(mean_male_age)
    #print(mean_female_age)
    male_height_variance = 0
    male_weight_variance = 0

    female_height_variance = 0
    female_weight_variance = 0

    for i in range(len(x_train)):
        if (y_train[i] == 'M'):
            male_height_variance +=  pow((x_train[i][0] - mean_male_height),2)
            male_weight_variance += (x_train[i][1] - mean_male_weight) ** 2


        if (y_train[i] == 'W'):
            female_height_variance +=  (x_train[i][0] - mean_male_height) ** 2
            female_weight_variance += (x_train[i][1] - mean_male_weight) ** 2


    male_height_variance = male_height_variance/ tot_count[0]
    male_weight_variance = male_weight_variance / tot_count[0]

    male_variance = [male_height_variance,male_height_variance]
    female_height_variance = female_height_variance / tot_count[1]
    female_weight_variance = female_weight_variance / tot_count[1]

    female_variance = [female_height_variance, female_height_variance]


    ht_given_male = likelihood(male_height_variance,mean_male_height,test_data[0][0])
    ht_given_female = likelihood(female_height_variance, mean_female_height, test_data[0][0])
    wt_given_male = likelihood(male_weight_variance,mean_male_weight,test_data[0][1])
    wt_given_female = likelihood(female_weight_variance, mean_female_weight, test_data[0][1])


    M_given_x = ht_given_male * wt_given_male *  tot_count[2]

    W_given_x = ht_given_female * wt_given_female *  tot_count[3]

    if(M_given_x > W_given_x):
        Final_result = "The result is M"
        print("The result is M")


    else:
        Final_result = "The result is W"
        print("The result is W")
    return Final_result



    #print("var is",male_height_variance)





data_clean()
Priors()
Calculate_mean()
