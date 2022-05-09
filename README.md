
# Study on Event-based Images Denoising Using Noise2Noise

**Wei Xu**

**Abstract**:

_This repository is for my Machine Learning course final project and based on [Noise2Noise](https://github.com/NVlabs/noise2noise)

## Resources

* [Paper (arXiv)](https://arxiv.org/abs/1803.04189)

All the material, including source code, is made freely available for non-commercial use under the Creative Commons [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) license. Feel free to use any of the material in your own work, as long as you give us appropriate credit by mentioning the title and author list of the Noise2Noise paper.

## Getting started

The below sections detail how to get set up for training the Noise2Noise network using the event based images dataset. 

### Python requirements

This code is tested with Python 3.6.  We're using [Anaconda 5.2](https://www.anaconda.com/download/) to manage the Python environment.  Here's how to create a clean environment and install library dependencies:

```
conda create -n n2n python=3.6
conda activate n2n
conda install tensorflow-gpu
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This will install TensorFlow and other dependencies used in this project.

### Preparing datasets for training and validation

This section explains how to prepare a dataset into a TFRecords file for use in training the Noise2Noise denoising network. The original data are obtained from [The Event-Camera Dataset and Simulator](https://rpg.ifi.uzh.ch/davis_data.html). Download the text files and put them into the `./datasets/events` directory. 

To generate the images and split them into training and validation sets, run:

```
python dataset_generate.py
python dataset_split.py
```

**Training dataset for event images**: To generate the event images training set tfrecords file, run:

```
# This should run through 648 images and output a file called `datasets/images_training.tfrecords`.
python dataset_tool_tf.py --input-dir ".datasets/images_training" --out=datasets/images_training.tfrecords
```

### Training networks

To train the noise2noise autoencoder on event images:

```
# try python config.py train --help for available options
python config.py --desc='-test' train --train-tfrecords=datasets/images_training.tfrecords --noise=gaussian
```

You can inspect the training process using TensorBoard:

```
cd results
tensorboard --logdir .
```

By default, this invocation will train a Gaussian denoising network using the ImageNet validation set.  This takes roughly 40 minites on an NVIDIA GTX 3090 GPU.

Upon completion, the training process produces a file called `network_final.pickle` under the `results/*` directory.

### Validation using a trained network

Once you've trained a network, you can run a validation dataset through the network:

Suppose your training run results were stored under `results/00001-autoencoder-1gpu-L-n2n`.  Here's how to run a set of images through this network:

```
python config.py validate --dataset-dir=datasets/images_val --network-snapshot=results/00001-autoencoder-1gpu-L-n2n/network_final.pickle
```

### Pre-trained networks

You can find pre-trained networks for Poisson and Gaussian noise removal in `.results/pretrained` directory. 

## Reproducing Noise2Noise paper results

Here's a summary of training options to reproduce results from the project report:

| Noise    | Noise2Noise | Command line |
| -----    | ----------- |--------------|
| Gaussian | Yes         | python config.py train --noise=gaussian --noise2noise=true --train-tfrecords=datasets/images_training.tfrecords |
| Gaussian | No          | python config.py train --noise=gaussian --noise2noise=false --train-tfrecords=datasets/images_training.tfrecords |
| Poisson  | Yes         | python config.py train --noise=poisson --noise2noise=true --train-tfrecords=datasets/images_training.tfrecords |
| Poisson  | No          | python config.py train --noise=poisson --noise2noise=false --train-tfrecords=datasets/images_training.tfrecords |

To validate against a trained network, use the following options:

| Noise    | Dataset     | Command line | Expected PSNR (dB)|
| -----    | ----------- |--------------|------------------|
| Gaussian | images_val       | python config.py validate --dataset-dir=datasets/images_val --noise=gaussian --network-snapshot=<.../network_final.pickle> | 29.03 (n2c) / 29.05 (n2n) |
| Poisson  | images_val       | python config.py validate --dataset-dir=datasets/images_val --noise=poisson --network-snapshot=<.../network_final.pickle> | 28.48 (n2c) / 28.50 (n2n) |

_Note: When running a validation set through the network, you should match the augmentation noise (e.g., Gaussian or Poisson) with the type of noise that was used to train the network._
