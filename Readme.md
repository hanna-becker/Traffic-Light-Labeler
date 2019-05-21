## Traffic Light Labeler
A tool for labeling traffic light images for training neural networks.


### Installation
1. `sudo apt-get install python3-tk`
2. `pip install -r requirements.txt `


### Usage
1. Replace example images in _images_ folder with the jpg images you would like to label.
2. `cd traffic-light-labeler`
3. `python3 __main__.py`
4. Follow instructions in terminal.
5. You will be notified when all images are labeled.
6. You can pause using _p_ any time you like. No need to re-label the images you already labeled in the next session.


### Output
The labeled images are output in the following format in _labeled_data.csv_:
```
PATH, LABEL
images/red.jpg, r
images/no_light.jpg, u
images/green.jpg, g
images/yellow.jpg, y
```

