# Deep learning introductory workshop
Notebooks for the introductory workshop on deep learning held at ETSISI, Universidad Politécnica de Madrid, in October '17.

## Content
* linear_regression: Contains all the linear regression examples we saw during the first session (house prices)
* logistic_regression: Contains all the logistic regression examples we saw during the first session (binary classification)
* ann_xor: Introduces the "Learning XOR" problem. The XOR is a very simple function that linear models such as logistic regression cannot learn. This serves as a motivation for introducing neural networks, and more generally, deep non-linear models.
* ann_mnist: This notebook introduces some aspects of the Keras API, demonstrated on the MNIST handwritten digit data set (a classic benchmark in computer vision).
* cnn_mnist: This notebook introduces convolutional neural networks, widely employed for computer vision, using Keras. Their performance is demonstrated on the MNIST handwritten digit data set.
* transfer_learning: This notebook introduces the concept of transfer learning in computer vision. We use the weights of the VGG-16 network, trained on the ImageNet data set, to quickly build a strikingly accurate image classifier using a moderately sized data set.
 * scripts/pad_ct101.py: This script converts all the images in the specified (hardcoded) directory to a convenient format for the VGG network. 

## Dependencies
* [scikit-learn][1]
* [Tensorflow][2]
* [Keras][3]
* [matplotlib][4]
* [numpy][5]

## A few interesting links
* A talk on CNNs by Andrej Karpathy: [must watch][6]
* [The rest of talks from that event][7]. Highly recommended. They are all leading experts.
* [Andrew Ng's machine learning course][14]
* [A very cool tool for visualizing CNNs][8]. Scroll down for the video.
* [A Stanford course on CNNs][9].
* [Reddit][11]
* [Stack exchange for machine learning and statistics][12]
* The paper describing the [VGG][15] network.

## Books
If you're serious about machine learning, you should start here.
* [Friedman, Jerome, Trevor Hastie, and Robert Tibshirani. The elements of statistical learning. Vol. 1. New York: Springer series in statistics, 2001.][10]
* Bishop, Christopher M. Pattern recognition and machine learning. springer, 2006.
* [Deep learning][13]

[1]: http://scikit-learn.org/stable/
[2]: https://www.tensorflow.org/
[3]: https://keras.io/
[4]: https://matplotlib.org/
[5]: http://www.numpy.org/
[6]: https://www.youtube.com/watch?v=u6aEYuemt0M
[7]: https://www.youtube.com/watch?v=zij_FTbJHsk&list=PLWtzrfzH7gsfxTs8neTRJDXuqAn7qeV4E
[8]: http://yosinski.com/deepvis
[9]: http://cs231n.github.io/
[10]: https://web.stanford.edu/~hastie/Papers/ESLII.pdf
[11]: https://www.reddit.com/r/MachineLearning/
[12]: https://stats.stackexchange.com/
[13]: http://www.deeplearningbook.org/
[14]: https://www.coursera.org/learn/machine-learning
[15]: https://arxiv.org/pdf/1409.1556.pdf
