{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1uDHGioiJTxocfyIAvu1Q0wk0GiN3zjKJ",
      "authorship_tag": "ABX9TyM80nS4Q6COZH0Lnz5rClNQ"
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
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DMgO__vsnf8U",
        "outputId": "7e187d35-0744-4d51-8c6d-f200d1dcd3e3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Готово! Новый файл успешно создан.\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "file_path = '/dataset-sots-seti-b62e6c94-57c9-4f77-a11f-4f9cd2af3e4e (1).xlsx'\n",
        "df = pd.read_excel(file_path)\n",
        "\n",
        "# Полный словарь маппинга для всех стран\n",
        "country_clean_map = {\n",
        "    'РФ': 'Россия', 'РОССИЯ': 'Россия',\n",
        "    'БЕЛАРУСЬ': 'Беларусь', 'РБ': 'Беларусь',\n",
        "    'АРМЕНИЯ': 'Армения', 'УЗБЕКИСТАН': 'Узбекистан',\n",
        "    'МОЛДОВА, РЕСПУБЛИКА': 'Молдова', 'КАЗАХСТАН': 'Казахстан',\n",
        "    'ТАДЖИКИСТАН': 'Таджикистан', 'ТУРКМЕНИЯ': 'Туркменистан',\n",
        "    'ИНДИЯ': 'Индия', 'УКРАИНА': 'Украина',\n",
        "    'КИРГИЗИЯ': 'Киргизия', 'ЛАТВИЯ': 'Латвия',\n",
        "    'АБХАЗИЯ': 'Абхазия', 'ГРУЗИЯ': 'Грузия',\n",
        "    'АЗЕРБАЙДЖАН': 'Азербайджан', 'ДНР': 'Донецк',\n",
        "    'ЛИТВА': 'Литва', 'ЛИВАН': 'Ливан', 'ЭСТОНИЯ': 'Эстония',\n",
        "    'СИРИЙСКАЯ АРАБСКАЯ РЕСПУБЛИКА': 'Сирия', 'МАРОККО': 'Марокко',\n",
        "    'ИЗРАИЛЬ': 'Израиль', 'ХОРВАТИЯ': 'Хорватия',\n",
        "    'ВЬЕТНАМ': 'Вьетнам', 'КИТАЙ': 'Китай', 'КУБА': 'Куба',\n",
        "    'ЕГИПЕТ': 'Египет', 'ГЕРМАНИЯ': 'Германия', 'ЯПОНИЯ': 'Япония',\n",
        "    'ИРАН, ИСЛАМСКАЯ РЕСПУБЛИКА': 'Иран', 'РУМЫНИЯ': 'Румыния',\n",
        "    'ИТАЛИЯ': 'Италия', 'ТУРЦИЯ': 'Турция', 'СЕРБИЯ': 'Сербия',\n",
        "    'БРАЗИЛИЯ': 'Бразилия', 'ПЕРУ': 'Перу', 'ЧИЛИ': 'Чили',\n",
        "    'КНДР': 'Северная Корея', 'ГАНА': 'Гана', 'ИСПАНИЯ': 'Испания',\n",
        "    'ПАНАМА': 'Панама', 'ЙЕМЕН': 'Йемен',\n",
        "    'БОСНИЯ И ГЕРЦЕГОВИНА': 'Босния и Герцеговина',\n",
        "    'КОРЕЯ, РЕСПУБЛИКА': 'Южная Корея', 'ИРАК': 'Ирак',\n",
        "    'ЧЕШСКАЯ РЕСПУБЛИКА': 'Чехия', 'КАНАДА': 'Канада',\n",
        "    'ПОЛЬША': 'Польша', 'КАТАР': 'Катар', 'ИОРДАНИЯ': 'Иордания',\n",
        "    'ТУНИС': 'Тунис', 'АВСТРИЯ': 'Австрия', 'ЭКВАДОР': 'Эквадор',\n",
        "    'СОЕДИНЕННЫЕ ШТАТЫ': 'США', 'США': 'США', 'БЕНИН': 'Бенин',\n",
        "    'ЮЖНАЯ ОСЕТИЯ': 'Южная Осетия', 'КАМЕРУН': 'Камерун',\n",
        "    'ТАИЛАНД': 'Таиланд', 'ЛУГАНСКАЯ НАРОДНАЯ РЕСПУБЛИКА': 'Луганск',\n",
        "    'БАНГЛАДЕШ': 'Бангладеш', 'ЮЖНАЯ АФРИКА': 'ЮАР',\n",
        "    'КОНГО, ДЕМОКР. РЕСПУБЛИКА': 'Конго'\n",
        "}\n",
        "\n",
        "df['citizenship_country_fixed'] = df['citizenship_country'].astype(str).str.strip().map(country_clean_map)\n",
        "\n",
        "output_file = 'dataset_fixed_for_datalens.xlsx'\n",
        "df.to_excel(output_file, index=False)\n",
        "print(\"Готово! Новый файл успешно создан.\")"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "d809c5fd",
        "outputId": "ea2614ef-aa6f-4841-9740-57d092144777"
      },
      "source": [
        "from google.colab import files\n",
        "\n",
        "files.download('dataset_fixed_for_datalens.xlsx')"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_f5865a57-d410-4f5b-8f52-5e8efab6ef31\", \"dataset_fixed_for_datalens.xlsx\", 37615399)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}