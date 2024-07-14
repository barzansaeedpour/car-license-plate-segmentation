"# car-license-plate-segmentation" 



# project structure

- dataset/
    - train/
        - images
        - labels
    - valid/
        - images
        - labels
    - test/
        - images
        - labels
- train.py
- test.py


## dataset

- download the dataset from roboflow: [download](https://universe.roboflow.com/barzan-farid/plate-segmentation-2)

- put it in the dataset directory like the project structure

- change directories in the `data.yaml` file

for example (for me) is like this:

- `train: E:/workspace/car-license-plate-segmentation/dataset/train/images`
- `val: E:/workspace/car-license-plate-segmentation/dataset/valid/images`
- `test: E:/workspace/car-license-plate-segmentation/dataset/test/images`


## Traning

- Just run `train.py`