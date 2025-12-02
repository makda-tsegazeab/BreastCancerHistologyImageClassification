import random
import os

LABELS = ['Normal', 'Benign', 'InSitu', 'Invasive']
LABELS_simple = ['n', 'b', 'is', 'iv']

# this file should be played just one time.

def string_three_digit_num(num):
  if num>=100:
    return str(num)
  else:
    if num>=10:
      return '0'+str(num)
    else:
      return '00'+str(num)

def choose_randomly(n, val, test):
  n_list = list(range(1,(n+1)))
  random.shuffle(n_list)
  return n_list[0:val], n_list[val:val+test]

def generate_filename(label_simple, num):
  return label_simple+string_three_digit_num(num)+'.tif'

data_num = 100
validation_num = round(data_num*0.2)
test_num = round(data_num*0.1)

# move img files from train to validation, test

# print(choose_randomly(10,3,2))
# origin = '/root/shc/ICIAR2018/dataset'
origin = '/root/shc/ICIAR2018/dataset'

for i in range(4):
  label = LABELS[i]
  label_simple = LABELS_simple[i]
  random_validation_num_list, random_test_num_list = choose_randomly(100,20,10)
  for val_num in random_validation_num_list:
    random_filename = generate_filename(label_simple, val_num)
    os.rename(origin+'/train/'+label+'/'+random_filename,
              origin+'/validation/'+label+'/'+random_filename)
  for test_num in random_test_num_list:
    random_filename = generate_filename(label_simple, test_num)
    os.rename(origin+'/train/'+label+'/'+random_filename,
              origin+'/test/'+random_filename)
  