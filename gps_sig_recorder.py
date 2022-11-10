#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class gps_sig_recorder(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "gps_sig_recorder")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.target_center = target_center = 1.57542e9
        self.samp_rate = samp_rate = 4e6
        self.center_freq = center_freq = target_center
        self.amplifier = amplifier = 1
        self.IF_LNA = IF_LNA = 40
        self.BB_VGA = BB_VGA = 38

        ##################################################
        # Blocks
        ##################################################
        self._center_freq_range = Range(target_center-10e6, target_center+10e6, 1, target_center, 200)
        self._center_freq_win = RangeWidget(self._center_freq_range, self.set_center_freq, 'center_freq', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._center_freq_win)
        self._amplifier_range = Range(0, 1, 1, 1, 200)
        self._amplifier_win = RangeWidget(self._amplifier_range, self.set_amplifier, 'amplifier', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplifier_win)
        self._IF_LNA_range = Range(0, 40, 1, 40, 200)
        self._IF_LNA_win = RangeWidget(self._IF_LNA_range, self.set_IF_LNA, 'IF_LNA', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._IF_LNA_win)
        self._BB_VGA_range = Range(0, 60, 1, 38, 200)
        self._BB_VGA_win = RangeWidget(self._BB_VGA_range, self.set_BB_VGA, 'BB_VGA', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._BB_VGA_win)
<<<<<<< Updated upstream
        self.soapy_hackrf_source_0 = None
        dev = 'driver=hackrf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_hackrf_source_0 = soapy.source(dev, "fc32", 1, 'bias_tx=true',
                                  stream_args, tune_args, settings)
        self.soapy_hackrf_source_0.set_sample_rate(0, samp_rate)
        self.soapy_hackrf_source_0.set_bandwidth(0, 2.75e6)
        self.soapy_hackrf_source_0.set_frequency(0, center_freq)
        self.soapy_hackrf_source_0.set_gain(0, 'AMP', amplifier)
        self.soapy_hackrf_source_0.set_gain(0, 'LNA', min(max(IF_LNA, 0.0), 40.0))
        self.soapy_hackrf_source_0.set_gain(0, 'VGA', min(max(BB_VGA, 0.0), 62.0))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
=======
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
>>>>>>> Stashed changes
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
<<<<<<< Updated upstream
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


=======
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
>>>>>>> Stashed changes

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
<<<<<<< Updated upstream
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/ht/raw_bb_gps_sig/l1_2022_09_22.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
=======
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'bias=1,hackrf=0'
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(amplifier, 0)
        self.osmosdr_source_0.set_if_gain(IF_LNA, 0)
        self.osmosdr_source_0.set_bb_gain(BB_VGA, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_multiply_const_xx_0_0 = blocks.multiply_const_ff(10, 1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(100, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10000, 1, 4000, 1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, 'G:\\data_1h\\1h_gps_4M_schar_hackrf.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_interleaved_char_0 = blocks.complex_to_interleaved_char(False, 1.0)
>>>>>>> Stashed changes


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_interleaved_char_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_complex_to_interleaved_char_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_multiply_const_xx_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_xx_0_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_multiply_const_xx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_const_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gps_sig_recorder")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_target_center(self):
        return self.target_center

    def set_target_center(self, target_center):
        self.target_center = target_center
        self.set_center_freq(self.target_center)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 1)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 2)

    def get_amplifier(self):
        return self.amplifier

    def set_amplifier(self, amplifier):
        self.amplifier = amplifier
        self.osmosdr_source_0.set_gain(self.amplifier, 0)
        self.osmosdr_source_0.set_gain(self.amplifier, 1)
        self.osmosdr_source_0.set_gain(self.amplifier, 2)

    def get_IF_LNA(self):
        return self.IF_LNA

    def set_IF_LNA(self, IF_LNA):
        self.IF_LNA = IF_LNA
        self.osmosdr_source_0.set_if_gain(self.IF_LNA, 0)
        self.osmosdr_source_0.set_if_gain(self.IF_LNA, 1)
        self.osmosdr_source_0.set_if_gain(self.IF_LNA, 2)

    def get_BB_VGA(self):
        return self.BB_VGA

    def set_BB_VGA(self, BB_VGA):
        self.BB_VGA = BB_VGA
        self.osmosdr_source_0.set_bb_gain(self.BB_VGA, 0)
        self.osmosdr_source_0.set_bb_gain(self.BB_VGA, 1)
        self.osmosdr_source_0.set_bb_gain(self.BB_VGA, 2)




def main(top_block_cls=gps_sig_recorder, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
