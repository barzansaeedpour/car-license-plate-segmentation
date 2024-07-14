# car-license-plate-segmentation 



## Project structure

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


## Dataset

- download the dataset from roboflow: [download](https://universe.roboflow.com/barzan-farid/plate-segmentation-2)

- put it in the dataset directory like the project structure

- change directories in the `data.yaml` file

for example (for me) is like this:

- `train: E:/workspace/car-license-plate-segmentation/dataset/train/images`
- `val: E:/workspace/car-license-plate-segmentation/dataset/valid/images`
- `test: E:/workspace/car-license-plate-segmentation/dataset/test/images`


## Training

- ```
    python train.py
    ```

## Predicting (Testing)

- ```
    python test.py
    ```