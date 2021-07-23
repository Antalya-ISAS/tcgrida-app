# -*- coding: UTF-8 -*-

################################


class Style:
    ## rgba(27, 29, 35, 160) for dark background, rgba(230, 230, 230, 160) for light background

    style_line = (
        u"QLineEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}"
    )

    style_combo = (
        u"QComboBox{\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding: 5px;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox QAbstractItemView {\n"
        "	color: rgb(61, 180, 255);	\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 10px;\n"
        "	selection-background-color: rgb(39, 44, 54);\n"
        "}"
    )

    style_circ_btn = (
        u"QPushButton {	\n"
        "	border: 5px solid rgb(61, 180, 255);\n"
        "	background-color: rgb(22, 25, 28);\n"
        "	width: 30px;\n"
        "	height: 30px;\n"
        "       padding:5px;\n"
        "	border-radius: 25px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 5px solid rgb(220, 220, 220);\n"
        "	background-color: rgb(61, 180, 255);\n"
        "}"
    )

    style_circ_btn2 = (
        u"QPushButton {	\n"
        "	border: 5px solid rgb(180, 0, 0);\n"
        "	background-color: rgb(58, 8, 8);\n"
        "	width: 30px;\n"
        "	height: 30px;\n"
        "       padding:5px;\n"
        "	border-radius"
        ": 25px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(95, 15, 15);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 5px solid rgb(220, 220, 220);\n"
        "	background-color: rgb(180, 0, 0);\n"
        "}"
    )

    style_btn_toggle = (
        u"QPushButton {\n"
        "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        "	border: none;\n"
        "	background-color: rgb(27, 29, 35);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(33, 37, 43);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgb(61, 180, 255);\n"
        "}"
    )

    style_frame_main = (
        u"/* LINE EDIT */\n"
        "QLineEdit {\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "	border: 2px solid rgb(91, 101, 124);\n"
        "}\n"
        "\n"
        "/* COMMAND LINK BUTTON */\n"
        "QCommandLinkButton {	\n"
        "	color: rgb(85, 170, 255);\n"
        "	border-radius: 5px;\n"
        "	padding: 5px;\n"
        "}\n"
        "QCommandLinkButton:hover {	\n"
        "	color: rgb(210, 210, 210);\n"
        "	background-color: rgb(44, 49, 60);\n"
        "}\n"
        "QCommandLinkButton:pressed {	\n"
        "	color: rgb(210, 210, 210);\n"
        "	background-color: rgb(52, 58, 71);\n"
        "}"
        "/* RADIO BUTTON */\n"
        "QRadioButton::indicator {\n"
        "    border: 5px solid rgb(84, 22, 22);\n"
        "	width: 30px;\n"
        "	height: 30px;\n"
        "	border-radius"
        ": 20px;\n"
        "    background: rgb(188, 3, 3);\n"
        "}\n"
        "QRadioButton::indicator:hover {\n"
        "    border: 5px solid rgb(84, 22, 22);\n"
        "    background: rgb(137, 0, 0);\n"
        "}\n"
        "QRadioButton::indicator:checked {\n"
        "    background: rgb(137, 10, 10);\n"
        "    border: 5px solid rgb(100, 0, 0);\n"
        "	width: 30px;\n"
        "	height: 30px;\n"
        "	border-radius"
        ": 20px;\n"
        "}\n"
        "\n"
        "/* COMBOBOX */\n"
        "QComboBox{\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	border-radius: 5px;\n"
        "	border: 2px solid rgb(27, 29, 35);\n"
        "	padding: 5px;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "	border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox::drop-down {\n"
        "	subcontrol-origin: padding;\n"
        "	subcontrol-position: top right;\n"
        "	width: 25px; \n"
        "	border-left-width: 3px;\n"
        "	border-left-color: rgba(39, 44, 54, 150);\n"
        "	border-left-style: solid;\n"
        "	border-top-right-radius: 3px;\n"
        "	border-bottom-right-radius: 3px;	\n"
        "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
        "	background-position: center;\n"
        "	background-repeat: no-reperat;\n"
        " }\n"
        "QComboBox QAbstractItemView {\n"
        "	color: rgb(61, 180, 255);	\n"
        "	background-color: rgb(27, 29, 35);\n"
        "	padding: 10px;\n"
        "	selection-background-color: rgb(39, 44, 54);\n"
        "}\n"
        "\n"
        ""
    )

    style_bt_standard = """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """
