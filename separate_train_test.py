## Separates the dataset into train and test in separate folders
import shutil
import pickle

with open('train_test_split.txt') as f:
    train_test_split = f.read().splitlines()

with open('images.txt') as f:
    images = f.read().splitlines()
    # imageID, image name

#print(train_test_split)
train_filenames = []
test_filenames = []

#print(images)

count = 1;
for image in images:
    image = image.split()
    id = image[0]
    path = image[1]
    #print(path)
    if (int(train_test_split[int(id) - 1].split()[1]) == 1):
        #Value 1 = training, value 0 = test
        #print('Image ID = ' + str(id) + '\t Train or test = ' + str(train_test_split[int(id)].split()[1]))
        #print('Image ID = ' + str(id) + '\t Train')
        shutil.copyfile('./images/' +path, './train/' + str(count))
        train_filenames.append(str(count))
    else:
        #test
        #print('Image ID = ' + str(id) + '\t Train or test = ' + str(train_test_split[int(id)].split()[1]))
        #print('Image ID = ' + str(id) + '\t Test')
        shutil.copyfile('./images/' + path, './test/' + str(count))
        test_filenames.append(str(count))

    count+=1;
    if(count%100 == 0):
        print('Reached %sth image' % str(count))
    #if(count == 10):
    #    print('10 images moved. Exiting....')
    #    exit(0);

with open('train_filenames.pickle', 'wb') as f:
    pickle.dump(train_filenames, f)

with open('test_filenames.pickle', 'wb') as f:
    pickle.dump(test_filenames, f)
#
