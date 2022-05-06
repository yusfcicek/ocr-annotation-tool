# OCR Annotation Tool
OCR Annotation Tool is a graphical image annotation tool.
It is written in Python and uses Qt for its graphical interface. You can use it to tag your own data for the [Deep Text Recognition Repository](https://github.com/clovaai/deep-text-recognition-benchmark). 
Its interface and usage diagram is taken as an example from the [LabelImg](https://github.com/tzutalin/labelImg) repository for easy use for the user. 

### In-app photo
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_001.png)

### How to Use?
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_002.gif)
![](https://raw.githubusercontent.com/yusfcicek/ocr-annotation-tool/main/tests/usecase_003.gif)

## In the future, 

- [x] Labeling rectangles where have texts, With this feature, the positions of curved texts can be detected. [East Text Detection](https://github.com/SakuraRiven/EAST)
- [ ] Labeling texts as polygons, 
- [ ] Export and import, 
- [ ] Cropping text rectangles and labeling as new photos will come.

### How to Run?

Miniconda environment is used in this project. The PyQt6 and PySide6 libraries are used for the graphical interface.

#### How to install required packages?

```
pip install pyqt6
pip install pyside6
```

After completing the installation steps

```
python main.py
```
