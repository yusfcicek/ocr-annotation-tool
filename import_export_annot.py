import os

from PIL import Image
from database_con import DataBase


def export_annot():
    annots = DataBase.pull_all_annot()

    if len(annots) > 0:
        folderPath = "./output/img"
        isExist = os.path.exists(folderPath)
        if not isExist:
            os.makedirs(folderPath)

        f = open("./output/gt.txt", "w")

        for i, annot in enumerate(annots):
            img = Image.open(annot[0])
            area = (annot[3][0], annot[3][1], annot[4][0], annot[4][1])
            cropped_img = img.crop(area)

            outputImgName = f"{i}.png"
            for _ in range(len(str(len(annots))) + 1 - len(str(i))):
                outputImgName = "0" + outputImgName

            path = f"{folderPath}/{outputImgName}"
            cropped_img.save(path)

            f.write(f"img/{outputImgName}\t{annot[2]}\n")

        f.close()


export_annot()
