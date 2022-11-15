from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QWidget, QLabel, QGroupBox, QLineEdit, QGridLayout, QRadioButton, QPushButton
from pyperclip import copy

from utilities.PopupWindow import PopupWindow
from utilities.Validator import is_empty, is_correct_binary, is_correct_decimal, is_correct_hexadecimal, is_correct_any_ip_dec, \
    is_correct_any_ip_bin


class ConversionNumeros(QWidget):
    def __init__(self):
        super(ConversionNumeros, self).__init__()

        # App attributes
        self.bin_format_base = None
        self.bin_format_base_byte = None


        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Input
        self.inputbox = QGroupBox("Ingresar:")
        self.inputbox.setMaximumWidth(400)

        main_layout.addWidget(self.inputbox, 0, 0)

        inputbox_layout = QGridLayout()
        inputbox_layout.setHorizontalSpacing(25)
        inputbox_layout.setVerticalSpacing(35)
        inputbox_layout.setAlignment(Qt.AlignCenter)

        self.inputbox.setLayout(inputbox_layout)

        self.input_number_label = QLabel("Número a convertir")
        self.input_number_textfield = QLineEdit()
        self.input_number_textfield.setPlaceholderText("192")
        self.input_number_textfield.setAlignment(Qt.AlignCenter)
        self.input_number_textfield.returnPressed.connect(self.convert_action)

        inputbox_layout.addWidget(self.input_number_label, 0, 0, alignment=Qt.AlignCenter)
        inputbox_layout.addWidget(self.input_number_textfield, 0, 1)

        button_layout = QVBoxLayout()
        self.bin_button = QRadioButton("Binario")
        self.bin_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("11100010"))
        self.dec_button = QRadioButton("Decimal")
        self.dec_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("192"))
        self.hex_button = QRadioButton("Hexadecimal")
        self.hex_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("FF"))
        self.dec_button.setChecked(True)
        button_layout.addWidget(self.bin_button)
        button_layout.addWidget(self.dec_button)
        button_layout.addWidget(self.hex_button)
        inputbox_layout.addLayout(button_layout, 0, 3, 1, 2)

        self.convert_button = QPushButton("Convertir")
        self.convert_button.clicked.connect(self.convert_action)
        self.convert_button.setIcon(QIcon("static/images/exchange.png"))
        inputbox_layout.addWidget(self.convert_button, 1, 1, alignment=Qt.AlignCenter)

        # Output
        self.outputbox = QGroupBox("Resultado")
        main_layout.addWidget(self.outputbox, 0, 1)
        outputbox_layout = QGridLayout()
        outputbox_layout.setHorizontalSpacing(25)
        self.outputbox.setLayout(outputbox_layout)

        self.bin_label = QLabel("Binario")
        self.bin_label.setAlignment(Qt.AlignCenter)

        self.dec_label = QLabel("Decimal")
        self.dec_label.setAlignment(Qt.AlignCenter)

        self.hex_label = QLabel("Hexadecimal")
        self.hex_label.setAlignment(Qt.AlignCenter)

        self.bin_output = QLineEdit()
        self.bin_output.setReadOnly(True)
        self.bin_output.setAlignment(Qt.AlignCenter)

        self.dec_output = QLineEdit()
        self.dec_output.setReadOnly(True)
        self.dec_output.setAlignment(Qt.AlignCenter)

        self.hex_output = QLineEdit()
        self.hex_output.setReadOnly(True)
        self.hex_output.setAlignment(Qt.AlignCenter)

        self.bin_output_copy_button = QPushButton("Copiar")
        self.bin_output_copy_button.setIcon(QIcon("static/images/copy_clipboard.png"))
        self.bin_output_copy_button.clicked.connect(lambda: copy_action(self.bin_output.text()))

        self.dec_output_copy_button = QPushButton("Copiar")
        self.dec_output_copy_button.setIcon(QIcon("static/images/copy_clipboard.png"))
        self.dec_output_copy_button.clicked.connect(lambda: copy_action(self.dec_output.text()))

        self.hex_output_copy_button = QPushButton("Copiar")
        self.hex_output_copy_button.setIcon(QIcon("static/images/copy_clipboard.png"))
        self.hex_output_copy_button.clicked.connect(lambda: copy_action(self.hex_output.text()))

        outputbox_layout.addWidget(self.bin_label, 0, 0)
        outputbox_layout.addWidget(self.bin_output, 0, 1)
        outputbox_layout.addWidget(self.bin_output_copy_button, 0, 2)

        outputbox_layout.addWidget(self.dec_label, 1, 0)
        outputbox_layout.addWidget(self.dec_output, 1, 1)
        outputbox_layout.addWidget(self.dec_output_copy_button, 1, 2)

        outputbox_layout.addWidget(self.hex_label, 2, 0)
        outputbox_layout.addWidget(self.hex_output, 2, 1)
        outputbox_layout.addWidget(self.hex_output_copy_button, 2, 2)

        # IP address/mask number conversion
        self.ip_address_number_conversion_box = QGroupBox("Conversión de dirección IP/máscara de subred")
        main_layout.addWidget(self.ip_address_number_conversion_box, 1, 0, 1, 2)

        ip_address_number_conversion_layout = QGridLayout()
        ip_address_number_conversion_layout.setAlignment(Qt.AlignCenter)
        ip_address_number_conversion_layout.setHorizontalSpacing(25)
        ip_address_number_conversion_layout.setVerticalSpacing(24)
        self.ip_address_number_conversion_box.setLayout(ip_address_number_conversion_layout)

        self.input_label = QLabel("IP/Máscara")
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setMaximumWidth(150)
        self.input_textfield = QLineEdit()
        self.input_textfield.setPlaceholderText("192.168.1.1")
        self.input_textfield.setAlignment(Qt.AlignLeft)
        self.input_textfield.setMaximumWidth(300)
        self.input_textfield.setAlignment(Qt.AlignCenter)
        self.input_textfield.returnPressed.connect(self.convert_action_2)
        ip_address_number_conversion_layout.addWidget(self.input_label, 0, 0)
        ip_address_number_conversion_layout.addWidget(self.input_textfield, 0, 1)

        button_layout_2 = QVBoxLayout()
        self.dec_to_bin_button = QRadioButton("Decimal a binario")
        self.dec_to_bin_button.clicked.connect(lambda: self.input_textfield.setPlaceholderText("192.168.1.1"))
        self.dec_to_bin_button.setMaximumWidth(150)

        self.bin_to_dec_button = QRadioButton("Binario a decimal")
        self.bin_to_dec_button.clicked.connect(lambda: self.input_textfield.setPlaceholderText("11000000.10101000.00000001.00000001"))
        self.bin_to_dec_button.setMaximumWidth(150)
        self.dec_to_bin_button.setChecked(True)
        button_layout_2.addWidget(self.dec_to_bin_button)
        button_layout_2.addWidget(self.bin_to_dec_button)
        ip_address_number_conversion_layout.addLayout(button_layout_2, 0, 2)

        self.output_label = QLabel("Resultado")
        self.output_label.setAlignment(Qt.AlignCenter)
        self.output_textfield = QLineEdit()
        self.output_textfield.setMaximumWidth(300)
        self.output_textfield.setReadOnly(True)
        self.output_textfield.setAlignment(Qt.AlignCenter)
        ip_address_number_conversion_layout.addWidget(self.output_label, 1, 0)
        ip_address_number_conversion_layout.addWidget(self.output_textfield, 1, 1)

        self.output_textfield_copy_button = QPushButton("Copiar")
        self.output_textfield_copy_button.setIcon(QIcon("static/images/copy_clipboard.png"))
        self.output_textfield_copy_button.clicked.connect(lambda: copy_action(self.output_textfield.text()))
        ip_address_number_conversion_layout.addWidget(self.output_textfield_copy_button, 1, 2, alignment=Qt.AlignLeft)

        self.convert_button_2 = QPushButton("Convertir")
        self.convert_button_2.clicked.connect(self.convert_action_2)
        self.convert_button_2.setIcon(QIcon("static/images/exchange.png"))
        ip_address_number_conversion_layout.addWidget(self.convert_button_2, 2, 0, 1, 3, alignment=Qt.AlignHCenter)

    def convert_action(self):
        if is_empty(self.input_number_textfield.text()):
            PopupWindow("warning",
                        "Ingrese el número a convertir",
                        self.input_number_textfield)
        else:
            if self.bin_button.isChecked():
                self.source_bin(self.input_number_textfield.text())
            elif self.dec_button.isChecked():
                self.source_dec(self.input_number_textfield.text())
            else:
                self.source_hex(self.input_number_textfield.text())

    def source_bin(self, bin_number):
        bin_number_corrected = get_corrected_number(bin_number)
        bin_number_corrected_byte = bin_number_corrected.rjust(8, "0")
        if not is_correct_binary(bin_number_corrected):
            PopupWindow("warning",
                        "Número binario inválido",
                        self.input_number_textfield)
        else:
            if 0 <= int(bin_number_corrected, 2) <= 255:
                if bin_number_corrected != bin_number_corrected_byte:
                    self.bin_format_base = bin_number_corrected
                    self.bin_format_base_byte = bin_number_corrected_byte
                    bin_format = get_bin_format(self.bin_format_base,
                                                "en formato byte: ",
                                                self.bin_format_base_byte)
                else:
                    bin_format = self.bin_format_base
            else:
                bin_format = bin_number_corrected
            dec_format = str(int(bin_number_corrected, 2))
            hex_format = hex(int(bin_number_corrected, 2)).replace("0x", "").upper()
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def source_dec(self, dec_number):
        dec_number_corrected = get_corrected_number(dec_number)
        if not is_correct_decimal(dec_number_corrected):
            PopupWindow("warning",
                        "Número decimal inválido",
                        self.input_number_textfield)
        else:
            if 0 <= int(dec_number_corrected) <= 255:
                self.bin_format_base = bin(int(dec_number_corrected)).replace("0b", "")
                self.bin_format_base_byte = self.bin_format_base.rjust(8, "0")
                if self.bin_format_base != self.bin_format_base_byte:
                    bin_format = get_bin_format(self.bin_format_base,
                                                "en formato byte: ",
                                                self.bin_format_base_byte)
                else:
                    bin_format = self.bin_format_base
            else:
                bin_format = bin(int(dec_number_corrected)).replace("0b", "")
            dec_format = dec_number_corrected
            hex_format = hex(int(dec_number_corrected)).replace("0x", "").upper()
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def source_hex(self, hex_number):
        hex_number_corrected = get_corrected_number(hex_number).upper()
        if not is_correct_hexadecimal(hex_number_corrected):
            PopupWindow("warning",
                        "Número hexadecimal inválido",
                        self.input_number_textfield)
        else:
            if 0 <= int(hex_number_corrected, 16) <= 255:
                self.bin_format_base = bin(int(hex_number_corrected, 16)).replace("0b", "")
                self.bin_format_base_byte = self.bin_format_base.rjust(8, "0")
                if self.bin_format_base != self.bin_format_base_byte:
                    bin_format = get_bin_format(self.bin_format_base,
                                                "en formato byte: ",
                                                self.bin_format_base_byte)
                else:
                    bin_format = self.bin_format_base
            else:
                bin_format = bin(int(hex_number_corrected, 16)).replace("0b", "")
            dec_format = str(int(hex_number_corrected, 16))
            hex_format = hex_number_corrected
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def convert_action_2(self):
        if is_empty(self.input_textfield.text()):
            PopupWindow("warning",
                        "La dirección IP/Máscara no puede estar vacía",
                        self.input_textfield)
        elif self.dec_to_bin_button.isChecked():
            if is_correct_any_ip_dec(self.input_textfield.text()):
                self.output_textfield.setText(dec_to_bin(self.input_textfield.text()))
            else:
                PopupWindow("warning",
                            "Dirección Ip inválida",
                            self.input_textfield)
        else:
            if is_correct_any_ip_bin(self.input_textfield.text()):
                self.output_textfield.setText(bin_to_dec(self.input_textfield.text()))
            else:
                PopupWindow("warning",
                            "Máscara de subred inválida",
                            self.input_textfield)


def dec_to_bin(ip_address):
    binary_format = ""
    for octet in ip_address.split("."):
        binary_format += f'{bin(int(octet)).replace("0b", "").rjust(8, "0")}.'
    return binary_format[:-1]


def copy_action(input_field_text):
    if input_field_text:
        copy(input_field_text)


def get_corrected_number(number):
    only_zeros = True
    for i in number:
        if not i == "0":
            only_zeros = False
    if not only_zeros:
        count_zero = 0
        if number[0] == "0":
            for i in number:
                if i == "0":
                    count_zero += 1
                if not i == "0":
                    break
            return number[count_zero:]
        return number
    return "0"


def bin_to_dec(ip_address_bin):
    decimal_format = ""
    for octet in ip_address_bin.split("."):
        decimal_format += f"{int(octet, 2)}."
    return decimal_format[:-1]


def get_bin_format(bin_format_base, byte_format_str, bin_format_base_byte):
    return f"{bin_format_base} ({byte_format_str} {bin_format_base_byte})"
