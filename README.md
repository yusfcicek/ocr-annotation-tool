# OCR Annotation Tool
OCR Annotation Tool is a graphical text annotation tool.
It is written in Python and uses Qt for its graphical interface. You can use it to tag your own data for the [Deep Text Recognition Repository](https://github.com/clovaai/deep-text-recognition-benchmark). 
Its interface and usage diagram is taken as an example from the [LabelImg](https://github.com/tzutalin/labelImg) repository for easy use for the user. 

## In-app photo
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_001.png)

## How to Use?
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_002.gif)
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_003.gif)

## In the future, 

- [x] Labeling rectangles where have texts
- [x] Export, Cropping text rectangles and labeling as new photos 
- [ ] Import, Integration of exported annotations on another computer
- [ ] Labeling texts as polygons, With this feature, the positions of curved texts can be detected. [East Text Detection](https://github.com/SakuraRiven/EAST)

## How to Run?

Miniconda environment is used in this project. The PyQt6 and PySide6 libraries are used for the graphical interface.

### How to install required packages?

```
pip install pyqt6
pip install pyside6
pip install pillow
```

After completing the installation steps

```
python main.py
```

### How to export Annotations?

```
python import_export_annot.py
```
The structure of exported annotations folder as below.
```
output
├── gt.txt
└── img
    ├── 001.png
    ├── 002.png
    ├── 003.png
    └── ...
```
At this time, `gt.txt` is like `{imagepath}\t{label}\n` <br>
For example
```
img/001.png	SAUL
img/002.png	GOODMAN
img/003.png	"Better
...
```
