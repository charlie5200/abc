{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdNOB9Ab7pyu+42WN/zuFL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/charlie5200/abc/blob/main/Untitled20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "st.title(num = input('輸入你的發票號碼：'))\n",
        "ns = '05701942'                         # 特別獎\n",
        "n1 = '97718570'                         # 特獎\n",
        "n2 = ['88400675','73475574','53038222'] # 頭獎\n",
        "if num == ns: print('對中 1000 萬元！')   # 對中特別獎\n",
        "if num == n1: print('對中 200 萬元！')    # 對中特獎\n",
        "# 頭獎判斷\n",
        "for i in n2:\n",
        "    if num == i:\n",
        "        print('對中 20 萬元！')   # 對中頭獎\n",
        "        break\n",
        "    if num[-7:] == i[-7:]:\n",
        "        print('對中 4 萬元！')    # 末七碼相同\n",
        "        break\n",
        "    if num[-6:] == i[-6:]:\n",
        "        print('對中 1 萬元！')    # 末六碼相同\n",
        "        break\n",
        "    if num[-5:] == i[-5:]:\n",
        "        print('對中 4000 元！')   # 末五碼相同\n",
        "        break\n",
        "    if num[-4:] == i[-4:]:\n",
        "        print('對中 1000 元！')   # 末四碼相同\n",
        "        break\n",
        "    if num[-3:] == i[-3:]:\n",
        "        print('對中 200 元！')    # 末三碼相同\n",
        "        break\n",
        "    else:\n",
        "       st.write('再接再厲')\n",
        "       break"
      ],
      "metadata": {
        "id": "vYZupUs4idTB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}