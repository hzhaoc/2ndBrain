Learning materials:
- [Stanford CS231n:Convolutional Neural Networks: Architectures, Convolution / Pooling Layers](https://cs231n.github.io/convolutional-networks/#norm)
 - [Stanford CS231n: Visualizing what ConvNets learn](https://cs231n.github.io/understanding-cnn/)
 - [Stanford CS231n: Transfer Learning](https://cs231n.github.io/transfer-learning/)

# Inspiration [^1]
## Receptive fields in the visual cortex
Work by Hubel and Wiesel in the 1950s and 1960s showed that cat and monkey visual cortexes contain neurons that individually respond to small regions of the visual field. Provided the eyes are not moving, the region of visual space within which visual stimuli affect the firing of a single neuron is known as its **receptive field**. Neighboring cells have similar and overlapping receptive fields. Receptive field size and location varies systematically across the cortex to form a complete map of visual space. The cortex in each hemisphere represents the contralateral visual field.

Their 1968 paper identified two basic visual cell types in the brain:
- Simple cells, whose output is maximized by straight edges having particular orientations within their receptive field
- Complex cells, which have larger receptive fields, whose output is insensitive to the exact position of the edges in the field.
Hubel and Wiesel also proposed a cascading model of these two types of cells for use in pattern recognition tasks.

## Neocognition origin of the CNN architecture
The "neocognitron" was introduced by Kunihiko Fukushima in 1980. It was inspired by the above-mentioned work of Hubel and Wiesel. The neocognitron introduced the two basic types of layers in CNNs: **convolutional layers**, and **downsampling layers**. A convolutional layer contains units whose receptive fields cover a patch of the previous layer. The weight vector (the set of adaptive parameters) of such a unit is often called a **filter**. Units can share filters. Downsampling layers contain units whose receptive fields cover patches of previous convolutional layers. Such a unit typically computes the average of the activations of the units in its patch. This downsampling helps to correctly classify objects in visual scenes even when the objects are shifted.

In a variant of the neocognitron called the cresceptron instead of using Fukushima's spatial averaging, J. Weng et al introduced a method called max-pooling where a downsampling unit computes the maximum of the activations of the units in its patch. Max-pooling is often used in modern CNNs. 

Several supervised and unsupervised learning algorithms have been proposed over the decades to train the weights of a neocognitron. Today, however, the CNN architecture is usually trained through backpropagation

The neocognitron is the first CNN which requires units located at multiple network positions to have shared weights. Neocognitrons were adapted in 1988 to analyze time-varying signals.

# CNN Architecture
## Some excerpts from above materials
Typical layers:
- Convolutional layers
- Pooling layers
- Normalization layers (fell out of due to minimal contribution)
- Fully Connected layers

A simple ConvNet for CIFAR-10 classification could have the architecture `INPUT - CONV - RELU - POOL - FC`. In more detail:

- `INPUT [32x32x3]` will hold the raw pixel values of the image, in this case an image of width 32, height 32, and with three color channels R,G,B.
- `CONV` layer will compute the output of neurons that are connected to local regions in the input, each computing a dot product between their weights and a small region they are connected to in the input volume. This may result in volume such as `[32x32x12]` if we decided to use 12 filters.
- `RELU` layer will apply an elementwise activation function, such as the max(0,x) thresholding at zero. This leaves the size of the volume unchanged (`[32x32x12]`).
- `POOL` layer will perform a downsampling operation along the spatial dimensions (width, height), resulting in volume such as `[16x16x12]`.
- `FC` (i.e. fully-connected) layer will compute the class scores, resulting in volume of size `[1x1x10]`, where each of the 10 numbers correspond to a class score, such as among the 10 categories of CIFAR-10. As with ordinary Neural Networks and as the name implies, each neuron in this layer will be connected to all the numbers in the previous volume.

A more complex example `VGGNet` which is the runner-up in 2014 image competition, is composed of `CONV` layers that perform `3x3` convolutions with `stride 1` and `pad 1`, and of `POOL` layers that perform `2x2 max pooling` with `stride 2` (and `no padding`). We can write out the size of the representation at each step of the processing and keep track of both the representation size and the total number of weights:

```
INPUT:     [224x224x3]  memory:  224*224*3=150K   weights: 0
CONV3-64:  [224x224x64] memory:  224*224*64=3.2M  weights: (3*3*3)*64 = 1,728
CONV3-64:  [224x224x64] memory:  224*224*64=3.2M  weights: (3*3*64)*64 = 36,864
POOL2:     [112x112x64] memory:  112*112*64=800K  weights: 0
CONV3-128: [112x112x128]memory:  112*112*128=1.6M weights: (3*3*64)*128 = 73,728
CONV3-128: [112x112x128]memory:  112*112*128=1.6M weights: (3*3*128)*128 = 147,456
POOL2:     [56x56x128]  memory:  56*56*128=400K   weights: 0
CONV3-256: [56x56x256]  memory:  56*56*256=800K   weights: (3*3*128)*256 = 294,912
CONV3-256: [56x56x256]  memory:  56*56*256=800K   weights: (3*3*256)*256 = 589,824
CONV3-256: [56x56x256]  memory:  56*56*256=800K   weights: (3*3*256)*256 = 589,824
POOL2: 	   [28x28x256]  memory:  28*28*256=200K   weights: 0
CONV3-512: [28x28x512]  memory:  28*28*512=400K   weights: (3*3*256)*512 = 1,179,648
CONV3-512: [28x28x512]  memory:  28*28*512=400K   weights: (3*3*512)*512 = 2,359,296
CONV3-512: [28x28x512]  memory:  28*28*512=400K   weights: (3*3*512)*512 = 2,359,296
POOL2: 	   [14x14x512]  memory:  14*14*512=100K   weights: 0
CONV3-512: [14x14x512]  memory:  14*14*512=100K   weights: (3*3*512)*512 = 2,359,296
CONV3-512: [14x14x512]  memory:  14*14*512=100K   weights: (3*3*512)*512 = 2,359,296
CONV3-512: [14x14x512]  memory:  14*14*512=100K   weights: (3*3*512)*512 = 2,359,296
POOL2:     [7x7x512]    memory:  7*7*512=25K      weights: 0
FC: 	   [1x1x4096]   memory:  4096             weights: 7*7*512*4096 = 102,760,448
FC:        [1x1x4096]   memory:  4096             weights: 4096*4096 = 16,777,216
FC:        [1x1x1000]   memory:  1000             weights: 4096*1000 = 4,096,000

TOTAL memory: 24M * 4 bytes ~= 93MB / image (only forward! ~*2 for bwd)
TOTAL params: 138M parameters
```

## Transfer Learning
Learn from a pretrained CNN for your model:

| Scenario | Approach |
|---|---|
| Small, similar dataset | Extract higher-level features from CNN as input to train a simple model like linear SVM |
| Large, similar dataset | Fine-tune the full CNN |
| Small, different dataset | Extract lower-level features from CNN as input to train a simple model like linear SVM |
| Large, different dataset | Train new CNN from scratch or from pretrained model's weights |

[^1]: [CNN history](https://en.wikipedia.org/wiki/Convolutional_neural_network)