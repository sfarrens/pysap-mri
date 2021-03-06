# -*- coding: utf-8 -*-
##########################################################################
# pySAP - Copyright (C) CEA, 2017 - 2018
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# System import
import unittest
import numpy

# Package import
from mri.reconstruct.linear import WaveletN


class TestAdjointOperatorWaveletTransform(unittest.TestCase):
    """ Test the adjoint operator of the Wavelets both for 2D and 3D.
    """

    def setUp(self):
        """ Set the number of iterations.
        """
        self.N = 64
        self.max_iter = 10

    def test_Wavelet2D_ISAP(self):
        """Test the adjoint operator for the 2D Wavelet transform
        """
        for i in range(self.max_iter):
            print("Process Wavelet2D_ISAP test '{0}'...", i)
            wavelet_op_adj = WaveletN(wavelet_name="HaarWaveletTransform",
                                      nb_scale=4)
            Img = (numpy.random.randn(self.N, self.N) +
                   1j * numpy.random.randn(self.N, self.N))
            f_p = wavelet_op_adj.op(Img)
            f = (numpy.random.randn(*f_p.shape) +
                 1j * numpy.random.randn(*f_p.shape))
            I_p = wavelet_op_adj.adj_op(f)
            x_d = numpy.vdot(Img, I_p)
            x_ad = numpy.vdot(f_p, f)
            numpy.testing.assert_allclose(x_d, x_ad, rtol=1e-6)
        print(" Wavelet2 adjoint test passes")

    def test_Wavelet2D_PyWt(self):
        """Test the adjoint operator for the 2D Wavelet transform
        """
        for i in range(self.max_iter):
            print("Process Wavelet2D PyWt test '{0}'...", i)
            wavelet_op_adj = WaveletN(wavelet_name="sym8",
                                      nb_scale=4)
            Img = (numpy.random.randn(self.N, self.N) +
                   1j * numpy.random.randn(self.N, self.N))
            f_p = wavelet_op_adj.op(Img)
            f = (numpy.random.randn(*f_p.shape) +
                 1j * numpy.random.randn(*f_p.shape))
            I_p = wavelet_op_adj.adj_op(f)
            x_d = numpy.vdot(Img, I_p)
            x_ad = numpy.vdot(f_p, f)
            numpy.testing.assert_allclose(x_d, x_ad, rtol=1e-6)
        print(" Wavelet2 adjoint test passes")

    def test_Wavelet3D_PyWt(self):
        """Test the adjoint operator for the 3D Wavelet transform
        """
        for i in range(self.max_iter):
            print("Process Wavelet3D PyWt test '{0}'...", i)
            wavelet_op_adj = WaveletN(wavelet_name="sym8",
                                      nb_scale=4, dim=3,
                                      padding_mode='periodization')
            Img = (numpy.random.randn(self.N, self.N, self.N) +
                   1j * numpy.random.randn(self.N, self.N, self.N))
            f_p = wavelet_op_adj.op(Img)
            f = (numpy.random.randn(*f_p.shape) +
                 1j * numpy.random.randn(*f_p.shape))
            I_p = wavelet_op_adj.adj_op(f)
            x_d = numpy.vdot(Img, I_p)
            x_ad = numpy.vdot(f_p, f)
            numpy.testing.assert_allclose(x_d, x_ad, rtol=1e-6)
        print(" Wavelet3 adjoint test passes")


if __name__ == "__main__":
    unittest.main()
