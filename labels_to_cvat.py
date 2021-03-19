import os
import shutil
import argparse


def create_texts(folder, img_list, classes):

    class_labels = classes.split(",")

    # create train.txt
    prefix_train = "data/obj_train_data/"
    train_txt = os.path.join(folder, "cvat_upload", "train.txt")
    with open(train_txt, "w") as file_object:
        for image in img_list:
            file_object.write(prefix_train + image + "\n")

    # create obj.data
    n_classes = len(class_labels)
    name = "obj.data"
    classes = "classes = " + str(n_classes)
    train = "train = data/train.txt"
    names = "names = data/obj.names"
    backup = "backup = backup/"

    with open(os.path.join(folder, "cvat_upload", name), "w") as file_object:
        file_object.write(classes + "\n" + train + "\n" + names + "\n" + backup)

    # create obj.names
    name = "obj.names"
    with open(os.path.join(folder, "cvat_upload", name), "w") as file_object:
        for i in class_labels:
            file_object.write(i + "\n")


def create_zip(path, no_zip):
    folder = path
    # create images_zip
    if no_zip:
        shutil.make_archive(
            os.path.join(folder, "images_upload"), "zip", os.path.join(folder, "images")
        )

    # create upload_to_cvat.zip
    shutil.make_archive(
        os.path.join(folder, "annotations_upload"),
        "zip",
        os.path.join(folder, "cvat_upload"),
    )


def move_files(path, classes):
    folder = path
    files = os.listdir(folder)
    img_list = [
        f
        for f in files
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".png", ".PNG", ".jpg", ".jpeg"))
    ]

    labels = [f for f in files if f not in img_list]
    assert len(labels) == len(img_list)

    # create the images folder
    os.mkdir(os.path.join(folder, "images"))

    # move images into the images folder
    for image in img_list:
        src = os.path.join(folder, image)
        dst = os.path.join(folder, "images", image)
        shutil.move(src, dst)

    # create the cvat project folder
    os.mkdir(os.path.join(folder, "cvat_upload"))

    # create obj_train_data
    os.mkdir(os.path.join(os.path.join(folder, "cvat_upload"), "obj_train_data"))

    # move .txts into obj_train_data
    for label in labels:
        src = os.path.join(folder, label)
        dst = os.path.join(folder, "cvat_upload", "obj_train_data", label)
        shutil.move(src, dst)

    create_texts(folder, img_list, classes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Convert dataset into CVAT upload format""")
    parser.add_argument("-folder", "-f", type=str, required=True, help="Path dataset folder")
    parser.add_argument( "-classes", "-c", type=str, required=True, help="Class labels separated by comma")
    parser.add_argument("-no_zip", help="Dont save images_upload.zip", action="store_false")
    args = parser.parse_args()

    move_files(args.folder, args.classes)
    create_zip(args.folder, args.no_zip)
    print("Done")
