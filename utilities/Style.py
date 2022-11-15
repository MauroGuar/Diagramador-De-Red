def style():
    my_style = '''
QWidget {
    font-size: 12px;
    border-radius: 5%;
    margin: 2px;
}

QMainWindow {
    background-color: #2e3440;
}

QGroupBox  {
    background-color: #3b4252;
    color: white;
}

QTabWidget::pane {
    border: none;
}

QTabBar::tab {
    background-color: #434c5e;
    color: white;
}

QTabBar::tab:hover {
    background-color: #4c566a;
    color: white;
}

QTabBar::tab:selected {
    background-color: #D8DEE9;
    color: black;
}

QRadioButton {
    color: white;
}

QPushButton {
    background-color: #ECEFF4;
    border: 1px solid white;
    border-style: outset;
    color: black;
    min-width: 5em;
    min-height: 1.3em;
    padding: 7px;
}

QPushButton:hover {
    background-color: #D8DEE9;
    color: black;
}

QLabel {
    color: white;
    font-size: 13px;
}

QLineEdit {
    font-size: 15px;
    padding: 1px;
}

QLineEdit:read-only {
    background-color: #81a1c1;
}

QTableWidget {
    background-color: #4C566A;
    color: white;
    gridline-color: #4C566A;
}

QTableWidget::

QTableWidget::item:hover {
    background-color: #2E3440;
    color: white;
}

QHeaderView::section {
    background-color: #646464;
    color: white;
    border: 1px solid #fffff8;
    font-size: 9pt;
}

QProgressBar {
    text-align: center;
}

QProgressBar::chunk {
    background-color: white;
}

QRadioButton {    
    font-size: 11px;
    padding: 2px;
}

QRadioButton::indicator:unchecked {
   width: 7px;
    height: 7px;
    left: 1px;
    margin-right: 1px;
    background-color: white;
    border: 2px solid white;
    border-radius: 5px;
}

QRadioButton::indicator:unchecked:hover {
    width: 10px;
    height: 10px;
    left: -0.5px;
    bottom: -1.5px;
    border: 1px solid rgb(0, 120, 215);
    border-radius: 5px;    
}

QRadioButton::indicator:checked {
    width: 7px;
    height: 7px;
    left: 1px;
    margin-right: 1px;
    background-color: rgb(51, 51, 51);
    border: 2px solid white;
    border-radius: 5px;
}

QRadioButton::indicator:checked:hover {
    background-color: rgb(0, 120, 215);
}

    '''
    return my_style
