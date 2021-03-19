# labels_to_cvat


## How to use 

Run:
```
$ python labels_to_cvat -f <path to folder with the images and .txt> -c <class1name,class2name...> 
```

## demo

we have a folder named 'images' with the images and their corresponding label (yolo format .txt) like:




![tutorial_1](/github_images/img1.png)




there are 2 types of objects labeled: dog,person


Run: (remember to change the /user/ or the full path if neccesary)
```
$ python labels_to_cvat -f /home/user/Desktop/images -c dog,person
```

![tutorial_2](/github_images/img2.png)




## Autores ✒️
* **Oscar Mauriaca** - *Desarrollo* - [xaerincl](https://github.com/xaerincl)
