# Towards A Deeper Understanding of Global Covariance Pooling in Deep Learning: An Optimization Perspective

## Introduction
This paper delves deep into the optimization behaviors of deep Global Covariance Pooling (GCP) networks with matrix power normalization. The authors undertake a thorough analysis and understanding of the effect of GCP on deep architectures, primarily from an optimization perspective. The research can be summarized into three successive parts:

Analysis of the impact of GCP with matrix power normalization on deep architectures. This involves examining the behaviors of both optimization loss (e.g., smoother loss landscape and flatter local minima) and gradient computation.
Investigation and improvement of post-normalization key for optimizing GCP networks. This led to the proposal of the DropCov method, a novel technique for efficiently normalizing GCP. The DropCov method was found to be superior or competitive with existing methods in terms of both efficiency and effectiveness.
Exploration of three new benefits of GCP for deep architectures that have not been previously recognized or fully explored.

![GCP-DropCov](https://github.com/Terror03/GCP-DropCov/assets/45889633/5b80b7a8-0b9f-4ed9-ad44-8c1f35653f15))
![GCP-DropCov2](https://github.com/Terror03/GCP-DropCov/assets/45889633/f98c4c3c-383e-4987-b862-217bf92aa4b8)

## Main Results
|Method           | Acc@1(%) | #Params.(M) | FLOPs(G) | Checkpoint                                                          |
| ------------------ | ----- | ------- | ----- | ------------------------------------------------------------ |
| ResNet-50   |  76.07 |  25.6   |   3.86  |               |
|    | 0  |   0  |  0   | |

## Usage

### Environments
●OS：18.04  
●CUDA：11.6  
●Toolkit：mindspore1.9  
●GPU:GTX 3090 


### Install
●First, Install the driver of NVIDIA  
●Then, Install the driver of CUDA  
●Last, Install cudnn

create virtual enviroment mindspore
conda create -n mindspore python=3.7.5 -y
conda activate mindspore
CUDA 10.1 
```bash
conda install mindspore-gpu cudatoolkit=10.1 -c mindspore -c conda-forge
```
CUDA 11.1 
```bash
conda install mindspore-gpu cudatoolkit=11.1 -c mindspore -c conda-forge
```
validataion 
```bash
python -c "import mindspore;mindspore.run_check()"
```

### Data preparation
Download and extract ImageNet train and val images from http://image-net.org/. (https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder), and the training and validation data is expected to be in the `train/` folder and `val/` folder respectively:


```
/path/to/imagenet/
  train/
    class1/
      img1.jpeg
    class2/
      img2.jpeg
  val/
    class1/
      img3.jpeg
    class/2
      img4.jpeg
```
### Evaluation
To evaluate a pre-trained model on ImageNet val with GPUs run:

```
CUDA_VISIBLE_DEVICES={device_ids}  python eval.py --data_path={IMAGENET_PATH} --checkpoint_file_path={CHECKPOINT_PATH} --device_target="GPU" --config_path={CONFIG_FILE} &> log &
```

### Training

#### Train with ResNet

You can run the `main.py` to train as follow:

```
mpirun --allow-run-as-root -n {RANK_SIZE} --output-filename log_output --merge-stderr-to-stdout python train.py  --config_path={CONFIG_FILE} --run_distribute=True --device_num={DEVICE_NUM} --device_target="GPU" --data_path={IMAGENET_PATH}  --output_path './output' &> log &
```
For example:

```bash
mpirun --allow-run-as-root -n 4 --output-filename log_output --merge-stderr-to-stdout python train.py  --config_path="./config/resnet50_imagenet2012_config.yaml" --run_distribute=True --device_num=4 --device_target="GPU" --data_path=./imagenet --output_path './output' &> log &
```
## Citation

@inproceedings{wang2023TPAMI,
  title={Towards A Deeper Understanding of Global Covariance Pooling in Deep Learning: An Optimization Perspective},
  author={Qilong Wang1, Li Zhang, Banggu Wu, Dongwei Ren, Peihua Li, Wangmeng Zuo, Qinghua Hu},
  booktitle={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  pages={ },
  year={2023}
}

## Acknowledgement
The work was sponsored by National Natural Science Foundation of China (Grant No.s 62276186, 61925602, 61971086 and 61732011) and CCF-Baidu Open Fund (NO.2021PP15002000).
