{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "from spectral import *\n",
    "\n",
    "img = open_image('92AV3C.lan')\n",
    "\n",
    "img.__class__\n",
    "\n",
    "print(img)\n",
    "\n",
    "img.shape\n",
    "\n",
    "pixel = img[50,100]\n",
    "\n",
    "pixel.shape\n",
    "\n",
    "band6 = img[:,:,5]\n",
    "band6.shape\n",
    "\n",
    "arr = img.load()\n",
    "arr.__class__\n",
    "print(arr.info())\n",
    "\n",
    "arr.shape\n",
    "\n",
    "#Also the NumPy memmap interface can be used to load an entire image into memory\n",
    "\n",
    "img_numpy = numpy.memmap('92AV3C.lan')\n",
    "\n",
    "print(img_numpy)\n",
    "\n",
    "#Since spectral.ImageArray uses 32-bit floating point values, the amount of memory consumed will be approximately 4 * numRows * numCols * numBands bytes.\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
