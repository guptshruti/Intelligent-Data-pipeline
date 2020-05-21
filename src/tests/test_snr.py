import unittest
import sys
import glob

sys.path.append("../../src")

from scripts.snr import SNR


class TestSNR(unittest.TestCase):

    def test_compute_file_snr(self):
        obj = SNR()
        self.assertEqual(obj.compute_file_snr('test_resources/test.wav'), 19.939861)

    def test_fit_return_type(self):
        obj = SNR()
        input_dir = 'test_resources/'
        wav_files = glob.glob(f"{input_dir}*wav")
        file_snr = obj.fit(wav_files)
        self.assertEqual(type(file_snr), type({}))

    def test_fit_return_value(self):
        obj = SNR()
        input_dir = 'test_resources/'
        wav_files = glob.glob(f"{input_dir}*wav")
        file_snr = obj.fit(wav_files)
        self.assertEqual(file_snr['test_resources/test.wav'], 19.939861)