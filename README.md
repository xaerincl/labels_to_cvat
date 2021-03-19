# labels_to_cvat


## How to use 

Run:
```
$ python labels_to_cvat.py -f <path to folder with the images and .txt> -c <class1name,class2name...> 
```
add -no_zip at the end if you dont need/want the .zip files with the images


## Demo

we have a folder named 'images' with 2 images and their corresponding label (yolo format .txt) like:




![tutorial_1](/github_images/img1.png)




there are 2 types of objects labeled: dog,person


Run: (remember to change the /user/ part or the full path if neccesary)
```
$ python labels_to_cvat.py -f /home/user/Desktop/images -c dog,person

if you have the images folder and the labels_to_cvat.py in the same folder its easier to run:

$ python labels_to_cvat.py -f images -c dog,person
```

This will create the images_upload.zip and the annotations_upload.zip inside the images. The first contains all the images and the second zipfile contains the annotations plus the obj.names, obj.data and train.txt files necessary to upload to CVAT in order to edit the labels or export them into another format.


![tutorial_2](/github_images/img2.png)


The files will be rearranged and will look like:


![tutorial_3](/github_images/img3.png)

## Autores ✒️
* **Oscar Mauriaca** - *Desarrollo* - [xaerincl](https://github.com/xaerincl)
